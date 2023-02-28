"""
-------------------------------------------------------------------------------
data_pipeline_sec.py

Create Date:    2023-02-21
Author:         Stefan Dombek <dombek@uni-leipzig.de>
Description:    This script is intended to enable the documentation of derived 
                tables. To do this, data is taken from the database catalog and 
                combined with manually created data. An HTML page is output.
-------------------------------------------------------------------------------
Copyright (C) 2018-2023 The Open Library Foundation

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
-------------------------------------------------------------------------------
"""
###############################################################################
#                                                                             #
# Load modules                                                                #
#                                                                             #
###############################################################################

import psycopg2
import psycopg2.extras
import csv
import io
import requests
import pandas as pd
from io import StringIO
import tabulate
from cryptography.fernet import Fernet

###############################################################################
#                                                                             #
# Login credentials                                                           #
#                                                                             #
###############################################################################

# load key
key            = open('config.key', 'r')
key            = key.read()
f              = Fernet(key)

# load encrypted file
encrypted_file = open('enc_credentials.csv', 'rb')
encrypted      = encrypted_file.read()

# decrypt the content
decrypted      = f.decrypt(encrypted)
credentials    = decrypted.decode('utf-8').split(sep=',')

# load the login credentials in variables for database connection
hostname       = credentials[0]
database       = credentials[1]
username       = credentials[2]
pwd            = credentials[3]
port_id        = credentials[4]

###############################################################################
#                                                                             #
# Set variables                                                               #
#                                                                             #
###############################################################################

# variables for error handling for database connection
conn        = None
cur         = None

###############################################################################
#                                                                             #
# Try to connect to database, else print error message                        #
#                                                                             #
###############################################################################

try:
	
    ###############################################################################
    #                                                                             #
    # Read data from postgres catalog                                             #
    #                                                                             #
    ###############################################################################

    # open database connection
    conn = psycopg2.connect(
                host     = hostname,
                dbname   = database,
                user     = username,
                password = pwd,
                port     = port_id)

    # configure cursor for fetching data from database
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # configure the database query and execute the database query
    cur.execute("""
        SELECT
            columns.table_name AS "table",
            columns.ordinal_position AS "attribute #", 
            columns.column_name AS "attribute",
            columns.udt_name AS "datatype",
            COALESCE(pg_description.description, '') AS description
        FROM
            pg_catalog.pg_statio_all_tables
            LEFT JOIN pg_catalog.pg_description ON pg_description.objoid = pg_statio_all_tables.relid
            RIGHT JOIN information_schema.columns ON pg_description.objsubid = columns.ordinal_position 
                AND columns.table_schema = pg_statio_all_tables.schemaname 
                AND columns.table_name = pg_statio_all_tables.relname
        WHERE 
            columns.table_schema = 'folio_derived'
        ORDER BY 
            columns.table_name,
            columns.ordinal_position
    """)

    # save the result from the database query
    result = cur.fetchall()

    attributes = pd.DataFrame(result, columns=["table","attribute #","attributeName","datatype","description"]).set_index(['table','attributeName'])

    ###############################################################################
    #                                                                             #
    # fetch csv data                                                              #
    #                                                                             #
    ###############################################################################

    url      = 'https://raw.githubusercontent.com/stdombek/folio_reporting_project_extracted_derived_tables/main/csv/derived_tables_columns_doc.csv'
    response = requests.get(url)

    if response.status_code == 200:

        #buffer    = io.StringIO(response.text)
        #reader    = csv.DictReader(buffer)

        file_name = "../csv/derived_tables_columns_doc.CSV"
        csv_file  = open(file_name, "w")
        csv_file.write(response.text)
        csv_file.close() 

        csv_data = pd.read_csv(StringIO(response.text), sep=",").set_index(['table','attributeName'])

    else:
        
        print("Oh, something went wrong! Cannot fetch csv file from GitHub")
        print(response.status_code)

        #reader = csv.DictReader(open('../csv/derived_tables_columns_doc.CSV'), delimiter=',')
        csv_data = pd.read_csv('../csv/derived_tables_columns_doc.CSV').set_index(['table','attributeName'])

    response.close()


    ###############################################################################
    #                                                                             #
    # Add csv_data to attributes dictionary                                       #
    #                                                                             #
    ###############################################################################

    column_names = ['table', 'Attribute', 'Attribute #', 'Type', 'Description', 'Source - Schema', 'Source - Table', 'Source - Attribute', 'Source - Type', 'Source - Multiple values', 'Aggregation', 'Notes']
    desired_columns = ['Attribute #', 'Attribute', 'Type', 'Source - Schema', 'Source - Table', 'Source - Attribute', 'Source - Type', 'Source - Multiple values', 'Aggregation', 'Description', 'Notes']

    combined = attributes.join(csv_data).reset_index()
    combined.columns = column_names


    ###############################################################################
    #                                                                             #
    # Markdown output as file for each table                                      #
    #                                                                             #
    ###############################################################################


    table_names = combined.table.unique()

    #create a data frame dictionary to store your data frames
    #DataFrameDict = {elem : pd.DataFrame() for elem in table_names}


    for tbl in table_names:

        tbl_df = combined[desired_columns][combined.table == tbl]
        markdown_table = tbl_df.fillna('').to_markdown(index=False)

        title = "title: " + tbl + ".sql"
        yaml = "---\n" + title + "\n---\n"

        h1 = "# Documentation: " + tbl + ".sql\n\n"

        h2 = "## Attributes:\n\n"

        ###############################################################################
        #                                                                             #
        # Create the section with the mermaid er diagram                              #
        #                                                                             #
        ###############################################################################        

        # ToDo
        mermaid_diagram = ''

        ###############################################################################
        #                                                                             #
        # Combine all components
        #                                                                             #
        ###############################################################################        

        markdown = yaml + h1 + h2 + markdown_table + mermaid_diagram

        ###############################################################################
        #                                                                             #
        # Create file on system                                                       #
        #                                                                             #
        ############################################################################### 

        file_name = "../Output/" + tbl + ".md"
        md_file = open(file_name, "w")
        md_file.write(markdown)
        md_file.close()	


###############################################################################
#                                                                             #
# Error handler for database connection                                       #
#                                                                             #
###############################################################################

except Exception as error:
    print(error)

###############################################################################
#                                                                             #
# Close the connection                                                        #
#                                                                             #
###############################################################################

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()

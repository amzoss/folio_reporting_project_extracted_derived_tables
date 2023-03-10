"""
-------------------------------------------------------------------------------
data_pipeline.py

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
import tabulate
from io import StringIO
from cryptography.fernet import Fernet

# Local packages
from pkg_output import html, markdown

###############################################################################
#                                                                             #
# Login credentials                                                           #
#                                                                             #
###############################################################################

# Load key
key            = open('config.key', 'r')
key            = key.read()
f              = Fernet(key)

# Load encrypted file
encrypted_file = open('enc_credentials.csv', 'rb')
encrypted      = encrypted_file.read()

# Decrypt the content
decrypted      = f.decrypt(encrypted)
credentials    = decrypted.decode('utf-8').split(sep=',')

# Load the login credentials in variables for database connection
hostname       = credentials[0]
database       = credentials[1]
username       = credentials[2]
pwd            = credentials[3]
port_id        = credentials[4]

# Alternative: If no KEY file is used
# login credentials to database
#hostname      = ''
#database      = ''
#username      = ''
#pwd           = ''
#port_id       = ''

###############################################################################
#                                                                             #
# Set variables                                                               #
#                                                                             #
###############################################################################

# Set variables for error handling for database connection
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

    # Open database connection
    conn = psycopg2.connect(
                host     = hostname,
                dbname   = database,
                user     = username,
                password = pwd,
                port     = port_id)

    # Configure cursor for fetching data from database
    cur       = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # Prepare the query string; Get the query from SQL file
    file_name = "../sql/derived_tables/pg_catalog_extraction_derivedTables.sql"
    sql_file  = open(file_name, "r")
    query     = ''
    for line in sql_file:
        query += line
    sql_file.close()
       
    # Configure the database query and execute the database query
    cur.execute(query)

    # Save the result from the database query
    result = cur.fetchall()

    ###############################################################################
    #                                                                             #
    # Create DataFrame with pandas                                                #
    #                                                                             #
    ###############################################################################

    # Create a DataFrame with the result from the query, set the column names and the index for the merging process
    attributes = pd.DataFrame(result, columns=["table","attribute #","attributeName","datatype","description"]).set_index(['table','attributeName'])

    ###############################################################################
    #                                                                             #
    # Fetch csv data                                                              #
    #                                                                             #
    ###############################################################################

    # Prepare string for the url source
    url      = 'https://raw.githubusercontent.com/stdombek/folio_reporting_project_extracted_derived_tables/main/data/csv/derived_tables_columns_doc.csv'
    
    # Fetch data from the server and save it in the object "response"
    response = requests.get(url)

    # If the connection is etablished
    if response.status_code == 200:

        # Write the data from the server in the local file
        file_name = "../data/csv/derived_tables_columns_doc.CSV"
        csv_file  = open(file_name, "w")
        csv_file.write(response.text)
        csv_file.close() 

        # Create a DataFrame with pandas for the data from the server
        csv_data = pd.read_csv(StringIO(response.text), sep=",").set_index(['table','attributeName'])

    # If the connection is not etablished
    else:
        
        # Show the error message for the user
        print("Oh, something went wrong! Cannot fetch csv file from GitHub")
        print(response.status_code)

        # Create a DataFrame with pandas for the data from the local file (fallback)
        csv_data = pd.read_csv('../data/csv/derived_tables_columns_doc.CSV').set_index(['table','attributeName'])

    # Close the connection
    response.close()

    ###############################################################################
    #                                                                             #
    # Combine the DataFrames                                                      #
    #                                                                             #
    ###############################################################################

    column_names     = ['table', 'Attribute', 'Attribute #', 'Type', 'Description', 'Source - Schema', 'Source - Table', 'Source - Attribute', 'Source - Type', 'Source - Multiple values', 'Aggregation', 'Notes']
    desired_columns  = ['Attribute #', 'Attribute', 'Type', 'Source - Schema', 'Source - Table', 'Source - Attribute', 'Source - Type', 'Source - Multiple values', 'Aggregation', 'Description', 'Notes']

    combined         = attributes.join(csv_data).reset_index()
    combined.columns = column_names

    ###############################################################################
    #                                                                             #
    # Create a list for the tables names                                          #
    #                                                                             #
    ###############################################################################

    # Find all table names in the DataFrame and create a list of table names
    table_names = combined.table.unique()

    ###############################################################################
    #                                                                             #
    # Output                                                                      #
    # Create files for each table                                                 #
    #                                                                             #
    ###############################################################################

    # html
    html.create_html_files(table_names, combined, desired_columns)
   
    # markdown
    markdown.create_markdown_files(table_names, combined, desired_columns)

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

"""
-------------------------------------------------------------------------------
data_pipeline.py

Create Date:    2023-02-05
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

###############################################################################
#                                                                             #
# Set variables                                                               #
#                                                                             #
###############################################################################

# login credentials to database
hostname    = ''
database    = ''
username    = ''
pwd         = ''
port_id     = ''

# variables for error handling for database connection
conn        = None
cur         = None

# dictionaries and lists
table_names = []
tables      = {}
attributes  = {}
csv_data    = {}

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
            pg_description.description 
        FROM 
            pg_catalog.pg_statio_all_tables 
            INNER JOIN pg_catalog.pg_description ON pg_description.objoid = pg_statio_all_tables.relid 
            INNER JOIN information_schema.columns ON pg_description.objsubid = columns.ordinal_position 
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

    ###############################################################################
    #                                                                             #
    # create dictionary for tables                                                #
    #                                                                             #
    ###############################################################################

    for record in result:

        if record['table'] not in table_names:
            table_names.append(record['table'])
	
    counter = 0
    for i in table_names:

        tables[counter]          = {}		
        tables[counter]['table'] = table_names[counter]

        counter += 1
	
    ###############################################################################
    #                                                                             #
    # create dictionary for attributes                                            #
    #                                                                             #
    ###############################################################################

    counter = 0

    for record in result:	
		
        attributes[counter]                    = {}
        attributes[counter]['table']           = str(record['table']) # for matching
        attributes[counter]['attributeNumber'] = str(record['attribute #'])
        attributes[counter]['attributeName']   = str(record['attribute'])
        attributes[counter]['datatype']        = str(record['datatype'])
        attributes[counter]['description']     = str(record['description'])

        counter += 1

    ###############################################################################
    #                                                                             #
    # create dictionary for csv data                                              #
    #                                                                             #
    ###############################################################################

    reader = csv.DictReader(open('../csv/derived_tables_columns_doc.CSV'), delimiter=',')

    counter = 0

    for row in reader:	
		
        csv_data[counter]                         = {}
        csv_data[counter]['table']                = str(row['table'])
        csv_data[counter]['attributeName']        = str(row['attributeName'])
        csv_data[counter]['sourceSchema']         = str(row['sourceSchema'])
        csv_data[counter]['sourceTable']          = str(row['sourceTable'])
        csv_data[counter]['sourceAttribute']      = str(row['sourceAttribute'])
        csv_data[counter]['sourceType']           = str(row['sourceType'])
        csv_data[counter]['sourceMultipleValues'] = str(row['sourceMultipleValues'])
        csv_data[counter]['aggregation']          = str(row['aggregation'])
        csv_data[counter]['notes']                = str(row['notes'])

        counter += 1

    ###############################################################################
    #                                                                             #
    # Add csv_data to attributes dictionary                                       #
    #                                                                             #
    ###############################################################################

    # At first, add new attributes with no data to the dictionary attributes

    for i in range(0, len(attributes), 1):

        no_entry_handler = {
            'sourceSchema': '', 
            'sourceTable': '', 
            'sourceAttribute': '', 
            'sourceType': '', 
            'sourceMultipleValues': '', 
            'aggregation': '', 
            'notes': ''}

        attributes[i].update(no_entry_handler)

    # After that, overwrite the attributes where are data in the csv 

    for i in range(0, len(attributes), 1):
	
        for j in range(0, len(csv_data), 1):

            # Overwrite where there is a match between table name and attribute name

            if csv_data[j]['table'] == attributes[i]['table'] and csv_data[j]['attributeName'] == attributes[i]['attributeName']:

                attributes[i]['sourceSchema']         = csv_data[j]['sourceSchema']
                attributes[i]['sourceTable']          = csv_data[j]['sourceTable']
                attributes[i]['sourceAttribute']      = csv_data[j]['sourceAttribute']
                attributes[i]['sourceType']           = csv_data[j]['sourceType']
                attributes[i]['sourceMultipleValues'] = csv_data[j]['sourceMultipleValues']
                attributes[i]['aggregation']          = csv_data[j]['aggregation']
                attributes[i]['notes']                = csv_data[j]['notes']

    ###############################################################################
    #                                                                             #
    # html output as file for each table                                          #
    #                                                                             #
    ###############################################################################

    for i in range(0, len(tables), 1):

        html_output_string = "<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'></head>"\
                "<title>" + tables[i]['table'] + ".sql</title>"\
                "<body>"\
                "<h1>Documentation: " + tables[i]['table'] + ".sql</h1>"\
                "<hr border='1'>"\
                "<!-- Table of attributes --><p>"\
                "<h2>Attributes:</h2>"\
                "<table border='1'>"\
                "<th>Attribut #</th>"\
                "<th>Attribut</th>"\
                "<th>Type</th>"\
                "<th>Source - Schema</th>"\
                "<th>Source - Table</th>"\
                "<th>Source - Attribut</th>"\
                "<th>Source - Type</th>"\
                "<th>Source - Multiple values</th>"\
                "<th>Aggregation</th>"\
                "<th>Description</th>"\
                "<th>Notes</th>"

        for j in range(0, len(attributes), 1):
            if tables[i]['table'] == attributes[j]['table']:
                html_output_string += "<tr>"\
                "<td>" + attributes[j]['attributeNumber'] + "</td>"\
                "<td>" + attributes[j]['attributeName'] + "</td>"\
                "<td>" + attributes[j]['datatype'] + "</td>"\
                "<td>" + attributes[j]['sourceSchema'] + "</td>"\
                "<td>" + attributes[j]['sourceTable'] + "</td>"\
                "<td>" + attributes[j]['sourceAttribute'] + "</td>"\
                "<td>" + attributes[j]['sourceType'] + "</td>"\
                "<td>" + attributes[j]['sourceMultipleValues'] + "</td>"\
                "<td>" + attributes[j]['aggregation'] + "</td>"\
                "<td>" + attributes[j]['description'] + "</td>"\
                "<td>" + attributes[j]['notes'] + "</td>"\
                "</tr>"

        html_output_string += "</table><hr border='1'></body></html>"

        file_name = "../Output/" + tables[i]['table'] + ".html"
        html_file = open(file_name, "w")
        html_file.write(html_output_string)
        html_file.close()	

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

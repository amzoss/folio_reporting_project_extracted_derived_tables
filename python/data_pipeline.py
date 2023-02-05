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
# Import modules
import psycopg2
import psycopg2.extras
import csv

# declare and initialize variables
# variables for the login credentials to metadb
hostname = ''
database = ''
username = ''
pwd = ''
port_id = ''
# variables for database connection
conn = None
cur = None
# dictionaries
table_names = []
attribute_properties_secound_level = {}
tables_first_level = {}
csv_information_thirth_level = {}

# Try to connect to database, else print error message
try:
	# open database connection
	conn = psycopg2.connect(
				host = hostname,
				dbname = database,
				user = username,
				password = pwd,
				port = port_id)
	
	# configure cursor for fetching data from database
	cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
	
	# configure the database query and execute the database query
	cur.execute('SELECT columns.table_name AS "table", columns.ordinal_position AS "attribute #", columns.column_name AS "attribute", columns.udt_name AS "datatype", pg_description.description FROM pg_catalog.pg_statio_all_tables INNER JOIN pg_catalog.pg_description ON pg_description.objoid = pg_statio_all_tables.relid INNER JOIN information_schema.columns ON pg_description.objsubid = columns.ordinal_position AND columns.table_schema = pg_statio_all_tables.schemaname AND columns.table_name = pg_statio_all_tables.relname WHERE columns.table_schema = \'folio_derived\' ORDER BY columns.table_name, columns.ordinal_position')
	result = cur.fetchall()

	# create dictionary for tables
	for record in result:
		# if table name is not in the list, add the table name to the list
		if record['table'] not in table_names:
			table_names.append(record['table'])
	
	counter = 0
	for i in table_names:
		tables_first_level[counter] = {}		
		tables_first_level[counter]['table'] = table_names[counter]
		
		counter += 1
		
	# create dictionary for attributes
	counter = 0
	for record in result:	
		# if table not in dictionary set counter 0 --> new enumaration	
		attribute_properties_secound_level[counter] = {}
		attribute_properties_secound_level[counter]['table'] = str(record['table']) # for matching
		attribute_properties_secound_level[counter]['attributeNumber'] = str(record['attribute #'])
		attribute_properties_secound_level[counter]['attributeName'] = str(record['attribute'])
		attribute_properties_secound_level[counter]['datatype'] = str(record['datatype'])
		attribute_properties_secound_level[counter]['description'] = str(record['description'])

		counter += 1

	# read csv file informations
	reader = csv.DictReader(open('../csv/derived_tables_columns_doc.CSV'), delimiter=',')
	
	counter = 0
	for row in reader:
		
		csv_information_thirth_level[counter] = {}
		csv_information_thirth_level[counter]['table'] = str(row['table'])
		csv_information_thirth_level[counter]['attributeName'] = str(row['attributeName'])
		csv_information_thirth_level[counter]['sourceSchema'] = str(row['sourceSchema'])
		csv_information_thirth_level[counter]['sourceTable'] = str(row['sourceTable'])
		csv_information_thirth_level[counter]['sourceAttribute'] = str(row['sourceAttribute'])
		csv_information_thirth_level[counter]['sourceType'] = str(row['sourceType'])
		csv_information_thirth_level[counter]['sourceMultipleValues'] = str(row['sourceMultipleValues'])
		csv_information_thirth_level[counter]['aggregation'] = str(row['aggregation'])
		csv_information_thirth_level[counter]['notes'] = str(row['notes'])

		counter += 1

	# combine the two dictionaries
	for i in range(0, len(attribute_properties_secound_level), 1):
		no_entry_handler = {'sourceSchema': '', 'sourceTable': '', 'sourceAttribute': '', 'sourceType': '', 'sourceMultipleValues': '', 'aggregation': '', 'notes': ''}
		attribute_properties_secound_level[i].update(no_entry_handler)
	
	for i in range(0, len(attribute_properties_secound_level), 1):
		for j in range(0, len(csv_information_thirth_level), 1):
			if csv_information_thirth_level[j]['table'] == attribute_properties_secound_level[i]['table'] and csv_information_thirth_level[j]['attributeName'] == attribute_properties_secound_level[i]['attributeName']:
				attribute_properties_secound_level[i]['sourceSchema'] = csv_information_thirth_level[j]['sourceSchema']
				attribute_properties_secound_level[i]['sourceTable'] = csv_information_thirth_level[j]['sourceTable']
				attribute_properties_secound_level[i]['sourceAttribute'] = csv_information_thirth_level[j]['sourceAttribute']
				attribute_properties_secound_level[i]['sourceType'] = csv_information_thirth_level[j]['sourceType']
				attribute_properties_secound_level[i]['sourceMultipleValues'] = csv_information_thirth_level[j]['sourceMultipleValues']
				attribute_properties_secound_level[i]['aggregation'] = csv_information_thirth_level[j]['aggregation']
				attribute_properties_secound_level[i]['notes'] = csv_information_thirth_level[j]['notes']

	# html output as file for each table
	for i in range(0, len(tables_first_level), 1):

		html_output_string = "<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'></head>"\
				"<title>" + tables_first_level[i]['table'] + ".sql</title>"\
				"<body>"\
				"<h1>Documentation: " + tables_first_level[i]['table'] + ".sql</h1>"\
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

		for j in range(0, len(attribute_properties_secound_level), 1):
			if tables_first_level[i]['table'] == attribute_properties_secound_level[j]['table']:
				html_output_string += "<tr>"\
				"<td>" + attribute_properties_secound_level[j]['attributeNumber'] + "</td>"\
				"<td>" + attribute_properties_secound_level[j]['attributeName'] + "</td>"\
				"<td>" + attribute_properties_secound_level[j]['datatype'] + "</td>"\
				"<td>" + attribute_properties_secound_level[j]['sourceSchema'] + "</td>"\
				"<td>" + attribute_properties_secound_level[j]['sourceTable'] + "</td>"\
				"<td>" + attribute_properties_secound_level[j]['sourceAttribute'] + "</td>"\
				"<td>" + attribute_properties_secound_level[j]['sourceType'] + "</td>"\
				"<td>" + attribute_properties_secound_level[j]['sourceMultipleValues'] + "</td>"\
				"<td>" + attribute_properties_secound_level[j]['aggregation'] + "</td>"\
				"<td>" + attribute_properties_secound_level[j]['description'] + "</td>"\
				"<td>" + attribute_properties_secound_level[j]['notes'] + "</td>"\
				"</tr>"
	
		html_output_string_end = "</table><hr border='1'></body></html>"
		html_output_string = html_output_string + html_output_string_end
		
		#print(html_output_string)
		file_name = "../Output/" + tables_first_level[i]['table'] + ".html"
		html_file = open(file_name, "w")
		html_file.write(html_output_string)
		html_file.close()	

# Error handler for database connection	
except Exception as error:
	print(error)
# Close the connection in every case	
finally:
	if cur is not None:
		cur.close()
	if conn is not None:
		conn.close()

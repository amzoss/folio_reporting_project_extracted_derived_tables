"""
-------------------------------------------------------------------------------
test_script_derived_table_dictionary.py

Create Date:    2023-01-30
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
postgres_catalog_information = {}
csv_information = {}

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
	
	# read postgres informations
	counter = 0
	for record in cur.fetchall():
		
		postgres_catalog_information[counter] = {}
		postgres_catalog_information[counter]['table'] = record['table']
		postgres_catalog_information[counter]['attributeNumber'] = record['attribute #']
		postgres_catalog_information[counter]['attributeName'] = record['attribute']
		postgres_catalog_information[counter]['datatype'] = record['datatype']
		postgres_catalog_information[counter]['description'] = record['description'] 

		counter += 1

	#print(postgres_catalog_information)

	# read csv file informations
	reader = csv.DictReader(open('../csv/derived_tables_columns_doc.CSV'), delimiter=',')

	counter = 0
	for row in reader:
		
		csv_information[counter] = {}
		csv_information[counter]['table'] = row['table']
		csv_information[counter]['attributeName'] = row['attributeName']
		csv_information[counter]['sourceSchema'] = row['sourceSchema']
		csv_information[counter]['sourceTable'] = row['sourceTable']
		csv_information[counter]['sourceAttribute'] = row['sourceAttribute']
		csv_information[counter]['sourceType'] = row['sourceType']
		csv_information[counter]['sourceMultipleValues'] = row['sourceMultipleValues']
		csv_information[counter]['aggregation'] = row['aggregation']
		csv_information[counter]['notes'] = row['notes']

		counter += 1
	
	#print(csv_information)

	# Combine the dictionaries
	for i in postgres_catalog_information:
		for j in csv_information:
			if csv_information[j]['table'] == postgres_catalog_information[i]['table'] and csv_information[j]['attributeName'] == postgres_catalog_information[i]['attributeName']:
				postgres_catalog_information[i]['sourceSchema'] = csv_information[j]['sourceSchema']
				postgres_catalog_information[i]['sourceTable'] = csv_information[j]['sourceTable']
				postgres_catalog_information[i]['sourceAttribute'] = csv_information[j]['sourceAttribute']
				postgres_catalog_information[i]['sourceType'] = csv_information[j]['sourceType']
				postgres_catalog_information[i]['sourceMultipleValues'] = csv_information[j]['sourceMultipleValues']
				postgres_catalog_information[i]['aggregation'] = csv_information[j]['aggregation']
				postgres_catalog_information[i]['notes'] = csv_information[j]['notes']

	# test: print the results
	for output in postgres_catalog_information:
		if postgres_catalog_information[output]['table'] == "agreements_subscription_agreement":
			print(postgres_catalog_information[output])
	# html output
	
# Error handler for database connection	
except Exception as error:
	print(error)
# Close the connection in every case	
finally:
	if cur is not None:
		cur.close()
	if conn is not None:
		conn.close()

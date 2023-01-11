"""
-------------------------------------------------------------------------------
test_script_derived_table.py

Create Date:    2023-01-11
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
	
	# print the results
	# for the first test only an output in the shell with the data from the database. Later it is the section for the html output.
	for record in cur.fetchall():
		print(
			record['table'],
			record['attribute #'], 
			record['attribute'], 
			record['datatype'],
			record['description']
		)
	
# Error handler for database connection	
except Exception as error:
	print(error)
# Close the connection in every case	
finally:
	if cur is not None:
		cur.close()
	if conn is not None:
		conn.close()

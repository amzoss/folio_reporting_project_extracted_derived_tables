"""
-------------------------------------------------------------------------------
data_pipeline.py

Author:         Stefan Dombek <dombek@uni-leipzig.de>
Description:    This script is intended to enable the documentation of derived 
                tables. To do this, data is taken from the database catalog and 
                combined with manually created data.
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

#from binascii import Error
from cryptography.fernet import Fernet #,InvalidToken
import csv
import io
from io import StringIO
import os.path
import pandas as pd
import psycopg2
import psycopg2.extras
import requests
import tabulate
import xml.etree.ElementTree as ET

# Local packages
from pkg_output import html, markdown, markdown_index

xml = "https://metadb.dev/schema/folio/folio_derived/folio.folio_derived.xml"
print("fetching XML: " + xml)

response = requests.get(xml)

#print(response)

if response.status_code == 200:

    with open('../data/xml/folio.folio_derived.xml', 'wb') as f:
        f.write(response.content)

# If the TSV is not available
else:
    
    # Show the error message for the user
    print("Oh, something went wrong! Cannot fetch XML from SchemaSpy. Using previous file.")
    print(response.status_code)

# Close the connection
response.close()

###############################################################################
#                                                                             #
# Create DataFrame with pandas                                                #
#                                                                             #
###############################################################################

tree = ET.parse('../data/xml/folio.folio_derived.xml')

# get root element
root = tree.getroot()

# create empty list for news items
all_tables_attrs = []

# iterate tables
for tbl in root.findall('./tables/table'):

    tbl_name = tbl.attrib['name']

    # iterate child elements of item
    for attr in tbl.findall('./column'):

        # empty dictionary
        attrs = {}

        attrs['table'] = tbl_name
        attrs['attribute #'] = attr.attrib['id']
        attrs['attributeName'] = attr.attrib['name']
        attrs['datatype'] = attr.attrib['type']
        attrs['description'] = attr.attrib['remarks']

        #print(attrs)

        # append attribute row to all_tables_attrs list
        all_tables_attrs.append(attrs)
    
# Create a DataFrame with the result from the XML, set the column names and the index for the merging process
attributes = pd.DataFrame.from_records(all_tables_attrs).set_index(['table','attributeName'])

#print(attributes)


###############################################################################
#                                                                             #
# Fetch csv data                                                              #
#                                                                             #
###############################################################################

# Create a DataFrame with pandas for the data from the local file (fallback)
csv_data = pd.read_csv('../data/csv/derived_tables_columns_doc.csv').set_index(['table','attributeName'])


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
#markdown.create_markdown_files(table_names, combined, desired_columns)

# markdown index file
markdown_index.create_markdown_index_file(table_names, combined, desired_columns)

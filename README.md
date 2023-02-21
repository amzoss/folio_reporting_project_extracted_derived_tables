# FOLIO Reporting SIG - Project: Build a directory of extracted and derived tables

## Dependencies
* Python 3
* Python modules
  *  psycopg2
  *  csv
  *  io
  *  requests
  *  cryptography

## Description
https://wiki.folio.org/display/RPT/Build+a+directory+of+extracted+and+derived+tables

| Type | Description |
|:-----|:------------|
| Extracted tables | Tables that LDP creates. |
| Derived tables | Tables created by the community and located in the folio-analytics repository. |

## Directories
* /csv: Contains CSV files with additional data for enrichment.
* /python: Contains the Python scripts for the data pipeline.
  *  data_pipeline.py: Script for use with plain text login credentials
  *  data_pipeline_sec.py: Script for use with encrypted login credentials
  *  key_generator.py: Script to create a key to encrypt the login credentials and encrypt the credentials in a file
* /sql: Contains the SQL queries used.
  *  /derived_tables: Contains the query for querying information about derived tables from the PostgresSQL database catalog.

## Instructions

The Python script is written for Python 3 and tested for metadb. It assumes that derived tables exist in metadb.

1. Download the repository.
2. Create a new subdirectory with the name "Output".
3. Fill out the CSV file in the subdirectory "/csv". The data to be added to the data from the database is stored in the CSV file. In the CSV file, the "table" and "attributeName" columns must be filled out as they are stored in the database. A matching takes place later via these attributes. You can check the information beforehand using the SQL query in the "/sql/derived_tables" subdirectory.
4. Python script:
   
   4.1. Install Python on your system.
   
   4.2. Install the Python modules on your system.
   
   4.3. Login credentials
   
      4.3.1. There are two versions of the script. If you want to use login credentials in plain text, then please use data_pipeline.py. Enter the login credentials in the script there. Then please continue with point 4.4.
      
      4.3.2. If you need encrypted login credentials, please use data_pipeline_sec.py and key_generator.py. Use key_generator.py to create a key and an encrypted file with the login credentials. (Description not yet complete.)
      
   4.4. Run the Python script.

5. The generated HTML pages with the documentation have been created in the "Output" directory.

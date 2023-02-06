# FOLIO Reporting SIG - Project: Build a directory of extracted and derived tables

Description:
https://wiki.folio.org/display/RPT/Build+a+directory+of+extracted+and+derived+tables

| Type | Description |
|:-----|:------------|
| Extracted tables | Tables that LDP creates. |
| Derived tables | Tables created by the community and located in the folio-analytics repository. |

**Directories**
* /csv: Contains CSV files with additional data for enrichment.
* /python: Contains the Python script for the data pipeline.
* /sql: Contains the SQL queries used.
  *  /derived_tables: Contains the query for querying information about derived tables from the PostgresSQL database catalog.

**Instructions**

The Python script is written and tested for metadb. It assumes that derived tables exist in metadb.

1. Download the repository.
2. Create a new subdirectory with the name "Output".
3. Fill out the CSV file. In the CSV file, the "table" and "attributeName" columns must be filled out as they are stored in the database. A matching takes place later via these attributes.
4. Python script:
   
   4.1. Install Python on your system.
   
   4.2. Install the Python package "psycopg2" on your system.
   
   4.3. Open the Python file and fill out your login credentials.
   
   4.4. Run the Python script.

5. The generated HTML pages with the documentation have been created in the "Output" directory.

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

1. 

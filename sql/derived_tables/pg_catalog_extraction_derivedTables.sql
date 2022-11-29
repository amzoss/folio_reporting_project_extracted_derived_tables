-- The report lists the attributes of the derived tables from folio-analytics and links to the source in the repository.
SELECT
    columns.table_name AS "table",
    columns.ordinal_position AS "attribute #", 
    columns.column_name AS "attribute",
    columns.udt_name AS "datatype",
    pg_description.description,
    'https://github.com/folio-org/folio-analytics/tree/main/sql_metadb/derived_tables' || '/' || columns.table_name || '.sql' AS "Link"
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

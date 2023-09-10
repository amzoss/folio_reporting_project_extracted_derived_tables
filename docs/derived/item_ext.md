---
title: item_ext.sql
---
# Documentation: item_ext.sql

## Attributes:

|   Attribute # | Attribute                                 | Type      | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:------------------------------------------|:----------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | item_id                                   | uuid      |                   |                  |                      |                 |                            |               |               |         |
|             2 | item_hrid                                 | text      |                   |                  |                      |                 |                            |               |               |         |
|             3 | accession_number                          | text      |                   |                  |                      |                 |                            |               |               |         |
|             4 | barcode                                   | text      |                   |                  |                      |                 |                            |               |               |         |
|             5 | chronology                                | text      |                   |                  |                      |                 |                            |               |               |         |
|             6 | copy_number                               | text      |                   |                  |                      |                 |                            |               |               |         |
|             7 | enumeration                               | text      |                   |                  |                      |                 |                            |               |               |         |
|             8 | volume                                    | text      |                   |                  |                      |                 |                            |               |               |         |
|             9 | in_transit_destination_service_point_id   | uuid      |                   |                  |                      |                 |                            |               |               |         |
|            10 | in_transit_destination_service_point_name | text      |                   |                  |                      |                 |                            |               |               |         |
|            11 | identifier                                | text      |                   |                  |                      |                 |                            |               |               |         |
|            12 | call_number                               | text      |                   |                  |                      |                 |                            |               |               |         |
|            13 | call_number_type_id                       | uuid      |                   |                  |                      |                 |                            |               |               |         |
|            14 | call_number_type_name                     | text      |                   |                  |                      |                 |                            |               |               |         |
|            15 | effective_call_number_prefix              | text      |                   |                  |                      |                 |                            |               |               |         |
|            16 | effective_call_number                     | text      |                   |                  |                      |                 |                            |               |               |         |
|            17 | effective_call_number_suffix              | text      |                   |                  |                      |                 |                            |               |               |         |
|            18 | effective_call_number_type_id             | uuid      |                   |                  |                      |                 |                            |               |               |         |
|            19 | effective_call_number_type_name           | text      |                   |                  |                      |                 |                            |               |               |         |
|            20 | damaged_status_id                         | uuid      |                   |                  |                      |                 |                            |               |               |         |
|            21 | damaged_status_name                       | text      |                   |                  |                      |                 |                            |               |               |         |
|            22 | material_type_id                          | uuid      |                   |                  |                      |                 |                            |               |               |         |
|            23 | material_type_name                        | text      |                   |                  |                      |                 |                            |               |               |         |
|            24 | number_of_pieces                          | text      |                   |                  |                      |                 |                            |               |               |         |
|            25 | number_of_missing_pieces                  | text      |                   |                  |                      |                 |                            |               |               |         |
|            26 | permanent_loan_type_id                    | uuid      |                   |                  |                      |                 |                            |               |               |         |
|            27 | permanent_loan_type_name                  | text      |                   |                  |                      |                 |                            |               |               |         |
|            28 | temporary_loan_type_id                    | uuid      |                   |                  |                      |                 |                            |               |               |         |
|            29 | temporary_loan_type_name                  | text      |                   |                  |                      |                 |                            |               |               |         |
|            30 | permanent_location_id                     | uuid      |                   |                  |                      |                 |                            |               |               |         |
|            31 | permanent_location_name                   | text      |                   |                  |                      |                 |                            |               |               |         |
|            32 | temporary_location_id                     | uuid      |                   |                  |                      |                 |                            |               |               |         |
|            33 | temporary_location_name                   | text      |                   |                  |                      |                 |                            |               |               |         |
|            34 | effective_location_id                     | uuid      |                   |                  |                      |                 |                            |               |               |         |
|            35 | effective_location_name                   | text      |                   |                  |                      |                 |                            |               |               |         |
|            36 | description_of_pieces                     | text      |                   |                  |                      |                 |                            |               |               |         |
|            37 | status_date                               | text      |                   |                  |                      |                 |                            |               |               |         |
|            38 | status_name                               | text      |                   |                  |                      |                 |                            |               |               |         |
|            39 | holdings_record_id                        | uuid      |                   |                  |                      |                 |                            |               |               |         |
|            40 | discovery_suppress                        | bool      |                   |                  |                      |                 |                            |               |               |         |
|            41 | created_date                              | timestamp |                   |                  |                      |                 |                            |               |               |         |
|            42 | updated_by_user_id                        | uuid      |                   |                  |                      |                 |                            |               |               |         |
|            43 | updated_date                              | text      |                   |                  |                      |                 |                            |               |               |         |
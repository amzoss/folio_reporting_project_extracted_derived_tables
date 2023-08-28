---
title: holdings_ext.sql
---
# Documentation: holdings_ext.sql

## Attributes:

|   Attribute # | Attribute               | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:------------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | holdings_id             | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             2 | holdings_hrid           | text   |                   |                  |                      |                 |                            |               |               |         |
|             3 | acquisition_method      | text   |                   |                  |                      |                 |                            |               |               |         |
|             4 | call_number             | text   |                   |                  |                      |                 |                            |               |               |         |
|             5 | call_number_prefix      | text   |                   |                  |                      |                 |                            |               |               |         |
|             6 | call_number_suffix      | text   |                   |                  |                      |                 |                            |               |               |         |
|             7 | call_number_type_id     | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             8 | call_number_type_name   | text   |                   |                  |                      |                 |                            |               |               |         |
|             9 | copy_number             | text   |                   |                  |                      |                 |                            |               |               |         |
|            10 | type_id                 | uuid   |                   |                  |                      |                 |                            |               |               |         |
|            11 | type_name               | text   |                   |                  |                      |                 |                            |               |               |         |
|            12 | ill_policy_id           | text   |                   |                  |                      |                 |                            |               |               |         |
|            13 | ill_policy_name         | text   |                   |                  |                      |                 |                            |               |               |         |
|            14 | instance_id             | uuid   |                   |                  |                      |                 |                            |               |               |         |
|            15 | permanent_location_id   | uuid   |                   |                  |                      |                 |                            |               |               |         |
|            16 | permanent_location_name | text   |                   |                  |                      |                 |                            |               |               |         |
|            17 | temporary_location_id   | text   |                   |                  |                      |                 |                            |               |               |         |
|            18 | temporary_location_name | text   |                   |                  |                      |                 |                            |               |               |         |
|            19 | receipt_status          | text   |                   |                  |                      |                 |                            |               |               |         |
|            20 | retention_policy        | text   |                   |                  |                      |                 |                            |               |               |         |
|            21 | shelving_title          | text   |                   |                  |                      |                 |                            |               |               |         |
|            22 | discovery_suppress      | text   |                   |                  |                      |                 |                            |               |               |         |
|            23 | created_date            | text   |                   |                  |                      |                 |                            |               |               |         |
|            24 | updated_by_user_id      | text   |                   |                  |                      |                 |                            |               |               |         |
|            25 | updated_date            | text   |                   |                  |                      |                 |                            |               |               |         |
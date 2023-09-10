---
title: instance_ext.sql
---
## Attributes:

|   Attribute # | Attribute             | Type        | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:----------------------|:------------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | instance_id           | uuid        |                   |                  |                      |                 |                            |               |               |         |
|             2 | instance_hrid         | text        |                   |                  |                      |                 |                            |               |               |         |
|             3 | match_key             | text        |                   |                  |                      |                 |                            |               |               |         |
|             4 | record_source         | text        |                   |                  |                      |                 |                            |               |               |         |
|             5 | discovery_suppress    | bool        |                   |                  |                      |                 |                            |               |               |         |
|             6 | staff_suppress        | bool        |                   |                  |                      |                 |                            |               |               |         |
|             7 | previously_held       | bool        |                   |                  |                      |                 |                            |               |               |         |
|             8 | is_bound_with         | bool        |                   |                  |                      |                 |                            |               |               |         |
|             9 | instance_type_id      | uuid        |                   |                  |                      |                 |                            |               |               |         |
|            10 | instance_type_name    | text        |                   |                  |                      |                 |                            |               |               |         |
|            11 | title                 | text        |                   |                  |                      |                 |                            |               |               |         |
|            12 | index_title           | text        |                   |                  |                      |                 |                            |               |               |         |
|            13 | mode_of_issuance_id   | uuid        |                   |                  |                      |                 |                            |               |               |         |
|            14 | mode_of_issuance_name | text        |                   |                  |                      |                 |                            |               |               |         |
|            15 | cataloged_date        | date        |                   |                  |                      |                 |                            |               |               |         |
|            16 | created_date          | timestamptz |                   |                  |                      |                 |                            |               |               |         |
|            17 | updated_date          | timestamptz |                   |                  |                      |                 |                            |               |               |         |
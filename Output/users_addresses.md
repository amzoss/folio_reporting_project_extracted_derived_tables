---
title: users_addresses.sql
---
# Documentation: users_addresses.sql

## Attributes:

|   Attribute # | Attribute                | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:-------------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | user_id                  | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             2 | address_id               | text   |                   |                  |                      |                 |                            |               |               |         |
|             3 | address_country_id       | text   |                   |                  |                      |                 |                            |               |               |         |
|             4 | address_line_1           | text   |                   |                  |                      |                 |                            |               |               |         |
|             5 | address_line_2           | text   |                   |                  |                      |                 |                            |               |               |         |
|             6 | address_city             | text   |                   |                  |                      |                 |                            |               |               |         |
|             7 | address_region           | text   |                   |                  |                      |                 |                            |               |               |         |
|             8 | address_postal_code      | text   |                   |                  |                      |                 |                            |               |               |         |
|             9 | address_type_id          | uuid   |                   |                  |                      |                 |                            |               |               |         |
|            10 | address_type_name        | text   |                   |                  |                      |                 |                            |               |               |         |
|            11 | address_type_description | text   |                   |                  |                      |                 |                            |               |               |         |
|            12 | is_primary_address       | bool   |                   |                  |                      |                 |                            |               |               |         |
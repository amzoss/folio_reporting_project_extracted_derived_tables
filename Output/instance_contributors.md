---
title: instance_contributors.sql
---
# Documentation: instance_contributors.sql

## Attributes:

|   Attribute # | Attribute                  | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:---------------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | instance_id                | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             2 | instance_hrid              | text   |                   |                  |                      |                 |                            |               |               |         |
|             3 | contributor_name           | text   |                   |                  |                      |                 |                            |               |               |         |
|             4 | contributor_is_primary     | bool   |                   |                  |                      |                 |                            |               |               |         |
|             5 | contributor_type_id        | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             6 | contributor_type_name      | text   |                   |                  |                      |                 |                            |               |               |         |
|             7 | contributor_type_text      | text   |                   |                  |                      |                 |                            |               |               |         |
|             8 | contributor_name_type_id   | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             9 | contributor_name_type_name | text   |                   |                  |                      |                 |                            |               |               |         |
|            10 | contributor_ordinality     | int8   |                   |                  |                      |                 |                            |               |               |         |
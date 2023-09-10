---
title: instance_relationships_ext.sql
---
## Attributes:

|   Attribute # | Attribute                      | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:-------------------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | relationship_id                | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             2 | relationship_type_id           | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             3 | relationship_type_name         | text   |                   |                  |                      |                 |                            |               |               |         |
|             4 | relationship_sub_instance_id   | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             5 | relationship_super_instance_id | uuid   |                   |                  |                      |                 |                            |               |               |         |
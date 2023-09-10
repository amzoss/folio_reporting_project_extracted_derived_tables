---
title: po_prod_ids.sql
---
## Attributes:

|   Attribute # | Attribute       | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description                                              | Notes   |
|--------------:|:----------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:---------------------------------------------------------|:--------|
|             1 | pol_id          | uuid   |                   |                  |                      |                 |                            |               | UUID identifying this purchase order line                |         |
|             2 | pol_number      | text   |                   |                  |                      |                 |                            |               | A human readable ID assigned to this purchase order line |         |
|             3 | product_id      | text   |                   |                  |                      |                 |                            |               | The actual product identifier                            |         |
|             4 | product_id_type | text   |                   |                  |                      |                 |                            |               | The type of product identifier                           |         |
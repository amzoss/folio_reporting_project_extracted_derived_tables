---
title: po_lines_tags.sql
---
# Documentation: po_lines_tags.sql

## Attributes:

|   Attribute # | Attribute          | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description                                             | Notes   |
|--------------:|:-------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------------------------------------------------|:--------|
|             1 | pol_id             | uuid   |                   |                  |                      |                 |                            |               | UUID identifying this purchase order line               |         |
|             2 | pol_tag            | text   |                   |                  |                      |                 |                            |               | Arbitrary tags associated with this purchase order line |         |
|             3 | pol_tag_ordinality | int8   |                   |                  |                      |                 |                            |               | The ordinality of the tag associated with the po line   |         |
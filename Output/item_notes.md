---
title: item_notes.sql
---
# Documentation: item_notes.sql

## Attributes:

|   Attribute # | Attribute          | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:-------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | item_id            | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             2 | item_hrid          | text   |                   |                  |                      |                 |                            |               |               |         |
|             3 | holdings_record_id | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             4 | note_type_id       | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             5 | note_type_name     | text   |                   |                  |                      |                 |                            |               |               |         |
|             6 | note               | text   |                   |                  |                      |                 |                            |               |               |         |
|             7 | staff_only         | bool   |                   |                  |                      |                 |                            |               |               |         |
|             8 | note_ordinality    | int8   |                   |                  |                      |                 |                            |               |               |         |
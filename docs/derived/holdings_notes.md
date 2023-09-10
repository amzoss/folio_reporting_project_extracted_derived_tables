---
title: holdings_notes.sql
---
## Attributes:

|   Attribute # | Attribute               | Type      | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:------------------------|:----------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | instance_id             | uuid      |                   |                  |                      |                 |                            |               |               |         |
|             2 | instance_hrid           | text      |                   |                  |                      |                 |                            |               |               |         |
|             3 | holding_id              | uuid      |                   |                  |                      |                 |                            |               |               |         |
|             4 | holding_hrid            | text      |                   |                  |                      |                 |                            |               |               |         |
|             5 | note                    | text      |                   |                  |                      |                 |                            |               |               |         |
|             6 | note_type_name          | text      |                   |                  |                      |                 |                            |               |               |         |
|             7 | note_type_id            | uuid      |                   |                  |                      |                 |                            |               |               |         |
|             8 | note_ordinality         | int8      |                   |                  |                      |                 |                            |               |               |         |
|             9 | note_date_created       | timestamp |                   |                  |                      |                 |                            |               |               |         |
|            10 | note_created_by_user_id | text      |                   |                  |                      |                 |                            |               |               |         |
|            11 | note_date_updated       | text      |                   |                  |                      |                 |                            |               |               |         |
|            12 | note_updated_by_user_id | text      |                   |                  |                      |                 |                            |               |               |         |
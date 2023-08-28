---
title: holdings_administrative_notes.sql
---
# Documentation: holdings_administrative_notes.sql

## Attributes:

|   Attribute # | Attribute                      | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description                                                                                                       | Notes   |
|--------------:|:-------------------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:------------------------------------------------------------------------------------------------------------------|:--------|
|             1 | instance_id                    | uuid   |                   |                  |                      |                 |                            |               | Inventory instances identifier                                                                                    |         |
|             2 | holdings_id                    | uuid   |                   |                  |                      |                 |                            |               | the unique ID of the holdings record, UUID                                                                        |         |
|             3 | holdings_hrid                  | text   |                   |                  |                      |                 |                            |               | the human readable ID, also called eye readable ID. A system-assigned sequential ID which maps to the Instance ID |         |
|             4 | administrative_note            | text   |                   |                  |                      |                 |                            |               | Administrative notes                                                                                              |         |
|             5 | administrative_note_ordinality | int8   |                   |                  |                      |                 |                            |               | Administrative note ordinality                                                                                    |         |
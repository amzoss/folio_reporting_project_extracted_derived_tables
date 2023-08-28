---
title: instance_notes.sql
---
# Documentation: instance_notes.sql

## Attributes:

|   Attribute # | Attribute                 | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:--------------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | instance_id               | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             2 | instance_hrid             | text   |                   |                  |                      |                 |                            |               |               |         |
|             3 | instance_note             | text   |                   |                  |                      |                 |                            |               |               |         |
|             4 | staff_only_note           | bool   |                   |                  |                      |                 |                            |               |               |         |
|             5 | instance_note_type_id     | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             6 | instance_note_type_name   | text   |                   |                  |                      |                 |                            |               |               |         |
|             7 | instance_notes_ordinality | int8   |                   |                  |                      |                 |                            |               |               |         |
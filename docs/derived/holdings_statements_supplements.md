---
title: holdings_statements_supplements.sql
---
# Documentation: holdings_statements_supplements.sql

## Attributes:

|   Attribute # | Attribute            | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:---------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | instance_id          | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             2 | instance_hrid        | text   |                   |                  |                      |                 |                            |               |               |         |
|             3 | holdings_id          | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             4 | holdings_hrid        | text   |                   |                  |                      |                 |                            |               |               |         |
|             5 | holdings_statement   | text   |                   |                  |                      |                 |                            |               |               |         |
|             6 | public_note          | text   |                   |                  |                      |                 |                            |               |               |         |
|             7 | staff_note           | text   |                   |                  |                      |                 |                            |               |               |         |
|             8 | statement_ordinality | int8   |                   |                  |                      |                 |                            |               |               |         |
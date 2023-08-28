---
title: loans_renewal_dates.sql
---
# Documentation: loans_renewal_dates.sql

## Attributes:

|   Attribute # | Attribute          | Type        | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:-------------------|:------------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | loan_action_date   | timestamptz |                   |                  |                      |                 |                            |               |               |         |
|             2 | loan_id            | uuid        |                   |                  |                      |                 |                            |               |               |         |
|             3 | item_id            | text        |                   |                  |                      |                 |                            |               |               |         |
|             4 | loan_action        | text        |                   |                  |                      |                 |                            |               |               |         |
|             5 | loan_renewal_count | text        |                   |                  |                      |                 |                            |               |               |         |
|             6 | loan_status        | text        |                   |                  |                      |                 |                            |               |               |         |
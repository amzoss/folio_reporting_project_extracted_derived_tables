---
title: po_ongoing.sql
---
## Attributes:

|   Attribute # | Attribute                  | Type        | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description                                                     | Notes   |
|--------------:|:---------------------------|:------------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:----------------------------------------------------------------|:--------|
|             1 | po_id                      | uuid        |                   |                  |                      |                 |                            |               | UUID of this purchase order                                     |         |
|             2 | po_ongoing_interval        | int4        |                   |                  |                      |                 |                            |               | The subscription interval in days                               |         |
|             3 | po_ongoing_is_subscription | bool        |                   |                  |                      |                 |                            |               | Whether or not this is a subscription                           |         |
|             4 | po_ongoing_manual_renewal  | bool        |                   |                  |                      |                 |                            |               | Whether or not this is a manual renewal                         |         |
|             5 | po_ongoing_renewal_date    | timestamptz |                   |                  |                      |                 |                            |               | The date this Ongoing PO's order lines were renewed             |         |
|             6 | po_ongoing_review_period   | int4        |                   |                  |                      |                 |                            |               | Time prior to renewal where changes can be made to subscription |         |
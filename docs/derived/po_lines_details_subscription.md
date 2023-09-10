---
title: po_lines_details_subscription.sql
---
## Attributes:

|   Attribute # | Attribute                 | Type        | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description                               | Notes   |
|--------------:|:--------------------------|:------------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:------------------------------------------|:--------|
|             1 | pol_id                    | uuid        |                   |                  |                      |                 |                            |               | UUID identifying this purchase order line |         |
|             2 | pol_subscription_from     | timestamptz |                   |                  |                      |                 |                            |               | the start date of the subscription        |         |
|             3 | pol_subscription_to       | timestamptz |                   |                  |                      |                 |                            |               | the end date of the subscription          |         |
|             4 | pol_subscription_interval | int4        |                   |                  |                      |                 |                            |               | the subscription interval in days         |         |
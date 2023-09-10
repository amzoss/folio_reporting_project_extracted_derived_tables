---
title: feesfines_accounts_actions.sql
---
## Attributes:

|   Attribute # | Attribute               | Type        | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:------------------------|:------------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | fine_account_id         | uuid        |                   |                  |                      |                 |                            |               |               |         |
|             2 | fine_account_amount     | numeric     |                   |                  |                      |                 |                            |               |               |         |
|             3 | fine_date               | timestamptz |                   |                  |                      |                 |                            |               |               |         |
|             4 | fine_updated_date       | timestamptz |                   |                  |                      |                 |                            |               |               |         |
|             5 | fee_fine_id             | uuid        |                   |                  |                      |                 |                            |               |               |         |
|             6 | owner_id                | uuid        |                   |                  |                      |                 |                            |               |               |         |
|             7 | fee_fine_owner          | text        |                   |                  |                      |                 |                            |               |               |         |
|             8 | fee_fine_type           | text        |                   |                  |                      |                 |                            |               |               |         |
|             9 | material_type_id        | uuid        |                   |                  |                      |                 |                            |               |               |         |
|            10 | material_type           | text        |                   |                  |                      |                 |                            |               |               |         |
|            11 | payment_status          | text        |                   |                  |                      |                 |                            |               |               |         |
|            12 | fine_status             | text        |                   |                  |                      |                 |                            |               |               |         |
|            13 | account_user_id         | uuid        |                   |                  |                      |                 |                            |               |               |         |
|            14 | transaction_id          | uuid        |                   |                  |                      |                 |                            |               |               |         |
|            15 | account_id              | uuid        |                   |                  |                      |                 |                            |               |               |         |
|            16 | transaction_amount      | numeric     |                   |                  |                      |                 |                            |               |               |         |
|            17 | account_balance         | numeric     |                   |                  |                      |                 |                            |               |               |         |
|            18 | type_action             | text        |                   |                  |                      |                 |                            |               |               |         |
|            19 | transaction_date        | timestamptz |                   |                  |                      |                 |                            |               |               |         |
|            20 | transaction_location    | text        |                   |                  |                      |                 |                            |               |               |         |
|            21 | transaction_information | text        |                   |                  |                      |                 |                            |               |               |         |
|            22 | operator_id             | text        |                   |                  |                      |                 |                            |               |               |         |
|            23 | payment_method          | text        |                   |                  |                      |                 |                            |               |               |         |
|            24 | user_id                 | uuid        |                   |                  |                      |                 |                            |               |               |         |
|            25 | user_patron_group_id    | uuid        |                   |                  |                      |                 |                            |               |               |         |
|            26 | patron_group_id         | uuid        |                   |                  |                      |                 |                            |               |               |         |
|            27 | patron_group_name       | text        |                   |                  |                      |                 |                            |               |               |         |
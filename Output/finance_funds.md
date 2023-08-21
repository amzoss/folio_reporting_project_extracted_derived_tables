---
title: finance_funds.sql
---
# Documentation: finance_funds.sql

## Attributes:

|   Attribute # | Attribute                | Type        | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description                                     | Notes   |
|--------------:|:-------------------------|:------------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:------------------------------------------------|:--------|
|             1 | fiscal_year_id           | uuid        |                   |                  |                      |                 |                            |               | UUID of the fiscal year record                  |         |
|             2 | fiscal_year_code         | text        |                   |                  |                      |                 |                            |               | The code of the fiscal year                     |         |
|             3 | fiscal_year_name         | text        |                   |                  |                      |                 |                            |               | The name of the fiscal year                     |         |
|             4 | fiscal_year_period_start | timestamptz |                   |                  |                      |                 |                            |               | The start date of the fiscal year               |         |
|             5 | fiscal_year_period_end   | timestamptz |                   |                  |                      |                 |                            |               | The end date of the fiscal year                 |         |
|             6 | fiscal_year_description  | text        |                   |                  |                      |                 |                            |               | The description of the fiscal year              |         |
|             7 | budget_id                | uuid        |                   |                  |                      |                 |                            |               | UUID of this budget                             |         |
|             8 | budget_name              | text        |                   |                  |                      |                 |                            |               | The name of the budget                          |         |
|             9 | budget_status            | text        |                   |                  |                      |                 |                            |               | The status of the budget                        |         |
|            10 | fund_id                  | uuid        |                   |                  |                      |                 |                            |               | UUID of this fund                               |         |
|            11 | fund_code                | text        |                   |                  |                      |                 |                            |               | A unique code associated with the fund          |         |
|            12 | fund_name                | text        |                   |                  |                      |                 |                            |               | The name of this fund                           |         |
|            13 | fund_status              | text        |                   |                  |                      |                 |                            |               | The current status of this fund                 |         |
|            14 | fund_description         | text        |                   |                  |                      |                 |                            |               | The description of this fund                    |         |
|            15 | fund_type_id             | uuid        |                   |                  |                      |                 |                            |               | UUID of the fund type associated with this fund |         |
|            16 | fund_type_name           | text        |                   |                  |                      |                 |                            |               | Name of fund type                               |         |
|            17 | ledger_id                | uuid        |                   |                  |                      |                 |                            |               | UUID of this ledger                             |         |
|            18 | ledger_code              | text        |                   |                  |                      |                 |                            |               | The code for the ledger                         |         |
|            19 | ledger_name              | text        |                   |                  |                      |                 |                            |               | The name of the ledger                          |         |
|            20 | ledger_status            | text        |                   |                  |                      |                 |                            |               | The status of the ledger                        |         |
|            21 | ledger_description       | text        |                   |                  |                      |                 |                            |               | The description of the ledger                   |         |
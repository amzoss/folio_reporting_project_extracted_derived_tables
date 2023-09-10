---
title: finance_invoice_transactions.sql
---
# Documentation: finance_invoice_transactions.sql

## Attributes:

|   Attribute # | Attribute                         | Type        | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:----------------------------------|:------------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | invoice_id                        | uuid        |                   |                  |                      |                 |                            |               |               |         |
|             2 | folio_invoice_number              | text        |                   |                  |                      |                 |                            |               |               |         |
|             3 | vendor_id                         | uuid        |                   |                  |                      |                 |                            |               |               |         |
|             4 | vendor_name                       | text        |                   |                  |                      |                 |                            |               |               |         |
|             5 | vendor_invoice_number             | text        |                   |                  |                      |                 |                            |               |               |         |
|             6 | invoice_date                      | timestamptz |                   |                  |                      |                 |                            |               |               |         |
|             7 | invoice_status                    | text        |                   |                  |                      |                 |                            |               |               |         |
|             8 | invoice_line_id                   | uuid        |                   |                  |                      |                 |                            |               |               |         |
|             9 | invoice_line_total                | numeric     |                   |                  |                      |                 |                            |               |               |         |
|            10 | invoice_currency                  | text        |                   |                  |                      |                 |                            |               |               |         |
|            11 | invoice_line_distribution_value   | numeric     |                   |                  |                      |                 |                            |               |               |         |
|            12 | invoice_line_distribution_type    | text        |                   |                  |                      |                 |                            |               |               |         |
|            13 | invoice_line_fiscal_year_id       | uuid        |                   |                  |                      |                 |                            |               |               |         |
|            14 | invoice_line_fiscal_year          | text        |                   |                  |                      |                 |                            |               |               |         |
|            15 | invoice_line_ledger_id            | uuid        |                   |                  |                      |                 |                            |               |               |         |
|            16 | invoice_line_ledger_name          | text        |                   |                  |                      |                 |                            |               |               |         |
|            17 | invoice_line_budget_id            | uuid        |                   |                  |                      |                 |                            |               |               |         |
|            18 | invoice_line_budget_name          | text        |                   |                  |                      |                 |                            |               |               |         |
|            19 | invoice_line_fund_id              | uuid        |                   |                  |                      |                 |                            |               |               |         |
|            20 | invoice_line_fund_code            | text        |                   |                  |                      |                 |                            |               |               |         |
|            21 | invoice_exchange_rate             | numeric     |                   |                  |                      |                 |                            |               |               |         |
|            22 | invoice_line_transaction_id       | uuid        |                   |                  |                      |                 |                            |               |               |         |
|            23 | invoice_line_transaction_amount   | numeric     |                   |                  |                      |                 |                            |               |               |         |
|            24 | invoice_line_transaction_currency | text        |                   |                  |                      |                 |                            |               |               |         |
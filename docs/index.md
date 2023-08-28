---
Derived Table Documentation
---

## Documentation: [agreements_subscription_agreement_org_ext](agreements_subscription_agreement_org_ext.md)

### Attributes:

|   Attribute # | Attribute                 | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description                                     | Notes   |
|--------------:|:--------------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:------------------------------------------------|:--------|
|             1 | sao_id                    | uuid   |                   |                  |                      |                 |                            |               | UUID for subscription and organization pairing  |         |
|             2 | subscription_agreement_id | uuid   |                   |                  |                      |                 |                            |               | UUId for the subscritpion and agreement pairing |         |
|             3 | sao_org_id                | uuid   |                   |                  |                      |                 |                            |               | The unique UUID for an organization             |         |
|             4 | sao_org_name              | text   |                   |                  |                      |                 |                            |               | The name of an organization                     |         |
|             5 | sao_role_id               | uuid   |                   |                  |                      |                 |                            |               | ID of the type of provider role                 |         |
|             6 | sao_role_value            | text   |                   |                  |                      |                 |                            |               | Name of the type of provider role               |         |
|             7 | sao_role_label            | text   |                   |                  |                      |                 |                            |               | Public name of the type of provider role        |         |
|             8 | sao_note                  | text   |                   |                  |                      |                 |                            |               | Notes attached                                  |         |
|             9 | org_orgs_uuid             | uuid   |                   |                  |                      |                 |                            |               | UUID of organization attached to the agreement  |         |

## Documentation: [feesfines_accounts_actions](feesfines_accounts_actions.md)

### Attributes:

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

## Documentation: [finance_funds](finance_funds.md)

### Attributes:

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

## Documentation: [finance_invoice_transactions](finance_invoice_transactions.md)

### Attributes:

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

## Documentation: [finance_transaction_invoices](finance_transaction_invoices.md)

### Attributes:

|   Attribute # | Attribute                    | Type    | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description                                                                                                                  | Notes   |
|--------------:|:-----------------------------|:--------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:-----------------------------------------------------------------------------------------------------------------------------|:--------|
|             1 | transaction_id               | uuid    |                   |                  |                      |                 |                            |               | UUID of this transaction                                                                                                     |         |
|             2 | transaction_amount           | numeric |                   |                  |                      |                 |                            |               | The amount of this transaction. For encumbrances: This is initialAmountEncumbered - (amountAwaitingPayment + amountExpended) |         |
|             3 | transaction_currency         | text    |                   |                  |                      |                 |                            |               | Currency code for this transaction - from the system currency                                                                |         |
|             4 | transaction_created_date     | date    |                   |                  |                      |                 |                            |               | Date and time when the record was created                                                                                    |         |
|             5 | transaction_updated_date     | date    |                   |                  |                      |                 |                            |               | Date and time when the record was last updated                                                                               |         |
|             6 | transaction_description      | text    |                   |                  |                      |                 |                            |               | Description of this transaction                                                                                              |         |
|             7 | transaction_expense_class_id | uuid    |                   |                  |                      |                 |                            |               | UUID of the associated expense class                                                                                         |         |
|             8 | transaction_fiscal_year_id   | uuid    |                   |                  |                      |                 |                            |               | UUID of the fiscal year that the transaction is taking place in                                                              |         |
|             9 | transaction_from_fund_id     | uuid    |                   |                  |                      |                 |                            |               | UUID of the fund money is moving from                                                                                        |         |
|            10 | transaction_from_fund_name   | text    |                   |                  |                      |                 |                            |               | The name of this fund money is moving from                                                                                   |         |
|            11 | transaction_from_fund_code   | text    |                   |                  |                      |                 |                            |               | A unique code associated with the fund money is moving from                                                                  |         |
|            12 | transaction_to_fund_id       | uuid    |                   |                  |                      |                 |                            |               | UUID of the fund money is moving to                                                                                          |         |
|            13 | transaction_to_fund_name     | text    |                   |                  |                      |                 |                            |               | The name of the fund money is moving to                                                                                      |         |
|            14 | transaction_to_fund_code     | text    |                   |                  |                      |                 |                            |               | A unique code associated with the fund money is moving to                                                                    |         |
|            15 | effective_fund_id            | uuid    |                   |                  |                      |                 |                            |               | UUID of the current effective fund                                                                                           |         |
|            16 | effective_fund_name          | text    |                   |                  |                      |                 |                            |               | The name of the current effective fund                                                                                       |         |
|            17 | effective_fund_code          | text    |                   |                  |                      |                 |                            |               | A unique code for the current effective fund                                                                                 |         |
|            18 | transaction_from_budget_id   | uuid    |                   |                  |                      |                 |                            |               | UUID of the budget the transaction is coming from                                                                            |         |
|            19 | transaction_from_budget_name | text    |                   |                  |                      |                 |                            |               | The name of the budget the transation is comign from                                                                         |         |
|            20 | invoice_id                   | uuid    |                   |                  |                      |                 |                            |               | UUID of this invoice                                                                                                         |         |
|            21 | invoice_line_id              | uuid    |                   |                  |                      |                 |                            |               | UUID of the invoice line associated with this fund distribution                                                              |         |
|            22 | transaction_type             | text    |                   |                  |                      |                 |                            |               | This describes the type of transaction                                                                                       |         |
|            23 | invoice_date                 | text    |                   |                  |                      |                 |                            |               | Invoice date                                                                                                                 |         |
|            24 | invoice_payment_date         | text    |                   |                  |                      |                 |                            |               | When the invoice was actually paid                                                                                           |         |
|            25 | invoice_exchange_rate        | numeric |                   |                  |                      |                 |                            |               | Exchange rate                                                                                                                |         |
|            26 | invoice_line_total           | numeric |                   |                  |                      |                 |                            |               | Total of each separate invoice line                                                                                          |         |
|            27 | invoice_currency             | text    |                   |                  |                      |                 |                            |               | Ideally this is the ISO code and not something the user defines                                                              |         |
|            28 | po_line_id                   | text    |                   |                  |                      |                 |                            |               | UUID of encumbrance record associated with this fund distribution                                                            |         |
|            29 | invoice_vendor_id            | uuid    |                   |                  |                      |                 |                            |               | UUID for vendor                                                                                                              |         |
|            30 | invoice_vendor_name          | text    |                   |                  |                      |                 |                            |               | Name of vendor                                                                                                               |         |

## Documentation: [finance_transaction_purchase_order](finance_transaction_purchase_order.md)

### Attributes:

|   Attribute # | Attribute                                       | Type    | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description                                                                                                                  | Notes   |
|--------------:|:------------------------------------------------|:--------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:-----------------------------------------------------------------------------------------------------------------------------|:--------|
|             1 | transaction_id                                  | uuid    |                   |                  |                      |                 |                            |               | UUID of this transaction                                                                                                     |         |
|             2 | transaction_amount                              | numeric |                   |                  |                      |                 |                            |               | The amount of this transaction. For encumbrances: This is initialAmountEncumbered - (amountAwaitingPayment + amountExpended) |         |
|             3 | transaction_currency                            | text    |                   |                  |                      |                 |                            |               | Currency code for this transaction - from the system currency                                                                |         |
|             4 | transaction_expense_class_id                    | uuid    |                   |                  |                      |                 |                            |               | UUID of the associated expense class                                                                                         |         |
|             5 | transaction_fiscal_year_id                      | uuid    |                   |                  |                      |                 |                            |               | UUID of the fiscal year that the transaction is taking place in                                                              |         |
|             6 | transaction_from_fund_id                        | uuid    |                   |                  |                      |                 |                            |               | UUID of the fund money is moving from                                                                                        |         |
|             7 | transaction_from_fund_name                      | text    |                   |                  |                      |                 |                            |               | The name of this fund                                                                                                        |         |
|             8 | transaction_from_fund_code                      | text    |                   |                  |                      |                 |                            |               | A unique code associated with the fund                                                                                       |         |
|             9 | transaction_from_budget_id                      | uuid    |                   |                  |                      |                 |                            |               | UUID of this budget                                                                                                          |         |
|            10 | transaction_from_budget_name                    | text    |                   |                  |                      |                 |                            |               | The name of the budget                                                                                                       |         |
|            11 | transaction_encumbrance_amount_awaiting_payment | numeric |                   |                  |                      |                 |                            |               | Deprecated! Going to be removed in next release. The amount of awaiting for payment                                          |         |
|            12 | transaction_encumbrance_amount_expended         | numeric |                   |                  |                      |                 |                            |               | The amount currently expended by this encumbrance                                                                            |         |
|            13 | transaction_encumbrance_initial_amount          | numeric |                   |                  |                      |                 |                            |               | The initial amount of this encumbrance. Should not change once create                                                        |         |
|            14 | transaction_encumbrance_order_type              | text    |                   |                  |                      |                 |                            |               | Taken from the purchase order                                                                                                |         |
|            15 | transaction_encumbrance_subscription            | text    |                   |                  |                      |                 |                            |               | Taken from the purchase Order,for fiscal year rollover                                                                       |         |
|            16 | transaction_encumbrance_status                  | text    |                   |                  |                      |                 |                            |               | The status of this encumbrance                                                                                               |         |
|            17 | po_line_id                                      | uuid    |                   |                  |                      |                 |                            |               | UUID referencing the poLine that represents the package that this POLs title belongs to                                      |         |
|            18 | po_id                                           | uuid    |                   |                  |                      |                 |                            |               | UUID identifying this purchase order line                                                                                    |         |
|            19 | pol_number                                      | text    |                   |                  |                      |                 |                            |               | A human readable number assigned to this PO line                                                                             |         |
|            20 | pol_description                                 | text    |                   |                  |                      |                 |                            |               | purchase order line description                                                                                              |         |
|            21 | pol_acquisition_method                          | text    |                   |                  |                      |                 |                            |               | UUID of the acquisition method for this purchase order line                                                                  |         |
|            22 | po_order_type                                   | text    |                   |                  |                      |                 |                            |               | the purchase order type                                                                                                      |         |
|            23 | po_vendor_id                                    | uuid    |                   |                  |                      |                 |                            |               | UUID of the vendor record                                                                                                    |         |
|            24 | po_vendor_name                                  | text    |                   |                  |                      |                 |                            |               | The name of vendor                                                                                                           |         |

## Documentation: [holdings_administrative_notes](holdings_administrative_notes.md)

### Attributes:

|   Attribute # | Attribute                      | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description                                                                                                       | Notes   |
|--------------:|:-------------------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:------------------------------------------------------------------------------------------------------------------|:--------|
|             1 | instance_id                    | uuid   |                   |                  |                      |                 |                            |               | Inventory instances identifier                                                                                    |         |
|             2 | holdings_id                    | uuid   |                   |                  |                      |                 |                            |               | the unique ID of the holdings record, UUID                                                                        |         |
|             3 | holdings_hrid                  | text   |                   |                  |                      |                 |                            |               | the human readable ID, also called eye readable ID. A system-assigned sequential ID which maps to the Instance ID |         |
|             4 | administrative_note            | text   |                   |                  |                      |                 |                            |               | Administrative notes                                                                                              |         |
|             5 | administrative_note_ordinality | int8   |                   |                  |                      |                 |                            |               | Administrative note ordinality                                                                                    |         |

## Documentation: [holdings_electronic_access](holdings_electronic_access.md)

### Attributes:

|   Attribute # | Attribute              | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:-----------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | instance_id            | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             2 | instance_hrid          | text   |                   |                  |                      |                 |                            |               |               |         |
|             3 | holdings_id            | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             4 | holdings_hrid          | text   |                   |                  |                      |                 |                            |               |               |         |
|             5 | relationship_id        | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             6 | relationship_name      | text   |                   |                  |                      |                 |                            |               |               |         |
|             7 | uri                    | text   |                   |                  |                      |                 |                            |               |               |         |
|             8 | link_text              | text   |                   |                  |                      |                 |                            |               |               |         |
|             9 | material_specification | text   |                   |                  |                      |                 |                            |               |               |         |
|            10 | public_note            | text   |                   |                  |                      |                 |                            |               |               |         |
|            11 | eaccess_ordinality     | int8   |                   |                  |                      |                 |                            |               |               |         |

## Documentation: [holdings_ext](holdings_ext.md)

### Attributes:

|   Attribute # | Attribute               | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:------------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | holdings_id             | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             2 | holdings_hrid           | text   |                   |                  |                      |                 |                            |               |               |         |
|             3 | acquisition_method      | text   |                   |                  |                      |                 |                            |               |               |         |
|             4 | call_number             | text   |                   |                  |                      |                 |                            |               |               |         |
|             5 | call_number_prefix      | text   |                   |                  |                      |                 |                            |               |               |         |
|             6 | call_number_suffix      | text   |                   |                  |                      |                 |                            |               |               |         |
|             7 | call_number_type_id     | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             8 | call_number_type_name   | text   |                   |                  |                      |                 |                            |               |               |         |
|             9 | copy_number             | text   |                   |                  |                      |                 |                            |               |               |         |
|            10 | type_id                 | uuid   |                   |                  |                      |                 |                            |               |               |         |
|            11 | type_name               | text   |                   |                  |                      |                 |                            |               |               |         |
|            12 | ill_policy_id           | text   |                   |                  |                      |                 |                            |               |               |         |
|            13 | ill_policy_name         | text   |                   |                  |                      |                 |                            |               |               |         |
|            14 | instance_id             | uuid   |                   |                  |                      |                 |                            |               |               |         |
|            15 | permanent_location_id   | uuid   |                   |                  |                      |                 |                            |               |               |         |
|            16 | permanent_location_name | text   |                   |                  |                      |                 |                            |               |               |         |
|            17 | temporary_location_id   | text   |                   |                  |                      |                 |                            |               |               |         |
|            18 | temporary_location_name | text   |                   |                  |                      |                 |                            |               |               |         |
|            19 | receipt_status          | text   |                   |                  |                      |                 |                            |               |               |         |
|            20 | retention_policy        | text   |                   |                  |                      |                 |                            |               |               |         |
|            21 | shelving_title          | text   |                   |                  |                      |                 |                            |               |               |         |
|            22 | discovery_suppress      | text   |                   |                  |                      |                 |                            |               |               |         |
|            23 | created_date            | text   |                   |                  |                      |                 |                            |               |               |         |
|            24 | updated_by_user_id      | text   |                   |                  |                      |                 |                            |               |               |         |
|            25 | updated_date            | text   |                   |                  |                      |                 |                            |               |               |         |

## Documentation: [holdings_notes](holdings_notes.md)

### Attributes:

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

## Documentation: [holdings_statements](holdings_statements.md)

### Attributes:

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

## Documentation: [holdings_statements_indexes](holdings_statements_indexes.md)

### Attributes:

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

## Documentation: [holdings_statements_supplements](holdings_statements_supplements.md)

### Attributes:

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

## Documentation: [holdings_statistical_codes](holdings_statistical_codes.md)

### Attributes:

|   Attribute # | Attribute                   | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:----------------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | instance_id                 | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             2 | instance_hrid               | text   |                   |                  |                      |                 |                            |               |               |         |
|             3 | holdings_id                 | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             4 | holdings_hrid               | text   |                   |                  |                      |                 |                            |               |               |         |
|             5 | statistical_code_id         | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             6 | statistical_code_type_id    | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             7 | statistical_code_type_name  | text   |                   |                  |                      |                 |                            |               |               |         |
|             8 | statistical_code            | text   |                   |                  |                      |                 |                            |               |               |         |
|             9 | statistical_code_name       | text   |                   |                  |                      |                 |                            |               |               |         |
|            10 | statistical_code_ordinality | int8   |                   |                  |                      |                 |                            |               |               |         |

## Documentation: [holdings_tags](holdings_tags.md)

### Attributes:

|   Attribute # | Attribute               | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:------------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | instance_id             | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             2 | holdings_id             | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             3 | holdings_hrid           | text   |                   |                  |                      |                 |                            |               |               |         |
|             4 | holdings_tag            | text   |                   |                  |                      |                 |                            |               |               |         |
|             5 | holdings_tag_ordinality | int8   |                   |                  |                      |                 |                            |               |               |         |

## Documentation: [instance_administrative_notes](instance_administrative_notes.md)

### Attributes:

|   Attribute # | Attribute                      | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:-------------------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | instance_id                    | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             2 | instance_hrid                  | text   |                   |                  |                      |                 |                            |               |               |         |
|             3 | administrative_note            | text   |                   |                  |                      |                 |                            |               |               |         |
|             4 | administrative_note_ordinality | int8   |                   |                  |                      |                 |                            |               |               |         |

## Documentation: [instance_alternative_titles](instance_alternative_titles.md)

### Attributes:

|   Attribute # | Attribute                    | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:-----------------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | instance_id                  | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             2 | instance_hrid                | text   |                   |                  |                      |                 |                            |               |               |         |
|             3 | alternative_title            | text   |                   |                  |                      |                 |                            |               |               |         |
|             4 | alternative_title_type_id    | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             5 | alternative_title_ordinality | int8   |                   |                  |                      |                 |                            |               |               |         |
|             6 | alternative_title_type_name  | text   |                   |                  |                      |                 |                            |               |               |         |

## Documentation: [instance_classifications](instance_classifications.md)

### Attributes:

|   Attribute # | Attribute                 | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:--------------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | instance_id               | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             2 | instance_hrid             | text   |                   |                  |                      |                 |                            |               |               |         |
|             3 | classification_number     | text   |                   |                  |                      |                 |                            |               |               |         |
|             4 | classification_type_id    | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             5 | classification_ordinality | int8   |                   |                  |                      |                 |                            |               |               |         |
|             6 | classification_name       | text   |                   |                  |                      |                 |                            |               |               |         |

## Documentation: [instance_contributors](instance_contributors.md)

### Attributes:

|   Attribute # | Attribute                  | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:---------------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | instance_id                | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             2 | instance_hrid              | text   |                   |                  |                      |                 |                            |               |               |         |
|             3 | contributor_name           | text   |                   |                  |                      |                 |                            |               |               |         |
|             4 | contributor_is_primary     | bool   |                   |                  |                      |                 |                            |               |               |         |
|             5 | contributor_type_id        | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             6 | contributor_type_name      | text   |                   |                  |                      |                 |                            |               |               |         |
|             7 | contributor_type_text      | text   |                   |                  |                      |                 |                            |               |               |         |
|             8 | contributor_name_type_id   | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             9 | contributor_name_type_name | text   |                   |                  |                      |                 |                            |               |               |         |
|            10 | contributor_ordinality     | int8   |                   |                  |                      |                 |                            |               |               |         |

## Documentation: [instance_editions](instance_editions.md)

### Attributes:

|   Attribute # | Attribute          | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:-------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | instance_id        | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             2 | instance_hrid      | text   |                   |                  |                      |                 |                            |               |               |         |
|             3 | edition            | text   |                   |                  |                      |                 |                            |               |               |         |
|             4 | edition_ordinality | int8   |                   |                  |                      |                 |                            |               |               |         |

## Documentation: [instance_electronic_access](instance_electronic_access.md)

### Attributes:

|   Attribute # | Attribute                    | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:-----------------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | instance_id                  | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             2 | instance_hrid                | text   |                   |                  |                      |                 |                            |               |               |         |
|             3 | uri                          | text   |                   |                  |                      |                 |                            |               |               |         |
|             4 | link_text                    | text   |                   |                  |                      |                 |                            |               |               |         |
|             5 | materials_specification      | text   |                   |                  |                      |                 |                            |               |               |         |
|             6 | public_note                  | text   |                   |                  |                      |                 |                            |               |               |         |
|             7 | relationship_id              | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             8 | relationship_name            | text   |                   |                  |                      |                 |                            |               |               |         |
|             9 | electronic_access_ordinality | int8   |                   |                  |                      |                 |                            |               |               |         |

## Documentation: [instance_ext](instance_ext.md)

### Attributes:

|   Attribute # | Attribute             | Type        | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:----------------------|:------------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | instance_id           | uuid        |                   |                  |                      |                 |                            |               |               |         |
|             2 | instance_hrid         | text        |                   |                  |                      |                 |                            |               |               |         |
|             3 | match_key             | text        |                   |                  |                      |                 |                            |               |               |         |
|             4 | record_source         | text        |                   |                  |                      |                 |                            |               |               |         |
|             5 | discovery_suppress    | bool        |                   |                  |                      |                 |                            |               |               |         |
|             6 | staff_suppress        | bool        |                   |                  |                      |                 |                            |               |               |         |
|             7 | previously_held       | bool        |                   |                  |                      |                 |                            |               |               |         |
|             8 | is_bound_with         | bool        |                   |                  |                      |                 |                            |               |               |         |
|             9 | instance_type_id      | uuid        |                   |                  |                      |                 |                            |               |               |         |
|            10 | instance_type_name    | text        |                   |                  |                      |                 |                            |               |               |         |
|            11 | title                 | text        |                   |                  |                      |                 |                            |               |               |         |
|            12 | index_title           | text        |                   |                  |                      |                 |                            |               |               |         |
|            13 | mode_of_issuance_id   | uuid        |                   |                  |                      |                 |                            |               |               |         |
|            14 | mode_of_issuance_name | text        |                   |                  |                      |                 |                            |               |               |         |
|            15 | cataloged_date        | date        |                   |                  |                      |                 |                            |               |               |         |
|            16 | created_date          | timestamptz |                   |                  |                      |                 |                            |               |               |         |
|            17 | updated_date          | timestamptz |                   |                  |                      |                 |                            |               |               |         |

## Documentation: [instance_formats](instance_formats.md)

### Attributes:

|   Attribute # | Attribute                  | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:---------------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | instance_id                | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             2 | instance_hrid              | text   |                   |                  |                      |                 |                            |               |               |         |
|             3 | instance_format_id         | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             4 | instance_format_ordinality | int8   |                   |                  |                      |                 |                            |               |               |         |
|             5 | instance_format_code       | text   |                   |                  |                      |                 |                            |               |               |         |
|             6 | instance_format_name       | text   |                   |                  |                      |                 |                            |               |               |         |
|             7 | instance_format_source     | text   |                   |                  |                      |                 |                            |               |               |         |

## Documentation: [instance_identifiers](instance_identifiers.md)

### Attributes:

|   Attribute # | Attribute             | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:----------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | instance_id           | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             2 | instance_hrid         | text   |                   |                  |                      |                 |                            |               |               |         |
|             3 | identifier_type_id    | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             4 | identifier_type_name  | text   |                   |                  |                      |                 |                            |               |               |         |
|             5 | identifier            | text   |                   |                  |                      |                 |                            |               |               |         |
|             6 | identifier_ordinality | int8   |                   |                  |                      |                 |                            |               |               |         |

## Documentation: [instance_languages](instance_languages.md)

### Attributes:

|   Attribute # | Attribute           | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:--------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | instance_id         | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             2 | instance_hrid       | text   |                   |                  |                      |                 |                            |               |               |         |
|             3 | instance_language   | text   |                   |                  |                      |                 |                            |               |               |         |
|             4 | language_ordinality | int8   |                   |                  |                      |                 |                            |               |               |         |

## Documentation: [instance_nature_content](instance_nature_content.md)

### Attributes:

|   Attribute # | Attribute                     | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:------------------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | instance_id                   | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             2 | instance_hrid                 | text   |                   |                  |                      |                 |                            |               |               |         |
|             3 | nature_of_content_term_id     | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             4 | nature_of_content_term_name   | text   |                   |                  |                      |                 |                            |               |               |         |
|             5 | nature_of_content_term_source | text   |                   |                  |                      |                 |                            |               |               |         |
|             6 | nature_of_content_ordinality  | int8   |                   |                  |                      |                 |                            |               |               |         |

## Documentation: [instance_notes](instance_notes.md)

### Attributes:

|   Attribute # | Attribute                 | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:--------------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | instance_id               | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             2 | instance_hrid             | text   |                   |                  |                      |                 |                            |               |               |         |
|             3 | instance_note             | text   |                   |                  |                      |                 |                            |               |               |         |
|             4 | staff_only_note           | bool   |                   |                  |                      |                 |                            |               |               |         |
|             5 | instance_note_type_id     | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             6 | instance_note_type_name   | text   |                   |                  |                      |                 |                            |               |               |         |
|             7 | instance_notes_ordinality | int8   |                   |                  |                      |                 |                            |               |               |         |

## Documentation: [instance_physical_descriptions](instance_physical_descriptions.md)

### Attributes:

|   Attribute # | Attribute                       | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:--------------------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | instance_id                     | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             2 | instance_hrid                   | text   |                   |                  |                      |                 |                            |               |               |         |
|             3 | physical_description            | text   |                   |                  |                      |                 |                            |               |               |         |
|             4 | physical_description_ordinality | int8   |                   |                  |                      |                 |                            |               |               |         |

## Documentation: [instance_publication](instance_publication.md)

### Attributes:

|   Attribute # | Attribute              | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:-----------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | instance_id            | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             2 | instance_hrid          | text   |                   |                  |                      |                 |                            |               |               |         |
|             3 | publication_place      | text   |                   |                  |                      |                 |                            |               |               |         |
|             4 | publisher              | text   |                   |                  |                      |                 |                            |               |               |         |
|             5 | publication_role       | text   |                   |                  |                      |                 |                            |               |               |         |
|             6 | date_of_publication    | text   |                   |                  |                      |                 |                            |               |               |         |
|             7 | publication_ordinality | int8   |                   |                  |                      |                 |                            |               |               |         |

## Documentation: [instance_relationships_ext](instance_relationships_ext.md)

### Attributes:

|   Attribute # | Attribute                      | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:-------------------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | relationship_id                | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             2 | relationship_type_id           | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             3 | relationship_type_name         | text   |                   |                  |                      |                 |                            |               |               |         |
|             4 | relationship_sub_instance_id   | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             5 | relationship_super_instance_id | uuid   |                   |                  |                      |                 |                            |               |               |         |

## Documentation: [instance_series](instance_series.md)

### Attributes:

|   Attribute # | Attribute         | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | instance_id       | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             2 | instance_hrid     | text   |                   |                  |                      |                 |                            |               |               |         |
|             3 | series            | text   |                   |                  |                      |                 |                            |               |               |         |
|             4 | series_ordinality | int8   |                   |                  |                      |                 |                            |               |               |         |

## Documentation: [instance_statistical_codes](instance_statistical_codes.md)

### Attributes:

|   Attribute # | Attribute                  | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:---------------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | instance_id                | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             2 | instance_hrid              | text   |                   |                  |                      |                 |                            |               |               |         |
|             3 | statistical_code_id        | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             4 | statistical_code_type_id   | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             5 | statistical_code_type_name | text   |                   |                  |                      |                 |                            |               |               |         |
|             6 | statistical_code           | text   |                   |                  |                      |                 |                            |               |               |         |
|             7 | statistical_code_name      | text   |                   |                  |                      |                 |                            |               |               |         |
|             8 | stat_code_ordinality       | int8   |                   |                  |                      |                 |                            |               |               |         |

## Documentation: [instance_subjects](instance_subjects.md)

### Attributes:

|   Attribute # | Attribute           | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:--------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | instance_id         | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             2 | instance_hrid       | text   |                   |                  |                      |                 |                            |               |               |         |
|             3 | subjects            | text   |                   |                  |                      |                 |                            |               |               |         |
|             4 | subjects_ordinality | int8   |                   |                  |                      |                 |                            |               |               |         |

## Documentation: [instance_tags](instance_tags.md)

### Attributes:

|   Attribute # | Attribute               | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:------------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | instance_id             | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             2 | instance_hrid           | text   |                   |                  |                      |                 |                            |               |               |         |
|             3 | instance_tag            | text   |                   |                  |                      |                 |                            |               |               |         |
|             4 | instance_tag_ordinality | int8   |                   |                  |                      |                 |                            |               |               |         |

## Documentation: [invoice_adjustments_ext](invoice_adjustments_ext.md)

### Attributes:

|   Attribute # | Attribute                         | Type    | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description                                                                                                                                                     | Notes   |
|--------------:|:----------------------------------|:--------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------|
|             1 | invoice_id                        | uuid    |                   |                  |                      |                 |                            |               | UUID of this invoice                                                                                                                                            |         |
|             2 | invl_id                           | uuid    |                   |                  |                      |                 |                            |               | UUID of the invoice line associated with this fund distribution                                                                                                 |         |
|             3 | invoice_line_value                | numeric |                   |                  |                      |                 |                            |               | The percentage of the cost to be applied to this fund                                                                                                           |         |
|             4 | transaction_invoice_line_value    | numeric |                   |                  |                      |                 |                            |               | This is invoice_line_value in system currency                                                                                                                   |         |
|             5 | inv_adjust_total_value            | numeric |                   |                  |                      |                 |                            |               | Total adjustment amount                                                                                                                                         |         |
|             6 | transaction_invoice_adj_value     | numeric |                   |                  |                      |                 |                            |               | This is inv_adjust_total_value in system currency                                                                                                               |         |
|             7 | invls_total                       | numeric |                   |                  |                      |                 |                            |               | Invoice line total amount which is sum of subTotal and adjustmentsTotal. This amount is always calculated by system.                                            |         |
|             8 | inv_adj_prorate                   | text    |                   |                  |                      |                 |                            |               | Displayed in invoice line per adjustment in toggled on in settings                                                                                              |         |
|             9 | inv_adj_relationtototal           | text    |                   |                  |                      |                 |                            |               | Relationship of this adjustment to the total;In addition to: added to subtotal;Included in: reported as subtotal portion;Separate from:calculated from subtotal |         |
|            10 | ratio_of_inv_adj_per_invoice_line | numeric |                   |                  |                      |                 |                            |               | This is the ratio of the invoice adjustment per invoice line                                                                                                    |         |
|            11 | inv_adj_total                     | numeric |                   |                  |                      |                 |                            |               | This is the adjustment at the invoice line level, taking into consideration the total ratio per invoice line.                                                   |         |
|            12 | transactions_inv_adj_total        | numeric |                   |                  |                      |                 |                            |               | This is the adjustment at the invoice line level, taking into consideration the total ratio per invoice line. IN SYSTEM CURRENCY                                |         |

## Documentation: [invoice_adjustments_in_addition_to](invoice_adjustments_in_addition_to.md)

### Attributes:

|   Attribute # | Attribute                  | Type    | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description                                                                                                                                                                                                                                                                                              | Notes   |
|--------------:|:---------------------------|:--------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------|
|             1 | invoice_id                 | uuid    |                   |                  |                      |                 |                            |               | UUID of this invoice                                                                                                                                                                                                                                                                                     |         |
|             2 | adjustment_description     | text    |                   |                  |                      |                 |                            |               | List of invoice level adjustments. The adjustments can be pro-rated which are defined at the invoice level, but are applied to the invoice lines. A generic example is a shipping fee which should be spread out across all of the invoice lines so that all funds involved pay some portion of the fee. |         |
|             3 | adjustment_prorate         | text    |                   |                  |                      |                 |                            |               | Displayed in invoice line per adjustment in toggled on in settings                                                                                                                                                                                                                                       |         |
|             4 | adjustment_relationtototal | text    |                   |                  |                      |                 |                            |               | Relationship of this adjustment to the total;In addition to: added to subtotal;Included in: reported as subtotal portion;Separate from:calculated from subtotal                                                                                                                                          |         |
|             5 | adjustment_type            | text    |                   |                  |                      |                 |                            |               | Adjustment type                                                                                                                                                                                                                                                                                          |         |
|             6 | adjustment_value           | numeric |                   |                  |                      |                 |                            |               | Adjustment value                                                                                                                                                                                                                                                                                         |         |

## Documentation: [invoice_lines_adjustments](invoice_lines_adjustments.md)

### Attributes:

|   Attribute # | Attribute                    | Type    | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description                                                                                                                                                                                                                                                                                              | Notes   |
|--------------:|:-----------------------------|:--------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------|
|             1 | invoice_line_id              | uuid    |                   |                  |                      |                 |                            |               | UUID of this invoice line id                                                                                                                                                                                                                                                                             |         |
|             2 | adjustment_description       | text    |                   |                  |                      |                 |                            |               | List of invoice level adjustments. The adjustments can be pro-rated which are defined at the invoice level, but are applied to the invoice lines. A generic example is a shipping fee which should be spread out across all of the invoice lines so that all funds involved pay some portion of the fee. |         |
|             3 | adjustment_prorate           | text    |                   |                  |                      |                 |                            |               | Displayed in invoice line per adjustment in toggled on in settings                                                                                                                                                                                                                                       |         |
|             4 | adjustment_relation_to_total | text    |                   |                  |                      |                 |                            |               | Relationship of this adjustment to the total                                                                                                                                                                                                                                                             |         |
|             5 | adjustment_type              | text    |                   |                  |                      |                 |                            |               | Adjustment type                                                                                                                                                                                                                                                                                          |         |
|             6 | adjustment_value             | numeric |                   |                  |                      |                 |                            |               | Adjustment value                                                                                                                                                                                                                                                                                         |         |
|             7 | adjustment_adjustments_total | numeric |                   |                  |                      |                 |                            |               | Total amount which is sum of all invoice line adjustments and all non-prorated invoice level adjustments. This amount is always calculated by system.                                                                                                                                                    |         |

## Documentation: [invoice_lines_fund_distributions](invoice_lines_fund_distributions.md)

### Attributes:

|   Attribute # | Attribute               | Type    | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description                                                                                                          | Notes   |
|--------------:|:------------------------|:--------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:---------------------------------------------------------------------------------------------------------------------|:--------|
|             1 | invoice_line_id         | uuid    |                   |                  |                      |                 |                            |               | UUID of the invoice line associated with this fund distribution                                                      |         |
|             2 | fund_distribution_id    | uuid    |                   |                  |                      |                 |                            |               | UUID of the fund distribution                                                                                        |         |
|             3 | fund_status             | text    |                   |                  |                      |                 |                            |               | The current status of this fund                                                                                      |         |
|             4 | fund_code               | text    |                   |                  |                      |                 |                            |               | The code of the fund associated with this fund distribution                                                          |         |
|             5 | fund_name               | text    |                   |                  |                      |                 |                            |               | The name of the fund associated with this fund distribution                                                          |         |
|             6 | fund_type_id            | uuid    |                   |                  |                      |                 |                            |               | UUID of the fund type associated with this fund                                                                      |         |
|             7 | fund_type_name          | text    |                   |                  |                      |                 |                            |               | The name of this fund type                                                                                           |         |
|             8 | fund_distribution_value | numeric |                   |                  |                      |                 |                            |               | The percentage of the cost to be applied to this fund                                                                |         |
|             9 | fund_distribution_type  | text    |                   |                  |                      |                 |                            |               | Percentage or amount type of the value property                                                                      |         |
|            10 | invoice_line_sub_total  | numeric |                   |                  |                      |                 |                            |               | Invoice line amount before adjustments are applied                                                                   |         |
|            11 | invoice_line_total      | numeric |                   |                  |                      |                 |                            |               | Invoice line total amount which is sum of subTotal and adjustmentsTotal. This amount is always calculated by system. |         |

## Documentation: [invoice_voucher_lines_fund_distributions](invoice_voucher_lines_fund_distributions.md)

### Attributes:

|   Attribute # | Attribute                                     | Type    | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description                                                                                                       | Notes   |
|--------------:|:----------------------------------------------|:--------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:------------------------------------------------------------------------------------------------------------------|:--------|
|             1 | invoice_voucher_line_id                       | uuid    |                   |                  |                      |                 |                            |               | UUID of this voucher line                                                                                         |         |
|             2 | voucher_id                                    | uuid    |                   |                  |                      |                 |                            |               | UUID of this voucher                                                                                              |         |
|             3 | voucher_number                                | text    |                   |                  |                      |                 |                            |               | Number generated by folio that will eventually identify the payment request sent out to external financial system |         |
|             4 | invoice_voucher_lines_amount                  | numeric |                   |                  |                      |                 |                            |               | Total amount of this voucher                                                                                      |         |
|             5 | fund_distribution_type                        | text    |                   |                  |                      |                 |                            |               | Percentage or amount type of the value property                                                                   |         |
|             6 | fund_distribution_id                          | uuid    |                   |                  |                      |                 |                            |               | UUID of the fund associated with this fund distribution                                                           |         |
|             7 | fund_distribution_code                        | text    |                   |                  |                      |                 |                            |               | Code of the fund associated with this fund distribution                                                           |         |
|             8 | fund_name                                     | text    |                   |                  |                      |                 |                            |               | Name of this fund                                                                                                 |         |
|             9 | fund_distribution_invl_id                     | uuid    |                   |                  |                      |                 |                            |               | UUID of the invoice line associated with this fund distribution                                                   |         |
|            10 | fund_distribution_expense_class_id            | uuid    |                   |                  |                      |                 |                            |               | UUID of the expense class associated with this fund distribution                                                  |         |
|            11 | expense_class_name                            | text    |                   |                  |                      |                 |                            |               | Name of the expense class                                                                                         |         |
|            12 | fund_distribution_value                       | numeric |                   |                  |                      |                 |                            |               | Percentage of the cost to be applied to this fund                                                                 |         |
|            13 | fund_status                                   | text    |                   |                  |                      |                 |                            |               | Current status of this fund                                                                                       |         |
|            14 | fund_type_id                                  | uuid    |                   |                  |                      |                 |                            |               | UUID of fund type                                                                                                 |         |
|            15 | fund_type_name                                | text    |                   |                  |                      |                 |                            |               | Name of fund type                                                                                                 |         |
|            16 | invoice_voucher_lines_external_account_number | text    |                   |                  |                      |                 |                            |               | All distributions that come from funds with the same account number are grouped by voucher line                   |         |

## Documentation: [item_administrative_notes](item_administrative_notes.md)

### Attributes:

|   Attribute # | Attribute                      | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:-------------------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | item_id                        | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             2 | item_hrid                      | text   |                   |                  |                      |                 |                            |               |               |         |
|             3 | holdings_record_id             | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             4 | administrative_note            | text   |                   |                  |                      |                 |                            |               |               |         |
|             5 | administrative_note_ordinality | int8   |                   |                  |                      |                 |                            |               |               |         |

## Documentation: [item_electronic_access](item_electronic_access.md)

### Attributes:

|   Attribute # | Attribute               | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:------------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | item_id                 | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             2 | item_hrid               | text   |                   |                  |                      |                 |                            |               |               |         |
|             3 | link_text               | text   |                   |                  |                      |                 |                            |               |               |         |
|             4 | materials_specification | text   |                   |                  |                      |                 |                            |               |               |         |
|             5 | public_note             | text   |                   |                  |                      |                 |                            |               |               |         |
|             6 | relationship_id         | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             7 | relationship_name       | text   |                   |                  |                      |                 |                            |               |               |         |
|             8 | uri                     | text   |                   |                  |                      |                 |                            |               |               |         |

## Documentation: [item_ext](item_ext.md)

### Attributes:

|   Attribute # | Attribute                                 | Type      | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:------------------------------------------|:----------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | item_id                                   | uuid      |                   |                  |                      |                 |                            |               |               |         |
|             2 | item_hrid                                 | text      |                   |                  |                      |                 |                            |               |               |         |
|             3 | accession_number                          | text      |                   |                  |                      |                 |                            |               |               |         |
|             4 | barcode                                   | text      |                   |                  |                      |                 |                            |               |               |         |
|             5 | chronology                                | text      |                   |                  |                      |                 |                            |               |               |         |
|             6 | copy_number                               | text      |                   |                  |                      |                 |                            |               |               |         |
|             7 | enumeration                               | text      |                   |                  |                      |                 |                            |               |               |         |
|             8 | volume                                    | text      |                   |                  |                      |                 |                            |               |               |         |
|             9 | in_transit_destination_service_point_id   | uuid      |                   |                  |                      |                 |                            |               |               |         |
|            10 | in_transit_destination_service_point_name | text      |                   |                  |                      |                 |                            |               |               |         |
|            11 | identifier                                | text      |                   |                  |                      |                 |                            |               |               |         |
|            12 | call_number                               | text      |                   |                  |                      |                 |                            |               |               |         |
|            13 | call_number_type_id                       | uuid      |                   |                  |                      |                 |                            |               |               |         |
|            14 | call_number_type_name                     | text      |                   |                  |                      |                 |                            |               |               |         |
|            15 | effective_call_number_prefix              | text      |                   |                  |                      |                 |                            |               |               |         |
|            16 | effective_call_number                     | text      |                   |                  |                      |                 |                            |               |               |         |
|            17 | effective_call_number_suffix              | text      |                   |                  |                      |                 |                            |               |               |         |
|            18 | effective_call_number_type_id             | uuid      |                   |                  |                      |                 |                            |               |               |         |
|            19 | effective_call_number_type_name           | text      |                   |                  |                      |                 |                            |               |               |         |
|            20 | damaged_status_id                         | uuid      |                   |                  |                      |                 |                            |               |               |         |
|            21 | damaged_status_name                       | text      |                   |                  |                      |                 |                            |               |               |         |
|            22 | material_type_id                          | uuid      |                   |                  |                      |                 |                            |               |               |         |
|            23 | material_type_name                        | text      |                   |                  |                      |                 |                            |               |               |         |
|            24 | number_of_pieces                          | text      |                   |                  |                      |                 |                            |               |               |         |
|            25 | number_of_missing_pieces                  | text      |                   |                  |                      |                 |                            |               |               |         |
|            26 | permanent_loan_type_id                    | uuid      |                   |                  |                      |                 |                            |               |               |         |
|            27 | permanent_loan_type_name                  | text      |                   |                  |                      |                 |                            |               |               |         |
|            28 | temporary_loan_type_id                    | uuid      |                   |                  |                      |                 |                            |               |               |         |
|            29 | temporary_loan_type_name                  | text      |                   |                  |                      |                 |                            |               |               |         |
|            30 | permanent_location_id                     | uuid      |                   |                  |                      |                 |                            |               |               |         |
|            31 | permanent_location_name                   | text      |                   |                  |                      |                 |                            |               |               |         |
|            32 | temporary_location_id                     | uuid      |                   |                  |                      |                 |                            |               |               |         |
|            33 | temporary_location_name                   | text      |                   |                  |                      |                 |                            |               |               |         |
|            34 | effective_location_id                     | uuid      |                   |                  |                      |                 |                            |               |               |         |
|            35 | effective_location_name                   | text      |                   |                  |                      |                 |                            |               |               |         |
|            36 | description_of_pieces                     | text      |                   |                  |                      |                 |                            |               |               |         |
|            37 | status_date                               | text      |                   |                  |                      |                 |                            |               |               |         |
|            38 | status_name                               | text      |                   |                  |                      |                 |                            |               |               |         |
|            39 | holdings_record_id                        | uuid      |                   |                  |                      |                 |                            |               |               |         |
|            40 | discovery_suppress                        | bool      |                   |                  |                      |                 |                            |               |               |         |
|            41 | created_date                              | timestamp |                   |                  |                      |                 |                            |               |               |         |
|            42 | updated_by_user_id                        | uuid      |                   |                  |                      |                 |                            |               |               |         |
|            43 | updated_date                              | text      |                   |                  |                      |                 |                            |               |               |         |

## Documentation: [item_notes](item_notes.md)

### Attributes:

|   Attribute # | Attribute          | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:-------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | item_id            | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             2 | item_hrid          | text   |                   |                  |                      |                 |                            |               |               |         |
|             3 | holdings_record_id | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             4 | note_type_id       | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             5 | note_type_name     | text   |                   |                  |                      |                 |                            |               |               |         |
|             6 | note               | text   |                   |                  |                      |                 |                            |               |               |         |
|             7 | staff_only         | bool   |                   |                  |                      |                 |                            |               |               |         |
|             8 | note_ordinality    | int8   |                   |                  |                      |                 |                            |               |               |         |

## Documentation: [item_statistical_codes](item_statistical_codes.md)

### Attributes:

|   Attribute # | Attribute                  | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:---------------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | item_id                    | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             2 | item_hrid                  | text   |                   |                  |                      |                 |                            |               |               |         |
|             3 | statistical_code_id        | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             4 | statistical_code           | text   |                   |                  |                      |                 |                            |               |               |         |
|             5 | statistical_code_name      | text   |                   |                  |                      |                 |                            |               |               |         |
|             6 | statistical_code_type_id   | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             7 | statistical_code_type_name | text   |                   |                  |                      |                 |                            |               |               |         |

## Documentation: [item_tags](item_tags.md)

### Attributes:

|   Attribute # | Attribute           | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:--------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | item_id             | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             2 | item_hrid           | text   |                   |                  |                      |                 |                            |               |               |         |
|             3 | item_tag            | text   |                   |                  |                      |                 |                            |               |               |         |
|             4 | item_tag_ordinality | int8   |                   |                  |                      |                 |                            |               |               |         |

## Documentation: [licenses_license_ext](licenses_license_ext.md)

### Attributes:

|   Attribute # | Attribute           | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description                                           | Notes   |
|--------------:|:--------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:------------------------------------------------------|:--------|
|             1 | license_id          | uuid   |                   |                  |                      |                 |                            |               | The UUID of the license                               |         |
|             2 | license_name        | text   |                   |                  |                      |                 |                            |               | Name of license                                       |         |
|             3 | license_description | text   |                   |                  |                      |                 |                            |               | Description of license                                |         |
|             4 | license_start       | date   |                   |                  |                      |                 |                            |               | Start date of this license                            |         |
|             5 | license_end         | date   |                   |                  |                      |                 |                            |               | End date of this license                              |         |
|             6 | license_type        | text   |                   |                  |                      |                 |                            |               | Reference data value for license type                 |         |
|             7 | license_status      | text   |                   |                  |                      |                 |                            |               | Reference data value for license status               |         |
|             8 | license_org         | text   |                   |                  |                      |                 |                            |               | Name of the organization                              |         |
|             9 | license_org_role    | text   |                   |                  |                      |                 |                            |               | Reference data value for the role of the organization |         |
|            10 | license_org_uuid    | uuid   |                   |                  |                      |                 |                            |               | UUID of organization                                  |         |

## Documentation: [loans_items](loans_items.md)

### Attributes:

|   Attribute # | Attribute                                        | Type        | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:-------------------------------------------------|:------------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | loan_id                                          | uuid        |                   |                  |                      |                 |                            |               |               |         |
|             2 | item_id                                          | uuid        |                   |                  |                      |                 |                            |               |               |         |
|             3 | item_status                                      | text        |                   |                  |                      |                 |                            |               |               |         |
|             4 | loan_status                                      | text        |                   |                  |                      |                 |                            |               |               |         |
|             5 | loan_date                                        | timestamptz |                   |                  |                      |                 |                            |               |               |         |
|             6 | loan_due_date                                    | timestamptz |                   |                  |                      |                 |                            |               |               |         |
|             7 | loan_return_date                                 | timestamptz |                   |                  |                      |                 |                            |               |               |         |
|             8 | system_return_date                               | timestamptz |                   |                  |                      |                 |                            |               |               |         |
|             9 | checkin_service_point_id                         | uuid        |                   |                  |                      |                 |                            |               |               |         |
|            10 | checkin_service_point_name                       | text        |                   |                  |                      |                 |                            |               |               |         |
|            11 | checkout_service_point_id                        | uuid        |                   |                  |                      |                 |                            |               |               |         |
|            12 | checkout_service_point_name                      | text        |                   |                  |                      |                 |                            |               |               |         |
|            13 | item_effective_location_id_at_check_out          | uuid        |                   |                  |                      |                 |                            |               |               |         |
|            14 | item_effective_location_name_at_check_out        | text        |                   |                  |                      |                 |                            |               |               |         |
|            15 | in_transit_destination_service_point_id          | uuid        |                   |                  |                      |                 |                            |               |               |         |
|            16 | in_transit_destination_service_point_name        | text        |                   |                  |                      |                 |                            |               |               |         |
|            17 | current_item_effective_location_id               | uuid        |                   |                  |                      |                 |                            |               |               |         |
|            18 | current_item_effective_location_name             | text        |                   |                  |                      |                 |                            |               |               |         |
|            19 | current_item_temporary_location_id               | uuid        |                   |                  |                      |                 |                            |               |               |         |
|            20 | current_item_temporary_location_name             | text        |                   |                  |                      |                 |                            |               |               |         |
|            21 | current_item_permanent_location_id               | uuid        |                   |                  |                      |                 |                            |               |               |         |
|            22 | current_item_permanent_location_name             | text        |                   |                  |                      |                 |                            |               |               |         |
|            23 | current_item_permanent_location_library_id       | uuid        |                   |                  |                      |                 |                            |               |               |         |
|            24 | current_item_permanent_location_library_name     | text        |                   |                  |                      |                 |                            |               |               |         |
|            25 | current_item_permanent_location_campus_id        | uuid        |                   |                  |                      |                 |                            |               |               |         |
|            26 | current_item_permanent_location_campus_name      | text        |                   |                  |                      |                 |                            |               |               |         |
|            27 | current_item_permanent_location_institution_id   | uuid        |                   |                  |                      |                 |                            |               |               |         |
|            28 | current_item_permanent_location_institution_name | text        |                   |                  |                      |                 |                            |               |               |         |
|            29 | loan_policy_id                                   | uuid        |                   |                  |                      |                 |                            |               |               |         |
|            30 | loan_policy_name                                 | text        |                   |                  |                      |                 |                            |               |               |         |
|            31 | lost_item_policy_id                              | uuid        |                   |                  |                      |                 |                            |               |               |         |
|            32 | lost_item_policy_name                            | text        |                   |                  |                      |                 |                            |               |               |         |
|            33 | overdue_fine_policy_id                           | uuid        |                   |                  |                      |                 |                            |               |               |         |
|            34 | overdue_fine_policy_name                         | text        |                   |                  |                      |                 |                            |               |               |         |
|            35 | patron_group_id_at_checkout                      | uuid        |                   |                  |                      |                 |                            |               |               |         |
|            36 | patron_group_name                                | text        |                   |                  |                      |                 |                            |               |               |         |
|            37 | user_id                                          | uuid        |                   |                  |                      |                 |                            |               |               |         |
|            38 | proxy_user_id                                    | uuid        |                   |                  |                      |                 |                            |               |               |         |
|            39 | barcode                                          | text        |                   |                  |                      |                 |                            |               |               |         |
|            40 | chronology                                       | text        |                   |                  |                      |                 |                            |               |               |         |
|            41 | copy_number                                      | text        |                   |                  |                      |                 |                            |               |               |         |
|            42 | enumeration                                      | text        |                   |                  |                      |                 |                            |               |               |         |
|            43 | holdings_record_id                               | uuid        |                   |                  |                      |                 |                            |               |               |         |
|            44 | hrid                                             | text        |                   |                  |                      |                 |                            |               |               |         |
|            45 | item_level_call_number                           | text        |                   |                  |                      |                 |                            |               |               |         |
|            46 | material_type_id                                 | uuid        |                   |                  |                      |                 |                            |               |               |         |
|            47 | material_type_name                               | text        |                   |                  |                      |                 |                            |               |               |         |
|            48 | number_of_pieces                                 | text        |                   |                  |                      |                 |                            |               |               |         |
|            49 | permanent_loan_type_id                           | uuid        |                   |                  |                      |                 |                            |               |               |         |
|            50 | permanent_loan_type_name                         | text        |                   |                  |                      |                 |                            |               |               |         |
|            51 | temporary_loan_type_id                           | uuid        |                   |                  |                      |                 |                            |               |               |         |
|            52 | temporary_loan_type_name                         | text        |                   |                  |                      |                 |                            |               |               |         |
|            53 | renewal_count                                    | int8        |                   |                  |                      |                 |                            |               |               |         |

## Documentation: [loans_renewal_count](loans_renewal_count.md)

### Attributes:

|   Attribute # | Attribute          | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:-------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | current_as_of_date | date   |                   |                  |                      |                 |                            |               |               |         |
|             2 | item_id            | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             3 | num_loans          | int8   |                   |                  |                      |                 |                            |               |               |         |
|             4 | num_renewals       | int8   |                   |                  |                      |                 |                            |               |               |         |

## Documentation: [loans_renewal_dates](loans_renewal_dates.md)

### Attributes:

|   Attribute # | Attribute          | Type        | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:-------------------|:------------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | loan_action_date   | timestamptz |                   |                  |                      |                 |                            |               |               |         |
|             2 | loan_id            | uuid        |                   |                  |                      |                 |                            |               |               |         |
|             3 | item_id            | text        |                   |                  |                      |                 |                            |               |               |         |
|             4 | loan_action        | text        |                   |                  |                      |                 |                            |               |               |         |
|             5 | loan_renewal_count | text        |                   |                  |                      |                 |                            |               |               |         |
|             6 | loan_status        | text        |                   |                  |                      |                 |                            |               |               |         |

## Documentation: [locations_libraries](locations_libraries.md)

### Attributes:

|   Attribute # | Attribute              | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:-----------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | campus_id              | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             2 | campus_name            | text   |                   |                  |                      |                 |                            |               |               |         |
|             3 | location_id            | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             4 | location_name          | text   |                   |                  |                      |                 |                            |               |               |         |
|             5 | discovery_display_name | text   |                   |                  |                      |                 |                            |               |               |         |
|             6 | library_id             | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             7 | library_name           | text   |                   |                  |                      |                 |                            |               |               |         |
|             8 | institution_id         | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             9 | institution_name       | text   |                   |                  |                      |                 |                            |               |               |         |

## Documentation: [locations_service_points](locations_service_points.md)

### Attributes:

|   Attribute # | Attribute                            | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:-------------------------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | service_point_id                     | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             2 | service_point_discovery_display_name | text   |                   |                  |                      |                 |                            |               |               |         |
|             3 | service_point_name                   | text   |                   |                  |                      |                 |                            |               |               |         |
|             4 | location_id                          | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             5 | location_discovery_display_name      | text   |                   |                  |                      |                 |                            |               |               |         |
|             6 | location_name                        | text   |                   |                  |                      |                 |                            |               |               |         |
|             7 | library_id                           | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             8 | library_name                         | text   |                   |                  |                      |                 |                            |               |               |         |
|             9 | campus_id                            | uuid   |                   |                  |                      |                 |                            |               |               |         |
|            10 | campus_name                          | text   |                   |                  |                      |                 |                            |               |               |         |
|            11 | institution_id                       | uuid   |                   |                  |                      |                 |                            |               |               |         |
|            12 | institution_name                     | text   |                   |                  |                      |                 |                            |               |               |         |

## Documentation: [po_acq_unit_ids](po_acq_unit_ids.md)

### Attributes:

|   Attribute # | Attribute                | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description                                       | Notes   |
|--------------:|:-------------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------------------------------------------|:--------|
|             1 | po_id                    | uuid   |                   |                  |                      |                 |                            |               | UUID of this purchase order                       |         |
|             2 | po_number                | text   |                   |                  |                      |                 |                            |               | human readable ID assigned to this purchase order |         |
|             3 | po_acquisition_unit_id   | uuid   |                   |                  |                      |                 |                            |               | UUID of this acquisitions unit record             |         |
|             4 | po_acquisition_unit_name | text   |                   |                  |                      |                 |                            |               | Name for this acquisitions unit                   |         |

## Documentation: [po_instance](po_instance.md)

### Attributes:

|   Attribute # | Attribute           | Type        | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description                                                                             | Notes   |
|--------------:|:--------------------|:------------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:----------------------------------------------------------------------------------------|:--------|
|             1 | manual_po           | bool        |                   |                  |                      |                 |                            |               | If true, order cannot be sent automatically, e.g. via EDI                               |         |
|             2 | rush                | bool        |                   |                  |                      |                 |                            |               | Whether or not this is a rush order                                                     |         |
|             3 | requester           | text        |                   |                  |                      |                 |                            |               | Who requested this material and needs to be notified on arrival                         |         |
|             4 | selector            | text        |                   |                  |                      |                 |                            |               | Who selected this material                                                              |         |
|             5 | po_number           | text        |                   |                  |                      |                 |                            |               | A human readable number assigned to PO                                                  |         |
|             6 | po_number_id        | uuid        |                   |                  |                      |                 |                            |               | UUID identifying this PO                                                                |         |
|             7 | po_line_number      | text        |                   |                  |                      |                 |                            |               | A human readable number assigned to PO line                                             |         |
|             8 | po_line_id          | uuid        |                   |                  |                      |                 |                            |               | UUID identifying this purchase order line                                               |         |
|             9 | vendor_code         | text        |                   |                  |                      |                 |                            |               | The code of the vendor                                                                  |         |
|            10 | created_by_username | text        |                   |                  |                      |                 |                            |               | Username of the user who created the record (when available)                            |         |
|            11 | po_workflow_status  | text        |                   |                  |                      |                 |                            |               | Workflow status of purchase order                                                       |         |
|            12 | status_approved     | bool        |                   |                  |                      |                 |                            |               | Wether purchase order is approved or not                                                |         |
|            13 | created_date        | timestamptz |                   |                  |                      |                 |                            |               | Date when the purchase order was created                                                |         |
|            14 | bill_to             | text        |                   |                  |                      |                 |                            |               | Name of the bill_to location of the purchase order                                      |         |
|            15 | ship_to             | text        |                   |                  |                      |                 |                            |               | Name of the ship_to location of the purchase order                                      |         |
|            16 | pol_instance_id     | uuid        |                   |                  |                      |                 |                            |               | UUID of the instance record this purchase order line is related to                      |         |
|            17 | pol_instance_hrid   | text        |                   |                  |                      |                 |                            |               | A human readable number of the instance record this purchase order line is related to   |         |
|            18 | pol_holding_id      | uuid        |                   |                  |                      |                 |                            |               | UUID of the holdings this purchase order line is related to                             |         |
|            19 | pol_location_id     | uuid        |                   |                  |                      |                 |                            |               | UUID of the location created for this purcase order line                                |         |
|            20 | pol_location_name   | text        |                   |                  |                      |                 |                            |               | Name of the purchase order line location                                                |         |
|            21 | pol_location_source | text        |                   |                  |                      |                 |                            |               | Wether location is a holdings location or permanent location of the purchase order line |         |
|            22 | title               | text        |                   |                  |                      |                 |                            |               | Title of the material                                                                   |         |
|            23 | publication_date    | text        |                   |                  |                      |                 |                            |               | Date (year) of the material's publication                                               |         |
|            24 | publisher           | text        |                   |                  |                      |                 |                            |               | Publisher of the material                                                               |         |

## Documentation: [po_line_fund_distribution_transactions](po_line_fund_distribution_transactions.md)

### Attributes:

|   Attribute # | Attribute                               | Type    | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description                                                                                                                                 | Notes   |
|--------------:|:----------------------------------------|:--------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------------------------------------------------------------------------------------------------------------------------------------|:--------|
|             1 | po_id                                   | uuid    |                   |                  |                      |                 |                            |               | UUID identifying this entity                                                                                                                |         |
|             2 | po_number                               | text    |                   |                  |                      |                 |                            |               | A human readable ID assigned to this purchase order                                                                                         |         |
|             3 | po_workflowstatus                       | text    |                   |                  |                      |                 |                            |               | the workflow status for this purchase order                                                                                                 |         |
|             4 | po_line_id                              | uuid    |                   |                  |                      |                 |                            |               | UUID identifying this purchase order line                                                                                                   |         |
|             5 | poline_number                           | text    |                   |                  |                      |                 |                            |               | A human readable number assigned to this PO line                                                                                            |         |
|             6 | poline_title_or_package                 | text    |                   |                  |                      |                 |                            |               | title of the material                                                                                                                       |         |
|             7 | poline_listunitprice                    | numeric |                   |                  |                      |                 |                            |               | The per-item list price for physical or resources of Other order format                                                                     |         |
|             8 | poline_quantityphysical                 | int4    |                   |                  |                      |                 |                            |               | Quantity of physical items or resources of Other order format in this purchase order line                                                   |         |
|             9 | poline_listunitpriceelectronic          | numeric |                   |                  |                      |                 |                            |               | The e-resource per-item list price                                                                                                          |         |
|            10 | poline_quantityelectronic               | int4    |                   |                  |                      |                 |                            |               | Quantity of electronic items in this purchase order line                                                                                    |         |
|            11 | poline_currency                         | text    |                   |                  |                      |                 |                            |               | An ISO currency code                                                                                                                        |         |
|            12 | poline_discount                         | text    |                   |                  |                      |                 |                            |               | Percentage (0 to 100) or amount (positive number) that is subtracted from the list price time quantities calculation before additional cost |         |
|            13 | poline_discounttype                     | text    |                   |                  |                      |                 |                            |               | Percentage or amount discount type                                                                                                          |         |
|            14 | poline_additionalcost                   | numeric |                   |                  |                      |                 |                            |               | Lump sum that is added to the total estimated price - not affected by discount                                                              |         |
|            15 | poline_estimated_price                  | numeric |                   |                  |                      |                 |                            |               | The calculated total estimated price for this purchase order line: list price time quantities minus discount amount plus additional cost    |         |
|            16 | po_line_fyroadjustmentamount            | numeric |                   |                  |                      |                 |                            |               | Adjustment amount if rollover was happen                                                                                                    |         |
|            17 | fund_distribution_value                 | numeric |                   |                  |                      |                 |                            |               | The value of the cost to be applied to this fund                                                                                            |         |
|            18 | fund_distribution_type                  | text    |                   |                  |                      |                 |                            |               | Percentage or amount type of the value property                                                                                             |         |
|            19 | budget_id                               | uuid    |                   |                  |                      |                 |                            |               | UUID of the budget record                                                                                                                   |         |
|            20 | budget_name                             | text    |                   |                  |                      |                 |                            |               | The name of the budget                                                                                                                      |         |
|            21 | fund_id                                 | uuid    |                   |                  |                      |                 |                            |               | UUID of the fund associated with this fund distribution                                                                                     |         |
|            22 | fund_code                               | text    |                   |                  |                      |                 |                            |               | the fund code                                                                                                                               |         |
|            23 | fiscal_year_id                          | uuid    |                   |                  |                      |                 |                            |               | UUID of the fiscal year record                                                                                                              |         |
|            24 | fiscal_year                             | text    |                   |                  |                      |                 |                            |               | The fiscal year                                                                                                                             |         |
|            25 | transaction_id                          | uuid    |                   |                  |                      |                 |                            |               | UUID of this transaction                                                                                                                    |         |
|            26 | transaction_currency                    | text    |                   |                  |                      |                 |                            |               | Currency code for this transaction - from the system currency                                                                               |         |
|            27 | transaction_amount                      | numeric |                   |                  |                      |                 |                            |               | The amount of this transaction. For encumbrances: This is initialAmountEncumbered - (amountAwaitingPayment + amountExpended)                |         |
|            28 | transaction_encumbrance_initial_amount  | numeric |                   |                  |                      |                 |                            |               | The initial amount of this encumbrance. Should not change once create                                                                       |         |
|            29 | transaction_encumbrance_amount_expended | numeric |                   |                  |                      |                 |                            |               | The amount currently expended by this encumbrance                                                                                           |         |
|            30 | transaction_encumbrance_order_type      | text    |                   |                  |                      |                 |                            |               | Taken from the purchase order                                                                                                               |         |
|            31 | transaction_encumbrance_subscription    | bool    |                   |                  |                      |                 |                            |               | Taken from the purchase Order,for fiscal year rollover                                                                                      |         |

## Documentation: [po_line_vendor_reference_number](po_line_vendor_reference_number.md)

### Attributes:

|   Attribute # | Attribute                    | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description                                      | Notes   |
|--------------:|:-----------------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:-------------------------------------------------|:--------|
|             1 | po_line_id                   | uuid   |                   |                  |                      |                 |                            |               | UUID identifying this purchase order line        |         |
|             2 | po_line_number               | text   |                   |                  |                      |                 |                            |               | A human readable number assigned to this PO line |         |
|             3 | vendor_reference_number      | text   |                   |                  |                      |                 |                            |               | A reference number for this purchase order line  |         |
|             4 | vendor_reference_number_type | text   |                   |                  |                      |                 |                            |               | The reference number type                        |         |
|             5 | vendor_instructions          | text   |                   |                  |                      |                 |                            |               | Special instructions for the vendor              |         |

## Documentation: [po_lines_cost](po_lines_cost.md)

### Attributes:

|   Attribute # | Attribute                    | Type    | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description                                                                                                                                 | Notes   |
|--------------:|:-----------------------------|:--------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------------------------------------------------------------------------------------------------------------------------------------|:--------|
|             1 | pol_id                       | uuid    |                   |                  |                      |                 |                            |               | purchaseOrders                                                                                                                              |         |
|             2 | po_line_list_unit_price_phys | numeric |                   |                  |                      |                 |                            |               | The per-item list price for physical or resources of Other order format                                                                     |         |
|             3 | po_line_quant_phys           | text    |                   |                  |                      |                 |                            |               | Quantity of physical items or resources of Other order format in this purchase order line                                                   |         |
|             4 | po_line_list_unit_price_elec | numeric |                   |                  |                      |                 |                            |               | The e-resource per-item list price                                                                                                          |         |
|             5 | po_line_quant_elec           | text    |                   |                  |                      |                 |                            |               | Quantity of electronic items in this purchase order line                                                                                    |         |
|             6 | po_line_additional_cost      | numeric |                   |                  |                      |                 |                            |               | Lump sum that is added to the total estimated price - not affected by discount                                                              |         |
|             7 | po_line_currency             | text    |                   |                  |                      |                 |                            |               | An ISO currency code                                                                                                                        |         |
|             8 | po_line_discount             | numeric |                   |                  |                      |                 |                            |               | Percentage (0 to 100) or amount (positive number) that is subtracted from the list price time quantities calculation before additional cost |         |
|             9 | po_line_discount_type        | text    |                   |                  |                      |                 |                            |               | Percentage or amount discount type                                                                                                          |         |
|            10 | po_line_estimated_price      | numeric |                   |                  |                      |                 |                            |               | The calculated total estimated price for this purchase order line: list price time quantities minus discount amount plus additional cost    |         |

## Documentation: [po_lines_details_subscription](po_lines_details_subscription.md)

### Attributes:

|   Attribute # | Attribute                 | Type        | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description                               | Notes   |
|--------------:|:--------------------------|:------------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:------------------------------------------|:--------|
|             1 | pol_id                    | uuid        |                   |                  |                      |                 |                            |               | UUID identifying this purchase order line |         |
|             2 | pol_subscription_from     | timestamptz |                   |                  |                      |                 |                            |               | the start date of the subscription        |         |
|             3 | pol_subscription_to       | timestamptz |                   |                  |                      |                 |                            |               | the end date of the subscription          |         |
|             4 | pol_subscription_interval | int4        |                   |                  |                      |                 |                            |               | the subscription interval in days         |         |

## Documentation: [po_lines_er_mat_type](po_lines_er_mat_type.md)

### Attributes:

|   Attribute # | Attribute            | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description                               | Notes   |
|--------------:|:---------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:------------------------------------------|:--------|
|             1 | pol_id               | uuid   |                   |                  |                      |                 |                            |               | UUID identifying this purchase order line |         |
|             2 | pol_er_mat_type_id   | uuid   |                   |                  |                      |                 |                            |               | UUID of the material type                 |         |
|             3 | pol_er_mat_type_name | text   |                   |                  |                      |                 |                            |               | Name of the material type                 |         |

## Documentation: [po_lines_eresource](po_lines_eresource.md)

### Attributes:

|   Attribute # | Attribute               | Type        | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description                                                                                                      | Notes   |
|--------------:|:------------------------|:------------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:-----------------------------------------------------------------------------------------------------------------|:--------|
|             1 | pol_id                  | uuid        |                   |                  |                      |                 |                            |               | UUID identifying this purchase order line                                                                        |         |
|             2 | pol_holding_id          | uuid        |                   |                  |                      |                 |                            |               | Holding UUID associated with order line                                                                          |         |
|             3 | pol_holding_hrid        | text        |                   |                  |                      |                 |                            |               | the human readable ID, also called eye readable ID. A system-assigned sequential ID which maps to the Holding ID |         |
|             4 | pol_location_id         | uuid        |                   |                  |                      |                 |                            |               | UUID of the (inventory) location record                                                                          |         |
|             5 | location_name           | text        |                   |                  |                      |                 |                            |               | Displayed location name                                                                                          |         |
|             6 | pol_location_source     | text        |                   |                  |                      |                 |                            |               | Shows if the displayed location is sourced from the pol_location_id or pol_holding_id                            |         |
|             7 | pol_access_provider     | uuid        |                   |                  |                      |                 |                            |               | UUID of the access provider                                                                                      |         |
|             8 | provider_org_name       | text        |                   |                  |                      |                 |                            |               | Displayed access provider name                                                                                   |         |
|             9 | pol_activated           | text        |                   |                  |                      |                 |                            |               | whether or not this resource is activated                                                                        |         |
|            10 | pol_activation_due      | text        |                   |                  |                      |                 |                            |               | number of days until activation, from date of order placement                                                    |         |
|            11 | pol_create_inventory    | text        |                   |                  |                      |                 |                            |               | Shows what inventory objects need to be created for electronic resource                                          |         |
|            12 | pol_expected_activation | timestamptz |                   |                  |                      |                 |                            |               | expected date the resource will be activated                                                                     |         |
|            13 | pol_license_code        | text        |                   |                  |                      |                 |                            |               | license code                                                                                                     |         |
|            14 | pol_license_desc        | text        |                   |                  |                      |                 |                            |               | license description                                                                                              |         |
|            15 | pol_license_reference   | text        |                   |                  |                      |                 |                            |               | license reference                                                                                                |         |
|            16 | pol_material_type_id    | uuid        |                   |                  |                      |                 |                            |               | UUID of the material Type                                                                                        |         |
|            17 | pol_er_mat_type_name    | text        |                   |                  |                      |                 |                            |               | Material Type name                                                                                               |         |
|            18 | pol_trial               | text        |                   |                  |                      |                 |                            |               | whether or not this is a trial                                                                                   |         |
|            19 | pol_user_limit          | text        |                   |                  |                      |                 |                            |               | the concurrent user-limit                                                                                        |         |
|            20 | pol_resource_url        | text        |                   |                  |                      |                 |                            |               | Electronic resource can be access via this URL                                                                   |         |

## Documentation: [po_lines_locations](po_lines_locations.md)

### Attributes:

|   Attribute # | Attribute           | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description                                                                                 | Notes   |
|--------------:|:--------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------------------------------------------------------------------------------------|:--------|
|             1 | pol_id              | uuid   |                   |                  |                      |                 |                            |               | UUID identifying this purchase order line                                                   |         |
|             2 | pol_loc_qty         | int4   |                   |                  |                      |                 |                            |               | Combined/total quantity of physical and electronic items                                    |         |
|             3 | pol_loc_qty_elec    | int4   |                   |                  |                      |                 |                            |               | Quantity of electronic items in this purchase order line                                    |         |
|             4 | pol_loc_qty_phys    | int4   |                   |                  |                      |                 |                            |               | Quantity of physical items or resources of "Other" order format in this purchase order line |         |
|             5 | pol_location_id     | uuid   |                   |                  |                      |                 |                            |               | UUID of the (inventory) location record or Holding UUID associated with order line          |         |
|             6 | pol_location_name   | text   |                   |                  |                      |                 |                            |               | Name of the location associated with pol_location_id                                        |         |
|             7 | pol_location_source | text   |                   |                  |                      |                 |                            |               | Source of the location associated with pol_location_id                                      |         |

## Documentation: [po_lines_phys_mat_type](po_lines_phys_mat_type.md)

### Attributes:

|   Attribute # | Attribute            | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description                               | Notes   |
|--------------:|:---------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:------------------------------------------|:--------|
|             1 | pol_id               | uuid   |                   |                  |                      |                 |                            |               | UUID identifying this purchase order line |         |
|             2 | pol_phys_mat_type_id | uuid   |                   |                  |                      |                 |                            |               | UUID of the material Type                 |         |
|             3 | pol_mat_type_name    | text   |                   |                  |                      |                 |                            |               | Name of the material type                 |         |

## Documentation: [po_lines_physical](po_lines_physical.md)

### Attributes:

|   Attribute # | Attribute                      | Type        | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description                                                                         | Notes   |
|--------------:|:-------------------------------|:------------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:------------------------------------------------------------------------------------|:--------|
|             1 | pol_id                         | uuid        |                   |                  |                      |                 |                            |               | UUID identifying this purchase order line                                           |         |
|             2 | pol_phys_create_inventory      | text        |                   |                  |                      |                 |                            |               | Shows what inventory objects need to be created for electronic resource             |         |
|             3 | pol_phys_mat_type_id           | uuid        |                   |                  |                      |                 |                            |               | UUID of the material Type                                                           |         |
|             4 | pol_phys_mat_type_name         | text        |                   |                  |                      |                 |                            |               | Label for the material type                                                         |         |
|             5 | pol_phys_mat_supplier_id       | uuid        |                   |                  |                      |                 |                            |               | UUID of the material supplier record                                                |         |
|             6 | supplier_org_name              | text        |                   |                  |                      |                 |                            |               | UUID of this purchase order                                                         |         |
|             7 | pol_phys_expected_receipt_date | timestamptz |                   |                  |                      |                 |                            |               | Vendor agreed date prior to the Receipt Due date item is expected to be received by |         |
|             8 | pol_phys_receipt_due           | timestamptz |                   |                  |                      |                 |                            |               | Date item should be received by                                                     |         |
|             9 | pol_volumes                    | text        |                   |                  |                      |                 |                            |               | List of volumes included to the physical material                                   |         |
|            10 | pol_volumes_ordinality         | int8        |                   |                  |                      |                 |                            |               | Volumes ordinality                                                                  |         |

## Documentation: [po_lines_tags](po_lines_tags.md)

### Attributes:

|   Attribute # | Attribute          | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description                                             | Notes   |
|--------------:|:-------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------------------------------------------------|:--------|
|             1 | pol_id             | uuid   |                   |                  |                      |                 |                            |               | UUID identifying this purchase order line               |         |
|             2 | pol_tag            | text   |                   |                  |                      |                 |                            |               | Arbitrary tags associated with this purchase order line |         |
|             3 | pol_tag_ordinality | int8   |                   |                  |                      |                 |                            |               | The ordinality of the tag associated with the po line   |         |

## Documentation: [po_ongoing](po_ongoing.md)

### Attributes:

|   Attribute # | Attribute                  | Type        | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description                                                     | Notes   |
|--------------:|:---------------------------|:------------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:----------------------------------------------------------------|:--------|
|             1 | po_id                      | uuid        |                   |                  |                      |                 |                            |               | UUID of this purchase order                                     |         |
|             2 | po_ongoing_interval        | int4        |                   |                  |                      |                 |                            |               | The subscription interval in days                               |         |
|             3 | po_ongoing_is_subscription | bool        |                   |                  |                      |                 |                            |               | Whether or not this is a subscription                           |         |
|             4 | po_ongoing_manual_renewal  | bool        |                   |                  |                      |                 |                            |               | Whether or not this is a manual renewal                         |         |
|             5 | po_ongoing_renewal_date    | timestamptz |                   |                  |                      |                 |                            |               | The date this Ongoing PO's order lines were renewed             |         |
|             6 | po_ongoing_review_period   | int4        |                   |                  |                      |                 |                            |               | Time prior to renewal where changes can be made to subscription |         |

## Documentation: [po_organization](po_organization.md)

### Attributes:

|   Attribute # | Attribute                | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description                                      | Notes   |
|--------------:|:-------------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:-------------------------------------------------|:--------|
|             1 | po_number                | text   |                   |                  |                      |                 |                            |               | A human readable number assigned to PO           |         |
|             2 | vendor_id                | uuid   |                   |                  |                      |                 |                            |               | The unique UUID for the vendor                   |         |
|             3 | organization_id          | uuid   |                   |                  |                      |                 |                            |               | The unique UUID for the organization             |         |
|             4 | organization_code        | text   |                   |                  |                      |                 |                            |               | The code of the organization                     |         |
|             5 | organization_name        | text   |                   |                  |                      |                 |                            |               | The name of the organization                     |         |
|             6 | organization_description | text   |                   |                  |                      |                 |                            |               | The description for the organization             |         |
|             7 | is_vendor                | bool   |                   |                  |                      |                 |                            |               | Indication for the organization if also a vendor |         |
|             8 | contact_first_name       | text   |                   |                  |                      |                 |                            |               | Contact First name for the organization          |         |
|             9 | contact_last_name        | text   |                   |                  |                      |                 |                            |               | Contact Last name for the organization           |         |

## Documentation: [po_prod_ids](po_prod_ids.md)

### Attributes:

|   Attribute # | Attribute       | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description                                              | Notes   |
|--------------:|:----------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:---------------------------------------------------------|:--------|
|             1 | pol_id          | uuid   |                   |                  |                      |                 |                            |               | UUID identifying this purchase order line                |         |
|             2 | pol_number      | text   |                   |                  |                      |                 |                            |               | A human readable ID assigned to this purchase order line |         |
|             3 | product_id      | text   |                   |                  |                      |                 |                            |               | The actual product identifier                            |         |
|             4 | product_id_type | text   |                   |                  |                      |                 |                            |               | The type of product identifier                           |         |

## Documentation: [requests_items](requests_items.md)

### Attributes:

|   Attribute # | Attribute                                 | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:------------------------------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | request_id                                | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             2 | item_id                                   | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             3 | request_date                              | date   |                   |                  |                      |                 |                            |               |               |         |
|             4 | request_type                              | text   |                   |                  |                      |                 |                            |               |               |         |
|             5 | request_status                            | text   |                   |                  |                      |                 |                            |               |               |         |
|             6 | pickup_service_point_id                   | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             7 | pickup_service_point_name                 | text   |                   |                  |                      |                 |                            |               |               |         |
|             8 | pickup_service_point_disc_disp_name       | text   |                   |                  |                      |                 |                            |               |               |         |
|             9 | in_transit_dest_serv_point_id             | uuid   |                   |                  |                      |                 |                            |               |               |         |
|            10 | in_transit_dest_serv_point_name           | text   |                   |                  |                      |                 |                            |               |               |         |
|            11 | in_transit_dest_serv_point_disc_disp_name | text   |                   |                  |                      |                 |                            |               |               |         |
|            12 | requester_id                              | uuid   |                   |                  |                      |                 |                            |               |               |         |
|            13 | fulfillment_preference                    | text   |                   |                  |                      |                 |                            |               |               |         |
|            14 | patron_group_id                           | uuid   |                   |                  |                      |                 |                            |               |               |         |
|            15 | patron_group_name                         | text   |                   |                  |                      |                 |                            |               |               |         |
|            16 | item_level_call_number                    | text   |                   |                  |                      |                 |                            |               |               |         |
|            17 | barcode                                   | text   |                   |                  |                      |                 |                            |               |               |         |
|            18 | chronology                                | text   |                   |                  |                      |                 |                            |               |               |         |
|            19 | item_copy_number                          | text   |                   |                  |                      |                 |                            |               |               |         |
|            20 | item_permanent_location_id                | uuid   |                   |                  |                      |                 |                            |               |               |         |
|            21 | item_temporary_location_id                | uuid   |                   |                  |                      |                 |                            |               |               |         |
|            22 | enumeration                               | text   |                   |                  |                      |                 |                            |               |               |         |
|            23 | item_effective_location_id                | uuid   |                   |                  |                      |                 |                            |               |               |         |
|            24 | item_effective_location_name              | text   |                   |                  |                      |                 |                            |               |               |         |
|            25 | item_permanent_location_name              | text   |                   |                  |                      |                 |                            |               |               |         |
|            26 | item_temporary_location_name              | text   |                   |                  |                      |                 |                            |               |               |         |
|            27 | holdings_record_id                        | uuid   |                   |                  |                      |                 |                            |               |               |         |
|            28 | hrid                                      | text   |                   |                  |                      |                 |                            |               |               |         |
|            29 | item_identifier                           | text   |                   |                  |                      |                 |                            |               |               |         |
|            30 | material_type_id                          | uuid   |                   |                  |                      |                 |                            |               |               |         |
|            31 | material_type_name                        | text   |                   |                  |                      |                 |                            |               |               |         |
|            32 | number_of_pieces                          | text   |                   |                  |                      |                 |                            |               |               |         |
|            33 | item_permanent_loan_type_id               | uuid   |                   |                  |                      |                 |                            |               |               |         |
|            34 | item_permanent_loan_type_name             | text   |                   |                  |                      |                 |                            |               |               |         |
|            35 | item_temporary_loan_type_id               | uuid   |                   |                  |                      |                 |                            |               |               |         |
|            36 | item_temporary_loan_type_name             | text   |                   |                  |                      |                 |                            |               |               |         |

## Documentation: [users_addresses](users_addresses.md)

### Attributes:

|   Attribute # | Attribute                | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description   | Notes   |
|--------------:|:-------------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------|:--------|
|             1 | user_id                  | uuid   |                   |                  |                      |                 |                            |               |               |         |
|             2 | address_id               | text   |                   |                  |                      |                 |                            |               |               |         |
|             3 | address_country_id       | text   |                   |                  |                      |                 |                            |               |               |         |
|             4 | address_line_1           | text   |                   |                  |                      |                 |                            |               |               |         |
|             5 | address_line_2           | text   |                   |                  |                      |                 |                            |               |               |         |
|             6 | address_city             | text   |                   |                  |                      |                 |                            |               |               |         |
|             7 | address_region           | text   |                   |                  |                      |                 |                            |               |               |         |
|             8 | address_postal_code      | text   |                   |                  |                      |                 |                            |               |               |         |
|             9 | address_type_id          | uuid   |                   |                  |                      |                 |                            |               |               |         |
|            10 | address_type_name        | text   |                   |                  |                      |                 |                            |               |               |         |
|            11 | address_type_description | text   |                   |                  |                      |                 |                            |               |               |         |
|            12 | is_primary_address       | bool   |                   |                  |                      |                 |                            |               |               |         |

## Documentation: [users_departments_unpacked](users_departments_unpacked.md)

### Attributes:

|   Attribute # | Attribute             | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description                                                            | Notes   |
|--------------:|:----------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:-----------------------------------------------------------------------|:--------|
|             1 | user_id               | uuid   |                   |                  |                      |                 |                            |               | User ID (Generated UUID) of the user associated with the department(s) |         |
|             2 | department_id         | uuid   |                   |                  |                      |                 |                            |               | Department ID (Generated UUID) of the department                       |         |
|             3 | department_ordinality | int8   |                   |                  |                      |                 |                            |               | The ordinality of the department(s) associated with a user             |         |
|             4 | department_name       | text   |                   |                  |                      |                 |                            |               | The display name of the department                                     |         |
|             5 | department_code       | text   |                   |                  |                      |                 |                            |               | The (user-supplied) code for the department                            |         |

## Documentation: [users_groups](users_groups.md)

### Attributes:

|   Attribute # | Attribute                      | Type        | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description                                                                                                                                                                                 | Notes   |
|--------------:|:-------------------------------|:------------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------|
|             1 | user_id                        | uuid        |                   |                  |                      |                 |                            |               | A globally unique (UUID) identifier for the user                                                                                                                                            |         |
|             2 | active                         | bool        |                   |                  |                      |                 |                            |               | A flag to determine if the users account is effective and not expired. The tenant configuration can require the user to be active for login. Active is different from the loan patron block |         |
|             3 | barcode                        | text        |                   |                  |                      |                 |                            |               | The unique library barcode for this user                                                                                                                                                    |         |
|             4 | created_date                   | timestamptz |                   |                  |                      |                 |                            |               | Date and time when the user record was created                                                                                                                                              |         |
|             5 | enrollment_date                | timestamptz |                   |                  |                      |                 |                            |               | The date when the user joined the organization                                                                                                                                              |         |
|             6 | expiration_date                | timestamptz |                   |                  |                      |                 |                            |               | The date when the user will become inactive                                                                                                                                                 |         |
|             7 | external_system_id             | text        |                   |                  |                      |                 |                            |               | A unique ID that corresponds to an external authority                                                                                                                                       |         |
|             8 | patron_group                   | uuid        |                   |                  |                      |                 |                            |               | A UUID corresponding to the group the user belongs to, example groups are undergraduate and faculty; loan rules, patron blocks, fees/fines and expiration days can use the patron group     |         |
|             9 | group_description              | text        |                   |                  |                      |                 |                            |               | A description for the user group                                                                                                                                                            |         |
|            10 | group_name                     | text        |                   |                  |                      |                 |                            |               | The unique name of the user group                                                                                                                                                           |         |
|            11 | departments                    | text        |                   |                  |                      |                 |                            |               | A list of UUIDs corresponding to the departments the user belongs to                                                                                                                        |         |
|            12 | user_last_name                 | text        |                   |                  |                      |                 |                            |               | The users surname                                                                                                                                                                           |         |
|            13 | user_first_name                | text        |                   |                  |                      |                 |                            |               | The users given name                                                                                                                                                                        |         |
|            14 | user_middle_name               | text        |                   |                  |                      |                 |                            |               | The users middle name (if any)                                                                                                                                                              |         |
|            15 | user_preferred_first_name      | text        |                   |                  |                      |                 |                            |               | The users preferred name                                                                                                                                                                    |         |
|            16 | user_email                     | text        |                   |                  |                      |                 |                            |               | The users email address                                                                                                                                                                     |         |
|            17 | user_phone                     | text        |                   |                  |                      |                 |                            |               | The users primary phone number                                                                                                                                                              |         |
|            18 | user_mobile_phone              | text        |                   |                  |                      |                 |                            |               | The users mobile phone number                                                                                                                                                               |         |
|            19 | user_date_of_birth             | date        |                   |                  |                      |                 |                            |               | The users birth date                                                                                                                                                                        |         |
|            20 | user_preferred_contact_type_id | text        |                   |                  |                      |                 |                            |               | ID of users preferred contact type like Email, Mail or Text Message                                                                                                                         |         |
|            21 | user_type                      | text        |                   |                  |                      |                 |                            |               | The class of the user, like staff or patron; this is different from patronGroup                                                                                                             |         |
|            22 | updated_date                   | timestamptz |                   |                  |                      |                 |                            |               | Date and time when the user record was last updated                                                                                                                                         |         |
|            23 | username                       | text        |                   |                  |                      |                 |                            |               | A unique name belonging to a user. Typically used for login                                                                                                                                 |         |


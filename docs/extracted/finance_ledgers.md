---
title: finance_ledgers
---
## Source:

Module: mod-finance-storage

Interface: /finance-storage/ledgers

## Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          | The UUID format string                                                                             |
| _version                   | integer         | Record version for optimistic locking                                                              |
| name                       | string          | The name of the ledger                                                                             |
| code                       | string          | The code for the ledger                                                                            |
| description                | string          | The description of the ledger                                                                      |
| fiscalYearOneId            | string          | The UUID format string                                                                             |
| ledgerStatus               | string          | The status of the ledger                                                                           |
| allocated                  | number          | The amount currently allocated to this ledger                                                      |
| available                  | number          | The amount currently available in this ledger                                                      |
| netTransfers               | number          | Summing all the transfers from/to this ledger. Amount can be negative                              |
| unavailable                | number          | The amount already utilized from the allocated amount                                              |
| currency                   | string          | The ISO code for currency                                                                          |
| acqUnitIds                 | array           | acquisition unit ids associated with this ledger                                                   |
| restrictEncumbrance        | boolean         | If true, imposes restrictions on encumbrances                                                      |
| restrictExpenditures       | boolean         | If true, imposes restrictions on payments                                                          |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |
| initialAllocation          | number          | Summary of all related to this ledger budgets initialAllocation                                    |
| allocationTo               | number          | Summary of all related to this ledger budgets allocationTo                                         |
| allocationFrom             | number          | Summary of all related to this ledger budgets allocationFrom                                       |
| totalFunding               | number          | Summary of all related to this ledger budgets totalFunding                                         |
| cashBalance                | number          | Summary of all related to this ledger budgets cashBalance                                          |
| awaitingPayment            | number          | Summary of all related to this ledger budgets awaitingPayment                                      |
| encumbered                 | number          | Summary of all related to this ledger budgets encumbered                                           |
| expenditures               | number          | Summary of all related to this ledger budgets expenditures                                         |
| overEncumbrance            | number          | Summary of all related to this ledger budgets overEncumbrance                                      |
| overExpended               | number          | Summary of all related to this ledger budgets overExpended                                         |


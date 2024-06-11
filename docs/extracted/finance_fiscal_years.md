---
title: finance_fiscal_years
---
## Source:

Module: mod-finance-storage

Interface: /finance-storage/fiscal-years

## Attributes:

| Property Name                      | Property Type   | Property Description                                                                               |
|:-----------------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                                 | string          | The UUID format string                                                                             |
| _version                           | integer         | Record version for optimistic locking                                                              |
| acqUnitIds                         | array           | UUIDs of the acquisition units associated with this fiscal year                                    |
| name                               | string          | The name of the fiscal year                                                                        |
| code                               | string          | The code of the fiscal year                                                                        |
| currency                           | string          | Currency code which is recorded when the FY ends, otherwise the system currency can be assumed     |
| description                        | string          | The description of the fiscal year                                                                 |
| periodStart                        | string          | The start date of the fiscal year                                                                  |
| periodEnd                          | string          | The end date of the fiscal year                                                                    |
| series                             | string          | The fiscal year series                                                                             |
| financialSummary                   | object          | Funding information and Financial activity                                                         |
| financialSummary/allocated         | number          | Summary of all related to this fiscal year budgets allocated                                       |
| financialSummary/available         | number          | Summary of all related to this fiscal year budgets available                                       |
| financialSummary/unavailable       | number          | Summary of all related to this fiscal year budgets unavailable                                     |
| financialSummary/initialAllocation | number          | Summary of all related to this fiscal year budgets initialAllocation                               |
| financialSummary/allocationTo      | number          | Summary of all related to this fiscal year budgets allocationTo                                    |
| financialSummary/allocationFrom    | number          | Summary of all related to this fiscal year budgets allocationFrom                                  |
| financialSummary/totalFunding      | number          | Summary of all related to this fiscal year budgets totalFunding                                    |
| financialSummary/cashBalance       | number          | Summary of all related to this fiscal year budgets cashBalance                                     |
| financialSummary/awaitingPayment   | number          | Summary of all related to this fiscal year budgets awaitingPayment                                 |
| financialSummary/credits           | number          | Summary of all related to this fiscal year budgets credits                                         |
| financialSummary/encumbered        | number          | Summary of all related to this fiscal year budgets encumbered                                      |
| financialSummary/expenditures      | number          | Summary of all related to this ledger budgets expenditures                                         |
| financialSummary/overEncumbrance   | number          | Summary of all related to this ledger budgets overEncumbrance                                      |
| financialSummary/overExpended      | number          | Summary of all related to this ledger budgets overExpended                                         |
| metadata                           | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate               | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId           | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername         | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate               | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId           | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername         | string          | Username of the user who last updated the record (when available)                                  |


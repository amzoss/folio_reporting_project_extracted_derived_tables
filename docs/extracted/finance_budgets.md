---
title: finance_budgets
---
## Source:

Module: mod-finance-storage

Interface: /finance-storage/budgets

## Attributes:

| Property Name              | Property Type   | Property Description                                                                                     |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------------|
| id                         | string          | The UUID format string                                                                                   |
| _version                   | integer         | Record version for optimistic locking                                                                    |
| name                       | string          | The name of the budget                                                                                   |
| budgetStatus               | string          | The status of the budget                                                                                 |
| allowableEncumbrance       | number          | The encumbrance percentage limit for this budget                                                         |
| allowableExpenditure       | number          | The expenditure percentage limit for this budget                                                         |
| allocated                  | number          | The amount currently allocated to this budget                                                            |
| awaitingPayment            | number          | The amount currently awaiting payment for this budget                                                    |
| available                  | number          | The amount currently available for this budge                                                            |
| credits                    | number          | The amount currently credited for this budget                                                            |
| encumbered                 | number          | The amount currently encumbered for this budget                                                          |
| expenditures               | number          | The amount currently expended for this budget                                                            |
| netTransfers               | number          | Summing all the transfers on this budget                                                                 |
| unavailable                | number          | Unavailable amount for this budget                                                                       |
| overEncumbrance            | number          | The amount currently over-encumbered for this budget                                                     |
| overExpended               | number          | Amount the budget is over expended.                                                                      |
| fundId                     | string          | The UUID format string                                                                                   |
| fiscalYearId               | string          | The UUID format string                                                                                   |
| acqUnitIds                 | array           | acquisition unit ids associated with this budget                                                         |
| tags                       | object          | List of simple tags that can be added to an object                                                       |
| tags/tagList               | array           | List of tags                                                                                             |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)       |
| metadata/createdDate       | string          | Date and time when the record was created                                                                |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                                   |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                             |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                           |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                              |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                        |
| initialAllocation          | number          | The amount of the first allocation made to this budget                                                   |
| allocationTo               | number          | The sum of all allocation transaction amounts made TO this budget not including the Initial allocation   |
| allocationFrom             | number          | The sum of all allocation transaction amounts made FROM this budget not including the Initial allocation |
| totalFunding               | number          | budget.allocated + budget.netTransfers                                                                   |
| cashBalance                | number          | Total Funding minus Expended                                                                             |


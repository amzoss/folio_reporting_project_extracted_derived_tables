---
title: finance_expense_classes
---
## Source:

Module: mod-finance-storage

Interface: /finance-storage/expense-classes

## Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          | The UUID format string                                                                             |
| _version                   | integer         | Record version for optimistic locking                                                              |
| code                       | string          | The code of the expense class                                                                      |
| externalAccountNumberExt   | string          | An external account number extension                                                               |
| name                       | string          | The name of the expense class                                                                      |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |


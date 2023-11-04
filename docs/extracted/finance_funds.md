---
title: finance_funds
---
## Source:

Module: mod-finance-storage

Interface: /finance-storage/funds

## Attributes:

| Property Name              | Property Type   | Property Description                                                                                                                                                   |
|:---------------------------|:----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id                         | string          | The UUID format string                                                                                                                                                 |
| _version                   | integer         | Record version for optimistic locking                                                                                                                                  |
| allocatedFromIds           | array           | All the funds that this fund is allowed to receive money from. This would be 1 fund or none. If this field is blank their is no restriction on allocating to this fund |
| allocatedToIds             | array           | All the funds that this fund is allowed to send money to. This could be one or many.                                                                                   |
| code                       | string          | Fund code format                                                                                                                                                       |
| description                | string          | The description of this fund                                                                                                                                           |
| externalAccountNo          | string          | Corresponding account in the financial system. Will be recorded in payment generated as well.                                                                          |
| fundStatus                 | string          | The current status of this fund                                                                                                                                        |
| fundTypeId                 | string          | The UUID format string                                                                                                                                                 |
| ledgerId                   | string          | The UUID format string                                                                                                                                                 |
| name                       | string          | The name of this fund                                                                                                                                                  |
| acqUnitIds                 | array           | acquisition unit ids associated with this fund                                                                                                                         |
| donorOrganizationIds       | array           | donor organization ids associated with this fund                                                                                                                       |
| locationIds                | array           | location ids associated with this fund                                                                                                                                 |
| tags                       | object          | List of simple tags that can be added to an object                                                                                                                     |
| tags/tagList               | array           | List of tags                                                                                                                                                           |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                                                                     |
| metadata/createdDate       | string          | Date and time when the record was created                                                                                                                              |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                                                                                                 |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                                                                                           |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                                                                                         |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                                                                                            |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                                                                                      |


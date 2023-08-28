---
title: finance_groups
---
## Source:

Module: mod-finance-storage

Interface: /finance-storage/groups

## Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          | The UUID format string                                                                             |
| _version                   | integer         | Record version for optimistic locking                                                              |
| acqUnitIds                 | array           | UUIDs of the acquisition units associated with this group                                          |
| code                       | string          | The code of the group                                                                              |
| description                | string          | The description of the group                                                                       |
| name                       | string          | The name of the group                                                                              |
| status                     | string          | The status of the group                                                                            |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |


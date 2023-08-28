---
title: user_addresstypes
---
## Source:

Module: mod-users

Interface: /addresstypes

## Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| addressType                | string          | A unique name for this address type                                                                |
| desc                       | string          | An explanation of this address type                                                                |
| id                         | string          | A UUID identifying this address type                                                               |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |


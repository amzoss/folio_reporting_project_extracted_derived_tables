---
title: user_proxiesfor
---
## Source:

Module: mod-users

Interface: /proxiesfor

## Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| userId                     | string          | The id of the user for whom this proxy pertains                                                    |
| proxyUserId                | string          | The id of the user acting as the proxy                                                             |
| id                         | string          | A UUID identifying this proxy relationship                                                         |
| requestForSponsor          | string          | Can the user request a sponsor (yes/no)                                                            |
| createdDate                | string          | Deprecated                                                                                         |
| notificationsTo            | string          | Where notifications are sent                                                                       |
| accrueTo                   | string          | Where fees and fines accrue                                                                        |
| status                     | string          | Active or Inactive                                                                                 |
| expirationDate             | string          | The date this proxy relationship expires                                                           |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |


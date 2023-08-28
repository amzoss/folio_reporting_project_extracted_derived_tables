---
title: inventory_service_points_users
---
## Source:

Module: mod-inventory-storage

Interface: /service-points-users

## Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          | The id of record as a UUID.                                                                        |
| userId                     | string          | Id of the user as a UUID.                                                                          |
| servicePointsIds           | array           | The list of service points a user is allowed to work at.                                           |
| defaultServicePointId      | string          | The id of the user's default service point as UUID.                                                |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |


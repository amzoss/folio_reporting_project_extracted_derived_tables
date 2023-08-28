---
title: inventory_service_points
---
## Source:

Module: mod-inventory-storage

Interface: /service-points

## Attributes:

| Property Name                        | Property Type   | Property Description                                                                               |
|:-------------------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                                   | string          | Id of service-point object                                                                         |
| name                                 | string          | service-point name, a required field                                                               |
| code                                 | string          | service-point code, a required field                                                               |
| discoveryDisplayName                 | string          | display name, a required field                                                                     |
| description                          | string          | description of the service-point                                                                   |
| shelvingLagTime                      | integer         | shelving lag time                                                                                  |
| pickupLocation                       | boolean         | indicates whether or not the service point is a pickup location                                    |
| holdShelfExpiryPeriod                | object          | schema for time-period, which contains time interval 'duration' and the time unit                  |
| holdShelfExpiryPeriod/duration       | integer         | Duration interval                                                                                  |
| holdShelfExpiryPeriod/intervalId     | string          | Unit of time for the duration                                                                      |
| holdShelfClosedLibraryDateManagement | string          | enum for closedLibraryDateManagement associated with hold shelf                                    |
| staffSlips                           | array           | List of staff slips for this service point                                                         |
| staffSlips/id                        | string          | The ID of the staff slip                                                                           |
| staffSlips/printByDefault            | boolean         | Whether or not to print the staff slip by default                                                  |
| metadata                             | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate                 | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId             | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername           | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate                 | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId             | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername           | string          | Username of the user who last updated the record (when available)                                  |


---
title: inventory_locations
---
## Source:

Module: mod-inventory-storage

Interface: /locations

## Attributes:

| Property Name                                                  | Property Type   | Property Description                                                                               |
|:---------------------------------------------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                                                             | string          | id of this (shelf) location record as UUID.                                                        |
| name                                                           | string          | Name of the (shelf) location                                                                       |
| code                                                           | string          | Code of the (shelf) location, usually an abbreviation of the name.                                 |
| description                                                    | string          | Description of the (shelf) location.                                                               |
| discoveryDisplayName                                           | string          | Name of the (shelf) location to be shown in the discovery.                                         |
| isActive                                                       | boolean         | Whether this (shelf) location is active. Inactive (shelf) locations can no longer been used.       |
| institutionId                                                  | string          | The UUID of the institution, the first-level location unit, this (shelf) location belongs to.      |
| institution                                                    | object          | The institution, the first-level location unit, this (shelf) location belongs to.                  |
| campusId                                                       | string          | The UUID of the campus, the second-level location unit, this (shelf) location belongs to.          |
| campus                                                         | object          | The campus, the second-level location unit, this (shelf) location belongs to                       |
| libraryId                                                      | string          | The UUID of the library, the third-level location unit, this (shelf) location belongs to.          |
| library                                                        | object          | The library, the third-level location unit, this (shelf) location belongs to.                      |
| details                                                        | object          | Details about this (shelf) location.                                                               |
| primaryServicePoint                                            | string          | The UUID of the primary service point of this (shelf) location.                                    |
| primaryServicePointObject                                      | object          | A service point                                                                                    |
| primaryServicePointObject/id                                   | string          | Id of service-point object                                                                         |
| primaryServicePointObject/name                                 | string          | service-point name, a required field                                                               |
| primaryServicePointObject/code                                 | string          | service-point code, a required field                                                               |
| primaryServicePointObject/discoveryDisplayName                 | string          | display name, a required field                                                                     |
| primaryServicePointObject/description                          | string          | description of the service-point                                                                   |
| primaryServicePointObject/shelvingLagTime                      | integer         | shelving lag time                                                                                  |
| primaryServicePointObject/pickupLocation                       | boolean         | indicates whether or not the service point is a pickup location                                    |
| primaryServicePointObject/holdShelfExpiryPeriod                | object          | schema for time-period, which contains time interval 'duration' and the time unit                  |
| primaryServicePointObject/holdShelfExpiryPeriod/duration       | integer         | Duration interval                                                                                  |
| primaryServicePointObject/holdShelfExpiryPeriod/intervalId     | string          | Unit of time for the duration                                                                      |
| primaryServicePointObject/holdShelfClosedLibraryDateManagement | string          | enum for closedLibraryDateManagement associated with hold shelf                                    |
| primaryServicePointObject/staffSlips                           | array           | List of staff slips for this service point                                                         |
| primaryServicePointObject/staffSlips/id                        | string          | The ID of the staff slip                                                                           |
| primaryServicePointObject/staffSlips/printByDefault            | boolean         | Whether or not to print the staff slip by default                                                  |
| primaryServicePointObject/metadata                             | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| primaryServicePointObject/metadata/createdDate                 | string          | Date and time when the record was created                                                          |
| primaryServicePointObject/metadata/createdByUserId             | string          | ID of the user who created the record (when available)                                             |
| primaryServicePointObject/metadata/createdByUsername           | string          | Username of the user who created the record (when available)                                       |
| primaryServicePointObject/metadata/updatedDate                 | string          | Date and time when the record was last updated                                                     |
| primaryServicePointObject/metadata/updatedByUserId             | string          | ID of the user who last updated the record (when available)                                        |
| primaryServicePointObject/metadata/updatedByUsername           | string          | Username of the user who last updated the record (when available)                                  |
| servicePointIds                                                | array           | All service points that this (shelf) location has.                                                 |
| servicePoints                                                  | array           | List of dereferenced service points                                                                |
| metadata                                                       | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate                                           | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId                                       | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername                                     | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate                                           | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId                                       | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername                                     | string          | Username of the user who last updated the record (when available)                                  |


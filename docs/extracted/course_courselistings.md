---
title: course_courselistings
---
## Source:

Module: mod-courses

Interface: /coursereserves/courselistings

## Attributes:

| Property Name                                       | Property Type   | Property Description                                                                               |
|:----------------------------------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                                                  | string          | A UUID                                                                                             |
| registrarId                                         | string          | The registration id                                                                                |
| externalId                                          | string          | An external identifier associated with this listing                                                |
| servicepointId                                      | string          | A UUID                                                                                             |
| servicepointObject                                  | object          | The service point associated with this listing's reserves                                          |
| servicepointObject/id                               | string          | Id of service-point object                                                                         |
| servicepointObject/name                             | string          | service-point name, a required field                                                               |
| servicepointObject/code                             | string          | service-point code, a required field                                                               |
| servicepointObject/discoveryDisplayName             | string          | display name, a required field                                                                     |
| servicepointObject/description                      | string          | description of the service-point                                                                   |
| servicepointObject/shelvingLagTime                  | integer         | shelving lag time                                                                                  |
| servicepointObject/pickupLocation                   | boolean         | indicates whether or not the service point is a pickup location                                    |
| servicepointObject/holdShelfExpiryPeriod            | object          | schema for time-period, which contains time interval 'duration' and the time unit                  |
| servicepointObject/holdShelfExpiryPeriod/duration   | integer         | Duration interval                                                                                  |
| servicepointObject/holdShelfExpiryPeriod/intervalId | string          | Unit of time for the duration                                                                      |
| servicepointObject/staffSlips                       | array           | List of staff slips for this service point                                                         |
| servicepointObject/staffSlips/id                    | string          | The ID of the staff slip                                                                           |
| servicepointObject/staffSlips/printByDefault        | boolean         | Whether or not to print the staff slip by default                                                  |
| locationId                                          | string          | A UUID                                                                                             |
| locationObject                                      | object          | The location associated with this listing's reserves                                               |
| locationObject/id                                   | string          | id of this (shelf) location record as UUID.                                                        |
| locationObject/name                                 | string          | Name of the (shelf) location                                                                       |
| locationObject/code                                 | string          | Code of the (shelf) location, usually an abbreviation of the name.                                 |
| locationObject/description                          | string          | Description of the (shelf) location.                                                               |
| locationObject/discoveryDisplayName                 | string          | Name of the (shelf) location to be shown in the discovery.                                         |
| locationObject/isActive                             | boolean         | Whether this (shelf) location is active. Inactive (shelf) locations can no longer been used.       |
| locationObject/institutionId                        | string          | The UUID of the institution, the first-level location unit, this (shelf) location belongs to.      |
| locationObject/campusId                             | string          | The UUID of the campus, the second-level location unit, this (shelf) location belongs to.          |
| locationObject/libraryId                            | string          | The UUID of the library, the third-level location unit, this (shelf) location belongs to.          |
| locationObject/details                              | object          | Details about this (shelf) location.                                                               |
| locationObject/primaryServicePoint                  | string          | The UUID of the primary service point of this (shelf) location.                                    |
| locationObject/servicePointIds                      | array           | All service points that this (shelf) location has.                                                 |
| termId                                              | string          | A UUID                                                                                             |
| termObject                                          | object          | Temporal periods that listings exist in                                                            |
| termObject/id                                       | string          | A UUID                                                                                             |
| termObject/name                                     | string          | The name of period                                                                                 |
| termObject/startDate                                | string          | The beginning of the time period                                                                   |
| termObject/endDate                                  | string          | The ending of the time period                                                                      |
| termObject/metadata                                 | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| termObject/metadata/createdDate                     | string          | Date and time when the record was created                                                          |
| termObject/metadata/createdByUserId                 | string          | ID of the user who created the record (when available)                                             |
| termObject/metadata/createdByUsername               | string          | Username of the user who created the record (when available)                                       |
| termObject/metadata/updatedDate                     | string          | Date and time when the record was last updated                                                     |
| termObject/metadata/updatedByUserId                 | string          | ID of the user who last updated the record (when available)                                        |
| termObject/metadata/updatedByUsername               | string          | Username of the user who last updated the record (when available)                                  |
| courseTypeId                                        | string          | A UUID                                                                                             |
| courseTypeObject                                    | object          | The type of course a listing is                                                                    |
| courseTypeObject/id                                 | string          | A UUID                                                                                             |
| courseTypeObject/name                               | string          | The name of the type                                                                               |
| courseTypeObject/description                        | string          | A description of this type                                                                         |
| courseTypeObject/metadata                           | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| courseTypeObject/metadata/createdDate               | string          | Date and time when the record was created                                                          |
| courseTypeObject/metadata/createdByUserId           | string          | ID of the user who created the record (when available)                                             |
| courseTypeObject/metadata/createdByUsername         | string          | Username of the user who created the record (when available)                                       |
| courseTypeObject/metadata/updatedDate               | string          | Date and time when the record was last updated                                                     |
| courseTypeObject/metadata/updatedByUserId           | string          | ID of the user who last updated the record (when available)                                        |
| courseTypeObject/metadata/updatedByUsername         | string          | Username of the user who last updated the record (when available)                                  |
| instructorObjects                                   | array           | A listing of associated instructor objects                                                         |
| metadata                                            | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate                                | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId                            | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername                          | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate                                | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId                            | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername                          | string          | Username of the user who last updated the record (when available)                                  |


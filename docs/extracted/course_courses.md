---
title: course_courses
---
## Source:

Module: mod-courses

Interface: /coursereserves/courses

## Attributes:

| Property Name                                                           | Property Type   | Property Description                                                                               |
|:------------------------------------------------------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                                                                      | string          | A UUID                                                                                             |
| name                                                                    | string          | The name of course                                                                                 |
| description                                                             | string          | A description of the course                                                                        |
| departmentId                                                            | string          | A UUID                                                                                             |
| departmentObject                                                        | object          | The department a course belongs to                                                                 |
| departmentObject/id                                                     | string          | A UUID                                                                                             |
| departmentObject/name                                                   | string          | The name of the department                                                                         |
| departmentObject/description                                            | string          | A description of this department                                                                   |
| departmentObject/metadata                                               | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| departmentObject/metadata/createdDate                                   | string          | Date and time when the record was created                                                          |
| departmentObject/metadata/createdByUserId                               | string          | ID of the user who created the record (when available)                                             |
| departmentObject/metadata/createdByUsername                             | string          | Username of the user who created the record (when available)                                       |
| departmentObject/metadata/updatedDate                                   | string          | Date and time when the record was last updated                                                     |
| departmentObject/metadata/updatedByUserId                               | string          | ID of the user who last updated the record (when available)                                        |
| departmentObject/metadata/updatedByUsername                             | string          | Username of the user who last updated the record (when available)                                  |
| courseListingId                                                         | string          | A UUID                                                                                             |
| courseListingObject                                                     | object          | An actual instantiation in time and space of a course                                              |
| courseListingObject/id                                                  | string          | A UUID                                                                                             |
| courseListingObject/registrarId                                         | string          | The registration id                                                                                |
| courseListingObject/externalId                                          | string          | An external identifier associated with this listing                                                |
| courseListingObject/servicepointId                                      | string          | A UUID                                                                                             |
| courseListingObject/servicepointObject                                  | object          | The service point associated with this listing's reserves                                          |
| courseListingObject/servicepointObject/id                               | string          | Id of service-point object                                                                         |
| courseListingObject/servicepointObject/name                             | string          | service-point name, a required field                                                               |
| courseListingObject/servicepointObject/code                             | string          | service-point code, a required field                                                               |
| courseListingObject/servicepointObject/discoveryDisplayName             | string          | display name, a required field                                                                     |
| courseListingObject/servicepointObject/description                      | string          | description of the service-point                                                                   |
| courseListingObject/servicepointObject/shelvingLagTime                  | integer         | shelving lag time                                                                                  |
| courseListingObject/servicepointObject/pickupLocation                   | boolean         | indicates whether or not the service point is a pickup location                                    |
| courseListingObject/servicepointObject/holdShelfExpiryPeriod            | object          | schema for time-period, which contains time interval 'duration' and the time unit                  |
| courseListingObject/servicepointObject/holdShelfExpiryPeriod/duration   | integer         | Duration interval                                                                                  |
| courseListingObject/servicepointObject/holdShelfExpiryPeriod/intervalId | string          | Unit of time for the duration                                                                      |
| courseListingObject/servicepointObject/staffSlips                       | array           | List of staff slips for this service point                                                         |
| courseListingObject/servicepointObject/staffSlips/id                    | string          | The ID of the staff slip                                                                           |
| courseListingObject/servicepointObject/staffSlips/printByDefault        | boolean         | Whether or not to print the staff slip by default                                                  |
| courseListingObject/locationId                                          | string          | A UUID                                                                                             |
| courseListingObject/locationObject                                      | object          | The location associated with this listing's reserves                                               |
| courseListingObject/locationObject/id                                   | string          | id of this (shelf) location record as UUID.                                                        |
| courseListingObject/locationObject/name                                 | string          | Name of the (shelf) location                                                                       |
| courseListingObject/locationObject/code                                 | string          | Code of the (shelf) location, usually an abbreviation of the name.                                 |
| courseListingObject/locationObject/description                          | string          | Description of the (shelf) location.                                                               |
| courseListingObject/locationObject/discoveryDisplayName                 | string          | Name of the (shelf) location to be shown in the discovery.                                         |
| courseListingObject/locationObject/isActive                             | boolean         | Whether this (shelf) location is active. Inactive (shelf) locations can no longer been used.       |
| courseListingObject/locationObject/institutionId                        | string          | The UUID of the institution, the first-level location unit, this (shelf) location belongs to.      |
| courseListingObject/locationObject/campusId                             | string          | The UUID of the campus, the second-level location unit, this (shelf) location belongs to.          |
| courseListingObject/locationObject/libraryId                            | string          | The UUID of the library, the third-level location unit, this (shelf) location belongs to.          |
| courseListingObject/locationObject/details                              | object          | Details about this (shelf) location.                                                               |
| courseListingObject/locationObject/primaryServicePoint                  | string          | The UUID of the primary service point of this (shelf) location.                                    |
| courseListingObject/locationObject/servicePointIds                      | array           | All service points that this (shelf) location has.                                                 |
| courseListingObject/termId                                              | string          | A UUID                                                                                             |
| courseListingObject/termObject                                          | object          | Temporal periods that listings exist in                                                            |
| courseListingObject/termObject/id                                       | string          | A UUID                                                                                             |
| courseListingObject/termObject/name                                     | string          | The name of period                                                                                 |
| courseListingObject/termObject/startDate                                | string          | The beginning of the time period                                                                   |
| courseListingObject/termObject/endDate                                  | string          | The ending of the time period                                                                      |
| courseListingObject/termObject/metadata                                 | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| courseListingObject/termObject/metadata/createdDate                     | string          | Date and time when the record was created                                                          |
| courseListingObject/termObject/metadata/createdByUserId                 | string          | ID of the user who created the record (when available)                                             |
| courseListingObject/termObject/metadata/createdByUsername               | string          | Username of the user who created the record (when available)                                       |
| courseListingObject/termObject/metadata/updatedDate                     | string          | Date and time when the record was last updated                                                     |
| courseListingObject/termObject/metadata/updatedByUserId                 | string          | ID of the user who last updated the record (when available)                                        |
| courseListingObject/termObject/metadata/updatedByUsername               | string          | Username of the user who last updated the record (when available)                                  |
| courseListingObject/courseTypeId                                        | string          | A UUID                                                                                             |
| courseListingObject/courseTypeObject                                    | object          | The type of course a listing is                                                                    |
| courseListingObject/courseTypeObject/id                                 | string          | A UUID                                                                                             |
| courseListingObject/courseTypeObject/name                               | string          | The name of the type                                                                               |
| courseListingObject/courseTypeObject/description                        | string          | A description of this type                                                                         |
| courseListingObject/courseTypeObject/metadata                           | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| courseListingObject/courseTypeObject/metadata/createdDate               | string          | Date and time when the record was created                                                          |
| courseListingObject/courseTypeObject/metadata/createdByUserId           | string          | ID of the user who created the record (when available)                                             |
| courseListingObject/courseTypeObject/metadata/createdByUsername         | string          | Username of the user who created the record (when available)                                       |
| courseListingObject/courseTypeObject/metadata/updatedDate               | string          | Date and time when the record was last updated                                                     |
| courseListingObject/courseTypeObject/metadata/updatedByUserId           | string          | ID of the user who last updated the record (when available)                                        |
| courseListingObject/courseTypeObject/metadata/updatedByUsername         | string          | Username of the user who last updated the record (when available)                                  |
| courseListingObject/instructorObjects                                   | array           | A listing of associated instructor objects                                                         |
| courseListingObject/metadata                                            | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| courseListingObject/metadata/createdDate                                | string          | Date and time when the record was created                                                          |
| courseListingObject/metadata/createdByUserId                            | string          | ID of the user who created the record (when available)                                             |
| courseListingObject/metadata/createdByUsername                          | string          | Username of the user who created the record (when available)                                       |
| courseListingObject/metadata/updatedDate                                | string          | Date and time when the record was last updated                                                     |
| courseListingObject/metadata/updatedByUserId                            | string          | ID of the user who last updated the record (when available)                                        |
| courseListingObject/metadata/updatedByUsername                          | string          | Username of the user who last updated the record (when available)                                  |
| courseNumber                                                            | string          | A unique code identifying this course                                                              |
| sectionName                                                             | string          | A text field denoting this course's section                                                        |
| numberOfStudents                                                        | integer         | The number of students enrolled in this course                                                     |
| metadata                                                                | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate                                                    | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId                                                | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername                                              | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate                                                    | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId                                                | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername                                              | string          | Username of the user who last updated the record (when available)                                  |


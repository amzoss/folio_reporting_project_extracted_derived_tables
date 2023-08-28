---
title: course_reserves
---
## Source:

Module: mod-courses

Interface: /coursereserves/reserves

## Attributes:

| Property Name                                                      | Property Type   | Property Description                                                                                      |
|:-------------------------------------------------------------------|:----------------|:----------------------------------------------------------------------------------------------------------|
| id                                                                 | string          | A UUID                                                                                                    |
| courseListingId                                                    | string          | A UUID                                                                                                    |
| itemId                                                             | string          | A UUID                                                                                                    |
| processingStatusId                                                 | string          | A UUID                                                                                                    |
| processingStatusObject                                             | object          | The processing status for a reserve                                                                       |
| processingStatusObject/id                                          | string          | A UUID                                                                                                    |
| processingStatusObject/name                                        | string          | The name of the status                                                                                    |
| processingStatusObject/description                                 | string          | A description of this status                                                                              |
| processingStatusObject/metadata                                    | object          | Metadata about creation and changes to records, provided by the server (client should not provide)        |
| processingStatusObject/metadata/createdDate                        | string          | Date and time when the record was created                                                                 |
| processingStatusObject/metadata/createdByUserId                    | string          | ID of the user who created the record (when available)                                                    |
| processingStatusObject/metadata/createdByUsername                  | string          | Username of the user who created the record (when available)                                              |
| processingStatusObject/metadata/updatedDate                        | string          | Date and time when the record was last updated                                                            |
| processingStatusObject/metadata/updatedByUserId                    | string          | ID of the user who last updated the record (when available)                                               |
| processingStatusObject/metadata/updatedByUsername                  | string          | Username of the user who last updated the record (when available)                                         |
| startDate                                                          | string          | The beginning of the time period for this reserve                                                         |
| endDate                                                            | string          | The ending of the time period for this reserve                                                            |
| copiedItem                                                         | object          | Cached fields from the item record, for searching                                                         |
| copiedItem/barcode                                                 | string          | Item barcode, from item                                                                                   |
| copiedItem/temporaryLocationId                                     | string          | Temporary Location ID, from item                                                                          |
| copiedItem/temporaryLocationObject                                 | object          | Location record populated from inventory for course-reserves                                              |
| copiedItem/temporaryLocationObject/id                              | string          |                                                                                                           |
| copiedItem/temporaryLocationObject/name                            | string          | name, copied from inventory                                                                               |
| copiedItem/temporaryLocationObject/code                            | string          | code, copied from inventory                                                                               |
| copiedItem/temporaryLocationObject/description                     | string          | description, copied from inventory                                                                        |
| copiedItem/temporaryLocationObject/discoveryDisplayName            | string          | discoveryDisplayName, copied from inventory                                                               |
| copiedItem/temporaryLocationObject/isActive                        | boolean         | isActive, copied from inventory                                                                           |
| copiedItem/temporaryLocationObject/institutionId                   | string          | institutionId, copied from inventory                                                                      |
| copiedItem/temporaryLocationObject/campusId                        | string          | campusId, copied from inventory                                                                           |
| copiedItem/temporaryLocationObject/libraryId                       | string          | libraryId, copied from inventory                                                                          |
| copiedItem/temporaryLocationObject/details                         | object          | details, copied from inventory                                                                            |
| copiedItem/temporaryLocationObject/primaryServicePoint             | string          | primaryServicePoint, copied from inventory                                                                |
| copiedItem/temporaryLocationObject/servicePointIds                 | array           | servicePointIds, copied from inventory                                                                    |
| copiedItem/permanentLocationId                                     | string          | Permanent Location ID, from item                                                                          |
| copiedItem/permanentLocationObject                                 | object          | Location record populated from inventory for course-reserves                                              |
| copiedItem/permanentLocationObject/id                              | string          |                                                                                                           |
| copiedItem/permanentLocationObject/name                            | string          | name, copied from inventory                                                                               |
| copiedItem/permanentLocationObject/code                            | string          | code, copied from inventory                                                                               |
| copiedItem/permanentLocationObject/description                     | string          | description, copied from inventory                                                                        |
| copiedItem/permanentLocationObject/discoveryDisplayName            | string          | discoveryDisplayName, copied from inventory                                                               |
| copiedItem/permanentLocationObject/isActive                        | boolean         | isActive, copied from inventory                                                                           |
| copiedItem/permanentLocationObject/institutionId                   | string          | institutionId, copied from inventory                                                                      |
| copiedItem/permanentLocationObject/campusId                        | string          | campusId, copied from inventory                                                                           |
| copiedItem/permanentLocationObject/libraryId                       | string          | libraryId, copied from inventory                                                                          |
| copiedItem/permanentLocationObject/details                         | object          | details, copied from inventory                                                                            |
| copiedItem/permanentLocationObject/primaryServicePoint             | string          | primaryServicePoint, copied from inventory                                                                |
| copiedItem/permanentLocationObject/servicePointIds                 | array           | servicePointIds, copied from inventory                                                                    |
| copiedItem/title                                                   | string          | Title, from Instance                                                                                      |
| copiedItem/contributors                                            | array           | Contributor information, from Instance                                                                    |
| copiedItem/contributors/name                                       | string          | Personal name, corporate name, meeting name                                                               |
| copiedItem/contributors/contributorTypeId                          | string          | ID for the contributor type term defined as a referencetable in settings                                  |
| copiedItem/contributors/contributorTypeText                        | string          | Free text element for adding contributor type terms other that defined by the MARC code list for relators |
| copiedItem/contributors/contributorNameTypeId                      | string          | Contributor type terms defined by the MARC code list for relators                                         |
| copiedItem/contributors/primary                                    | boolean         | Whether this is the primary contributor                                                                   |
| copiedItem/publication                                             | array           | List of publication items, from Instance                                                                  |
| copiedItem/publication/publisher                                   | string          | Name of publisher, distributor, etc.                                                                      |
| copiedItem/publication/place                                       | string          | Place of publication, distribution, etc.                                                                  |
| copiedItem/publication/dateOfPublication                           | string          | Date (year YYYY) of publication, distribution, etc.                                                       |
| copiedItem/publication/role                                        | string          | The role of the publisher, distributor, etc.                                                              |
| copiedItem/callNumber                                              | string          | The item's call number                                                                                    |
| copiedItem/uri                                                     | string          | A URI to access the item                                                                                  |
| copiedItem/volume                                                  | string          | PENDING                                                                                                   |
| copiedItem/copy                                                    | string          | PENDING                                                                                                   |
| copiedItem/enumeration                                             | string          | PENDING                                                                                                   |
| copiedItem/url                                                     | string          | PENDING                                                                                                   |
| copiedItem/instanceId                                              | string          | The id of the associated instance record                                                                  |
| copiedItem/instanceHrid                                            | string          | The HRID of the associated instance record                                                                |
| copiedItem/instanceDiscoverySuppress                               | boolean         | Whether the associated instance record has been marked as suppressed from discovery                       |
| copiedItem/holdingsId                                              | string          | The id of the associated holdings record                                                                  |
| temporaryLoanTypeId                                                | string          | A UUID                                                                                                    |
| temporaryLoanTypeObject                                            | object          | A loan type                                                                                               |
| temporaryLoanTypeObject/id                                         | string          |                                                                                                           |
| temporaryLoanTypeObject/name                                       | string          | label for the loan type                                                                                   |
| copyrightTracking                                                  | object          | Information about copyright status, volume of material used, etc.                                         |
| copyrightTracking/additionalSectionsUsed                           | boolean         | Additional sections of this item used in this course                                                      |
| copyrightTracking/copyrightStatusId                                | string          | A UUID                                                                                                    |
| copyrightTracking/copyrightStatusObject                            | object          | The copyright status of a reserve                                                                         |
| copyrightTracking/copyrightStatusObject/id                         | string          | A UUID                                                                                                    |
| copyrightTracking/copyrightStatusObject/name                       | string          | The name of the type                                                                                      |
| copyrightTracking/copyrightStatusObject/description                | string          | A description of this type                                                                                |
| copyrightTracking/copyrightStatusObject/metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)        |
| copyrightTracking/copyrightStatusObject/metadata/createdDate       | string          | Date and time when the record was created                                                                 |
| copyrightTracking/copyrightStatusObject/metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                                    |
| copyrightTracking/copyrightStatusObject/metadata/createdByUsername | string          | Username of the user who created the record (when available)                                              |
| copyrightTracking/copyrightStatusObject/metadata/updatedDate       | string          | Date and time when the record was last updated                                                            |
| copyrightTracking/copyrightStatusObject/metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                               |
| copyrightTracking/copyrightStatusObject/metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                         |
| copyrightTracking/totalPagesInItem                                 | integer         | PENDING                                                                                                   |
| copyrightTracking/totalPagesUsed                                   | integer         | PENDING                                                                                                   |
| copyrightTracking/percentOfPages                                   | string          | Percent of pages used                                                                                     |
| copyrightTracking/paymentBasis                                     | string          | PENDING                                                                                                   |
| metadata                                                           | object          | Metadata about creation and changes to records, provided by the server (client should not provide)        |
| metadata/createdDate                                               | string          | Date and time when the record was created                                                                 |
| metadata/createdByUserId                                           | string          | ID of the user who created the record (when available)                                                    |
| metadata/createdByUsername                                         | string          | Username of the user who created the record (when available)                                              |
| metadata/updatedDate                                               | string          | Date and time when the record was last updated                                                            |
| metadata/updatedByUserId                                           | string          | ID of the user who last updated the record (when available)                                               |
| metadata/updatedByUsername                                         | string          | Username of the user who last updated the record (when available)                                         |


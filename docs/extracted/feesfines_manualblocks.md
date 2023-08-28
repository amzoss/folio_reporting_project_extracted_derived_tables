---
title: feesfines_manualblocks
---
## Source:

Module: mod-feesfines

Interface: /manualblocks

## Attributes:

| Property Name              | Property Type   | Property Description                                                                                                                                                                                                                                     |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| type                       | string          | Type of patron block                                                                                                                                                                                                                                     |
| desc                       | string          | Patron block description                                                                                                                                                                                                                                 |
| code                       | string          | Code of the template if block is defined based on a template (optional)                                                                                                                                                                                  |
| staffInformation           | string          | Additional information to staff (optional)                                                                                                                                                                                                               |
| patronMessage              | string          | Message to patron (optional)                                                                                                                                                                                                                             |
| expirationDate             | string          | Date and time the patron block expiration if is provided the patron block should be automatically removed on that date                                                                                                                                   |
| borrowing                  | boolean         | A flag to determine borrowing block action                                                                                                                                                                                                               |
| renewals                   | boolean         | A flag to determine renewal block action                                                                                                                                                                                                                 |
| requests                   | boolean         | A flag to determine request block action                                                                                                                                                                                                                 |
| userId                     | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                                                                                                                                                       |
| metadata/createdDate       | string          | Date and time when the record was created                                                                                                                                                                                                                |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                                                                                                                                                                                   |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                                                                                                                                                                             |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                                                                                                                                                                           |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                                                                                                                                                                              |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                                                                                                                                                                        |
| id                         | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |


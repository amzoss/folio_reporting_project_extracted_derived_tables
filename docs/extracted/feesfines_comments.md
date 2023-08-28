---
title: feesfines_comments
---
## Source:

Module: mod-feesfines

Interface: /comments

## Attributes:

| Property Name              | Property Type   | Property Description                                                                                                                                                                                                                                     |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| paid                       | boolean         | A flag to determine when paying if it is mandatory to add additional information                                                                                                                                                                         |
| waived                     | boolean         | A flag to determine when waiving if it is mandatory to add additional information                                                                                                                                                                        |
| refunded                   | boolean         | A flag to determine when refunding if it is mandatory to add additional information                                                                                                                                                                      |
| transferredManually        | boolean         | A flag to determine when transferring if it is mandatory to add additional information                                                                                                                                                                   |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                                                                                                                                                       |
| metadata/createdDate       | string          | Date and time when the record was created                                                                                                                                                                                                                |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                                                                                                                                                                                   |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                                                                                                                                                                             |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                                                                                                                                                                           |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                                                                                                                                                                              |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                                                                                                                                                                        |
| id                         | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |


---
title: feesfines_feefines
---
## Source:

Module: mod-feesfines

Interface: /feefines

## Attributes:

| Property Name              | Property Type   | Property Description                                                                                                                                                                                                                                     |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| automatic                  | boolean         | A flag to indicate that fee/fine was created automatically.                                                                                                                                                                                              |
| feeFineType                | string          | Description of fee/fine that is up to the discretion of the user                                                                                                                                                                                         |
| defaultAmount              | number          | Amount of fee or fine, which may be overridden.                                                                                                                                                                                                          |
| chargeNoticeId             | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| actionNoticeId             | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| ownerId                    | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                                                                                                                                                       |
| metadata/createdDate       | string          | Date and time when the record was created                                                                                                                                                                                                                |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                                                                                                                                                                                   |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                                                                                                                                                                             |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                                                                                                                                                                           |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                                                                                                                                                                              |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                                                                                                                                                                        |
| id                         | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |


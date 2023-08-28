---
title: inventory_bound_with_part
---
## Source:

Module: mod-inventory-storage

Interface: /inventory-storage/bound-with-parts

## Attributes:

| Property Name              | Property Type   | Property Description                                                                                                                                                                                                                                     |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id                         | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| holdingsRecordId           | string          | the ID of the holdings record representing a part of a bound-with; a UUID                                                                                                                                                                                |
| itemId                     | string          | the ID of the item representing the bind; a UUID                                                                                                                                                                                                         |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                                                                                                                                                       |
| metadata/createdDate       | string          | Date and time when the record was created                                                                                                                                                                                                                |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                                                                                                                                                                                   |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                                                                                                                                                                             |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                                                                                                                                                                           |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                                                                                                                                                                              |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                                                                                                                                                                        |


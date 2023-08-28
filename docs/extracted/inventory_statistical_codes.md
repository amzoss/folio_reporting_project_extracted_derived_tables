---
title: inventory_statistical_codes
---
## Source:

Module: mod-inventory-storage

Interface: /statistical-codes

## Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          | unique ID of the statistical code; a UUID                                                          |
| code                       | string          | statistical code; a distinct label                                                                 |
| name                       | string          | name or description of a statistical code                                                          |
| statisticalCodeTypeId      | string          | a UUID referencing a statistical code type                                                         |
| source                     |                 | label indicating where the statistical code originates from, i.e. 'folio' or 'local'               |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |


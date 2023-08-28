---
title: inventory_electronic_access_relationships
---
## Source:

Module: mod-inventory-storage

Interface: /electronic-access-relationships

## Attributes:

| Property Name              | Property Type   | Property Description                                                                                            |
|:---------------------------|:----------------|:----------------------------------------------------------------------------------------------------------------|
| id                         | string          |                                                                                                                 |
| name                       | string          | label for the type of relationship between a URL and an Instance                                                |
| source                     | string          | Origin of the electronic access relationship record, e.g. 'System', 'User', 'Consortium', 'folio', 'local' etc. |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)              |
| metadata/createdDate       | string          | Date and time when the record was created                                                                       |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                                          |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                                    |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                                  |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                                     |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                               |


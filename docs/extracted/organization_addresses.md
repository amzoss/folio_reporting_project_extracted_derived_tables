---
title: organization_addresses
---
## Source:

Module: mod-organizations-storage

Interface: /organizations-storage/addresses

## Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          | The UUID format string                                                                             |
| addressLine1               | string          | The first line of this address                                                                     |
| addressLine2               | string          | The second line of this address                                                                    |
| city                       | string          | The city for this address                                                                          |
| stateRegion                | string          | The state or region for this address                                                               |
| zipCode                    | string          | The zip code for this address                                                                      |
| country                    | string          | The country for this address                                                                       |
| isPrimary                  | boolean         | Used to set this address as primary for the contact                                                |
| categories                 | array           | The list of categories for this organization address                                               |
| language                   | string          | The language for this organization address                                                         |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |


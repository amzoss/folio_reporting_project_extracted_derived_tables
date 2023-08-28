---
title: organization_phone_numbers
---
## Source:

Module: mod-organizations-storage

Interface: /organizations-storage/phone-numbers

## Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          | The UUID format string                                                                             |
| phoneNumber                | string          | The entire sequence of digits for this phone number                                                |
| categories                 | array           | The list of categories for this organization phone                                                 |
| type                       | string          | The type of this phone number                                                                      |
| isPrimary                  | boolean         | Used to set this phone number as primary for the contact                                           |
| language                   | string          | The language for this organization phone                                                           |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |


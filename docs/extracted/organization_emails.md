---
title: organization_emails
---
## Source:

Module: mod-organizations-storage

Interface: /organizations-storage/emails

## Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          | The UUID format string                                                                             |
| value                      | string          | The value for this email                                                                           |
| description                | string          | The description for this email                                                                     |
| isPrimary                  | boolean         | Used to set this email as primary for the contact                                                  |
| categories                 | array           | The list of categories for this organization email                                                 |
| language                   | string          | The language for this organization email                                                           |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |


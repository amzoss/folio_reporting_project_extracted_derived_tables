---
title: organization_contacts
---
## Source:

Module: mod-organizations-storage

Interface: /organizations-storage/contacts

## Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          | The UUID format string                                                                             |
| prefix                     | string          | The prefix for this contact person                                                                 |
| firstName                  | string          | The first name of this contact person                                                              |
| lastName                   | string          | The last name of this contact person                                                               |
| language                   | string          | The preferred language for this contact person                                                     |
| notes                      | string          | The notes for this contact person                                                                  |
| phoneNumbers               | array           | The list of phone numbers for this contact person                                                  |
| emails                     | array           | The list of emails for this contact person                                                         |
| addresses                  | array           | The list of addresses for this contact person                                                      |
| urls                       | array           | The list of URLs for this contact person                                                           |
| categories                 | array           | The list of contact categories associated with this organization contact person                    |
| inactive                   | boolean         | Used to indicate that a contact is no longer active                                                |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |


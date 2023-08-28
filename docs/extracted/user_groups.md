---
title: user_groups
---
## Source:

Module: mod-users

Interface: /groups

## Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| group                      | string          | The unique name of this group                                                                      |
| desc                       | string          | An explanation of this group                                                                       |
| id                         | string          | A UUID identifying this group                                                                      |
| expirationOffsetInDays     | integer         | The default period in days after which a newly created user that belongs to this group will expire |
| source                     | string          | Origin of the group record, i.e. 'System' or 'User'                                                |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |


---
title: perm_permissions
---
## Source:

Module: mod-permissions

Interface: /perms/permissions

## Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| permissionName             | string          | The unique name of the permission                                                                  |
| displayName                | string          | The human-readable name of the permission                                                          |
| id                         | string          | The globally unique (UUID) identifier for the permission                                           |
| description                | string          | A description of the permission                                                                    |
| tags                       | array           | A list of tags for searching                                                                       |
| subPermissions             | array           | A list of child permissions granted by this permission                                             |
| childOf                    | array           | A list of permissions that 'own' this permission                                                   |
| grantedTo                  | array           | A list of permission users to whom this permission has been granted                                |
| mutable                    | boolean         | Whether or not this permission changes at runtime                                                  |
| visible                    | boolean         | Whether or not this permission is visible to users                                                 |
| dummy                      | boolean         | Is this a temporary dummy permission                                                               |
| deprecated                 | boolean         | Indicates whether this permissions has been marked for deletion (soft deleted)                     |
| moduleName                 | string          | The name of the module (not including version) that defined this permission                        |
| moduleVersion              | string          | The version of the module that defined this permission                                             |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |


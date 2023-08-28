---
title: organization_interfaces
---
## Source:

Module: mod-organizations-storage

Interface: /organizations-storage/interfaces

## Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          | The UUID format string                                                                             |
| name                       | string          | The name of this interface                                                                         |
| uri                        | string          | The URI of this interface                                                                          |
| notes                      | string          | The notes for this interface                                                                       |
| available                  | boolean         | The availability setting for this interface                                                        |
| deliveryMethod             | string          | The delivery method for this interface                                                             |
| statisticsFormat           | string          | The format of the statistics for this interface                                                    |
| locallyStored              | string          | The locally stored location of this interface                                                      |
| onlineLocation             | string          | The online location for this interface                                                             |
| statisticsNotes            | string          | The notes regarding the statistics for this interface                                              |
| type                       | array           | Interface types                                                                                    |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |


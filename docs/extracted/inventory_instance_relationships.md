---
title: inventory_instance_relationships
---
## Source:

Module: mod-inventory-storage

Interface: /instance-storage/instance-relationships

## Attributes:

| Property Name              | Property Type   | Property Description                                                                                                                                                      |
|:---------------------------|:----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id                         | string          |                                                                                                                                                                           |
| superInstanceId            | string          | ID (a UUID) of the super-instance. References an Instance record                                                                                                          |
| subInstanceId              | string          | ID (a UUID) of the sub-instance. References an Instance record                                                                                                            |
| instanceRelationshipTypeId | string          | ID (a UUID) of the InstanceRelationshipType. References controlled vocabulary InstanceRelationshipTypes. Indicates the type of relationship between two Instance records. |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                                                                        |
| metadata/createdDate       | string          | Date and time when the record was created                                                                                                                                 |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                                                                                                    |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                                                                                              |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                                                                                            |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                                                                                               |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                                                                                         |


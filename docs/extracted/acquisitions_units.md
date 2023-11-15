---
title: acquisitions_units
---
## Source:

Module: mod-orders-storage

Interface: /acquisitions-units-storage/units

## Attributes:

| Property Name              | Property Type   | Property Description                                                                                          |
|:---------------------------|:----------------|:--------------------------------------------------------------------------------------------------------------|
| id                         | string          | The UUID format string                                                                                        |
| name                       | string          | a name for this acquisitions unit                                                                             |
| description                | string          | The description of this acq unit                                                                              |
| isDeleted                  | boolean         | If true, the record is marked for deletion at some point. This prevents it from being assigned to any record. |
| protectCreate              | boolean         | if true, only members can create records associated with this acq unit.                                       |
| protectRead                | boolean         | if true, only members can read/view records associated with this acq unit.                                    |
| protectUpdate              | boolean         | if true, only members can update records associated with this acq unit.                                       |
| protectDelete              | boolean         | if true, only members can delete records associated with this acq unit.                                       |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)            |
| metadata/createdDate       | string          | Date and time when the record was created                                                                     |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                                        |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                                  |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                                |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                                   |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                             |


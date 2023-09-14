---
title: circulation_fixed_due_date_schedules
---
## Source:

Module: mod-circulation-storage

Interface: /fixed-due-date-schedule-storage/fixed-due-date...

## Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          | Unique ID (generated UUID)                                                                         |
| name                       | string          | Schedule name                                                                                      |
| description                | string          | Schedule description                                                                               |
| schedules                  | array           | List date ranges with a due date for each                                                          |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |


---
title: circulation_request_policies
---
## Source:

Module: mod-circulation-storage

Interface: /request-policy-storage/request-policies

## Attributes:

| Property Name               | Property Type     | Property Description                                                                               |
|:----------------------------|:------------------|:---------------------------------------------------------------------------------------------------|
| id                          | string            | Unique request policy ID                                                                           |
| name                        | string            | Unique request policy name, required                                                               |
| description                 | string            | Description of request policy                                                                      |
| requestTypes                | array             | Whether the item should be held upon return, recalled or paged for                                 |
| allowedServicePoints        | object            | Allowed pickup service point IDs by request type                                                   |
| allowedServicePoints/Page   | ['array', 'null'] | List of allowed pickup service point IDs                                                           |
| allowedServicePoints/Hold   | ['array', 'null'] | List of allowed pickup service point IDs                                                           |
| allowedServicePoints/Recall | ['array', 'null'] | List of allowed pickup service point IDs                                                           |
| metadata                    | object            | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate        | string            | Date and time when the record was created                                                          |
| metadata/createdByUserId    | string            | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername  | string            | Username of the user who created the record (when available)                                       |
| metadata/updatedDate        | string            | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId    | string            | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername  | string            | Username of the user who last updated the record (when available)                                  |


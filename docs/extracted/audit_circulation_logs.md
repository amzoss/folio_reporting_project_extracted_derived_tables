---
title: audit_circulation_logs
---
## Source:

Module: mod-audit

Interface: /audit-data/circulation/logs

## Attributes:

| Property Name            | Property Type   | Property Description           |
|:-------------------------|:----------------|:-------------------------------|
| id                       | string          | The UUID format string         |
| eventId                  | string          | The UUID format string         |
| userBarcode              | string          | User barcode                   |
| items                    | array           | Notice items                   |
| items/itemBarcode        | string          | Item barcode                   |
| items/itemId             | string          | The UUID format string         |
| items/instanceId         | string          | The UUID format string         |
| items/holdingId          | string          | The UUID format string         |
| items/loanId             | string          | The UUID format string         |
| object                   | string          | The purchase order line format |
| action                   | string          | The purchase order line format |
| date                     | string          | Event date                     |
| servicePointId           | string          | The UUID format string         |
| source                   | string          | Source                         |
| description              | string          | Description                    |
| linkToIds                | object          | Additional data for details    |
| linkToIds/userId         | string          | The UUID format string         |
| linkToIds/requestId      | string          | The UUID format string         |
| linkToIds/feeFineId      | string          | The UUID format string         |
| linkToIds/templateId     | string          | The UUID format string         |
| linkToIds/noticePolicyId | string          | The UUID format string         |


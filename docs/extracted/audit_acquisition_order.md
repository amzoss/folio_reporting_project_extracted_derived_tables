---
title: audit_acquisition_order
---
## Source:

Module: mod-audit

Interface: /audit-data/acquisition/order

## Attributes:

| Property Name   | Property Type   | Property Description                 |
|:----------------|:----------------|:-------------------------------------|
| id              | string          | The UUID format string               |
| action          | string          | The action of the audit event        |
| orderId         | string          | The UUID format string               |
| userId          | string          | The UUID format string               |
| eventDate       | string          | Date time when event triggered       |
| actionDate      | string          | Date time when order action occurred |
| orderSnapshot   | object          | Full snapshot of the order           |


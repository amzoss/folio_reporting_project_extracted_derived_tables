---
title: invoice_voucher_lines
---
## Source:

Module: mod-invoice-storage

Interface: /voucher-storage/voucher-lines

## Attributes:

| Property Name              | Property Type   | Property Description                                                                                                                                       |
|:---------------------------|:----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| id                         | string          | The UUID format string                                                                                                                                     |
| amount                     | number          | Total amount of this voucher                                                                                                                               |
| externalAccountNumber      | string          | All distributions that come from funds with the same account number are grouped by voucher line                                                            |
| fundDistributions          | array           | List of fund distributions                                                                                                                                 |
| sourceIds                  | array           | UUID of invoice lines. There could be many invoice lines against a single voucher line. These are group on a voucher line based on External account number |
| subTransactionId           | string          | The UUID format string                                                                                                                                     |
| voucherId                  | string          | The UUID format string                                                                                                                                     |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                                                         |
| metadata/createdDate       | string          | Date and time when the record was created                                                                                                                  |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                                                                                     |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                                                                               |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                                                                             |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                                                                                |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                                                                          |


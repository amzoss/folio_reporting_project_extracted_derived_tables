---
title: po_receiving_history
---
## Source:

Module: mod-orders-storage

Interface: /orders-storage/receiving-history

## Attributes:

| Property Name       | Property Type   | Property Description                                                                                               |
|:--------------------|:----------------|:-------------------------------------------------------------------------------------------------------------------|
| id                  | string          | The UUID format string                                                                                             |
| caption             | string          | Volume/enumeration information                                                                                     |
| checkin             | boolean         | If true this piece is for the Check-in workflow                                                                    |
| chronology          | string          | Chronology is the descriptive information for the dating scheme of a serial. Synchronized with inventory item.     |
| comment             | string          | Free form commentary                                                                                               |
| dateOrdered         | string          | Date and time when purchase order was opened                                                                       |
| discoverySuppress   | boolean         | Records the fact that the record should not be displayed in a discovery system                                     |
| displayOnHolding    | boolean         | Whether or not receiving history should be displayed in holding record view                                        |
| enumeration         | string          | Enumeration is the descriptive information for the numbering scheme of a serial. Synchronized with inventory item. |
| copyNumber          | string          | Copy number of the piece                                                                                           |
| instanceId          | string          | The UUID format string                                                                                             |
| itemId              | string          | The UUID format string                                                                                             |
| locationId          | string          | The UUID format string                                                                                             |
| pieceFormat         | string          | The format of the piece                                                                                            |
| poLineId            | string          | The UUID format string                                                                                             |
| poLineNumber        | string          | A human readable number assigned to this PO line                                                                   |
| poLineReceiptStatus | string          | The purchase order line receipt status                                                                             |
| purchaseOrderId     | string          | The UUID format string                                                                                             |
| receiptDate         | string          | Date that this item is expected to arrive                                                                          |
| receivedDate        | string          | date received                                                                                                      |
| receivingNote       | string          | A note at the poLine level pertaining to receiving/check-in                                                        |
| receivingStatus     | string          | the status of this piece                                                                                           |
| supplement          | boolean         | Whether or not this is supplementary material                                                                      |
| title               | string          | Title of the instance this poLine is associated with                                                               |


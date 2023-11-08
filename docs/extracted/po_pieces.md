---
title: po_pieces
---
## Source:

Module: mod-orders-storage

Interface: /orders-storage/pieces

## Attributes:

| Property Name     | Property Type   | Property Description                                                                                               |
|:------------------|:----------------|:-------------------------------------------------------------------------------------------------------------------|
| id                | string          | The UUID format string                                                                                             |
| caption           | string          | Volume/enumeration information                                                                                     |
| comment           | string          | Free form commentary                                                                                               |
| format            | string          | The format of the piece                                                                                            |
| itemId            | string          | The UUID format string                                                                                             |
| locationId        | string          | The UUID format string                                                                                             |
| poLineId          | string          | The UUID format string                                                                                             |
| titleId           | string          | The UUID format string                                                                                             |
| holdingId         | string          | The UUID format string                                                                                             |
| displayOnHolding  | boolean         | Whether or not receiving history should be displayed in holding record view                                        |
| enumeration       | string          | Enumeration is the descriptive information for the numbering scheme of a serial. Synchronized with inventory item. |
| chronology        | string          | Chronology is the descriptive information for the dating scheme of a serial. Synchronized with inventory item.     |
| discoverySuppress | boolean         | Records the fact that the record should not be displayed in a discovery system                                     |
| copyNumber        | string          | Copy number of the piece                                                                                           |
| receivingStatus   | string          | the status of this piece                                                                                           |
| supplement        | boolean         | Whether or not this is supplementary material                                                                      |
| receiptDate       | string          | Date that associated item is expected to arrive                                                                    |
| receivedDate      | string          | The date associated item is actually received                                                                      |
| statusUpdatedDate | string          | Date when the status of this piece was last updated                                                                |
| claimingInterval  | integer         | Time interval (in days) for processing claims related to this piece                                                |


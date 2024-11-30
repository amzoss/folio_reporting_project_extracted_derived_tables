---
title: po_pieces
---
## Source:

Module: mod-orders-storage

Interface: /orders-storage/pieces

## Attributes:

| Property Name              | Property Type   | Property Description                                                                                                   |
|:---------------------------|:----------------|:-----------------------------------------------------------------------------------------------------------------------|
| id                         | string          | The UUID format string                                                                                                 |
| displaySummary             | string          | Display summary information                                                                                            |
| comment                    | string          | Free form commentary                                                                                                   |
| format                     | string          | The format of the piece                                                                                                |
| itemId                     | string          | The UUID format string                                                                                                 |
| bindItemId                 | string          | The UUID format string                                                                                                 |
| bindItemTenantId           | string          | Bind item tenant for ECS-enabled clusters                                                                              |
| locationId                 | string          | The UUID format string                                                                                                 |
| poLineId                   | string          | The UUID format string                                                                                                 |
| titleId                    | string          | The UUID format string                                                                                                 |
| holdingId                  | string          | The UUID format string                                                                                                 |
| receivingTenantId          | string          | Receiving tenant for ECS-enabled clusters                                                                              |
| displayOnHolding           | boolean         | Whether or not receiving history should be displayed in holding record view                                            |
| displayToPublic            | boolean         | Whether or not the piece data should display to patrons at point of receipt                                            |
| enumeration                | string          | Enumeration is the descriptive information for the numbering scheme of a serial. Synchronized with inventory item.     |
| chronology                 | string          | Chronology is the descriptive information for the dating scheme of a serial. Synchronized with inventory item.         |
| barcode                    | string          | Barcode is the descriptive information for the barcode of a serial. Synchronized with inventory item.                  |
| accessionNumber            | string          | AccessionNumber is the descriptive information for the accession number of a serial. Synchronized with inventory item. |
| callNumber                 | string          | CallNumber is the descriptive information for the call number of a serial. Synchronized with inventory item.           |
| discoverySuppress          | boolean         | Records the fact that the record should not be displayed in a discovery system                                         |
| copyNumber                 | string          | Copy number of the piece                                                                                               |
| receivingStatus            | string          | The status of a piece                                                                                                  |
| supplement                 | boolean         | Whether or not this is supplementary material                                                                          |
| isBound                    | boolean         | Whether or not piece has already been bound                                                                            |
| receiptDate                | string          | Date that associated item is expected to arrive                                                                        |
| receivedDate               | string          | The date associated item is actually received                                                                          |
| statusUpdatedDate          | string          | Date when the status of this piece was last updated                                                                    |
| claimingInterval           | integer         | Time interval (in days) for processing claims related to this piece                                                    |
| internalNote               | string          | Internal note for Send Claim action                                                                                    |
| externalNote               | string          | External note for Send Claim action to share with Vendor                                                               |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                     |
| metadata/createdDate       | string          | Date and time when the record was created                                                                              |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                                                 |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                                           |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                                         |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                                            |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                                      |


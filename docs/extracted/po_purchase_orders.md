---
title: po_purchase_orders
---
## Source:

Module: mod-orders-storage

Interface: /orders-storage/purchase-orders

## Attributes:

| Property Name              | Property Type   | Property Description                                                                                   |
|:---------------------------|:----------------|:-------------------------------------------------------------------------------------------------------|
| id                         | string          | The UUID format string                                                                                 |
| approved                   | boolean         | whether or not the purchase order has been approved                                                    |
| approvedById               | string          | The UUID format string                                                                                 |
| approvalDate               | string          | Date and time when purchase order was approved                                                         |
| assignedTo                 | string          | UUID of the user this purchase order his assigned to                                                   |
| billTo                     | string          | UUID of the billing address                                                                            |
| closeReason                | object          | purchase order closing reason record                                                                   |
| closeReason/reason         | string          | close reason description                                                                               |
| closeReason/note           | string          | free-form notes related to closing reason                                                              |
| dateOrdered                | string          | Date and time when purchase order was opened                                                           |
| manualPo                   | boolean         | if true, order cannot be sent automatically, e.g. via EDI                                              |
| notes                      | array           | free-form notes associated with this purchase order                                                    |
| poNumber                   | string          | A human readable ID assigned to this purchase order                                                    |
| poNumberPrefix             | string          | Purchase order number prefix                                                                           |
| poNumberSuffix             | string          | Purchase order number suffix                                                                           |
| orderType                  | string          | the purchase order type                                                                                |
| reEncumber                 | boolean         | indicates this purchase order should be re-encumbered each fiscal year. Only applies to ongoing orders |
| ongoing                    | object          | Ongoing details for Purchase Order                                                                     |
| ongoing/interval           | integer         | Renewal interval (in days)                                                                             |
| ongoing/isSubscription     | boolean         | Whether or not this is a subscription                                                                  |
| ongoing/manualRenewal      | boolean         | Whether or not this is a manual renewal                                                                |
| ongoing/notes              | string          | Notes associated with the Ongoing order                                                                |
| ongoing/reviewPeriod       | integer         | Time prior to renewal where changes can be made to subscription                                        |
| ongoing/renewalDate        | string          | The date this Ongoing PO's order lines were renewed                                                    |
| ongoing/reviewDate         | string          | Date when Order has to be reviewed                                                                     |
| shipTo                     | string          | UUID of the shipping address                                                                           |
| template                   | string          | The ID of the order template used for this order. Applies to both PO and POL                           |
| vendor                     | string          | UUID of the vendor record                                                                              |
| workflowStatus             | string          | Composite workflow status                                                                              |
| acqUnitIds                 | array           | acquisition unit ids associated with this purchase order                                               |
| nextPolNumber              | integer         | Number that will be used next time a purchase order line is created                                    |
| tags                       | object          | List of simple tags that can be added to an object                                                     |
| tags/tagList               | array           | List of tags                                                                                           |
| customFields               | object          | Object that contains custom field                                                                      |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)     |
| metadata/createdDate       | string          | Date and time when the record was created                                                              |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                                 |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                           |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                         |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                            |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                      |


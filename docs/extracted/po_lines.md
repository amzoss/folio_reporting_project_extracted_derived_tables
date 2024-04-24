---
title: po_lines
---
## Source:

Module: mod-orders-storage

Interface: /orders-storage/po-lines

## Attributes:

| Property Name                 | Property Type      | Property Description                                                                                                                        |
|:------------------------------|:-------------------|:--------------------------------------------------------------------------------------------------------------------------------------------|
| id                            | string             | The UUID format string                                                                                                                      |
| edition                       | string             | edition of the material                                                                                                                     |
| checkinItems                  | boolean            | if true this will toggle the Check-in workflow for details associated with this PO line                                                     |
| agreementId                   | string             | The UUID format string                                                                                                                      |
| acquisitionMethod             | string             | The UUID format string                                                                                                                      |
| automaticExport               | boolean            | if true then line will be marked as available to export in the EDIFACT format or other format                                               |
| alerts                        | array              | an array of alert record IDs                                                                                                                |
| cancellationRestriction       | boolean            | whether or not there are cancellation restrictions for this purchase order line                                                             |
| cancellationRestrictionNote   | string             | free-form notes related to cancellation restrictions                                                                                        |
| claims                        | array              | list of claims                                                                                                                              |
| claimingActive                | boolean            | Indicates if there is an active claim or dispute                                                                                            |
| claimingInterval              | integer            | Specifies the time interval, in days, within which claims or disputes must be initiated                                                     |
| collection                    | boolean            | whether or not this purchase order line is for a collection                                                                                 |
| contributors                  | array              | list of contributors to the material                                                                                                        |
| cost                          | object             | purchase order line cost record                                                                                                             |
| cost/listUnitPrice            | number             | The per-item list price for physical or resources of 'Other' order format                                                                   |
| cost/listUnitPriceElectronic  | number             | The e-resource per-item list price                                                                                                          |
| cost/currency                 | string             | An ISO currency code                                                                                                                        |
| cost/additionalCost           | number             | Lump sum that is added to the total estimated price - not affected by discount                                                              |
| cost/discount                 | number             | Percentage (0 to 100) or amount (positive number) that is subtracted from the list price time quantities calculation before additional cost |
| cost/discountType             | string             | Percentage or amount discount type                                                                                                          |
| cost/exchangeRate             | number             | Exchange rate                                                                                                                               |
| cost/quantityPhysical         | integer            | Quantity of physical items or resources of 'Other' order format in this purchase order line                                                 |
| cost/quantityElectronic       | integer            | Quantity of electronic items in this purchase order line                                                                                    |
| cost/poLineEstimatedPrice     | number             | The calculated total estimated price for this purchase order line: list price time quantities minus discount amount plus additional cost    |
| cost/fyroAdjustmentAmount     | number             | Adjustment amount if rollover was happen                                                                                                    |
| description                   | string             | description of the material                                                                                                                 |
| details                       | object             | purchase order line details                                                                                                                 |
| details/receivingNote         | string             | notes regarding receiving instructions                                                                                                      |
| details/isAcknowledged        | boolean            | Flag for acknowledge receiving note                                                                                                         |
| details/isBindaryActive       | boolean            | Indicates that this POL is designated as required binding                                                                                   |
| details/productIds            | array              | a list of product identifiers                                                                                                               |
| details/subscriptionFrom      | ['string', 'null'] | the start date of the subscription                                                                                                          |
| details/subscriptionInterval  | integer            | the subscription interval in days                                                                                                           |
| details/subscriptionTo        | ['string', 'null'] | the end date of the subscription                                                                                                            |
| donor                         | string             | the donor contributing to this purchase order line                                                                                          |
| donorOrganizationIds          | array              | donor organization ids associated with this fund                                                                                            |
| eresource                     | object             | purchase order line e-resource details                                                                                                      |
| eresource/activated           | boolean            | whether or not this resource is activated                                                                                                   |
| eresource/activationDue       | integer            | number of days until activation, from date of order placement                                                                               |
| eresource/createInventory     | string             | Shows what inventory objects need to be created for electronic resource                                                                     |
| eresource/trial               | boolean            | whether or not this is a trial                                                                                                              |
| eresource/expectedActivation  | string             | expected date the resource will be activated                                                                                                |
| eresource/userLimit           | integer            | the concurrent user-limit                                                                                                                   |
| eresource/accessProvider      | string             | UUID of the access provider                                                                                                                 |
| eresource/license             | object             | purchase order line license record                                                                                                          |
| eresource/license/code        | string             | license code                                                                                                                                |
| eresource/license/description | string             | license description                                                                                                                         |
| eresource/license/reference   | string             | license reference                                                                                                                           |
| eresource/materialType        | string             | UUID of the material Type                                                                                                                   |
| eresource/resourceUrl         | string             | Electronic resource can be access via this URL                                                                                              |
| fundDistribution              | array              | Fund distribution records for this purchase order line                                                                                      |
| instanceId                    | string             | The UUID format string                                                                                                                      |
| isPackage                     | boolean            | Indicates that this POL is for a package                                                                                                    |
| locations                     | array              | Location records for this purchase order line                                                                                               |
| searchLocationIds             | array              | location ids used for search                                                                                                                |
| lastEDIExportDate             | string             | The last date when line was exported in the EDIFACT file                                                                                    |
| orderFormat                   | string             | The purchase order line format                                                                                                              |
| packagePoLineId               | string             | The UUID format string                                                                                                                      |
| paymentStatus                 | string             | Payment/Receipt status                                                                                                                      |
| physical                      | object             | purchase order line physical material details                                                                                               |
| physical/createInventory      | string             | Shows what inventory objects need to be created for physical resource                                                                       |
| physical/materialType         | string             | UUID of the material Type                                                                                                                   |
| physical/materialSupplier     | string             | UUID of the material supplier record                                                                                                        |
| physical/expectedReceiptDate  | ['string', 'null'] | vendor agreed date prior to the Receipt Due date item is expected to be received by                                                         |
| physical/receiptDue           | ['string', 'null'] | date item should be received by                                                                                                             |
| physical/volumes              | array              | list of volumes included to the physical material                                                                                           |
| poLineDescription             | string             | purchase order line description                                                                                                             |
| poLineNumber                  | string             | A human readable number assigned to this PO line                                                                                            |
| publicationDate               | string             | date (year) of the material's publication                                                                                                   |
| publisher                     | string             | publisher of the material                                                                                                                   |
| purchaseOrderId               | string             | The UUID format string                                                                                                                      |
| receiptDate                   | ['null', 'string'] | date the purchase order line was received                                                                                                   |
| receiptStatus                 | string             | The purchase order line receipt status                                                                                                      |
| renewalNote                   | string             | Renewal note for this purchase order line                                                                                                   |
| reportingCodes                | array              | a list of reporting codes associated with this purchase order line                                                                          |
| requester                     | string             | who requested this purchase order line                                                                                                      |
| rush                          | boolean            | whether or not this is a rush order                                                                                                         |
| selector                      | string             | who selected this material                                                                                                                  |
| source                        | string             | The source of the Order                                                                                                                     |
| tags                          | object             | List of simple tags that can be added to an object                                                                                          |
| tags/tagList                  | array              | List of tags                                                                                                                                |
| titleOrPackage                | string             | title of the material                                                                                                                       |
| vendorDetail                  | object             | purchase order line vendor details                                                                                                          |
| vendorDetail/instructions     | string             | special instructions for the vendor                                                                                                         |
| vendorDetail/noteFromVendor   | string             | free-form notes from the vendor                                                                                                             |
| vendorDetail/vendorAccount    | string             | the accound number on the vendor's end associated with this purchase order line                                                             |
| vendorDetail/referenceNumbers | array              | Reference number items array                                                                                                                |
| customFields                  | object             | Object that contains custom field                                                                                                           |
| metadata                      | object             | Metadata about creation and changes to records, provided by the server (client should not provide)                                          |
| metadata/createdDate          | string             | Date and time when the record was created                                                                                                   |
| metadata/createdByUserId      | string             | ID of the user who created the record (when available)                                                                                      |
| metadata/createdByUsername    | string             | Username of the user who created the record (when available)                                                                                |
| metadata/updatedDate          | string             | Date and time when the record was last updated                                                                                              |
| metadata/updatedByUserId      | string             | ID of the user who last updated the record (when available)                                                                                 |
| metadata/updatedByUsername    | string             | Username of the user who last updated the record (when available)                                                                           |


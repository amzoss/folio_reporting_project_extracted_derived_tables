---
title: finance_transactions
---
## Source:

Module: mod-finance-storage

Interface: /finance-storage/transactions

## Attributes:

| Property Name                       | Property Type   | Property Description                                                                                                         |
|:------------------------------------|:----------------|:-----------------------------------------------------------------------------------------------------------------------------|
| id                                  | string          | The UUID format string                                                                                                       |
| _version                            | integer         | Record version for optimistic locking                                                                                        |
| amount                              | number          | The amount of this transaction. For encumbrances: This is initialAmountEncumbered - (amountAwaitingPayment + amountExpended) |
| awaitingPayment                     | object          | Awaiting payment schema                                                                                                      |
| awaitingPayment/encumbranceId       | string          | The UUID format string                                                                                                       |
| awaitingPayment/releaseEncumbrance  | boolean         | Whether or not remaining encumbered money should be released                                                                 |
| currency                            | string          | Currency code for this transaction - from the system currency                                                                |
| description                         | string          | Description of this transaction                                                                                              |
| encumbrance                         | object          | The encumbrance associated with the payment/credit taking place                                                              |
| encumbrance/amountAwaitingPayment   | number          | Deprecated! Going to be removed in next release. The amount of awaiting for payment                                          |
| encumbrance/amountExpended          | number          | The amount currently expended by this encumbrance                                                                            |
| encumbrance/initialAmountEncumbered | number          | The initial amount of this encumbrance. Shouldn't change once create                                                         |
| encumbrance/status                  | string          | The status of this encumbrance                                                                                               |
| encumbrance/orderType               | string          | Taken from the purchase order                                                                                                |
| encumbrance/orderStatus             | string          | Taken from the purchase order                                                                                                |
| encumbrance/subscription            | boolean         | Taken from the purchase Order,for fiscal year rollover                                                                       |
| encumbrance/reEncumber              | boolean         | Taken from the purchase Order,for fiscal year rollover                                                                       |
| encumbrance/sourcePurchaseOrderId   | string          | The UUID format string                                                                                                       |
| encumbrance/sourcePoLineId          | string          | The UUID format string                                                                                                       |
| expenseClassId                      | string          | The UUID format string                                                                                                       |
| fiscalYearId                        | string          | The UUID format string                                                                                                       |
| fromFundId                          | string          | The UUID format string                                                                                                       |
| invoiceCancelled                    | boolean         | Indicates that related invoice was cancelled                                                                                 |
| paymentEncumbranceId                | string          | The UUID format string                                                                                                       |
| source                              | string          | The readable identifier of the record that resulted in the creation of this transaction                                      |
| sourceFiscalYearId                  | string          | The UUID format string                                                                                                       |
| sourceInvoiceId                     | string          | The UUID format string                                                                                                       |
| sourceInvoiceLineId                 | string          | The UUID format string                                                                                                       |
| tags                                | object          | List of simple tags that can be added to an object                                                                           |
| tags/tagList                        | array           | List of tags                                                                                                                 |
| toFundId                            | string          | The UUID format string                                                                                                       |
| transactionType                     | string          | This describes the type of transaction                                                                                       |
| voidedAmount                        | number          | Voided amount, not to be counted in budget totals                                                                            |
| metadata                            | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                           |
| metadata/createdDate                | string          | Date and time when the record was created                                                                                    |
| metadata/createdByUserId            | string          | ID of the user who created the record (when available)                                                                       |
| metadata/createdByUsername          | string          | Username of the user who created the record (when available)                                                                 |
| metadata/updatedDate                | string          | Date and time when the record was last updated                                                                               |
| metadata/updatedByUserId            | string          | ID of the user who last updated the record (when available)                                                                  |
| metadata/updatedByUsername          | string          | Username of the user who last updated the record (when available)                                                            |


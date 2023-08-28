---
title: organization_organizations
---
## Source:

Module: mod-organizations-storage

Interface: /organizations-storage/organizations

## Attributes:

| Property Name                | Property Type      | Property Description                                                                                                                                                                                                                                    |
|:-----------------------------|:-------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id                           | string             | The UUID format string                                                                                                                                                                                                                                  |
| name                         | string             | The name of this organization                                                                                                                                                                                                                           |
| code                         | string             | The code for this organization                                                                                                                                                                                                                          |
| description                  | string             | The description for this organization                                                                                                                                                                                                                   |
| exportToAccounting           | boolean            | This would keep the invoice from being feed into the batch process (i.e. not generate an external voucher/payment) but would still move values in the system. This might be defined by the vendor relationship and exposed for override on the invoice. |
| status                       | string             | The status of this organization                                                                                                                                                                                                                         |
| organizationTypes            | array              | A list of organization types assigned to this organization                                                                                                                                                                                              |
| language                     | string             | The language for this organization                                                                                                                                                                                                                      |
| aliases                      | array              | The list of aliases for this organization                                                                                                                                                                                                               |
| addresses                    | array              | The list of addresses for this organization                                                                                                                                                                                                             |
| phoneNumbers                 | array              | The list of phone numbers for this organization                                                                                                                                                                                                         |
| emails                       | array              | The list of emails for this organization                                                                                                                                                                                                                |
| urls                         | array              | The list of URLs for this organization                                                                                                                                                                                                                  |
| contacts                     | array              | An array of contact record IDs                                                                                                                                                                                                                          |
| agreements                   | array              | The the list of agreements for this organization                                                                                                                                                                                                        |
| erpCode                      | string             | The ERP code for this organization                                                                                                                                                                                                                      |
| paymentMethod                | string             | The payment method for this organization                                                                                                                                                                                                                |
| accessProvider               | boolean            | The access provider for this organization                                                                                                                                                                                                               |
| governmental                 | boolean            | The setting to mark this organization as governmental                                                                                                                                                                                                   |
| licensor                     | boolean            | The setting to mark this organization as a licensor                                                                                                                                                                                                     |
| materialSupplier             | boolean            | The setting to mark this organization as a material supplier                                                                                                                                                                                            |
| vendorCurrencies             | array              | The list of currencies used by this organization                                                                                                                                                                                                        |
| claimingInterval             | integer            | The claim interval for this organization                                                                                                                                                                                                                |
| discountPercent              | number             | The discount percentage for this organization                                                                                                                                                                                                           |
| expectedActivationInterval   | integer            | The expected activation interval (in days) for this organization                                                                                                                                                                                        |
| expectedInvoiceInterval      | integer            | The expected invoice interval (in days) for this organization                                                                                                                                                                                           |
| renewalActivationInterval    | integer            | The revewal activation interval (in days) for this organization                                                                                                                                                                                         |
| subscriptionInterval         | integer            | The subscription interval (in days) for this organization                                                                                                                                                                                               |
| expectedReceiptInterval      | integer            | The receipt interval (in days) for this organization                                                                                                                                                                                                    |
| taxId                        | string             | The tax ID for this organization                                                                                                                                                                                                                        |
| liableForVat                 | boolean            | The setting to mark this organization liable to collect VAT                                                                                                                                                                                             |
| taxPercentage                | number             | The tax percentage value for this organization                                                                                                                                                                                                          |
| edi                          | object             | The EDI object for this organization (only applicable when isVendor is true)                                                                                                                                                                            |
| edi/vendorEdiCode            | string             | The organization code for this EDI                                                                                                                                                                                                                      |
| edi/vendorEdiType            | string             | The organization type for this EDI                                                                                                                                                                                                                      |
| edi/libEdiCode               | string             | The library code for this EDI                                                                                                                                                                                                                           |
| edi/libEdiType               | string             | The library type for this EDI                                                                                                                                                                                                                           |
| edi/prorateTax               | boolean            | The setting to prorate tax for this EDI                                                                                                                                                                                                                 |
| edi/prorateFees              | boolean            | The setting to prorate fees for this EDI                                                                                                                                                                                                                |
| edi/ediNamingConvention      | string             | The naming convention for this EDI                                                                                                                                                                                                                      |
| edi/sendAcctNum              | boolean            | The setting to send the account number for this EDI                                                                                                                                                                                                     |
| edi/supportOrder             | boolean            | The setting to support order for this EDI                                                                                                                                                                                                               |
| edi/supportInvoice           | boolean            | The setting to support invoice for this EDI                                                                                                                                                                                                             |
| edi/notes                    | string             | The notes for this EDI                                                                                                                                                                                                                                  |
| edi/ediFtp                   | object             | The FTP object for this EDI                                                                                                                                                                                                                             |
| edi/ediFtp/ftpFormat         | string             | The FTP format for this EDI                                                                                                                                                                                                                             |
| edi/ediFtp/serverAddress     | ['string', 'null'] | The server address for this EDI                                                                                                                                                                                                                         |
| edi/ediFtp/username          | string             | The login username for this EDI                                                                                                                                                                                                                         |
| edi/ediFtp/password          | string             | The login password for this EDI                                                                                                                                                                                                                         |
| edi/ediFtp/ftpMode           | string             | The FTP mode for this EDI                                                                                                                                                                                                                               |
| edi/ediFtp/ftpConnMode       | string             | The FTP connection mode for this EDI                                                                                                                                                                                                                    |
| edi/ediFtp/ftpPort           | integer            | The port for this EDI                                                                                                                                                                                                                                   |
| edi/ediFtp/orderDirectory    | string             | The order directory for this EDI                                                                                                                                                                                                                        |
| edi/ediFtp/invoiceDirectory  | string             | The invoice directory for this EDI                                                                                                                                                                                                                      |
| edi/ediFtp/notes             | string             | The notes for this EDI                                                                                                                                                                                                                                  |
| edi/ediJob                   | object             | The job object for this EDI                                                                                                                                                                                                                             |
| edi/ediJob/scheduleEdi       | boolean            | Activate the schedule for this EDI job                                                                                                                                                                                                                  |
| edi/ediJob/schedulingDate    | ['string', 'null'] | The date (MM/DD/YYYY) for this EDI job to start running                                                                                                                                                                                                 |
| edi/ediJob/time              | ['string', 'null'] | The time (h:mm A) for this EDI job                                                                                                                                                                                                                      |
| edi/ediJob/isMonday          | boolean            | The setting to run this EDI job on Mondays                                                                                                                                                                                                              |
| edi/ediJob/isTuesday         | boolean            | The setting to run this EDI job on Tuesdays                                                                                                                                                                                                             |
| edi/ediJob/isWednesday       | boolean            | The setting to run this EDI job on Wednesdays                                                                                                                                                                                                           |
| edi/ediJob/isThursday        | boolean            | The setting to run this EDI job on Thursdays                                                                                                                                                                                                            |
| edi/ediJob/isFriday          | boolean            | The setting to run this EDI job on Fridays                                                                                                                                                                                                              |
| edi/ediJob/isSaturday        | boolean            | The setting to run this EDI job on Saturdays                                                                                                                                                                                                            |
| edi/ediJob/isSunday          | boolean            | The setting to run this EDI job on Sundays                                                                                                                                                                                                              |
| edi/ediJob/sendToEmails      | string             | The comma delimited list of email addresses to notify when this EDI job runs                                                                                                                                                                            |
| edi/ediJob/notifyAllEdi      | boolean            | The setting to notify all receivers when this EDI job runs                                                                                                                                                                                              |
| edi/ediJob/notifyInvoiceOnly | boolean            | The setting to notify only the invoice receiver when this EDI job runs                                                                                                                                                                                  |
| edi/ediJob/notifyErrorOnly   | boolean            | The setting to notiry on the error receiver when this EDI job runs                                                                                                                                                                                      |
| edi/ediJob/schedulingNotes   | string             | The schedule notes for this EDI job                                                                                                                                                                                                                     |
| interfaces                   | array              | The list of interfaces assigned to this organization                                                                                                                                                                                                    |
| accounts                     | array              | The list of accounts for this organization                                                                                                                                                                                                              |
| isVendor                     | boolean            | Used to indicate that this organization is also a vendor                                                                                                                                                                                                |
| sanCode                      | string             | The SAN code for this organization address                                                                                                                                                                                                              |
| changelogs                   | array              | The list of changes applied to this organization                                                                                                                                                                                                        |
| acqUnitIds                   | array              | Acquisition unit UUIDs associated with this organization                                                                                                                                                                                                |
| tags                         | object             | List of simple tags that can be added to an object                                                                                                                                                                                                      |
| tags/tagList                 | array              | List of tags                                                                                                                                                                                                                                            |
| metadata                     | object             | Metadata about creation and changes to records, provided by the server (client should not provide)                                                                                                                                                      |
| metadata/createdDate         | string             | Date and time when the record was created                                                                                                                                                                                                               |
| metadata/createdByUserId     | string             | ID of the user who created the record (when available)                                                                                                                                                                                                  |
| metadata/createdByUsername   | string             | Username of the user who created the record (when available)                                                                                                                                                                                            |
| metadata/updatedDate         | string             | Date and time when the record was last updated                                                                                                                                                                                                          |
| metadata/updatedByUserId     | string             | ID of the user who last updated the record (when available)                                                                                                                                                                                             |
| metadata/updatedByUsername   | string             | Username of the user who last updated the record (when available)                                                                                                                                                                                       |

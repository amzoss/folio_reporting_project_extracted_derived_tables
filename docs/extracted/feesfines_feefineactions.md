---
title: feesfines_feefineactions
---
## Source:

Module: mod-feesfines

Interface: /feefineactions

## Attributes:

| Property Name          | Property Type   | Property Description                                                                                                                                                                                                                                     |
|:-----------------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| dateAction             | string          | Date and time the transaction of the fine/fee was created                                                                                                                                                                                                |
| typeAction             | string          | Type of activity including the type of transaction                                                                                                                                                                                                       |
| comments               | string          | Additional information entered as part of the activity or on this screen as a 'Staff info only' activity                                                                                                                                                 |
| notify                 | boolean         | A flag to determine if a patron should be notified or not                                                                                                                                                                                                |
| amountAction           | number          | Amount of activity                                                                                                                                                                                                                                       |
| balance                | number          | Calculated amount of remaining balance based on original fee/fine and what has been paid/waived/transferred/refunded                                                                                                                                     |
| transactionInformation | string          | Number or other transaction id related to payment                                                                                                                                                                                                        |
| createdAt              | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| originalCreatedAt      | string          | Original invalid (non-UUID) value of 'createdAt' moved here when UUID-validation was enabled for 'createdAt'                                                                                                                                             |
| source                 | string          | Person who processed activity (from login information)                                                                                                                                                                                                   |
| paymentMethod          | string          | Overall status of the action-setting                                                                                                                                                                                                                     |
| accountId              | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| userId                 | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| id                     | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |


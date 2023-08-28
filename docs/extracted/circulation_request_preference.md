---
title: circulation_request_preference
---
## Source:

Module: mod-circulation-storage

Interface: /request-preference-storage/request-preference

## Attributes:

| Property Name                | Property Type   | Property Description                                                                               |
|:-----------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                           | string          | Unique request preference ID                                                                       |
| userId                       | string          | UUID of user associated with this request preference                                               |
| holdShelf                    | boolean         | Whether 'Hold Shelf' option is available to the user.                                              |
| delivery                     | boolean         | Whether 'Delivery' option is available to the user.                                                |
| defaultServicePointId        | string          | UUID of default service point for 'Hold Shelf' option                                              |
| defaultDeliveryAddressTypeId | string          | UUID of user's address type                                                                        |
| fulfillment                  | string          | Preferred fulfillment type. Possible values are 'Delivery', 'Hold Shelf'                           |
| metadata                     | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate         | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId     | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername   | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate         | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId     | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername   | string          | Username of the user who last updated the record (when available)                                  |


---
title: circulation_check_ins
---
## Source:

Module: mod-circulation-storage

Interface: /check-in-storage/check-ins

## Attributes:

| Property Name            | Property Type   | Property Description                                                                                                                                                                                                                                     |
|:-------------------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id                       | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| occurredDateTime         | string          | Date and time when the check-in occurred                                                                                                                                                                                                                 |
| itemId                   | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| itemStatusPriorToCheckIn | string          | Item status prior to check-in                                                                                                                                                                                                                            |
| requestQueueSize         | integer         | Request queue size for the item                                                                                                                                                                                                                          |
| itemLocationId           | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| servicePointId           | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| performedByUserId        | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |


---
title: po_organization.sql
---
# Documentation: po_organization.sql

## Attributes:

|   Attribute # | Attribute                | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description                                      | Notes   |
|--------------:|:-------------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:-------------------------------------------------|:--------|
|             1 | po_number                | text   |                   |                  |                      |                 |                            |               | A human readable number assigned to PO           |         |
|             2 | vendor_id                | uuid   |                   |                  |                      |                 |                            |               | The unique UUID for the vendor                   |         |
|             3 | organization_id          | uuid   |                   |                  |                      |                 |                            |               | The unique UUID for the organization             |         |
|             4 | organization_code        | text   |                   |                  |                      |                 |                            |               | The code of the organization                     |         |
|             5 | organization_name        | text   |                   |                  |                      |                 |                            |               | The name of the organization                     |         |
|             6 | organization_description | text   |                   |                  |                      |                 |                            |               | The description for the organization             |         |
|             7 | is_vendor                | bool   |                   |                  |                      |                 |                            |               | Indication for the organization if also a vendor |         |
|             8 | contact_first_name       | text   |                   |                  |                      |                 |                            |               | Contact First name for the organization          |         |
|             9 | contact_last_name        | text   |                   |                  |                      |                 |                            |               | Contact Last name for the organization           |         |
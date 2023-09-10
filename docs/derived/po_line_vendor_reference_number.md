---
title: po_line_vendor_reference_number.sql
---
## Attributes:

|   Attribute # | Attribute                    | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description                                      | Notes   |
|--------------:|:-----------------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:-------------------------------------------------|:--------|
|             1 | po_line_id                   | uuid   |                   |                  |                      |                 |                            |               | UUID identifying this purchase order line        |         |
|             2 | po_line_number               | text   |                   |                  |                      |                 |                            |               | A human readable number assigned to this PO line |         |
|             3 | vendor_reference_number      | text   |                   |                  |                      |                 |                            |               | A reference number for this purchase order line  |         |
|             4 | vendor_reference_number_type | text   |                   |                  |                      |                 |                            |               | The reference number type                        |         |
|             5 | vendor_instructions          | text   |                   |                  |                      |                 |                            |               | Special instructions for the vendor              |         |
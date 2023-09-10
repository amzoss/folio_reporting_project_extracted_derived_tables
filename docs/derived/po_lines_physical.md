---
title: po_lines_physical.sql
---
# Documentation: po_lines_physical.sql

## Attributes:

|   Attribute # | Attribute                      | Type        | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description                                                                         | Notes   |
|--------------:|:-------------------------------|:------------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:------------------------------------------------------------------------------------|:--------|
|             1 | pol_id                         | uuid        |                   |                  |                      |                 |                            |               | UUID identifying this purchase order line                                           |         |
|             2 | pol_phys_create_inventory      | text        |                   |                  |                      |                 |                            |               | Shows what inventory objects need to be created for electronic resource             |         |
|             3 | pol_phys_mat_type_id           | uuid        |                   |                  |                      |                 |                            |               | UUID of the material Type                                                           |         |
|             4 | pol_phys_mat_type_name         | text        |                   |                  |                      |                 |                            |               | Label for the material type                                                         |         |
|             5 | pol_phys_mat_supplier_id       | uuid        |                   |                  |                      |                 |                            |               | UUID of the material supplier record                                                |         |
|             6 | supplier_org_name              | text        |                   |                  |                      |                 |                            |               | UUID of this purchase order                                                         |         |
|             7 | pol_phys_expected_receipt_date | timestamptz |                   |                  |                      |                 |                            |               | Vendor agreed date prior to the Receipt Due date item is expected to be received by |         |
|             8 | pol_phys_receipt_due           | timestamptz |                   |                  |                      |                 |                            |               | Date item should be received by                                                     |         |
|             9 | pol_volumes                    | text        |                   |                  |                      |                 |                            |               | List of volumes included to the physical material                                   |         |
|            10 | pol_volumes_ordinality         | int8        |                   |                  |                      |                 |                            |               | Volumes ordinality                                                                  |         |
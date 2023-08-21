---
title: po_acq_unit_ids.sql
---
# Documentation: po_acq_unit_ids.sql

## Attributes:

|   Attribute # | Attribute                | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description                                       | Notes   |
|--------------:|:-------------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------------------------------------------|:--------|
|             1 | po_id                    | uuid   |                   |                  |                      |                 |                            |               | UUID of this purchase order                       |         |
|             2 | po_number                | text   |                   |                  |                      |                 |                            |               | human readable ID assigned to this purchase order |         |
|             3 | po_acquisition_unit_id   | uuid   |                   |                  |                      |                 |                            |               | UUID of this acquisitions unit record             |         |
|             4 | po_acquisition_unit_name | text   |                   |                  |                      |                 |                            |               | Name for this acquisitions unit                   |         |
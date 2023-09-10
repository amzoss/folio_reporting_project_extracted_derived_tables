---
title: po_lines_locations.sql
---
# Documentation: po_lines_locations.sql

## Attributes:

|   Attribute # | Attribute           | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description                                                                                 | Notes   |
|--------------:|:--------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:--------------------------------------------------------------------------------------------|:--------|
|             1 | pol_id              | uuid   |                   |                  |                      |                 |                            |               | UUID identifying this purchase order line                                                   |         |
|             2 | pol_loc_qty         | int4   |                   |                  |                      |                 |                            |               | Combined/total quantity of physical and electronic items                                    |         |
|             3 | pol_loc_qty_elec    | int4   |                   |                  |                      |                 |                            |               | Quantity of electronic items in this purchase order line                                    |         |
|             4 | pol_loc_qty_phys    | int4   |                   |                  |                      |                 |                            |               | Quantity of physical items or resources of "Other" order format in this purchase order line |         |
|             5 | pol_location_id     | uuid   |                   |                  |                      |                 |                            |               | UUID of the (inventory) location record or Holding UUID associated with order line          |         |
|             6 | pol_location_name   | text   |                   |                  |                      |                 |                            |               | Name of the location associated with pol_location_id                                        |         |
|             7 | pol_location_source | text   |                   |                  |                      |                 |                            |               | Source of the location associated with pol_location_id                                      |         |
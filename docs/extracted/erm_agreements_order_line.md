---
title: erm_agreements_order_line
---
## Source:

Module: mod_agreements

Interface: order_line

## Attributes:

| Property Name   | Property Type   | Property Description                                                                         |
|:----------------|:----------------|:---------------------------------------------------------------------------------------------|
| pol_id          |                 | UUID of order_line record                                                                    |
| pol_orders_fk   |                 | ID of purchase order line in Orders app                                                      |
| pol_owner_fk    |                 | ID of entitlement (mod_agreements.entitlement.ent_id) to which purchase order line is linked |


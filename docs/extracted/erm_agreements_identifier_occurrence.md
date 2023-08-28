---
title: erm_agreements_identifier_occurrence
---
## Source:

Module: mod_agreements

Interface: identifier_occurrence

## Attributes:

| Property Name    | Property Type   | Property Description                                                                                                     |
|:-----------------|:----------------|:-------------------------------------------------------------------------------------------------------------------------|
| io_id            |                 | UUID of identifier occurrence                                                                                            |
| io_ti_fk         |                 | ID of title_instance which is linked to the identifier                                                                   |
| io_status        |                 | ID of reference data value (mod_agreements.refdata_value.rdv_id) which describes the status of the identifier occurrence |
| io_identifier_fk |                 | ID of the identifier which is ‘occurring’ against a title_instance                                                       |


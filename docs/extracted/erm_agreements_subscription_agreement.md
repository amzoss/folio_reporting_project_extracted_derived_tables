---
title: erm_agreements_subscription_agreement
---
## Source:

Module: mod_agreements

Interface: subscription_agreement

## Attributes:

| Property Name         | Property Type   | Property Description                                                                                                                                                                                                                                     |
|:----------------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| sa_id                 |                 | UUID of Agreement                                                                                                                                                                                                                                        |
| sa_name               |                 | A name for the agreement assigned by the institution                                                                                                                                                                                                     |
| sa_description        |                 | A description for the agreement assigned by the institution                                                                                                                                                                                              |
| sa_agreement_status   |                 | ID of reference data value (mod_agreements.refdata_value.rdv_id) which describes the current status of the agreement (e.g. Active, Closed)                                                                                                               |
| sa_reason_for_closure |                 | ID of reference data value (mod_agreements.refdata_value.rdv_id) which describes for a closed agreement, the reason the agreement has been closed (a closed agreement is one with status == "Closed" - set via sa_agreement_status)                      |
| sa_renewal_priority   |                 | ID of reference data value (mod_agreements.refdata_value.rdv_id) which describes whether an agreement should be renewed, reviewed or cancelled                                                                                                           |
| sa_is_perpetual       |                 | ID of reference data value (mod_agreements.refdata_value.rdv_id) which describes whether the agreement is a perpetual agreement or not                                                                                                                   |
| sa_local_reference    |                 | Where an agreement has been created through an integration / data import from an external system the sa_local_reference is used to store a reference/identifier for the agreement in the external system to support ongoing data synchronisation/updates |
| sa_license_note       |                 | To record any general information about the license for the Agreement                                                                                                                                                                                    |
| custom_properties_id  |                 | ID used to link custom_properties (aka supplementary properties) via mod_agreements.custom_properties.parent_id to an agreement. (n.b. each agreement can have zero to many custom_properties)                                                           |


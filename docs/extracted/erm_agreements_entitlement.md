---
title: erm_agreements_entitlement
---
## Source:

Module: mod_agreements

Interface: entitlement

## Attributes:

| Property Name   | Property Type   | Property Description                                                                                                                                                                                               |
|:----------------|:----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ent_id          |                 | UUID of Entitlement (aka Agreement Line)                                                                                                                                                                           |
| ent_owner_fk    |                 | ID of Agreement (mod_agreements.subscription_agreement.sa_id) to which the entitlement belongs                                                                                                                     |
| ent_resource_fk |                 | ID of the resource (mod_agreements.erm_resource.id, mod_agreements.package.id, mod_agreements.package_content_item.id ) which the Entitlement gives access to                                                      |
| ent_active_from |                 | Date from which the entitlement was active in format yyyy-MM-dd. No time or timezone                                                                                                                               |
| ent_active_to   |                 | Date to which the entitlement was active in format yyyy-MM-dd. No time or timezone                                                                                                                                 |
| ent_authority   |                 | Where an entitlement gives access to a resource described in a source other than the mod_agreements internal knowledgebase, the ent_authority is a way of identifying where the definition of the resource is held |
| ent_reference   |                 | Where an entitlement gives access to a resource described in a source other than the mod_agreements internal knowledgebase, the ent_reference is the ID for the resource in the source identified by ent_authority |
| ent_note        |                 | A textual note about the entitlement                                                                                                                                                                               |


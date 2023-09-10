---
title: agreements_subscription_agreement_org_ext.sql
---
# Documentation: agreements_subscription_agreement_org_ext.sql

## Attributes:

|   Attribute # | Attribute                 | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description                                     | Notes   |
|--------------:|:--------------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:------------------------------------------------|:--------|
|             1 | sao_id                    | uuid   |                   |                  |                      |                 |                            |               | UUID for subscription and organization pairing  |         |
|             2 | subscription_agreement_id | uuid   |                   |                  |                      |                 |                            |               | UUId for the subscritpion and agreement pairing |         |
|             3 | sao_org_id                | uuid   |                   |                  |                      |                 |                            |               | The unique UUID for an organization             |         |
|             4 | sao_org_name              | text   |                   |                  |                      |                 |                            |               | The name of an organization                     |         |
|             5 | sao_role_id               | uuid   |                   |                  |                      |                 |                            |               | ID of the type of provider role                 |         |
|             6 | sao_role_value            | text   |                   |                  |                      |                 |                            |               | Name of the type of provider role               |         |
|             7 | sao_role_label            | text   |                   |                  |                      |                 |                            |               | Public name of the type of provider role        |         |
|             8 | sao_note                  | text   |                   |                  |                      |                 |                            |               | Notes attached                                  |         |
|             9 | org_orgs_uuid             | uuid   |                   |                  |                      |                 |                            |               | UUID of organization attached to the agreement  |         |
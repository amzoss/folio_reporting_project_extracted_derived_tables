---
title: licenses_license_ext.sql
---
# Documentation: licenses_license_ext.sql

## Attributes:

|   Attribute # | Attribute           | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description                                           | Notes   |
|--------------:|:--------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:------------------------------------------------------|:--------|
|             1 | license_id          | uuid   |                   |                  |                      |                 |                            |               | The UUID of the license                               |         |
|             2 | license_name        | text   |                   |                  |                      |                 |                            |               | Name of license                                       |         |
|             3 | license_description | text   |                   |                  |                      |                 |                            |               | Description of license                                |         |
|             4 | license_start       | date   |                   |                  |                      |                 |                            |               | Start date of this license                            |         |
|             5 | license_end         | date   |                   |                  |                      |                 |                            |               | End date of this license                              |         |
|             6 | license_type        | text   |                   |                  |                      |                 |                            |               | Reference data value for license type                 |         |
|             7 | license_status      | text   |                   |                  |                      |                 |                            |               | Reference data value for license status               |         |
|             8 | license_org         | text   |                   |                  |                      |                 |                            |               | Name of the organization                              |         |
|             9 | license_org_role    | text   |                   |                  |                      |                 |                            |               | Reference data value for the role of the organization |         |
|            10 | license_org_uuid    | uuid   |                   |                  |                      |                 |                            |               | UUID of organization                                  |         |
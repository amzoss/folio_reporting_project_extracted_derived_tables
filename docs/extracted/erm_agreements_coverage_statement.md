---
title: erm_agreements_coverage_statement
---
## Source:

Module: mod_agreements

Interface: coverage_statement

## Attributes:

| Property Name   | Property Type   | Property Description                                                                          |
|:----------------|:----------------|:----------------------------------------------------------------------------------------------|
| cs_id           |                 | UUID for coverage_statement                                                                   |
| cs_start_issue  |                 | Earliest issue of the resource available as part of this coverage                             |
| cs_end_issue    |                 | Latest issue of the resource available as part of this coverage                               |
| cs_start_volume |                 | Earliest volume of the resource available as part of this coverage                            |
| cs_end_volume   |                 | Latest volume of the resource available as part of this coverage                              |
| cs_resource_fk  |                 | The ID of the erm_resource to which this coverage_statement applies                           |
| cs_start_date   |                 | Earliest date of publication of material from the resource available as part of this coverage |
| cs_end_date     |                 | Latest date of publication of material from resource available as part of this coverage       |


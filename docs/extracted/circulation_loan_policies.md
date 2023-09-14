---
title: circulation_loan_policies
---
## Source:

Module: mod-circulation-storage

Interface: /loan-policy-storage/loan-policies

## Attributes:

| Property Name                                                      | Property Type   | Property Description                                                                               |
|:-------------------------------------------------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                                                                 | string          |                                                                                                    |
| name                                                               | string          | The name of the policy.                                                                            |
| description                                                        | string          | Description of the loan policy                                                                     |
| loanable                                                           | boolean         | Flag that indicates whether this policy allows loans                                               |
| loansPolicy                                                        | object          | Settings for loans                                                                                 |
| loansPolicy/profileId                                              | string          | Loan profile                                                                                       |
| loansPolicy/period                                                 | object          | Time interval defined by its duration                                                              |
| loansPolicy/period/duration                                        | integer         | Duration of the period, number of times the interval repeats                                       |
| loansPolicy/period/intervalId                                      | string          | Interval for the period, e.g. hours, days or weeks                                                 |
| loansPolicy/closedLibraryDueDateManagementId                       | string          | Closed library due date management                                                                 |
| loansPolicy/gracePeriod                                            | object          | Time interval defined by its duration                                                              |
| loansPolicy/gracePeriod/duration                                   | integer         | Duration of the period, number of times the interval repeats                                       |
| loansPolicy/gracePeriod/intervalId                                 | string          | Interval for the period, e.g. hours, days or weeks                                                 |
| loansPolicy/openingTimeOffset                                      | object          | Time interval defined by its duration                                                              |
| loansPolicy/openingTimeOffset/duration                             | integer         | Duration of the period, number of times the interval repeats                                       |
| loansPolicy/openingTimeOffset/intervalId                           | string          | Interval for the period, e.g. hours, days or weeks                                                 |
| loansPolicy/fixedDueDateScheduleId                                 | string          | Fixed due date schedule (due date limit)                                                           |
| loansPolicy/itemLimit                                              | integer         | Number of items allowed                                                                            |
| renewable                                                          | boolean         | Is item renewable                                                                                  |
| renewalsPolicy                                                     | object          | Settings for renewals                                                                              |
| renewalsPolicy/unlimited                                           | boolean         | Unlimited renewals                                                                                 |
| renewalsPolicy/numberAllowed                                       | number          | Number of renewals allowed                                                                         |
| renewalsPolicy/renewFromId                                         | string          | Renew from date                                                                                    |
| renewalsPolicy/differentPeriod                                     | boolean         | Renewal period different from original loan                                                        |
| renewalsPolicy/period                                              | object          | Time interval defined by its duration                                                              |
| renewalsPolicy/period/duration                                     | integer         | Duration of the period, number of times the interval repeats                                       |
| renewalsPolicy/period/intervalId                                   | string          | Interval for the period, e.g. hours, days or weeks                                                 |
| renewalsPolicy/alternateFixedDueDateScheduleId                     | string          | Alternate fixed due date schedule (due date limit) for renewals                                    |
| requestManagement                                                  | object          | Settings for various request types                                                                 |
| requestManagement/recalls                                          | object          | Settings for recall requests                                                                       |
| requestManagement/recalls/alternateGracePeriod                     | object          | Time interval defined by its duration                                                              |
| requestManagement/recalls/alternateGracePeriod/duration            | integer         | Duration of the period, number of times the interval repeats                                       |
| requestManagement/recalls/alternateGracePeriod/intervalId          | string          | Interval for the period, e.g. hours, days or weeks                                                 |
| requestManagement/recalls/minimumGuaranteedLoanPeriod              | object          | Time interval defined by its duration                                                              |
| requestManagement/recalls/minimumGuaranteedLoanPeriod/duration     | integer         | Duration of the period, number of times the interval repeats                                       |
| requestManagement/recalls/minimumGuaranteedLoanPeriod/intervalId   | string          | Interval for the period, e.g. hours, days or weeks                                                 |
| requestManagement/recalls/recallReturnInterval                     | object          | Time interval defined by its duration                                                              |
| requestManagement/recalls/recallReturnInterval/duration            | integer         | Duration of the period, number of times the interval repeats                                       |
| requestManagement/recalls/recallReturnInterval/intervalId          | string          | Interval for the period, e.g. hours, days or weeks                                                 |
| requestManagement/recalls/allowRecallsToExtendOverdueLoans         | boolean         | Whether recalls are allowed to extend overdue loans                                                |
| requestManagement/recalls/alternateRecallReturnInterval            | object          | Time interval defined by its duration                                                              |
| requestManagement/recalls/alternateRecallReturnInterval/duration   | integer         | Duration of the period, number of times the interval repeats                                       |
| requestManagement/recalls/alternateRecallReturnInterval/intervalId | string          | Interval for the period, e.g. hours, days or weeks                                                 |
| requestManagement/holds                                            | object          | Settings for hold requests                                                                         |
| requestManagement/holds/alternateCheckoutLoanPeriod                | object          | Time interval defined by its duration                                                              |
| requestManagement/holds/alternateCheckoutLoanPeriod/duration       | integer         | Duration of the period, number of times the interval repeats                                       |
| requestManagement/holds/alternateCheckoutLoanPeriod/intervalId     | string          | Interval for the period, e.g. hours, days or weeks                                                 |
| requestManagement/holds/renewItemsWithRequest                      | boolean         | Allow renewal of items with active, pending hold request                                           |
| requestManagement/holds/alternateRenewalLoanPeriod                 | object          | Time interval defined by its duration                                                              |
| requestManagement/holds/alternateRenewalLoanPeriod/duration        | integer         | Duration of the period, number of times the interval repeats                                       |
| requestManagement/holds/alternateRenewalLoanPeriod/intervalId      | string          | Interval for the period, e.g. hours, days or weeks                                                 |
| requestManagement/pages                                            | object          | Settings for page requests                                                                         |
| requestManagement/pages/alternateCheckoutLoanPeriod                | object          | Time interval defined by its duration                                                              |
| requestManagement/pages/alternateCheckoutLoanPeriod/duration       | integer         | Duration of the period, number of times the interval repeats                                       |
| requestManagement/pages/alternateCheckoutLoanPeriod/intervalId     | string          | Interval for the period, e.g. hours, days or weeks                                                 |
| requestManagement/pages/renewItemsWithRequest                      | boolean         | Allow renewal of items with active, pending page request                                           |
| requestManagement/pages/alternateRenewalLoanPeriod                 | object          | Time interval defined by its duration                                                              |
| requestManagement/pages/alternateRenewalLoanPeriod/duration        | integer         | Duration of the period, number of times the interval repeats                                       |
| requestManagement/pages/alternateRenewalLoanPeriod/intervalId      | string          | Interval for the period, e.g. hours, days or weeks                                                 |
| metadata                                                           | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate                                               | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId                                           | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername                                         | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate                                               | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId                                           | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername                                         | string          | Username of the user who last updated the record (when available)                                  |


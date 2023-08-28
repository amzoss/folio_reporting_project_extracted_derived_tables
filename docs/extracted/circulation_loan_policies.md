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
| loanable                                                           | boolean         |                                                                                                    |
| loansPolicy                                                        | object          |                                                                                                    |
| loansPolicy/profileId                                              | string          | Loan profile                                                                                       |
| loansPolicy/period                                                 | object          |                                                                                                    |
| loansPolicy/period/duration                                        | integer         | Duration of the period, number of times the interval repeats                                       |
| loansPolicy/period/intervalId                                      | string          | Interval for the period, e.g. hours, days or weeks                                                 |
| loansPolicy/closedLibraryDueDateManagementId                       | string          | Closed library due date management                                                                 |
| loansPolicy/gracePeriod                                            | object          |                                                                                                    |
| loansPolicy/gracePeriod/duration                                   | integer         | Duration of the period, number of times the interval repeats                                       |
| loansPolicy/gracePeriod/intervalId                                 | string          | Interval for the period, e.g. hours, days or weeks                                                 |
| loansPolicy/openingTimeOffset                                      | object          |                                                                                                    |
| loansPolicy/openingTimeOffset/duration                             | integer         | Duration of the period, number of times the interval repeats                                       |
| loansPolicy/openingTimeOffset/intervalId                           | string          | Interval for the period, e.g. hours, days or weeks                                                 |
| loansPolicy/fixedDueDateScheduleId                                 | string          | Fixed due date schedule (due date limit)                                                           |
| loansPolicy/itemLimit                                              | integer         | Number of items allowed                                                                            |
| renewable                                                          | boolean         | Is item renewable                                                                                  |
| renewalsPolicy                                                     | object          |                                                                                                    |
| renewalsPolicy/unlimited                                           | boolean         | Unlimited renewals                                                                                 |
| renewalsPolicy/numberAllowed                                       | number          | Number of renewals allowed                                                                         |
| renewalsPolicy/renewFromId                                         | string          | Renew from date                                                                                    |
| renewalsPolicy/differentPeriod                                     | boolean         | Renewal period different from original loan                                                        |
| renewalsPolicy/period                                              | object          |                                                                                                    |
| renewalsPolicy/period/duration                                     | integer         | Duration of the period, number of times the interval repeats                                       |
| renewalsPolicy/period/intervalId                                   | string          | Interval for the period, e.g. hours, days or weeks                                                 |
| renewalsPolicy/alternateFixedDueDateScheduleId                     | string          | Alternate fixed due date schedule (due date limit) for renewals                                    |
| requestManagement                                                  | object          |                                                                                                    |
| requestManagement/recalls                                          | object          |                                                                                                    |
| requestManagement/recalls/alternateGracePeriod                     | object          |                                                                                                    |
| requestManagement/recalls/alternateGracePeriod/duration            | integer         | Duration of the period, number of times the interval repeats                                       |
| requestManagement/recalls/alternateGracePeriod/intervalId          | string          | Interval for the period, e.g. hours, days or weeks                                                 |
| requestManagement/recalls/minimumGuaranteedLoanPeriod              | object          |                                                                                                    |
| requestManagement/recalls/minimumGuaranteedLoanPeriod/duration     | integer         | Duration of the period, number of times the interval repeats                                       |
| requestManagement/recalls/minimumGuaranteedLoanPeriod/intervalId   | string          | Interval for the period, e.g. hours, days or weeks                                                 |
| requestManagement/recalls/recallReturnInterval                     | object          |                                                                                                    |
| requestManagement/recalls/recallReturnInterval/duration            | integer         | Duration of the period, number of times the interval repeats                                       |
| requestManagement/recalls/recallReturnInterval/intervalId          | string          | Interval for the period, e.g. hours, days or weeks                                                 |
| requestManagement/recalls/allowRecallsToExtendOverdueLoans         | boolean         | Whether recalls are allowed to extend overdue loans                                                |
| requestManagement/recalls/alternateRecallReturnInterval            | object          |                                                                                                    |
| requestManagement/recalls/alternateRecallReturnInterval/duration   | integer         | Duration of the period, number of times the interval repeats                                       |
| requestManagement/recalls/alternateRecallReturnInterval/intervalId | string          | Interval for the period, e.g. hours, days or weeks                                                 |
| requestManagement/holds                                            | object          |                                                                                                    |
| requestManagement/holds/alternateCheckoutLoanPeriod                | object          |                                                                                                    |
| requestManagement/holds/alternateCheckoutLoanPeriod/duration       | integer         | Duration of the period, number of times the interval repeats                                       |
| requestManagement/holds/alternateCheckoutLoanPeriod/intervalId     | string          | Interval for the period, e.g. hours, days or weeks                                                 |
| requestManagement/holds/renewItemsWithRequest                      | boolean         | Allow renewal of items with active, pending hold request                                           |
| requestManagement/holds/alternateRenewalLoanPeriod                 | object          |                                                                                                    |
| requestManagement/holds/alternateRenewalLoanPeriod/duration        | integer         | Duration of the period, number of times the interval repeats                                       |
| requestManagement/holds/alternateRenewalLoanPeriod/intervalId      | string          | Interval for the period, e.g. hours, days or weeks                                                 |
| requestManagement/pages                                            | object          |                                                                                                    |
| requestManagement/pages/alternateCheckoutLoanPeriod                | object          |                                                                                                    |
| requestManagement/pages/alternateCheckoutLoanPeriod/duration       | integer         | Duration of the period, number of times the interval repeats                                       |
| requestManagement/pages/alternateCheckoutLoanPeriod/intervalId     | string          | Interval for the period, e.g. hours, days or weeks                                                 |
| requestManagement/pages/renewItemsWithRequest                      | boolean         | Allow renewal of items with active, pending page request                                           |
| requestManagement/pages/alternateRenewalLoanPeriod                 | object          |                                                                                                    |
| requestManagement/pages/alternateRenewalLoanPeriod/duration        | integer         | Duration of the period, number of times the interval repeats                                       |
| requestManagement/pages/alternateRenewalLoanPeriod/intervalId      | string          | Interval for the period, e.g. hours, days or weeks                                                 |
| metadata                                                           | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate                                               | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId                                           | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername                                         | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate                                               | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId                                           | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername                                         | string          | Username of the user who last updated the record (when available)                                  |


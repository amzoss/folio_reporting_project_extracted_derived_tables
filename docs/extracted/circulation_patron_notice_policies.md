---
title: circulation_patron_notice_policies
---
## Source:

Module: mod-circulation-storage

Interface: /patron-notice-policy-storage/patron-notice-pol...

## Attributes:

| Property Name                                   | Property Type   | Property Description                                                                               |
|:------------------------------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                                              | string          | Patron notice policy id, UUID                                                                      |
| name                                            | string          | Patron notice policy name                                                                          |
| description                                     | string          | Patron notice policy description                                                                   |
| active                                          | boolean         | A flag to determine if a patron notice policy is active                                            |
| metadata                                        | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate                            | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId                        | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername                      | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate                            | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId                        | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername                      | string          | Username of the user who last updated the record (when available)                                  |
| loanNotices                                     | array           | List of loan notices                                                                               |
| loanNotices/name                                | string          | Notice name                                                                                        |
| loanNotices/templateId                          | string          | Template id, UUID                                                                                  |
| loanNotices/templateName                        | string          | Template name                                                                                      |
| loanNotices/format                              | string          | Notice format, send through email, sms etc.                                                        |
| loanNotices/frequency                           | string          | Frequency, send it once or more                                                                    |
| loanNotices/realTime                            | boolean         | Is this real time event                                                                            |
| loanNotices/sendOptions                         | object          | Notice sending options                                                                             |
| loanNotices/sendOptions/sendHow                 | string          | Defines how notice should be sent, before, after or upon                                           |
| loanNotices/sendOptions/sendWhen                | string          | Triggering event                                                                                   |
| loanNotices/sendOptions/sendBy                  | object          | Time interval                                                                                      |
| loanNotices/sendOptions/sendBy/duration         | integer         | Interval duration, number of time units                                                            |
| loanNotices/sendOptions/sendBy/intervalId       | string          | Unit of time                                                                                       |
| loanNotices/sendOptions/sendEvery               | object          | Time interval                                                                                      |
| loanNotices/sendOptions/sendEvery/duration      | integer         | Interval duration, number of time units                                                            |
| loanNotices/sendOptions/sendEvery/intervalId    | string          | Unit of time                                                                                       |
| feeFineNotices                                  | array           | List of fee/fine notices                                                                           |
| feeFineNotices/name                             | string          | Notice name                                                                                        |
| feeFineNotices/templateId                       | string          | Template id, UUID                                                                                  |
| feeFineNotices/templateName                     | string          | Template name                                                                                      |
| feeFineNotices/format                           | string          | Notice format, send through email, sms etc.                                                        |
| feeFineNotices/frequency                        | string          | Frequency, send it once or more                                                                    |
| feeFineNotices/realTime                         | boolean         | Is this real time event                                                                            |
| feeFineNotices/sendOptions                      | object          | Notice sending options                                                                             |
| feeFineNotices/sendOptions/sendHow              | string          | Defines how notice should be sent: after or upon                                                   |
| feeFineNotices/sendOptions/sendWhen             | string          | Triggering event                                                                                   |
| feeFineNotices/sendOptions/sendBy               | object          | Time interval                                                                                      |
| feeFineNotices/sendOptions/sendBy/duration      | integer         | Interval duration, number of time units                                                            |
| feeFineNotices/sendOptions/sendBy/intervalId    | string          | Unit of time                                                                                       |
| feeFineNotices/sendOptions/sendEvery            | object          | Time interval                                                                                      |
| feeFineNotices/sendOptions/sendEvery/duration   | integer         | Interval duration, number of time units                                                            |
| feeFineNotices/sendOptions/sendEvery/intervalId | string          | Unit of time                                                                                       |
| requestNotices                                  | array           | List of request notice                                                                             |
| requestNotices/name                             | string          | Notice name                                                                                        |
| requestNotices/templateId                       | string          | Template id, UUID                                                                                  |
| requestNotices/templateName                     | string          | Template name                                                                                      |
| requestNotices/format                           | string          | Notice format, send through email, sms etc.                                                        |
| requestNotices/frequency                        | string          | Frequency, send it once or more                                                                    |
| requestNotices/realTime                         | boolean         | Is this real time event                                                                            |
| requestNotices/sendOptions                      | object          | Notice sending options                                                                             |
| requestNotices/sendOptions/sendHow              | string          | Defines how notice should be sent, before, after or upon                                           |
| requestNotices/sendOptions/sendWhen             | string          | User initiated and time driven events for request related notices                                  |
| requestNotices/sendOptions/sendBy               | object          | Time interval                                                                                      |
| requestNotices/sendOptions/sendBy/duration      | integer         | Interval duration, number of time units                                                            |
| requestNotices/sendOptions/sendBy/intervalId    | string          | Unit of time                                                                                       |
| requestNotices/sendOptions/sendEvery            | object          | Time interval                                                                                      |
| requestNotices/sendOptions/sendEvery/duration   | integer         | Interval duration, number of time units                                                            |
| requestNotices/sendOptions/sendEvery/intervalId | string          | Unit of time                                                                                       |


---
title: email_email
---
## Source:

Module: mod-email

Interface: /email

## Attributes:

| Property Name              | Property Type   | Property Description                                                                                                                                                                                                                                     |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id                         | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| notificationId             | string          | notification identifier                                                                                                                                                                                                                                  |
| from                       | string          | sender's address                                                                                                                                                                                                                                         |
| to                         | string          | address of the recipient                                                                                                                                                                                                                                 |
| header                     | string          | subject of email                                                                                                                                                                                                                                         |
| outputFormat               | string          | format type: `text/html` or `text/plain`                                                                                                                                                                                                                 |
| body                       | string          | text of email                                                                                                                                                                                                                                            |
| attachments                | array           | attachment list                                                                                                                                                                                                                                          |
| status                     | string          | status of email                                                                                                                                                                                                                                          |
| shouldRetry                | boolean         | Should retry sending email                                                                                                                                                                                                                               |
| attemptCount               | integer         | Number of email sending attempts                                                                                                                                                                                                                         |
| message                    | string          | Server error message or other cause of the error                                                                                                                                                                                                         |
| date                       | string          | The date the email was sent to the SMTP server                                                                                                                                                                                                           |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                                                                                                                                                       |
| metadata/createdDate       | string          | Date and time when the record was created                                                                                                                                                                                                                |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                                                                                                                                                                                   |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                                                                                                                                                                             |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                                                                                                                                                                           |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                                                                                                                                                                              |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                                                                                                                                                                        |


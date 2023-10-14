---
title: Extracted Table Documentation
---
## Documentation: [erm_agreements_coverage_statement](erm_agreements_coverage_statement.md)

### Source:

Module: mod_agreements

Interface: coverage_statement

### Attributes:

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

## Documentation: [erm_agreements_entitlement](erm_agreements_entitlement.md)

### Source:

Module: mod_agreements

Interface: entitlement

### Attributes:

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

## Documentation: [erm_agreements_erm_resource](erm_agreements_erm_resource.md)

### Source:

Module: mod_agreements

Interface: erm_resource

### Attributes:

| Property Name   | Property Type   | Property Description                                                                                                              |
|:----------------|:----------------|:----------------------------------------------------------------------------------------------------------------------------------|
| id              |                 | ID of erm_resource                                                                                                                |
| res_name        |                 | Name of the resource (can be name of a package or other resource type or the title of a published work such as a book or journal) |
| res_type_fk     |                 | ID of reference data value for the type of resource.                                                                              |
| res_subtype_fk  |                 | ID of reference data value for the subtype of resource                                                                            |

## Documentation: [erm_agreements_holdings_coverage](erm_agreements_holdings_coverage.md)

### Source:

Module: mod_agreements

Interface: holdings_coverage

### Attributes:

| Property Name   | Property Type   | Property Description                                                                                                    |
|:----------------|:----------------|:------------------------------------------------------------------------------------------------------------------------|
| co_id           |                 | UUID for holdings_coverage                                                                                              |
| co_start_issue  |                 | Earliest issue of the resource linked to the entitlement available as part of this coverage                             |
| co_end_issue    |                 | Latest issue of the resource linked to the entitlement available as part of this coverage                               |
| co_start_volume |                 | Earliest volume of the resource linked to the entitlement available as part of this coverage                            |
| co_end_volume   |                 | Latest volume of the resource linked to the entitlement available as part of this coverage                              |
| co_ent_fk       |                 | The ID of the entitlement to which this holdings_coverage applies                                                       |
| co_start_date   |                 | Earliest date of publication of material from the resource linked to the entitlement available as part of this coverage |
| co_end_date     |                 | Latest date of publication of material from resourc linked to the entitlemente available as part of this coverage       |

## Documentation: [erm_agreements_identifier](erm_agreements_identifier.md)

### Source:

Module: mod_agreements

Interface: identifier

### Attributes:

| Property Name   | Property Type   | Property Description                                 |
|:----------------|:----------------|:-----------------------------------------------------|
| id_id           |                 | UUID of identifier                                   |
| id_ns_fk        |                 | ID of identifier namespace                           |
| id_value        |                 | Value of the identifier (i.e. the identifier string) |

## Documentation: [erm_agreements_identifier_namespace](erm_agreements_identifier_namespace.md)

### Source:

Module: mod_agreements

Interface: identifier_namespace

### Attributes:

| Property Name   | Property Type   | Property Description                                         |
|:----------------|:----------------|:-------------------------------------------------------------|
| idns_id         |                 | UUID of identifier_namespace                                 |
| idns_value      |                 | Value of the namespace (i.e. the namespace name as a string) |

## Documentation: [erm_agreements_identifier_occurrence](erm_agreements_identifier_occurrence.md)

### Source:

Module: mod_agreements

Interface: identifier_occurrence

### Attributes:

| Property Name    | Property Type   | Property Description                                                                                                     |
|:-----------------|:----------------|:-------------------------------------------------------------------------------------------------------------------------|
| io_id            |                 | UUID of identifier occurrence                                                                                            |
| io_ti_fk         |                 | ID of title_instance which is linked to the identifier                                                                   |
| io_status        |                 | ID of reference data value (mod_agreements.refdata_value.rdv_id) which describes the status of the identifier occurrence |
| io_identifier_fk |                 | ID of the identifier which is ‘occurring’ against a title_instance                                                       |

## Documentation: [erm_agreements_order_line](erm_agreements_order_line.md)

### Source:

Module: mod_agreements

Interface: order_line

### Attributes:

| Property Name   | Property Type   | Property Description                                                                         |
|:----------------|:----------------|:---------------------------------------------------------------------------------------------|
| pol_id          |                 | UUID of order_line record                                                                    |
| pol_orders_fk   |                 | ID of purchase order line in Orders app                                                      |
| pol_owner_fk    |                 | ID of entitlement (mod_agreements.entitlement.ent_id) to which purchase order line is linked |

## Documentation: [erm_agreements_package](erm_agreements_package.md)

### Source:

Module: mod_agreements

Interface: package

### Attributes:

| Property Name   | Property Type   | Property Description                                                                                 |
|:----------------|:----------------|:-----------------------------------------------------------------------------------------------------|
| id              |                 | ID of package                                                                                        |
| pkg_vendor_id   |                 | ID of the package provider organisation (in mod_agreements.orgs)                                     |
| pkg_source      |                 | String describing the source of the package data                                                     |
| pkg_remote_kb   |                 | ID of the remote knowledgebase from which the package data was obtained (in mod_agreements.remotekb) |
| pkg_reference   |                 | ID or reference for the package in an external system                                                |

## Documentation: [erm_agreements_package_content_item](erm_agreements_package_content_item.md)

### Source:

Module: mod_agreements

Interface: package_content_item

### Attributes:

| Property Name    | Property Type   | Property Description                                                         |
|:-----------------|:----------------|:-----------------------------------------------------------------------------|
| id               |                 | ID of the package content item                                               |
| pci_pti_fk       |                 | ID of the platform_title_instance that the package_content_item is linked to |
| pci_pkg_fk       |                 | ID of the package that the package_content_item belongs to                   |
| pci_access_start |                 | The date on which a package_content_item was first accessible in a package   |
| pci_access_end   |                 | The date on which a package_content_item was last accessible in a package    |

## Documentation: [erm_agreements_platform](erm_agreements_platform.md)

### Source:

Module: mod_agreements

Interface: platform

### Attributes:

| Property Name   | Property Type   | Property Description       |
|:----------------|:----------------|:---------------------------|
| pt_id           |                 | UUID of Platform           |
| pt_name         |                 | Name/label of the platform |

## Documentation: [erm_agreements_platform_title_instance](erm_agreements_platform_title_instance.md)

### Source:

Module: mod_agreements

Interface: platform_title_instance

### Attributes:

| Property Name   | Property Type   | Property Description                                                        |
|:----------------|:----------------|:----------------------------------------------------------------------------|
| id              |                 | ID of the platform_title_instance                                           |
| pti_pt_fk       |                 | The ID of the platform that the platform_title_instance belongs to          |
| pti_ti_fk       |                 | The ID of the title_instance to which the platform_title_instance is linked |
| pti_url         |                 | The URL of the platform_title_instance                                      |

## Documentation: [erm_agreements_subscription_agreement](erm_agreements_subscription_agreement.md)

### Source:

Module: mod_agreements

Interface: subscription_agreement

### Attributes:

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

## Documentation: [erm_agreements_title_instance](erm_agreements_title_instance.md)

### Source:

Module: mod_agreements

Interface: title_instance

### Attributes:

| Property Name               | Property Type   | Property Description                                                                                                                                             |
|:----------------------------|:----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id                          |                 | ID of the title_instance                                                                                                                                         |
| ti_work_fk                  |                 | The ID of the work to which the title_instance is linked                                                                                                         |
| ti_date_monograph_published |                 | For monographs (books), the date the monograph was first published in the media specified by the linked erm_resource subtype (typically “print” or “electronic”) |
| ti_first_author             |                 | For monographs (books), the last name of the book’s first author.                                                                                                |
| ti_monograph_edition        |                 | For monographs (books), the last name of the book’s first author.                                                                                                |
| ti_monograph_volume         |                 | For monographs (books), the volume number of the book                                                                                                            |
| ti_first_editor             |                 | For monographs (books), the last name of the book’s first editor.                                                                                                |

## Documentation: [erm_agreements_work](erm_agreements_work.md)

### Source:

Module: mod_agreements

Interface: work

### Attributes:

| Property Name   | Property Type   | Property Description   |
|:----------------|:----------------|:-----------------------|
| w_id            |                 | UUID of Work           |
| w_title         |                 | Title of the work      |

## Documentation: [audit_circulation_logs](audit_circulation_logs.md)

### Source:

Module: mod-audit

Interface: /audit-data/circulation/logs

### Attributes:

| Property Name            | Property Type   | Property Description           |
|:-------------------------|:----------------|:-------------------------------|
| id                       | string          | The UUID format string         |
| eventId                  | string          | The UUID format string         |
| userBarcode              | string          | User barcode                   |
| items                    | array           | Notice items                   |
| items/itemBarcode        | string          | Item barcode                   |
| items/itemId             | string          | The UUID format string         |
| items/instanceId         | string          | The UUID format string         |
| items/holdingId          | string          | The UUID format string         |
| items/loanId             | string          | The UUID format string         |
| object                   | string          | The purchase order line format |
| action                   | string          | The purchase order line format |
| date                     | string          | Event date                     |
| servicePointId           | string          | The UUID format string         |
| source                   | string          | Source                         |
| description              | string          | Description                    |
| linkToIds                | object          | Additional data for details    |
| linkToIds/userId         | string          | The UUID format string         |
| linkToIds/requestId      | string          | The UUID format string         |
| linkToIds/feeFineId      | string          | The UUID format string         |
| linkToIds/templateId     | string          | The UUID format string         |
| linkToIds/noticePolicyId | string          | The UUID format string         |

## Documentation: [audit_acquisition_order](audit_acquisition_order.md)

### Source:

Module: mod-audit

Interface: /audit-data/acquisition/order

### Attributes:

| Property Name   | Property Type   | Property Description                 |
|:----------------|:----------------|:-------------------------------------|
| id              | string          | The UUID format string               |
| action          | string          | The action of the audit event        |
| orderId         | string          | The UUID format string               |
| userId          | string          | The UUID format string               |
| eventDate       | string          | Date time when event triggered       |
| actionDate      | string          | Date time when order action occurred |
| orderSnapshot   | object          | Full snapshot of the order           |

## Documentation: [audit_acquisition_order_line](audit_acquisition_order_line.md)

### Source:

Module: mod-audit

Interface: /audit-data/acquisition/order-line

### Attributes:

| Property Name     | Property Type   | Property Description                 |
|:------------------|:----------------|:-------------------------------------|
| id                | string          | The UUID format string               |
| action            | string          | The action of the audit event        |
| orderId           | string          | The UUID format string               |
| orderLineId       | string          | The UUID format string               |
| userId            | string          | The UUID format string               |
| eventDate         | string          | Date time when event triggered       |
| actionDate        | string          | Date time when order action occurred |
| orderLineSnapshot | object          | Full snapshot of the order line      |

## Documentation: [circulation_cancellation_reasons](circulation_cancellation_reasons.md)

### Source:

Module: mod-circulation-storage

Interface: /cancellation-reason-storage/cancellation-reasons

### Attributes:

| Property Name                 | Property Type   | Property Description                                                                               |
|:------------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                            | string          |                                                                                                    |
| name                          | string          | Reason name                                                                                        |
| description                   | string          | Internal reason description                                                                        |
| publicDescription             | string          | Public reason description                                                                          |
| requiresAdditionalInformation | boolean         | Flag that indicates whether reason requires additional information                                 |
| source                        | string          | Origin of the cancellation reason record, e.g. 'System', 'User', 'Consortium' etc.                 |
| metadata                      | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate          | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId      | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername    | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate          | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId      | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername    | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [circulation_check_ins](circulation_check_ins.md)

### Source:

Module: mod-circulation-storage

Interface: /check-in-storage/check-ins

### Attributes:

| Property Name            | Property Type   | Property Description                                                                                                                                                                                                                                     |
|:-------------------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id                       | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| occurredDateTime         | string          | Date and time when the check-in occurred                                                                                                                                                                                                                 |
| itemId                   | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| itemStatusPriorToCheckIn | string          | Item status prior to check-in                                                                                                                                                                                                                            |
| requestQueueSize         | integer         | Request queue size for the item                                                                                                                                                                                                                          |
| itemLocationId           | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| servicePointId           | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| performedByUserId        | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |

## Documentation: [circulation_fixed_due_date_schedules](circulation_fixed_due_date_schedules.md)

### Source:

Module: mod-circulation-storage

Interface: /fixed-due-date-schedule-storage/fixed-due-date...

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          | Unique ID (generated UUID)                                                                         |
| name                       | string          | Schedule name                                                                                      |
| description                | string          | Schedule description                                                                               |
| schedules                  | array           | List date ranges with a due date for each                                                          |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [circulation_loan_history](circulation_loan_history.md)

### Source:

Module: mod-circulation-storage

Interface: /loan-storage/loan-history

### Attributes:

| Property Name                                            | Property Type   | Property Description                                                                                                                                                                                                                                     |
|:---------------------------------------------------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id                                                       | string          | Unique ID (generated UUID) of the snapshot of the loan record                                                                                                                                                                                            |
| operation                                                | string          | Type of change that triggered this loan record snapshot: I for insert, U for update, D for delete                                                                                                                                                        |
| creationDate                                             | string          | When this snapshot was created                                                                                                                                                                                                                           |
| loan                                                     | object          | Links the item with the patron and applies certain conditions based on policies                                                                                                                                                                          |
| loan/id                                                  | string          | Unique ID (generated UUID) of the loan                                                                                                                                                                                                                   |
| loan/userId                                              | string          | ID of the patron the item was lent to. Required for open loans, not required for closed loans (for anonymization).                                                                                                                                       |
| loan/proxyUserId                                         | string          | ID of the user representing a proxy for the patron                                                                                                                                                                                                       |
| loan/itemId                                              | string          | ID of the item lent to the patron                                                                                                                                                                                                                        |
| loan/itemEffectiveLocationIdAtCheckOut                   | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| loan/status                                              | object          | Overall status of the loan                                                                                                                                                                                                                               |
| loan/status/name                                         | string          | Name of the status (currently can be any value, values commonly used are Open and Closed)                                                                                                                                                                |
| loan/loanDate                                            | string          | Date time when the loan began (typically represented according to rfc3339 section-5.6. Has not had the date-time format validation applied as was not supported at point of introduction and would now be a breaking change)                             |
| loan/dueDate                                             | string          | Date time when the item is due to be returned                                                                                                                                                                                                            |
| loan/returnDate                                          | string          | Date time when the item is returned and the loan ends (typically represented according to rfc3339 section-5.6. Has not had the date-time format validation applied as was not supported at point of introduction and would now be a breaking change)     |
| loan/systemReturnDate                                    | string          | Date time when the returned item is actually processed                                                                                                                                                                                                   |
| loan/action                                              | string          | Last action performed on a loan (currently can be any value, values commonly used are checkedout and checkedin)                                                                                                                                          |
| loan/actionComment                                       | string          | Comment to last action performed on a loan                                                                                                                                                                                                               |
| loan/itemStatus                                          | string          | Last item status used in relation to this loan (currently can be any value, values commonly used are Checked out and Available)                                                                                                                          |
| loan/renewalCount                                        | integer         | Count of how many times a loan has been renewed (incremented by the client)                                                                                                                                                                              |
| loan/loanPolicyId                                        | string          | ID of last policy used in relation to this loan                                                                                                                                                                                                          |
| loan/checkoutServicePointId                              | string          | ID of the Service Point where the last checkout occured                                                                                                                                                                                                  |
| loan/checkinServicePointId                               | string          | ID of the Service Point where the last checkin occured                                                                                                                                                                                                   |
| loan/patronGroupIdAtCheckout                             | string          | Patron Group Id at checkout                                                                                                                                                                                                                              |
| loan/dueDateChangedByRecall                              | boolean         | Indicates whether or not this loan had its due date modified by a recall on the loaned item                                                                                                                                                              |
| loan/declaredLostDate                                    | string          | Date and time the item was declared lost during this loan                                                                                                                                                                                                |
| loan/claimedReturnedDate                                 | string          | Date and time the item was claimed returned for this loan                                                                                                                                                                                                |
| loan/overdueFinePolicyId                                 | string          | ID of overdue fines policy at the time the item is check-in or renewed                                                                                                                                                                                   |
| loan/lostItemPolicyId                                    | string          | ID of lost item policy which determines when the item ages to lost and the associated fees or the associated fees if the patron declares the item lost.                                                                                                  |
| loan/metadata                                            | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                                                                                                                                                       |
| loan/metadata/createdDate                                | string          | Date and time when the record was created                                                                                                                                                                                                                |
| loan/metadata/createdByUserId                            | string          | ID of the user who created the record (when available)                                                                                                                                                                                                   |
| loan/metadata/createdByUsername                          | string          | Username of the user who created the record (when available)                                                                                                                                                                                             |
| loan/metadata/updatedDate                                | string          | Date and time when the record was last updated                                                                                                                                                                                                           |
| loan/metadata/updatedByUserId                            | string          | ID of the user who last updated the record (when available)                                                                                                                                                                                              |
| loan/metadata/updatedByUsername                          | string          | Username of the user who last updated the record (when available)                                                                                                                                                                                        |
| loan/agedToLostDelayedBilling                            | object          | Aged to Lost Delayed Billing processing                                                                                                                                                                                                                  |
| loan/agedToLostDelayedBilling/lostItemHasBeenBilled      | boolean         | Indicates if the aged to lost fee has been billed (for use where delayed billing is set up)                                                                                                                                                              |
| loan/agedToLostDelayedBilling/dateLostItemShouldBeBilled | string          | Indicates when the aged to lost fee should be billed (for use where delayed billing is set up)                                                                                                                                                           |
| loan/agedToLostDelayedBilling/agedToLostDate             | string          | Date and time the item was aged to lost for this loan                                                                                                                                                                                                    |
| loan/reminders                                           | object          | Information about reminders for overdue loan                                                                                                                                                                                                             |
| loan/reminders/lastFeeBilled                             | object          | Information about the most recent reminder fee billing                                                                                                                                                                                                   |
| loan/reminders/lastFeeBilled/number                      | integer         | Last reminder fee billed, sequence number                                                                                                                                                                                                                |
| loan/reminders/lastFeeBilled/date                        | string          | Last reminder fee billed, date                                                                                                                                                                                                                           |

## Documentation: [circulation_loan_policies](circulation_loan_policies.md)

### Source:

Module: mod-circulation-storage

Interface: /loan-policy-storage/loan-policies

### Attributes:

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

## Documentation: [circulation_loans](circulation_loans.md)

### Source:

Module: mod-circulation-storage

Interface: /loan-storage/loans

### Attributes:

| Property Name                                       | Property Type   | Property Description                                                                                                                                                                                                                                     |
|:----------------------------------------------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id                                                  | string          | Unique ID (generated UUID) of the loan                                                                                                                                                                                                                   |
| userId                                              | string          | ID of the patron the item was lent to. Required for open loans, not required for closed loans (for anonymization).                                                                                                                                       |
| proxyUserId                                         | string          | ID of the user representing a proxy for the patron                                                                                                                                                                                                       |
| itemId                                              | string          | ID of the item lent to the patron                                                                                                                                                                                                                        |
| itemEffectiveLocationIdAtCheckOut                   | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| status                                              | object          | Overall status of the loan                                                                                                                                                                                                                               |
| status/name                                         | string          | Name of the status (currently can be any value, values commonly used are Open and Closed)                                                                                                                                                                |
| loanDate                                            | string          | Date time when the loan began (typically represented according to rfc3339 section-5.6. Has not had the date-time format validation applied as was not supported at point of introduction and would now be a breaking change)                             |
| dueDate                                             | string          | Date time when the item is due to be returned                                                                                                                                                                                                            |
| returnDate                                          | string          | Date time when the item is returned and the loan ends (typically represented according to rfc3339 section-5.6. Has not had the date-time format validation applied as was not supported at point of introduction and would now be a breaking change)     |
| systemReturnDate                                    | string          | Date time when the returned item is actually processed                                                                                                                                                                                                   |
| action                                              | string          | Last action performed on a loan (currently can be any value, values commonly used are checkedout and checkedin)                                                                                                                                          |
| actionComment                                       | string          | Comment to last action performed on a loan                                                                                                                                                                                                               |
| itemStatus                                          | string          | Last item status used in relation to this loan (currently can be any value, values commonly used are Checked out and Available)                                                                                                                          |
| renewalCount                                        | integer         | Count of how many times a loan has been renewed (incremented by the client)                                                                                                                                                                              |
| loanPolicyId                                        | string          | ID of last policy used in relation to this loan                                                                                                                                                                                                          |
| checkoutServicePointId                              | string          | ID of the Service Point where the last checkout occured                                                                                                                                                                                                  |
| checkinServicePointId                               | string          | ID of the Service Point where the last checkin occured                                                                                                                                                                                                   |
| patronGroupIdAtCheckout                             | string          | Patron Group Id at checkout                                                                                                                                                                                                                              |
| dueDateChangedByRecall                              | boolean         | Indicates whether or not this loan had its due date modified by a recall on the loaned item                                                                                                                                                              |
| declaredLostDate                                    | string          | Date and time the item was declared lost during this loan                                                                                                                                                                                                |
| claimedReturnedDate                                 | string          | Date and time the item was claimed returned for this loan                                                                                                                                                                                                |
| overdueFinePolicyId                                 | string          | ID of overdue fines policy at the time the item is check-in or renewed                                                                                                                                                                                   |
| lostItemPolicyId                                    | string          | ID of lost item policy which determines when the item ages to lost and the associated fees or the associated fees if the patron declares the item lost.                                                                                                  |
| metadata                                            | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                                                                                                                                                       |
| metadata/createdDate                                | string          | Date and time when the record was created                                                                                                                                                                                                                |
| metadata/createdByUserId                            | string          | ID of the user who created the record (when available)                                                                                                                                                                                                   |
| metadata/createdByUsername                          | string          | Username of the user who created the record (when available)                                                                                                                                                                                             |
| metadata/updatedDate                                | string          | Date and time when the record was last updated                                                                                                                                                                                                           |
| metadata/updatedByUserId                            | string          | ID of the user who last updated the record (when available)                                                                                                                                                                                              |
| metadata/updatedByUsername                          | string          | Username of the user who last updated the record (when available)                                                                                                                                                                                        |
| agedToLostDelayedBilling                            | object          | Aged to Lost Delayed Billing processing                                                                                                                                                                                                                  |
| agedToLostDelayedBilling/lostItemHasBeenBilled      | boolean         | Indicates if the aged to lost fee has been billed (for use where delayed billing is set up)                                                                                                                                                              |
| agedToLostDelayedBilling/dateLostItemShouldBeBilled | string          | Indicates when the aged to lost fee should be billed (for use where delayed billing is set up)                                                                                                                                                           |
| agedToLostDelayedBilling/agedToLostDate             | string          | Date and time the item was aged to lost for this loan                                                                                                                                                                                                    |
| reminders                                           | object          | Information about reminders for overdue loan                                                                                                                                                                                                             |
| reminders/lastFeeBilled                             | object          | Information about the most recent reminder fee billing                                                                                                                                                                                                   |
| reminders/lastFeeBilled/number                      | integer         | Last reminder fee billed, sequence number                                                                                                                                                                                                                |
| reminders/lastFeeBilled/date                        | string          | Last reminder fee billed, date                                                                                                                                                                                                                           |

## Documentation: [circulation_patron_action_sessions](circulation_patron_action_sessions.md)

### Source:

Module: mod-circulation-storage

Interface: /patron-action-session-storage/patron-action-se...

### Attributes:

| Property Name              | Property Type   | Property Description                                                                                                                                                                                                                                     |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id                         | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| sessionId                  | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| patronId                   | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| loanId                     | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| actionType                 | string          | Defines action type                                                                                                                                                                                                                                      |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                                                                                                                                                       |
| metadata/createdDate       | string          | Date and time when the record was created                                                                                                                                                                                                                |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                                                                                                                                                                                   |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                                                                                                                                                                             |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                                                                                                                                                                           |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                                                                                                                                                                              |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                                                                                                                                                                        |

## Documentation: [circulation_patron_notice_policies](circulation_patron_notice_policies.md)

### Source:

Module: mod-circulation-storage

Interface: /patron-notice-policy-storage/patron-notice-pol...

### Attributes:

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

## Documentation: [circulation_request_policies](circulation_request_policies.md)

### Source:

Module: mod-circulation-storage

Interface: /request-policy-storage/request-policies

### Attributes:

| Property Name               | Property Type     | Property Description                                                                               |
|:----------------------------|:------------------|:---------------------------------------------------------------------------------------------------|
| id                          | string            | Unique request policy ID                                                                           |
| name                        | string            | Unique request policy name, required                                                               |
| description                 | string            | Description of request policy                                                                      |
| requestTypes                | array             | Whether the item should be held upon return, recalled or paged for                                 |
| allowedServicePoints        | object            | Allowed pickup service point IDs by request type                                                   |
| allowedServicePoints/Page   | ['array', 'null'] | List of allowed pickup service point IDs                                                           |
| allowedServicePoints/Hold   | ['array', 'null'] | List of allowed pickup service point IDs                                                           |
| allowedServicePoints/Recall | ['array', 'null'] | List of allowed pickup service point IDs                                                           |
| metadata                    | object            | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate        | string            | Date and time when the record was created                                                          |
| metadata/createdByUserId    | string            | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername  | string            | Username of the user who created the record (when available)                                       |
| metadata/updatedDate        | string            | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId    | string            | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername  | string            | Username of the user who last updated the record (when available)                                  |

## Documentation: [circulation_request_preference](circulation_request_preference.md)

### Source:

Module: mod-circulation-storage

Interface: /request-preference-storage/request-preference

### Attributes:

| Property Name                | Property Type   | Property Description                                                                               |
|:-----------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                           | string          | Unique request preference ID                                                                       |
| userId                       | string          | UUID of user associated with this request preference                                               |
| holdShelf                    | boolean         | Whether 'Hold Shelf' option is available to the user.                                              |
| delivery                     | boolean         | Whether 'Delivery' option is available to the user.                                                |
| defaultServicePointId        | string          | UUID of default service point for 'Hold Shelf' option                                              |
| defaultDeliveryAddressTypeId | string          | UUID of user's address type                                                                        |
| fulfillment                  | string          | Preferred fulfillment type. Possible values are 'Delivery', 'Hold Shelf'                           |
| metadata                     | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate         | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId     | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername   | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate         | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId     | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername   | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [circulation_requests](circulation_requests.md)

### Source:

Module: mod-circulation-storage

Interface: /request-storage/requests

### Attributes:

| Property Name                               | Property Type   | Property Description                                                                                                                                                                                                                                     |
|:--------------------------------------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id                                          | string          | UUID of the request                                                                                                                                                                                                                                      |
| requestLevel                                | string          | Level of the request - Item or Title                                                                                                                                                                                                                     |
| requestType                                 | string          | Whether the item should be held upon return, recalled or paged for                                                                                                                                                                                       |
| requestDate                                 | string          | Date the request was made                                                                                                                                                                                                                                |
| patronComments                              | string          | Comments made by the patron                                                                                                                                                                                                                              |
| requesterId                                 | string          | ID of the requesting patron (user)                                                                                                                                                                                                                       |
| proxyUserId                                 | string          | ID of the user representing a proxy for the patron                                                                                                                                                                                                       |
| instanceId                                  | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| holdingsRecordId                            | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| itemId                                      | string          | ID of the item being requested                                                                                                                                                                                                                           |
| status                                      | string          | Status of the request                                                                                                                                                                                                                                    |
| cancellationReasonId                        | string          | The id of the relevant request reason                                                                                                                                                                                                                    |
| cancelledByUserId                           | string          | The id of the user that cancelled the request                                                                                                                                                                                                            |
| cancellationAdditionalInformation           | string          | Potential relevant information regarding a cancellation                                                                                                                                                                                                  |
| cancelledDate                               | string          | Date the request was cancelled                                                                                                                                                                                                                           |
| position                                    | integer         | Position of the request in the unified request queue                                                                                                                                                                                                     |
| instance                                    | object          | Copy of some instance metadata (used for searching and sorting)                                                                                                                                                                                          |
| instance/title                              | string          | title of the item                                                                                                                                                                                                                                        |
| instance/identifiers                        | array           | An extensible set of name-value pairs of identifiers associated with the resource                                                                                                                                                                        |
| instance/identifiers/value                  | string          | Resource identifier value                                                                                                                                                                                                                                |
| instance/identifiers/identifierTypeId       | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| item                                        | object          | Copy of some item metadata (used for searching and sorting)                                                                                                                                                                                              |
| item/barcode                                | string          | barcode of the item                                                                                                                                                                                                                                      |
| requester                                   | object          | Copy of some requesting patron metadata (used for searching and sorting)                                                                                                                                                                                 |
| requester/firstName                         | string          | first name of the requesting patron                                                                                                                                                                                                                      |
| requester/lastName                          | string          | last name of the requesting patron                                                                                                                                                                                                                       |
| requester/middleName                        | string          | middle name of the requesting patron                                                                                                                                                                                                                     |
| requester/barcode                           | string          | barcode of the requesting patron                                                                                                                                                                                                                         |
| requester/patronGroup                       | string          | DEPRECATED, to be removed in subsequent major version                                                                                                                                                                                                    |
| proxy                                       | object          | Copy of some proxy patron metadata (used for searching and sorting)                                                                                                                                                                                      |
| proxy/firstName                             | string          | first name of the proxy patron                                                                                                                                                                                                                           |
| proxy/lastName                              | string          | last name of the proxy patron                                                                                                                                                                                                                            |
| proxy/middleName                            | string          | middle name of the proxy patron                                                                                                                                                                                                                          |
| proxy/barcode                               | string          | barcode of the proxy patron                                                                                                                                                                                                                              |
| proxy/patronGroup                           | string          | DEPRECATED, to be removed in subsequent major version                                                                                                                                                                                                    |
| fulfillmentPreference                       | string          | How should the request be fulfilled (whether the item should be kept on the hold shelf for collection or delivered to the requester)                                                                                                                     |
| deliveryAddressTypeId                       | string          | Deliver to the address of this type, for the requesting patron                                                                                                                                                                                           |
| requestExpirationDate                       | string          | Date when the request expires                                                                                                                                                                                                                            |
| holdShelfExpirationDate                     | string          | Date when an item returned to the hold shelf expires                                                                                                                                                                                                     |
| pickupServicePointId                        | string          | The ID of the Service Point where this request can be picked up                                                                                                                                                                                          |
| metadata                                    | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                                                                                                                                                       |
| metadata/createdDate                        | string          | Date and time when the record was created                                                                                                                                                                                                                |
| metadata/createdByUserId                    | string          | ID of the user who created the record (when available)                                                                                                                                                                                                   |
| metadata/createdByUsername                  | string          | Username of the user who created the record (when available)                                                                                                                                                                                             |
| metadata/updatedDate                        | string          | Date and time when the record was last updated                                                                                                                                                                                                           |
| metadata/updatedByUserId                    | string          | ID of the user who last updated the record (when available)                                                                                                                                                                                              |
| metadata/updatedByUsername                  | string          | Username of the user who last updated the record (when available)                                                                                                                                                                                        |
| tags                                        | object          | List of simple tags that can be added to an object                                                                                                                                                                                                       |
| tags/tagList                                | array           | List of tags                                                                                                                                                                                                                                             |
| awaitingPickupRequestClosedDate             | string          | A date when the request with awaiting pickup status was closed                                                                                                                                                                                           |
| searchIndex                                 | object          | Request fields used for search                                                                                                                                                                                                                           |
| searchIndex/callNumberComponents            | object          | Effective call number components                                                                                                                                                                                                                         |
| searchIndex/callNumberComponents/callNumber | string          | Effective Call Number is an identifier assigned to an item or its holding and associated with the item.                                                                                                                                                  |
| searchIndex/callNumberComponents/prefix     | string          | Effective Call Number Prefix is the prefix of the identifier assigned to an item or its holding and associated with the item.                                                                                                                            |
| searchIndex/callNumberComponents/suffix     | string          | Effective Call Number Suffix is the suffix of the identifier assigned to an item or its holding and associated with the item.                                                                                                                            |
| searchIndex/shelvingOrder                   | string          | A system generated normalization of the call number that allows for call number sorting in reports and search results                                                                                                                                    |
| searchIndex/pickupServicePointName          | string          | The name of the request pickup service point                                                                                                                                                                                                             |

## Documentation: [circulation_scheduled_notices](circulation_scheduled_notices.md)

### Source:

Module: mod-circulation-storage

Interface: /scheduled-notice-storage/scheduled-notices

### Attributes:

| Property Name                           | Property Type   | Property Description                                                                                                                                                                                                                                     |
|:----------------------------------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id                                      | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| loanId                                  | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| requestId                               | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| feeFineActionId                         | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| recipientUserId                         | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| sessionId                               | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| nextRunTime                             | string          | Next run time                                                                                                                                                                                                                                            |
| triggeringEvent                         | string          | Scheduled notice triggering event                                                                                                                                                                                                                        |
| noticeConfig                            | object          | Scheduled notice configuration                                                                                                                                                                                                                           |
| noticeConfig/timing                     | string          | Timing represents when we need to send notice, before, at or after loan due date                                                                                                                                                                         |
| noticeConfig/recurringPeriod            | object          | Time interval defined by its duration                                                                                                                                                                                                                    |
| noticeConfig/recurringPeriod/duration   | integer         | Duration of the period, number of times the interval repeats                                                                                                                                                                                             |
| noticeConfig/recurringPeriod/intervalId | string          | Interval for the period, e.g. hours, days or weeks                                                                                                                                                                                                       |
| noticeConfig/templateId                 | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| noticeConfig/format                     | string          | Notice format                                                                                                                                                                                                                                            |
| noticeConfig/sendInRealTime             | boolean         | Real time notice flag                                                                                                                                                                                                                                    |
| metadata                                | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                                                                                                                                                       |
| metadata/createdDate                    | string          | Date and time when the record was created                                                                                                                                                                                                                |
| metadata/createdByUserId                | string          | ID of the user who created the record (when available)                                                                                                                                                                                                   |
| metadata/createdByUsername              | string          | Username of the user who created the record (when available)                                                                                                                                                                                             |
| metadata/updatedDate                    | string          | Date and time when the record was last updated                                                                                                                                                                                                           |
| metadata/updatedByUserId                | string          | ID of the user who last updated the record (when available)                                                                                                                                                                                              |
| metadata/updatedByUsername              | string          | Username of the user who last updated the record (when available)                                                                                                                                                                                        |

## Documentation: [circulation_staff_slips](circulation_staff_slips.md)

### Source:

Module: mod-circulation-storage

Interface: /staff-slips-storage/staff-slips

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          |                                                                                                    |
| name                       | string          | Staff slip name                                                                                    |
| description                | string          | Staff slip description                                                                             |
| active                     | boolean         | Flag that indicates whether staff slip is active                                                   |
| template                   | string          | Staff slip template                                                                                |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [configuration_entries](configuration_entries.md)

### Source:

Module: mod-configuration

Interface: /configurations/entries

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          |                                                                                                    |
| module                     | string          |                                                                                                    |
| configName                 | string          |                                                                                                    |
| code                       | string          |                                                                                                    |
| description                | string          |                                                                                                    |
| default                    | boolean         |                                                                                                    |
| enabled                    | boolean         |                                                                                                    |
| value                      | string          |                                                                                                    |
| userId                     | string          |                                                                                                    |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [course_copyrightstatuses](course_copyrightstatuses.md)

### Source:

Module: mod-courses

Interface: /coursereserves/copyrightstatuses

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          | A UUID                                                                                             |
| name                       | string          | The name of the type                                                                               |
| description                | string          | A description of this type                                                                         |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [course_courselistings](course_courselistings.md)

### Source:

Module: mod-courses

Interface: /coursereserves/courselistings

### Attributes:

| Property Name                                       | Property Type   | Property Description                                                                               |
|:----------------------------------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                                                  | string          | A UUID                                                                                             |
| registrarId                                         | string          | The registration id                                                                                |
| externalId                                          | string          | An external identifier associated with this listing                                                |
| servicepointId                                      | string          | A UUID                                                                                             |
| servicepointObject                                  | object          | The service point associated with this listing's reserves                                          |
| servicepointObject/id                               | string          | Id of service-point object                                                                         |
| servicepointObject/name                             | string          | service-point name, a required field                                                               |
| servicepointObject/code                             | string          | service-point code, a required field                                                               |
| servicepointObject/discoveryDisplayName             | string          | display name, a required field                                                                     |
| servicepointObject/description                      | string          | description of the service-point                                                                   |
| servicepointObject/shelvingLagTime                  | integer         | shelving lag time                                                                                  |
| servicepointObject/pickupLocation                   | boolean         | indicates whether or not the service point is a pickup location                                    |
| servicepointObject/holdShelfExpiryPeriod            | object          | schema for time-period, which contains time interval 'duration' and the time unit                  |
| servicepointObject/holdShelfExpiryPeriod/duration   | integer         | Duration interval                                                                                  |
| servicepointObject/holdShelfExpiryPeriod/intervalId | string          | Unit of time for the duration                                                                      |
| servicepointObject/staffSlips                       | array           | List of staff slips for this service point                                                         |
| servicepointObject/staffSlips/id                    | string          | The ID of the staff slip                                                                           |
| servicepointObject/staffSlips/printByDefault        | boolean         | Whether or not to print the staff slip by default                                                  |
| locationId                                          | string          | A UUID                                                                                             |
| locationObject                                      | object          | The location associated with this listing's reserves                                               |
| locationObject/id                                   | string          | id of this (shelf) location record as UUID.                                                        |
| locationObject/name                                 | string          | Name of the (shelf) location                                                                       |
| locationObject/code                                 | string          | Code of the (shelf) location, usually an abbreviation of the name.                                 |
| locationObject/description                          | string          | Description of the (shelf) location.                                                               |
| locationObject/discoveryDisplayName                 | string          | Name of the (shelf) location to be shown in the discovery.                                         |
| locationObject/isActive                             | boolean         | Whether this (shelf) location is active. Inactive (shelf) locations can no longer been used.       |
| locationObject/institutionId                        | string          | The UUID of the institution, the first-level location unit, this (shelf) location belongs to.      |
| locationObject/campusId                             | string          | The UUID of the campus, the second-level location unit, this (shelf) location belongs to.          |
| locationObject/libraryId                            | string          | The UUID of the library, the third-level location unit, this (shelf) location belongs to.          |
| locationObject/details                              | object          | Details about this (shelf) location.                                                               |
| locationObject/primaryServicePoint                  | string          | The UUID of the primary service point of this (shelf) location.                                    |
| locationObject/servicePointIds                      | array           | All service points that this (shelf) location has.                                                 |
| termId                                              | string          | A UUID                                                                                             |
| termObject                                          | object          | Temporal periods that listings exist in                                                            |
| termObject/id                                       | string          | A UUID                                                                                             |
| termObject/name                                     | string          | The name of period                                                                                 |
| termObject/startDate                                | string          | The beginning of the time period                                                                   |
| termObject/endDate                                  | string          | The ending of the time period                                                                      |
| termObject/metadata                                 | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| termObject/metadata/createdDate                     | string          | Date and time when the record was created                                                          |
| termObject/metadata/createdByUserId                 | string          | ID of the user who created the record (when available)                                             |
| termObject/metadata/createdByUsername               | string          | Username of the user who created the record (when available)                                       |
| termObject/metadata/updatedDate                     | string          | Date and time when the record was last updated                                                     |
| termObject/metadata/updatedByUserId                 | string          | ID of the user who last updated the record (when available)                                        |
| termObject/metadata/updatedByUsername               | string          | Username of the user who last updated the record (when available)                                  |
| courseTypeId                                        | string          | A UUID                                                                                             |
| courseTypeObject                                    | object          | The type of course a listing is                                                                    |
| courseTypeObject/id                                 | string          | A UUID                                                                                             |
| courseTypeObject/name                               | string          | The name of the type                                                                               |
| courseTypeObject/description                        | string          | A description of this type                                                                         |
| courseTypeObject/metadata                           | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| courseTypeObject/metadata/createdDate               | string          | Date and time when the record was created                                                          |
| courseTypeObject/metadata/createdByUserId           | string          | ID of the user who created the record (when available)                                             |
| courseTypeObject/metadata/createdByUsername         | string          | Username of the user who created the record (when available)                                       |
| courseTypeObject/metadata/updatedDate               | string          | Date and time when the record was last updated                                                     |
| courseTypeObject/metadata/updatedByUserId           | string          | ID of the user who last updated the record (when available)                                        |
| courseTypeObject/metadata/updatedByUsername         | string          | Username of the user who last updated the record (when available)                                  |
| instructorObjects                                   | array           | A listing of associated instructor objects                                                         |
| metadata                                            | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate                                | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId                            | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername                          | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate                                | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId                            | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername                          | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [course_courses](course_courses.md)

### Source:

Module: mod-courses

Interface: /coursereserves/courses

### Attributes:

| Property Name                                                           | Property Type   | Property Description                                                                               |
|:------------------------------------------------------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                                                                      | string          | A UUID                                                                                             |
| name                                                                    | string          | The name of course                                                                                 |
| description                                                             | string          | A description of the course                                                                        |
| departmentId                                                            | string          | A UUID                                                                                             |
| departmentObject                                                        | object          | The department a course belongs to                                                                 |
| departmentObject/id                                                     | string          | A UUID                                                                                             |
| departmentObject/name                                                   | string          | The name of the department                                                                         |
| departmentObject/description                                            | string          | A description of this department                                                                   |
| departmentObject/metadata                                               | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| departmentObject/metadata/createdDate                                   | string          | Date and time when the record was created                                                          |
| departmentObject/metadata/createdByUserId                               | string          | ID of the user who created the record (when available)                                             |
| departmentObject/metadata/createdByUsername                             | string          | Username of the user who created the record (when available)                                       |
| departmentObject/metadata/updatedDate                                   | string          | Date and time when the record was last updated                                                     |
| departmentObject/metadata/updatedByUserId                               | string          | ID of the user who last updated the record (when available)                                        |
| departmentObject/metadata/updatedByUsername                             | string          | Username of the user who last updated the record (when available)                                  |
| courseListingId                                                         | string          | A UUID                                                                                             |
| courseListingObject                                                     | object          | An actual instantiation in time and space of a course                                              |
| courseListingObject/id                                                  | string          | A UUID                                                                                             |
| courseListingObject/registrarId                                         | string          | The registration id                                                                                |
| courseListingObject/externalId                                          | string          | An external identifier associated with this listing                                                |
| courseListingObject/servicepointId                                      | string          | A UUID                                                                                             |
| courseListingObject/servicepointObject                                  | object          | The service point associated with this listing's reserves                                          |
| courseListingObject/servicepointObject/id                               | string          | Id of service-point object                                                                         |
| courseListingObject/servicepointObject/name                             | string          | service-point name, a required field                                                               |
| courseListingObject/servicepointObject/code                             | string          | service-point code, a required field                                                               |
| courseListingObject/servicepointObject/discoveryDisplayName             | string          | display name, a required field                                                                     |
| courseListingObject/servicepointObject/description                      | string          | description of the service-point                                                                   |
| courseListingObject/servicepointObject/shelvingLagTime                  | integer         | shelving lag time                                                                                  |
| courseListingObject/servicepointObject/pickupLocation                   | boolean         | indicates whether or not the service point is a pickup location                                    |
| courseListingObject/servicepointObject/holdShelfExpiryPeriod            | object          | schema for time-period, which contains time interval 'duration' and the time unit                  |
| courseListingObject/servicepointObject/holdShelfExpiryPeriod/duration   | integer         | Duration interval                                                                                  |
| courseListingObject/servicepointObject/holdShelfExpiryPeriod/intervalId | string          | Unit of time for the duration                                                                      |
| courseListingObject/servicepointObject/staffSlips                       | array           | List of staff slips for this service point                                                         |
| courseListingObject/servicepointObject/staffSlips/id                    | string          | The ID of the staff slip                                                                           |
| courseListingObject/servicepointObject/staffSlips/printByDefault        | boolean         | Whether or not to print the staff slip by default                                                  |
| courseListingObject/locationId                                          | string          | A UUID                                                                                             |
| courseListingObject/locationObject                                      | object          | The location associated with this listing's reserves                                               |
| courseListingObject/locationObject/id                                   | string          | id of this (shelf) location record as UUID.                                                        |
| courseListingObject/locationObject/name                                 | string          | Name of the (shelf) location                                                                       |
| courseListingObject/locationObject/code                                 | string          | Code of the (shelf) location, usually an abbreviation of the name.                                 |
| courseListingObject/locationObject/description                          | string          | Description of the (shelf) location.                                                               |
| courseListingObject/locationObject/discoveryDisplayName                 | string          | Name of the (shelf) location to be shown in the discovery.                                         |
| courseListingObject/locationObject/isActive                             | boolean         | Whether this (shelf) location is active. Inactive (shelf) locations can no longer been used.       |
| courseListingObject/locationObject/institutionId                        | string          | The UUID of the institution, the first-level location unit, this (shelf) location belongs to.      |
| courseListingObject/locationObject/campusId                             | string          | The UUID of the campus, the second-level location unit, this (shelf) location belongs to.          |
| courseListingObject/locationObject/libraryId                            | string          | The UUID of the library, the third-level location unit, this (shelf) location belongs to.          |
| courseListingObject/locationObject/details                              | object          | Details about this (shelf) location.                                                               |
| courseListingObject/locationObject/primaryServicePoint                  | string          | The UUID of the primary service point of this (shelf) location.                                    |
| courseListingObject/locationObject/servicePointIds                      | array           | All service points that this (shelf) location has.                                                 |
| courseListingObject/termId                                              | string          | A UUID                                                                                             |
| courseListingObject/termObject                                          | object          | Temporal periods that listings exist in                                                            |
| courseListingObject/termObject/id                                       | string          | A UUID                                                                                             |
| courseListingObject/termObject/name                                     | string          | The name of period                                                                                 |
| courseListingObject/termObject/startDate                                | string          | The beginning of the time period                                                                   |
| courseListingObject/termObject/endDate                                  | string          | The ending of the time period                                                                      |
| courseListingObject/termObject/metadata                                 | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| courseListingObject/termObject/metadata/createdDate                     | string          | Date and time when the record was created                                                          |
| courseListingObject/termObject/metadata/createdByUserId                 | string          | ID of the user who created the record (when available)                                             |
| courseListingObject/termObject/metadata/createdByUsername               | string          | Username of the user who created the record (when available)                                       |
| courseListingObject/termObject/metadata/updatedDate                     | string          | Date and time when the record was last updated                                                     |
| courseListingObject/termObject/metadata/updatedByUserId                 | string          | ID of the user who last updated the record (when available)                                        |
| courseListingObject/termObject/metadata/updatedByUsername               | string          | Username of the user who last updated the record (when available)                                  |
| courseListingObject/courseTypeId                                        | string          | A UUID                                                                                             |
| courseListingObject/courseTypeObject                                    | object          | The type of course a listing is                                                                    |
| courseListingObject/courseTypeObject/id                                 | string          | A UUID                                                                                             |
| courseListingObject/courseTypeObject/name                               | string          | The name of the type                                                                               |
| courseListingObject/courseTypeObject/description                        | string          | A description of this type                                                                         |
| courseListingObject/courseTypeObject/metadata                           | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| courseListingObject/courseTypeObject/metadata/createdDate               | string          | Date and time when the record was created                                                          |
| courseListingObject/courseTypeObject/metadata/createdByUserId           | string          | ID of the user who created the record (when available)                                             |
| courseListingObject/courseTypeObject/metadata/createdByUsername         | string          | Username of the user who created the record (when available)                                       |
| courseListingObject/courseTypeObject/metadata/updatedDate               | string          | Date and time when the record was last updated                                                     |
| courseListingObject/courseTypeObject/metadata/updatedByUserId           | string          | ID of the user who last updated the record (when available)                                        |
| courseListingObject/courseTypeObject/metadata/updatedByUsername         | string          | Username of the user who last updated the record (when available)                                  |
| courseListingObject/instructorObjects                                   | array           | A listing of associated instructor objects                                                         |
| courseListingObject/metadata                                            | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| courseListingObject/metadata/createdDate                                | string          | Date and time when the record was created                                                          |
| courseListingObject/metadata/createdByUserId                            | string          | ID of the user who created the record (when available)                                             |
| courseListingObject/metadata/createdByUsername                          | string          | Username of the user who created the record (when available)                                       |
| courseListingObject/metadata/updatedDate                                | string          | Date and time when the record was last updated                                                     |
| courseListingObject/metadata/updatedByUserId                            | string          | ID of the user who last updated the record (when available)                                        |
| courseListingObject/metadata/updatedByUsername                          | string          | Username of the user who last updated the record (when available)                                  |
| courseNumber                                                            | string          | A unique code identifying this course                                                              |
| sectionName                                                             | string          | A text field denoting this course's section                                                        |
| numberOfStudents                                                        | integer         | The number of students enrolled in this course                                                     |
| metadata                                                                | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate                                                    | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId                                                | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername                                              | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate                                                    | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId                                                | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername                                              | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [course_coursetypes](course_coursetypes.md)

### Source:

Module: mod-courses

Interface: /coursereserves/coursetypes

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          | A UUID                                                                                             |
| name                       | string          | The name of the type                                                                               |
| description                | string          | A description of this type                                                                         |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [course_departments](course_departments.md)

### Source:

Module: mod-courses

Interface: /coursereserves/departments

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          | A UUID                                                                                             |
| name                       | string          | The name of the department                                                                         |
| description                | string          | A description of this department                                                                   |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [course_processingstatuses](course_processingstatuses.md)

### Source:

Module: mod-courses

Interface: /coursereserves/processingstatuses

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          | A UUID                                                                                             |
| name                       | string          | The name of the status                                                                             |
| description                | string          | A description of this status                                                                       |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [course_reserves](course_reserves.md)

### Source:

Module: mod-courses

Interface: /coursereserves/reserves

### Attributes:

| Property Name                                                      | Property Type   | Property Description                                                                                      |
|:-------------------------------------------------------------------|:----------------|:----------------------------------------------------------------------------------------------------------|
| id                                                                 | string          | A UUID                                                                                                    |
| courseListingId                                                    | string          | A UUID                                                                                                    |
| itemId                                                             | string          | A UUID                                                                                                    |
| processingStatusId                                                 | string          | A UUID                                                                                                    |
| processingStatusObject                                             | object          | The processing status for a reserve                                                                       |
| processingStatusObject/id                                          | string          | A UUID                                                                                                    |
| processingStatusObject/name                                        | string          | The name of the status                                                                                    |
| processingStatusObject/description                                 | string          | A description of this status                                                                              |
| processingStatusObject/metadata                                    | object          | Metadata about creation and changes to records, provided by the server (client should not provide)        |
| processingStatusObject/metadata/createdDate                        | string          | Date and time when the record was created                                                                 |
| processingStatusObject/metadata/createdByUserId                    | string          | ID of the user who created the record (when available)                                                    |
| processingStatusObject/metadata/createdByUsername                  | string          | Username of the user who created the record (when available)                                              |
| processingStatusObject/metadata/updatedDate                        | string          | Date and time when the record was last updated                                                            |
| processingStatusObject/metadata/updatedByUserId                    | string          | ID of the user who last updated the record (when available)                                               |
| processingStatusObject/metadata/updatedByUsername                  | string          | Username of the user who last updated the record (when available)                                         |
| startDate                                                          | string          | The beginning of the time period for this reserve                                                         |
| endDate                                                            | string          | The ending of the time period for this reserve                                                            |
| copiedItem                                                         | object          | Cached fields from the item record, for searching                                                         |
| copiedItem/barcode                                                 | string          | Item barcode, from item                                                                                   |
| copiedItem/temporaryLocationId                                     | string          | Temporary Location ID, from item                                                                          |
| copiedItem/temporaryLocationObject                                 | object          | Location record populated from inventory for course-reserves                                              |
| copiedItem/temporaryLocationObject/id                              | string          |                                                                                                           |
| copiedItem/temporaryLocationObject/name                            | string          | name, copied from inventory                                                                               |
| copiedItem/temporaryLocationObject/code                            | string          | code, copied from inventory                                                                               |
| copiedItem/temporaryLocationObject/description                     | string          | description, copied from inventory                                                                        |
| copiedItem/temporaryLocationObject/discoveryDisplayName            | string          | discoveryDisplayName, copied from inventory                                                               |
| copiedItem/temporaryLocationObject/isActive                        | boolean         | isActive, copied from inventory                                                                           |
| copiedItem/temporaryLocationObject/institutionId                   | string          | institutionId, copied from inventory                                                                      |
| copiedItem/temporaryLocationObject/campusId                        | string          | campusId, copied from inventory                                                                           |
| copiedItem/temporaryLocationObject/libraryId                       | string          | libraryId, copied from inventory                                                                          |
| copiedItem/temporaryLocationObject/details                         | object          | details, copied from inventory                                                                            |
| copiedItem/temporaryLocationObject/primaryServicePoint             | string          | primaryServicePoint, copied from inventory                                                                |
| copiedItem/temporaryLocationObject/servicePointIds                 | array           | servicePointIds, copied from inventory                                                                    |
| copiedItem/permanentLocationId                                     | string          | Permanent Location ID, from item                                                                          |
| copiedItem/permanentLocationObject                                 | object          | Location record populated from inventory for course-reserves                                              |
| copiedItem/permanentLocationObject/id                              | string          |                                                                                                           |
| copiedItem/permanentLocationObject/name                            | string          | name, copied from inventory                                                                               |
| copiedItem/permanentLocationObject/code                            | string          | code, copied from inventory                                                                               |
| copiedItem/permanentLocationObject/description                     | string          | description, copied from inventory                                                                        |
| copiedItem/permanentLocationObject/discoveryDisplayName            | string          | discoveryDisplayName, copied from inventory                                                               |
| copiedItem/permanentLocationObject/isActive                        | boolean         | isActive, copied from inventory                                                                           |
| copiedItem/permanentLocationObject/institutionId                   | string          | institutionId, copied from inventory                                                                      |
| copiedItem/permanentLocationObject/campusId                        | string          | campusId, copied from inventory                                                                           |
| copiedItem/permanentLocationObject/libraryId                       | string          | libraryId, copied from inventory                                                                          |
| copiedItem/permanentLocationObject/details                         | object          | details, copied from inventory                                                                            |
| copiedItem/permanentLocationObject/primaryServicePoint             | string          | primaryServicePoint, copied from inventory                                                                |
| copiedItem/permanentLocationObject/servicePointIds                 | array           | servicePointIds, copied from inventory                                                                    |
| copiedItem/title                                                   | string          | Title, from Instance                                                                                      |
| copiedItem/contributors                                            | array           | Contributor information, from Instance                                                                    |
| copiedItem/contributors/name                                       | string          | Personal name, corporate name, meeting name                                                               |
| copiedItem/contributors/contributorTypeId                          | string          | ID for the contributor type term defined as a referencetable in settings                                  |
| copiedItem/contributors/contributorTypeText                        | string          | Free text element for adding contributor type terms other that defined by the MARC code list for relators |
| copiedItem/contributors/contributorNameTypeId                      | string          | Contributor type terms defined by the MARC code list for relators                                         |
| copiedItem/contributors/primary                                    | boolean         | Whether this is the primary contributor                                                                   |
| copiedItem/publication                                             | array           | List of publication items, from Instance                                                                  |
| copiedItem/publication/publisher                                   | string          | Name of publisher, distributor, etc.                                                                      |
| copiedItem/publication/place                                       | string          | Place of publication, distribution, etc.                                                                  |
| copiedItem/publication/dateOfPublication                           | string          | Date (year YYYY) of publication, distribution, etc.                                                       |
| copiedItem/publication/role                                        | string          | The role of the publisher, distributor, etc.                                                              |
| copiedItem/callNumber                                              | string          | The item's call number                                                                                    |
| copiedItem/uri                                                     | string          | A URI to access the item                                                                                  |
| copiedItem/volume                                                  | string          | PENDING                                                                                                   |
| copiedItem/copy                                                    | string          | PENDING                                                                                                   |
| copiedItem/enumeration                                             | string          | PENDING                                                                                                   |
| copiedItem/url                                                     | string          | PENDING                                                                                                   |
| copiedItem/instanceId                                              | string          | The id of the associated instance record                                                                  |
| copiedItem/instanceHrid                                            | string          | The HRID of the associated instance record                                                                |
| copiedItem/instanceDiscoverySuppress                               | boolean         | Whether the associated instance record has been marked as suppressed from discovery                       |
| copiedItem/holdingsId                                              | string          | The id of the associated holdings record                                                                  |
| temporaryLoanTypeId                                                | string          | A UUID                                                                                                    |
| temporaryLoanTypeObject                                            | object          | A loan type                                                                                               |
| temporaryLoanTypeObject/id                                         | string          |                                                                                                           |
| temporaryLoanTypeObject/name                                       | string          | label for the loan type                                                                                   |
| copyrightTracking                                                  | object          | Information about copyright status, volume of material used, etc.                                         |
| copyrightTracking/additionalSectionsUsed                           | boolean         | Additional sections of this item used in this course                                                      |
| copyrightTracking/copyrightStatusId                                | string          | A UUID                                                                                                    |
| copyrightTracking/copyrightStatusObject                            | object          | The copyright status of a reserve                                                                         |
| copyrightTracking/copyrightStatusObject/id                         | string          | A UUID                                                                                                    |
| copyrightTracking/copyrightStatusObject/name                       | string          | The name of the type                                                                                      |
| copyrightTracking/copyrightStatusObject/description                | string          | A description of this type                                                                                |
| copyrightTracking/copyrightStatusObject/metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)        |
| copyrightTracking/copyrightStatusObject/metadata/createdDate       | string          | Date and time when the record was created                                                                 |
| copyrightTracking/copyrightStatusObject/metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                                    |
| copyrightTracking/copyrightStatusObject/metadata/createdByUsername | string          | Username of the user who created the record (when available)                                              |
| copyrightTracking/copyrightStatusObject/metadata/updatedDate       | string          | Date and time when the record was last updated                                                            |
| copyrightTracking/copyrightStatusObject/metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                               |
| copyrightTracking/copyrightStatusObject/metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                         |
| copyrightTracking/totalPagesInItem                                 | integer         | PENDING                                                                                                   |
| copyrightTracking/totalPagesUsed                                   | integer         | PENDING                                                                                                   |
| copyrightTracking/percentOfPages                                   | string          | Percent of pages used                                                                                     |
| copyrightTracking/paymentBasis                                     | string          | PENDING                                                                                                   |
| metadata                                                           | object          | Metadata about creation and changes to records, provided by the server (client should not provide)        |
| metadata/createdDate                                               | string          | Date and time when the record was created                                                                 |
| metadata/createdByUserId                                           | string          | ID of the user who created the record (when available)                                                    |
| metadata/createdByUsername                                         | string          | Username of the user who created the record (when available)                                              |
| metadata/updatedDate                                               | string          | Date and time when the record was last updated                                                            |
| metadata/updatedByUserId                                           | string          | ID of the user who last updated the record (when available)                                               |
| metadata/updatedByUsername                                         | string          | Username of the user who last updated the record (when available)                                         |

## Documentation: [course_roles](course_roles.md)

### Source:

Module: mod-courses

Interface: /coursereserves/roles

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          | A UUID                                                                                             |
| name                       | string          | The name of the role                                                                               |
| description                | string          | A description of this role                                                                         |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [course_terms](course_terms.md)

### Source:

Module: mod-courses

Interface: /coursereserves/terms

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          | A UUID                                                                                             |
| name                       | string          | The name of period                                                                                 |
| startDate                  | string          | The beginning of the time period                                                                   |
| endDate                    | string          | The ending of the time period                                                                      |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [email_email](email_email.md)

### Source:

Module: mod-email

Interface: /email

### Attributes:

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

## Documentation: [feesfines_accounts](feesfines_accounts.md)

### Source:

Module: mod-feesfines

Interface: /accounts

### Attributes:

| Property Name              | Property Type   | Property Description                                                                                                                                                                                                                                     |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| amount                     | number          | Amount of the fine/fee                                                                                                                                                                                                                                   |
| remaining                  | number          | Remaining of the fine/fee                                                                                                                                                                                                                                |
| dateCreated                | string          | Date and time the account of the fine/fee was created                                                                                                                                                                                                    |
| dateUpdated                | string          | Date and time the account of the fine/fee was updated                                                                                                                                                                                                    |
| status                     | object          | Overall status of the fee/fine                                                                                                                                                                                                                           |
| status/name                | string          | Name of the status (values used are Open and Closed)                                                                                                                                                                                                     |
| paymentStatus              | object          | Overall status of the payment/waive/transfer/refund/cancel                                                                                                                                                                                               |
| paymentStatus/name         | string          | Name of the status                                                                                                                                                                                                                                       |
| feeFineType                | string          | Fee/fine that is up to the desecration of the user                                                                                                                                                                                                       |
| feeFineOwner               | string          | Owner of the fee/fine defined by the library and is associated with specific fees/fines                                                                                                                                                                  |
| title                      | string          | The title associated with the item                                                                                                                                                                                                                       |
| callNumber                 | string          | Identifier (Call number) assigned to an item                                                                                                                                                                                                             |
| barcode                    | string          | Text, with input likely validated by the barcode scanner                                                                                                                                                                                                 |
| materialType               | string          | Material type what define what type of thing the item is                                                                                                                                                                                                 |
| itemStatus                 | object          | The status of the item                                                                                                                                                                                                                                   |
| itemStatus/name            | string          | Name of the item state                                                                                                                                                                                                                                   |
| location                   | string          | Effective location is used to know the current home location for the item                                                                                                                                                                                |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                                                                                                                                                       |
| metadata/createdDate       | string          | Date and time when the record was created                                                                                                                                                                                                                |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                                                                                                                                                                                   |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                                                                                                                                                                             |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                                                                                                                                                                           |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                                                                                                                                                                              |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                                                                                                                                                                        |
| dueDate                    | string          | Date time when the item is due to be returned                                                                                                                                                                                                            |
| returnedDate               | string          | Date time when the item is returned and the loan ends, if the user does not have a loan associated, hyphen (-) is added as default                                                                                                                       |
| loanId                     | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| userId                     | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| itemId                     | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| materialTypeId             | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| feeFineId                  | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| ownerId                    | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| id                         | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| holdingsRecordId           | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| instanceId                 | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| contributors               | array           | List of contributors                                                                                                                                                                                                                                     |
| contributors/name          | string          | Personal name, corporate name, meeting name                                                                                                                                                                                                              |
| loanPolicyId               | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| overdueFinePolicyId        | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| lostItemFeePolicyId        | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| processId                  | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |

## Documentation: [feesfines_comments](feesfines_comments.md)

### Source:

Module: mod-feesfines

Interface: /comments

### Attributes:

| Property Name              | Property Type   | Property Description                                                                                                                                                                                                                                     |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| paid                       | boolean         | A flag to determine when paying if it is mandatory to add additional information                                                                                                                                                                         |
| waived                     | boolean         | A flag to determine when waiving if it is mandatory to add additional information                                                                                                                                                                        |
| refunded                   | boolean         | A flag to determine when refunding if it is mandatory to add additional information                                                                                                                                                                      |
| transferredManually        | boolean         | A flag to determine when transferring if it is mandatory to add additional information                                                                                                                                                                   |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                                                                                                                                                       |
| metadata/createdDate       | string          | Date and time when the record was created                                                                                                                                                                                                                |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                                                                                                                                                                                   |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                                                                                                                                                                             |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                                                                                                                                                                           |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                                                                                                                                                                              |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                                                                                                                                                                        |
| id                         | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |

## Documentation: [feesfines_feefineactions](feesfines_feefineactions.md)

### Source:

Module: mod-feesfines

Interface: /feefineactions

### Attributes:

| Property Name          | Property Type   | Property Description                                                                                                                                                                                                                                     |
|:-----------------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| dateAction             | string          | Date and time the transaction of the fine/fee was created                                                                                                                                                                                                |
| typeAction             | string          | Type of activity including the type of transaction                                                                                                                                                                                                       |
| comments               | string          | Additional information entered as part of the activity or on this screen as a 'Staff info only' activity                                                                                                                                                 |
| notify                 | boolean         | A flag to determine if a patron should be notified or not                                                                                                                                                                                                |
| amountAction           | number          | Amount of activity                                                                                                                                                                                                                                       |
| balance                | number          | Calculated amount of remaining balance based on original fee/fine and what has been paid/waived/transferred/refunded                                                                                                                                     |
| transactionInformation | string          | Number or other transaction id related to payment                                                                                                                                                                                                        |
| createdAt              | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| originalCreatedAt      | string          | Original invalid (non-UUID) value of 'createdAt' moved here when UUID-validation was enabled for 'createdAt'                                                                                                                                             |
| source                 | string          | Person who processed activity (from login information)                                                                                                                                                                                                   |
| paymentMethod          | string          | Overall status of the action-setting                                                                                                                                                                                                                     |
| accountId              | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| userId                 | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| id                     | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |

## Documentation: [feesfines_feefines](feesfines_feefines.md)

### Source:

Module: mod-feesfines

Interface: /feefines

### Attributes:

| Property Name              | Property Type   | Property Description                                                                                                                                                                                                                                     |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| automatic                  | boolean         | A flag to indicate that fee/fine was created automatically.                                                                                                                                                                                              |
| feeFineType                | string          | Description of fee/fine that is up to the discretion of the user                                                                                                                                                                                         |
| defaultAmount              | number          | Amount of fee or fine, which may be overridden.                                                                                                                                                                                                          |
| chargeNoticeId             | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| actionNoticeId             | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| ownerId                    | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                                                                                                                                                       |
| metadata/createdDate       | string          | Date and time when the record was created                                                                                                                                                                                                                |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                                                                                                                                                                                   |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                                                                                                                                                                             |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                                                                                                                                                                           |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                                                                                                                                                                              |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                                                                                                                                                                        |
| id                         | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |

## Documentation: [feesfines_lost_item_fees_policies](feesfines_lost_item_fees_policies.md)

### Source:

Module: mod-feesfines

Interface: /lost-item-fees-policies

### Attributes:

| Property Name                                    | Property Type   | Property Description                                                                                                                                                                                                                                     |
|:-------------------------------------------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name                                             | string          | Lost item fee policy name, is a required field                                                                                                                                                                                                           |
| description                                      | string          | Lost item fee policy description                                                                                                                                                                                                                         |
| itemAgedLostOverdue                              | object          | Period to lost item                                                                                                                                                                                                                                      |
| itemAgedLostOverdue/duration                     | integer         | Duration of the number of times the interval repeats                                                                                                                                                                                                     |
| itemAgedLostOverdue/intervalId                   | string          | Interval for the period, e.g. Hours, Days or Weeks                                                                                                                                                                                                       |
| patronBilledAfterAgedLost                        | object          | Period to lost item                                                                                                                                                                                                                                      |
| patronBilledAfterAgedLost/duration               | integer         | Duration of the number of times the interval repeats                                                                                                                                                                                                     |
| patronBilledAfterAgedLost/intervalId             | string          | Interval for the period, e.g. Hours, Days or Weeks                                                                                                                                                                                                       |
| recalledItemAgedLostOverdue                      | object          | Period to lost item                                                                                                                                                                                                                                      |
| recalledItemAgedLostOverdue/duration             | integer         | Duration of the number of times the interval repeats                                                                                                                                                                                                     |
| recalledItemAgedLostOverdue/intervalId           | string          | Interval for the period, e.g. Hours, Days or Weeks                                                                                                                                                                                                       |
| patronBilledAfterRecalledItemAgedLost            | object          | Period to lost item                                                                                                                                                                                                                                      |
| patronBilledAfterRecalledItemAgedLost/duration   | integer         | Duration of the number of times the interval repeats                                                                                                                                                                                                     |
| patronBilledAfterRecalledItemAgedLost/intervalId | string          | Interval for the period, e.g. Hours, Days or Weeks                                                                                                                                                                                                       |
| chargeAmountItem                                 | object          | Charge amount for item                                                                                                                                                                                                                                   |
| chargeAmountItem/chargeType                      | string          | Charge type amount for item may be Actual cost or an amount                                                                                                                                                                                              |
| chargeAmountItem/amount                          | number          | Charge amount for item may be Actual cost or an amount                                                                                                                                                                                                   |
| lostItemProcessingFee                            | number          | Lost item processing fee, must be = 0 or > 0                                                                                                                                                                                                             |
| chargeAmountItemPatron                           | boolean         | A flag to determine charge lost item processing fee if item declared lost by patron must be Yes or No, with default set to Yes                                                                                                                           |
| chargeAmountItemSystem                           | boolean         | A flag to determine charge lost item processing fee if item aged to lost by system must be Yes or No, with default set to Yes                                                                                                                            |
| lostItemChargeFeeFine                            | object          | Period to lost item                                                                                                                                                                                                                                      |
| lostItemChargeFeeFine/duration                   | integer         | Duration of the number of times the interval repeats                                                                                                                                                                                                     |
| lostItemChargeFeeFine/intervalId                 | string          | Interval for the period, e.g. Hours, Days or Weeks                                                                                                                                                                                                       |
| returnedLostItemProcessingFee                    | boolean         | A flag to determine if lost item returned, remove lost item processing fee                                                                                                                                                                               |
| replacedLostItemProcessingFee                    | boolean         | A flag to determine if lost item replaced, remove lost item processing fee                                                                                                                                                                               |
| replacementProcessingFee                         | number          | Amount for replacement process fee                                                                                                                                                                                                                       |
| replacementAllowed                               | boolean         | A flag to determine replacement allowed                                                                                                                                                                                                                  |
| lostItemReturned                                 | string          | Option to lost item returned may be Charge overdues based on returned date up to maximum (if applicable) or Remove overdue fines, with a default of _Charge overdues based on returned date up to maximum (if applicable)                                |
| feesFinesShallRefunded                           | object          | Period to lost item                                                                                                                                                                                                                                      |
| feesFinesShallRefunded/duration                  | integer         | Duration of the number of times the interval repeats                                                                                                                                                                                                     |
| feesFinesShallRefunded/intervalId                | string          | Interval for the period, e.g. Hours, Days or Weeks                                                                                                                                                                                                       |
| metadata                                         | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                                                                                                                                                       |
| metadata/createdDate                             | string          | Date and time when the record was created                                                                                                                                                                                                                |
| metadata/createdByUserId                         | string          | ID of the user who created the record (when available)                                                                                                                                                                                                   |
| metadata/createdByUsername                       | string          | Username of the user who created the record (when available)                                                                                                                                                                                             |
| metadata/updatedDate                             | string          | Date and time when the record was last updated                                                                                                                                                                                                           |
| metadata/updatedByUserId                         | string          | ID of the user who last updated the record (when available)                                                                                                                                                                                              |
| metadata/updatedByUsername                       | string          | Username of the user who last updated the record (when available)                                                                                                                                                                                        |
| id                                               | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |

## Documentation: [feesfines_manualblocks](feesfines_manualblocks.md)

### Source:

Module: mod-feesfines

Interface: /manualblocks

### Attributes:

| Property Name              | Property Type   | Property Description                                                                                                                                                                                                                                     |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| type                       | string          | Type of patron block                                                                                                                                                                                                                                     |
| desc                       | string          | Patron block description                                                                                                                                                                                                                                 |
| code                       | string          | Code of the template if block is defined based on a template (optional)                                                                                                                                                                                  |
| staffInformation           | string          | Additional information to staff (optional)                                                                                                                                                                                                               |
| patronMessage              | string          | Message to patron (optional)                                                                                                                                                                                                                             |
| expirationDate             | string          | Date and time the patron block expiration if is provided the patron block should be automatically removed on that date                                                                                                                                   |
| borrowing                  | boolean         | A flag to determine borrowing block action                                                                                                                                                                                                               |
| renewals                   | boolean         | A flag to determine renewal block action                                                                                                                                                                                                                 |
| requests                   | boolean         | A flag to determine request block action                                                                                                                                                                                                                 |
| userId                     | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                                                                                                                                                       |
| metadata/createdDate       | string          | Date and time when the record was created                                                                                                                                                                                                                |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                                                                                                                                                                                   |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                                                                                                                                                                             |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                                                                                                                                                                           |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                                                                                                                                                                              |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                                                                                                                                                                        |
| id                         | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |

## Documentation: [feesfines_overdue_fines_policies](feesfines_overdue_fines_policies.md)

### Source:

Module: mod-feesfines

Interface: /overdue-fines-policies

### Attributes:

| Property Name                                          | Property Type   | Property Description                                                                                                                                                                                                                                     |
|:-------------------------------------------------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name                                                   | string          | Overdue fine policy name                                                                                                                                                                                                                                 |
| description                                            | string          | Overdue fine policy description                                                                                                                                                                                                                          |
| overdueFine                                            | object          | Amount of times the interval repeats                                                                                                                                                                                                                     |
| overdueFine/quantity                                   | number          | Fine amount per interval                                                                                                                                                                                                                                 |
| overdueFine/intervalId                                 | string          | Interval for the period, e.g. hour, day, week, month or year                                                                                                                                                                                             |
| countClosed                                            | boolean         | A flag to determine if a fine is count closed                                                                                                                                                                                                            |
| maxOverdueFine                                         | number          | Maximum overdue fine                                                                                                                                                                                                                                     |
| forgiveOverdueFine                                     | boolean         | A flag to determine forgive overdue fine if item renewed                                                                                                                                                                                                 |
| overdueRecallFine                                      | object          | Amount of times the interval repeats                                                                                                                                                                                                                     |
| overdueRecallFine/quantity                             | number          | Fine amount per interval                                                                                                                                                                                                                                 |
| overdueRecallFine/intervalId                           | string          | Interval for the period, e.g. hour, day, week, month or year                                                                                                                                                                                             |
| gracePeriodRecall                                      | boolean         | Grace period for recall                                                                                                                                                                                                                                  |
| maxOverdueRecallFine                                   | number          | Maximum overdue recall fine                                                                                                                                                                                                                              |
| reminderFeesPolicy                                     | object          | Reminder fee policy as part of overdue fine policy                                                                                                                                                                                                       |
| reminderFeesPolicy/countClosed                         | boolean         | A flag to determine if a reminder fee should take closed days into account                                                                                                                                                                               |
| reminderFeesPolicy/ignoreGracePeriodRecall             | boolean         | Ignore grace period for recall                                                                                                                                                                                                                           |
| reminderFeesPolicy/ignoreGracePeriodHolds              | boolean         | Ignore grace period for holds                                                                                                                                                                                                                            |
| reminderFeesPolicy/allowRenewalOfItemsWithReminderFees | boolean         | Allow renewal of items with reminder fee(s)                                                                                                                                                                                                              |
| reminderFeesPolicy/clearPatronBlockWhenPaid            | boolean         | Clear patron block when paid                                                                                                                                                                                                                             |
| reminderFeesPolicy/reminderSchedule                    | array           | Ordered list of reminder notices                                                                                                                                                                                                                         |
| reminderFeesPolicy/reminderSchedule/interval           | integer         | Number of units of time before notice should be sent                                                                                                                                                                                                     |
| reminderFeesPolicy/reminderSchedule/timeUnitId         | string          | Time unit of interval                                                                                                                                                                                                                                    |
| reminderFeesPolicy/reminderSchedule/reminderFee        | number          | Fee amount accrued by reminder notice                                                                                                                                                                                                                    |
| reminderFeesPolicy/reminderSchedule/noticeFormat       | string          | Method of sending notice                                                                                                                                                                                                                                 |
| reminderFeesPolicy/reminderSchedule/noticeTemplateId   | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| reminderFeesPolicy/reminderSchedule/blockTemplateId    | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| metadata                                               | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                                                                                                                                                       |
| metadata/createdDate                                   | string          | Date and time when the record was created                                                                                                                                                                                                                |
| metadata/createdByUserId                               | string          | ID of the user who created the record (when available)                                                                                                                                                                                                   |
| metadata/createdByUsername                             | string          | Username of the user who created the record (when available)                                                                                                                                                                                             |
| metadata/updatedDate                                   | string          | Date and time when the record was last updated                                                                                                                                                                                                           |
| metadata/updatedByUserId                               | string          | ID of the user who last updated the record (when available)                                                                                                                                                                                              |
| metadata/updatedByUsername                             | string          | Username of the user who last updated the record (when available)                                                                                                                                                                                        |
| id                                                     | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |

## Documentation: [feesfines_owners](feesfines_owners.md)

### Source:

Module: mod-feesfines

Interface: /owners

### Attributes:

| Property Name              | Property Type   | Property Description                                                                                                                                                                                                                                     |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| owner                      | string          | Service desk (known as a fee/fine owner) is library-defined and is associated with specific fees/fines                                                                                                                                                   |
| desc                       | string          | Owner description                                                                                                                                                                                                                                        |
| servicePointOwner          | array           | Service points associated to a Owner                                                                                                                                                                                                                     |
| servicePointOwner/value    | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| servicePointOwner/label    | string          | Service-point name label                                                                                                                                                                                                                                 |
| defaultChargeNoticeId      | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| defaultActionNoticeId      | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                                                                                                                                                       |
| metadata/createdDate       | string          | Date and time when the record was created                                                                                                                                                                                                                |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                                                                                                                                                                                   |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                                                                                                                                                                             |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                                                                                                                                                                           |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                                                                                                                                                                              |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                                                                                                                                                                        |
| id                         | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |

## Documentation: [feesfines_payments](feesfines_payments.md)

### Source:

Module: mod-feesfines

Interface: /payments

### Attributes:

| Property Name              | Property Type   | Property Description                                                                                                                                                                                                                                     |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| nameMethod                 | string          | Payment method name                                                                                                                                                                                                                                      |
| allowedRefundMethod        | boolean         | A flag to determine if refund method is allowed default at 'Yes'                                                                                                                                                                                         |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                                                                                                                                                       |
| metadata/createdDate       | string          | Date and time when the record was created                                                                                                                                                                                                                |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                                                                                                                                                                                   |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                                                                                                                                                                             |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                                                                                                                                                                           |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                                                                                                                                                                              |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                                                                                                                                                                        |
| ownerId                    | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| id                         | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |

## Documentation: [feesfines_refunds](feesfines_refunds.md)

### Source:

Module: mod-feesfines

Interface: /refunds

### Attributes:

| Property Name              | Property Type   | Property Description                                                                                                                                                                                                                                     |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| nameReason                 | string          | Refund reason is required field                                                                                                                                                                                                                          |
| description                | string          | Refund reason description                                                                                                                                                                                                                                |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                                                                                                                                                       |
| metadata/createdDate       | string          | Date and time when the record was created                                                                                                                                                                                                                |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                                                                                                                                                                                   |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                                                                                                                                                                             |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                                                                                                                                                                           |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                                                                                                                                                                              |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                                                                                                                                                                        |
| accountId                  | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| id                         | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |

## Documentation: [feesfines_transfer_criterias](feesfines_transfer_criterias.md)

### Source:

Module: mod-feesfines

Interface: /transfer-criterias

### Attributes:

| Property Name   | Property Type   | Property Description                                                                                                                                                                                                                                     |
|:----------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| criteria        | string          | Not implemented yet                                                                                                                                                                                                                                      |
| type            | string          | Not implemented yet                                                                                                                                                                                                                                      |
| value           | number          | Not implemented yet                                                                                                                                                                                                                                      |
| interval        | string          | Not implemented yet                                                                                                                                                                                                                                      |
| id              | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |

## Documentation: [feesfines_transfers](feesfines_transfers.md)

### Source:

Module: mod-feesfines

Interface: /transfers

### Attributes:

| Property Name              | Property Type   | Property Description                                                                                                                                                                                                                                     |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| accountName                | string          | Transfer account name                                                                                                                                                                                                                                    |
| desc                       | string          | Transfer account description                                                                                                                                                                                                                             |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                                                                                                                                                       |
| metadata/createdDate       | string          | Date and time when the record was created                                                                                                                                                                                                                |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                                                                                                                                                                                   |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                                                                                                                                                                             |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                                                                                                                                                                           |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                                                                                                                                                                              |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                                                                                                                                                                        |
| ownerId                    | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| id                         | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |

## Documentation: [feesfines_waives](feesfines_waives.md)

### Source:

Module: mod-feesfines

Interface: /waives

### Attributes:

| Property Name              | Property Type   | Property Description                                                                                                                                                                                                                                     |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| nameReason                 | string          | Waive reason name                                                                                                                                                                                                                                        |
| description                | string          | Waive reason description                                                                                                                                                                                                                                 |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                                                                                                                                                       |
| metadata/createdDate       | string          | Date and time when the record was created                                                                                                                                                                                                                |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                                                                                                                                                                                   |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                                                                                                                                                                             |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                                                                                                                                                                           |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                                                                                                                                                                              |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                                                                                                                                                                        |
| accountId                  | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| id                         | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |

## Documentation: [finance_budgets](finance_budgets.md)

### Source:

Module: mod-finance-storage

Interface: /finance-storage/budgets

### Attributes:

| Property Name              | Property Type   | Property Description                                                                                     |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------------|
| id                         | string          | The UUID format string                                                                                   |
| _version                   | integer         | Record version for optimistic locking                                                                    |
| name                       | string          | The name of the budget                                                                                   |
| budgetStatus               | string          | The status of the budget                                                                                 |
| allowableEncumbrance       | number          | The encumbrance percentage limit for this budget                                                         |
| allowableExpenditure       | number          | The expenditure percentage limit for this budget                                                         |
| allocated                  | number          | The amount currently allocated to this budget                                                            |
| awaitingPayment            | number          | The amount currently awaiting payment for this budget                                                    |
| available                  | number          | The amount currently available for this budge                                                            |
| encumbered                 | number          | The amount currently encumbered for this budget                                                          |
| expenditures               | number          | The amount currently expended for this budget                                                            |
| netTransfers               | number          | Summing all the transfers on this budget                                                                 |
| unavailable                | number          | Unavailable amount for this budget                                                                       |
| overEncumbrance            | number          | The amount currently over-encumbered for this budget                                                     |
| overExpended               | number          | Amount the budget is over expended.                                                                      |
| fundId                     | string          | The UUID format string                                                                                   |
| fiscalYearId               | string          | The UUID format string                                                                                   |
| acqUnitIds                 | array           | acquisition unit ids associated with this budget                                                         |
| tags                       | object          | List of simple tags that can be added to an object                                                       |
| tags/tagList               | array           | List of tags                                                                                             |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)       |
| metadata/createdDate       | string          | Date and time when the record was created                                                                |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                                   |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                             |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                           |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                              |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                        |
| initialAllocation          | number          | The amount of the first allocation made to this budget                                                   |
| allocationTo               | number          | The sum of all allocation transaction amounts made TO this budget not including the Initial allocation   |
| allocationFrom             | number          | The sum of all allocation transaction amounts made FROM this budget not including the Initial allocation |
| totalFunding               | number          | budget.allocated + budget.netTransfers                                                                   |
| cashBalance                | number          | Total Funding minus Expended                                                                             |

## Documentation: [finance_expense_classes](finance_expense_classes.md)

### Source:

Module: mod-finance-storage

Interface: /finance-storage/expense-classes

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          | The UUID format string                                                                             |
| _version                   | integer         | Record version for optimistic locking                                                              |
| code                       | string          | The code of the expense class                                                                      |
| externalAccountNumberExt   | string          | An external account number extension                                                               |
| name                       | string          | The name of the expense class                                                                      |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [finance_fiscal_years](finance_fiscal_years.md)

### Source:

Module: mod-finance-storage

Interface: /finance-storage/fiscal-years

### Attributes:

| Property Name                      | Property Type   | Property Description                                                                               |
|:-----------------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                                 | string          | The UUID format string                                                                             |
| _version                           | integer         | Record version for optimistic locking                                                              |
| acqUnitIds                         | array           | UUIDs of the acquisition units associated with this fiscal year                                    |
| name                               | string          | The name of the fiscal year                                                                        |
| code                               | string          | The code of the fiscal year                                                                        |
| currency                           | string          | Currency code which is recorded when the FY ends, otherwise the system currency can be assumed     |
| description                        | string          | The description of the fiscal year                                                                 |
| periodStart                        | string          | The start date of the fiscal year                                                                  |
| periodEnd                          | string          | The end date of the fiscal year                                                                    |
| series                             | string          | The fiscal year series                                                                             |
| financialSummary                   | object          | Funding information and Financial activity                                                         |
| financialSummary/allocated         | number          | Summary of all related to this fiscal year budgets allocated                                       |
| financialSummary/available         | number          | Summary of all related to this fiscal year budgets available                                       |
| financialSummary/unavailable       | number          | Summary of all related to this fiscal year budgets unavailable                                     |
| financialSummary/initialAllocation | number          | Summary of all related to this fiscal year budgets initialAllocation                               |
| financialSummary/allocationTo      | number          | Summary of all related to this fiscal year budgets allocationTo                                    |
| financialSummary/allocationFrom    | number          | Summary of all related to this fiscal year budgets allocationFrom                                  |
| financialSummary/totalFunding      | number          | Summary of all related to this fiscal year budgets totalFunding                                    |
| financialSummary/cashBalance       | number          | Summary of all related to this fiscal year budgets cashBalance                                     |
| financialSummary/awaitingPayment   | number          | Summary of all related to this fiscal year budgets awaitingPayment                                 |
| financialSummary/encumbered        | number          | Summary of all related to this fiscal year budgets encumbered                                      |
| financialSummary/expenditures      | number          | Summary of all related to this ledger budgets expenditures                                         |
| financialSummary/overEncumbrance   | number          | Summary of all related to this ledger budgets overEncumbrance                                      |
| financialSummary/overExpended      | number          | Summary of all related to this ledger budgets overExpended                                         |
| metadata                           | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate               | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId           | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername         | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate               | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId           | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername         | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [finance_fund_types](finance_fund_types.md)

### Source:

Module: mod-finance-storage

Interface: /finance-storage/fund-types

### Attributes:

| Property Name   | Property Type   | Property Description                  |
|:----------------|:----------------|:--------------------------------------|
| id              | string          | The UUID format string                |
| _version        | integer         | Record version for optimistic locking |
| name            | string          | Name of fund type                     |

## Documentation: [finance_funds](finance_funds.md)

### Source:

Module: mod-finance-storage

Interface: /finance-storage/funds

### Attributes:

| Property Name              | Property Type   | Property Description                                                                                                                                                   |
|:---------------------------|:----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id                         | string          | The UUID format string                                                                                                                                                 |
| _version                   | integer         | Record version for optimistic locking                                                                                                                                  |
| allocatedFromIds           | array           | All the funds that this fund is allowed to receive money from. This would be 1 fund or none. If this field is blank their is no restriction on allocating to this fund |
| allocatedToIds             | array           | All the funds that this fund is allowed to send money to. This could be one or many.                                                                                   |
| code                       | string          | Fund code format                                                                                                                                                       |
| description                | string          | The description of this fund                                                                                                                                           |
| externalAccountNo          | string          | Corresponding account in the financial system. Will be recorded in payment generated as well.                                                                          |
| fundStatus                 | string          | The current status of this fund                                                                                                                                        |
| fundTypeId                 | string          | The UUID format string                                                                                                                                                 |
| ledgerId                   | string          | The UUID format string                                                                                                                                                 |
| name                       | string          | The name of this fund                                                                                                                                                  |
| acqUnitIds                 | array           | acquisition unit ids associated with this fund                                                                                                                         |
| tags                       | object          | List of simple tags that can be added to an object                                                                                                                     |
| tags/tagList               | array           | List of tags                                                                                                                                                           |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                                                                     |
| metadata/createdDate       | string          | Date and time when the record was created                                                                                                                              |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                                                                                                 |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                                                                                           |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                                                                                         |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                                                                                            |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                                                                                      |

## Documentation: [finance_group_fund_fiscal_years](finance_group_fund_fiscal_years.md)

### Source:

Module: mod-finance-storage

Interface: /finance-storage/group-fund-fiscal-years

### Attributes:

| Property Name   | Property Type   | Property Description                  |
|:----------------|:----------------|:--------------------------------------|
| id              | string          | The UUID format string                |
| _version        | integer         | Record version for optimistic locking |
| budgetId        | string          | The UUID format string                |
| groupId         | string          | The UUID format string                |
| fiscalYearId    | string          | The UUID format string                |
| fundId          | string          | The UUID format string                |

## Documentation: [finance_groups](finance_groups.md)

### Source:

Module: mod-finance-storage

Interface: /finance-storage/groups

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          | The UUID format string                                                                             |
| _version                   | integer         | Record version for optimistic locking                                                              |
| acqUnitIds                 | array           | UUIDs of the acquisition units associated with this group                                          |
| code                       | string          | The code of the group                                                                              |
| description                | string          | The description of the group                                                                       |
| name                       | string          | The name of the group                                                                              |
| status                     | string          | The status of the group                                                                            |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [finance_ledgers](finance_ledgers.md)

### Source:

Module: mod-finance-storage

Interface: /finance-storage/ledgers

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          | The UUID format string                                                                             |
| _version                   | integer         | Record version for optimistic locking                                                              |
| name                       | string          | The name of the ledger                                                                             |
| code                       | string          | The code for the ledger                                                                            |
| description                | string          | The description of the ledger                                                                      |
| fiscalYearOneId            | string          | The UUID format string                                                                             |
| ledgerStatus               | string          | The status of the ledger                                                                           |
| allocated                  | number          | The amount currently allocated to this ledger                                                      |
| available                  | number          | The amount currently available in this ledger                                                      |
| netTransfers               | number          | Summing all the transfers from/to this ledger. Amount can be negative                              |
| unavailable                | number          | The amount already utilized from the allocated amount                                              |
| currency                   | string          | The ISO code for currency                                                                          |
| acqUnitIds                 | array           | acquisition unit ids associated with this ledger                                                   |
| restrictEncumbrance        | boolean         | If true, imposes restrictions on encumbrances                                                      |
| restrictExpenditures       | boolean         | If true, imposes restrictions on payments                                                          |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |
| initialAllocation          | number          | Summary of all related to this ledger budgets initialAllocation                                    |
| allocationTo               | number          | Summary of all related to this ledger budgets allocationTo                                         |
| allocationFrom             | number          | Summary of all related to this ledger budgets allocationFrom                                       |
| totalFunding               | number          | Summary of all related to this ledger budgets totalFunding                                         |
| cashBalance                | number          | Summary of all related to this ledger budgets cashBalance                                          |
| awaitingPayment            | number          | Summary of all related to this ledger budgets awaitingPayment                                      |
| encumbered                 | number          | Summary of all related to this ledger budgets encumbered                                           |
| expenditures               | number          | Summary of all related to this ledger budgets expenditures                                         |
| overEncumbrance            | number          | Summary of all related to this ledger budgets overEncumbrance                                      |
| overExpended               | number          | Summary of all related to this ledger budgets overExpended                                         |

## Documentation: [finance_transactions](finance_transactions.md)

### Source:

Module: mod-finance-storage

Interface: /finance-storage/transactions

### Attributes:

| Property Name                       | Property Type   | Property Description                                                                                                         |
|:------------------------------------|:----------------|:-----------------------------------------------------------------------------------------------------------------------------|
| id                                  | string          | The UUID format string                                                                                                       |
| _version                            | integer         | Record version for optimistic locking                                                                                        |
| amount                              | number          | The amount of this transaction. For encumbrances: This is initialAmountEncumbered - (amountAwaitingPayment + amountExpended) |
| awaitingPayment                     | object          | Awaiting payment schema                                                                                                      |
| awaitingPayment/encumbranceId       | string          | The UUID format string                                                                                                       |
| awaitingPayment/releaseEncumbrance  | boolean         | Whether or not remaining encumbered money should be released                                                                 |
| currency                            | string          | Currency code for this transaction - from the system currency                                                                |
| description                         | string          | Description of this transaction                                                                                              |
| encumbrance                         | object          | The encumbrance associated with the payment/credit taking place                                                              |
| encumbrance/amountAwaitingPayment   | number          | Deprecated! Going to be removed in next release. The amount of awaiting for payment                                          |
| encumbrance/amountExpended          | number          | The amount currently expended by this encumbrance                                                                            |
| encumbrance/initialAmountEncumbered | number          | The initial amount of this encumbrance. Shouldn't change once create                                                         |
| encumbrance/status                  | string          | The status of this encumbrance                                                                                               |
| encumbrance/orderType               | string          | Taken from the purchase order                                                                                                |
| encumbrance/orderStatus             | string          | Taken from the purchase order                                                                                                |
| encumbrance/subscription            | boolean         | Taken from the purchase Order,for fiscal year rollover                                                                       |
| encumbrance/reEncumber              | boolean         | Taken from the purchase Order,for fiscal year rollover                                                                       |
| encumbrance/sourcePurchaseOrderId   | string          | The UUID format string                                                                                                       |
| encumbrance/sourcePoLineId          | string          | The UUID format string                                                                                                       |
| expenseClassId                      | string          | The UUID format string                                                                                                       |
| fiscalYearId                        | string          | The UUID format string                                                                                                       |
| fromFundId                          | string          | The UUID format string                                                                                                       |
| invoiceCancelled                    | boolean         | Indicates that related invoice was cancelled                                                                                 |
| paymentEncumbranceId                | string          | The UUID format string                                                                                                       |
| source                              | string          | The readable identifier of the record that resulted in the creation of this transaction                                      |
| sourceFiscalYearId                  | string          | The UUID format string                                                                                                       |
| sourceInvoiceId                     | string          | The UUID format string                                                                                                       |
| sourceInvoiceLineId                 | string          | The UUID format string                                                                                                       |
| tags                                | object          | List of simple tags that can be added to an object                                                                           |
| tags/tagList                        | array           | List of tags                                                                                                                 |
| toFundId                            | string          | The UUID format string                                                                                                       |
| transactionType                     | string          | This describes the type of transaction                                                                                       |
| voidedAmount                        | number          | Voided amount, not to be counted in budget totals                                                                            |
| metadata                            | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                           |
| metadata/createdDate                | string          | Date and time when the record was created                                                                                    |
| metadata/createdByUserId            | string          | ID of the user who created the record (when available)                                                                       |
| metadata/createdByUsername          | string          | Username of the user who created the record (when available)                                                                 |
| metadata/updatedDate                | string          | Date and time when the record was last updated                                                                               |
| metadata/updatedByUserId            | string          | ID of the user who last updated the record (when available)                                                                  |
| metadata/updatedByUsername          | string          | Username of the user who last updated the record (when available)                                                            |

## Documentation: [inventory_alternative_title_types](inventory_alternative_title_types.md)

### Source:

Module: mod-inventory-storage

Interface: /alternative-title-types

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          | unique ID of the alternative title type; a UUID                                                    |
| name                       | string          | name of the alternative title type                                                                 |
| source                     | string          | label indicating where the alternative title type entry originates from, i.e. 'folio' or 'local'   |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [inventory_bound_with_part](inventory_bound_with_part.md)

### Source:

Module: mod-inventory-storage

Interface: /inventory-storage/bound-with-parts

### Attributes:

| Property Name              | Property Type   | Property Description                                                                                                                                                                                                                                     |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id                         | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| holdingsRecordId           | string          | the ID of the holdings record representing a part of a bound-with; a UUID                                                                                                                                                                                |
| itemId                     | string          | the ID of the item representing the bind; a UUID                                                                                                                                                                                                         |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                                                                                                                                                       |
| metadata/createdDate       | string          | Date and time when the record was created                                                                                                                                                                                                                |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                                                                                                                                                                                   |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                                                                                                                                                                             |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                                                                                                                                                                           |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                                                                                                                                                                              |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                                                                                                                                                                        |

## Documentation: [inventory_call_number_types](inventory_call_number_types.md)

### Source:

Module: mod-inventory-storage

Interface: /call-number-types

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          | unique ID of the call number type; a UUID                                                          |
| name                       | string          | name of the call number type                                                                       |
| source                     | string          | label indicating where the call number type entry originates from, i.e. 'folio' or 'local'         |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [inventory_campuses](inventory_campuses.md)

### Source:

Module: mod-inventory-storage

Interface: /location-units/campuses

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          |                                                                                                    |
| name                       | string          | name of the location                                                                               |
| code                       | string          | distinct code for the location                                                                     |
| institutionId              | string          | ID of the first-level location unit that the second-level unit belongs to                          |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [inventory_classification_types](inventory_classification_types.md)

### Source:

Module: mod-inventory-storage

Interface: /classification-types

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          |                                                                                                    |
| name                       | string          | label for the classification type                                                                  |
| source                     | string          | label indicating where the classification type entry originates from, i.e. 'folio' or 'local'      |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [inventory_contributor_name_types](inventory_contributor_name_types.md)

### Source:

Module: mod-inventory-storage

Interface: /contributor-name-types

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          |                                                                                                    |
| name                       | string          | label for the type of contributor name                                                             |
| ordering                   | string          | used for ordering of contributor name types in displays, i.e. in select lists                      |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [inventory_contributor_types](inventory_contributor_types.md)

### Source:

Module: mod-inventory-storage

Interface: /contributor-types

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          |                                                                                                    |
| name                       | string          | label for the contributor type                                                                     |
| code                       | string          | distinct code for the contributor type                                                             |
| source                     |                 | origin of the contributor type record                                                              |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [inventory_electronic_access_relationships](inventory_electronic_access_relationships.md)

### Source:

Module: mod-inventory-storage

Interface: /electronic-access-relationships

### Attributes:

| Property Name              | Property Type   | Property Description                                                                                            |
|:---------------------------|:----------------|:----------------------------------------------------------------------------------------------------------------|
| id                         | string          |                                                                                                                 |
| name                       | string          | label for the type of relationship between a URL and an Instance                                                |
| source                     | string          | Origin of the electronic access relationship record, e.g. 'System', 'User', 'Consortium', 'folio', 'local' etc. |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)              |
| metadata/createdDate       | string          | Date and time when the record was created                                                                       |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                                          |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                                    |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                                  |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                                     |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                               |

## Documentation: [inventory_holdings](inventory_holdings.md)

### Source:

Module: mod-inventory-storage

Interface: /holdings-storage/holdings

### Attributes:

| Property Name                              | Property Type   | Property Description                                                                                                                                                                                                                                         |
|:-------------------------------------------|:----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id                                         | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/     |
| _version                                   | integer         | Record version for optimistic locking                                                                                                                                                                                                                        |
| hrid                                       | string          | the human readable ID, also called eye readable ID. A system-assigned sequential ID which maps to the Instance ID                                                                                                                                            |
| holdingsTypeId                             | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/     |
| formerIds                                  | array           | Previous ID(s) assigned to the holdings record                                                                                                                                                                                                               |
| instanceId                                 | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/     |
| permanentLocationId                        | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/     |
| permanentLocation                          | object          | The permanent shelving location in which an item resides                                                                                                                                                                                                     |
| temporaryLocationId                        | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/     |
| effectiveLocationId                        | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/     |
| electronicAccess                           | array           | List of electronic access items                                                                                                                                                                                                                              |
| electronicAccess/uri                       | string          | uniform resource identifier (URI) is a string of characters designed for unambiguous identification of resources                                                                                                                                             |
| electronicAccess/linkText                  | string          | the value of the MARC tag field 856 2nd indicator, where the values are: no information provided, resource, version of resource, related resource, no display constant generated                                                                             |
| electronicAccess/materialsSpecification    | string          | materials specified is used to specify to what portion or aspect of the resource the electronic location and access information applies (e.g. a portion or subset of the item is electronic, or a related electronic resource is being linked to the record) |
| electronicAccess/publicNote                | string          | URL public note to be displayed in the discovery                                                                                                                                                                                                             |
| electronicAccess/relationshipId            | string          | relationship between the electronic resource at the location identified and the item described in the record as a whole                                                                                                                                      |
| callNumberTypeId                           | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/     |
| callNumberPrefix                           | string          | Prefix of the call number on the holding level.                                                                                                                                                                                                              |
| callNumber                                 | string          | Call Number is an identifier assigned to an item, usually printed on a label attached to the item.                                                                                                                                                           |
| callNumberSuffix                           | string          | Suffix of the call number on the holding level.                                                                                                                                                                                                              |
| shelvingTitle                              | string          | Indicates the shelving form of title.                                                                                                                                                                                                                        |
| acquisitionFormat                          | string          | Format of holdings record acquisition                                                                                                                                                                                                                        |
| acquisitionMethod                          | string          | Method of holdings record acquisition                                                                                                                                                                                                                        |
| receiptStatus                              | string          | Receipt status (e.g. pending, awaiting receipt, partially received, fully received, receipt not required, and cancelled)                                                                                                                                     |
| administrativeNotes                        | array           | Administrative notes                                                                                                                                                                                                                                         |
| notes                                      | array           | Notes about action, copy, binding etc.                                                                                                                                                                                                                       |
| notes/holdingsNoteTypeId                   | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/     |
| notes/holdingsNoteType                     | object          | expanded note-type object corresponding to holdingsNoteTypeId                                                                                                                                                                                                |
| notes/note                                 | string          | Text content of the note                                                                                                                                                                                                                                     |
| notes/staffOnly                            | boolean         | If true, determines that the note should not be visible for others than staff                                                                                                                                                                                |
| illPolicyId                                | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/     |
| illPolicy                                  | object          | expanded ILL Policy object corresponding to illPolicyId                                                                                                                                                                                                      |
| retentionPolicy                            | string          | Records information regarding how long we have agreed to keep something.                                                                                                                                                                                     |
| digitizationPolicy                         | string          | Records information regarding digitization aspects.                                                                                                                                                                                                          |
| holdingsStatements                         | array           | Notes about action, copy, binding etc.                                                                                                                                                                                                                       |
| holdingsStatements/statement               | string          | Specifies the exact content to which the library has access, typically for continuing publications.                                                                                                                                                          |
| holdingsStatements/note                    | string          | Note attached to a holdings statement                                                                                                                                                                                                                        |
| holdingsStatements/staffNote               | string          | Private note attached to a holdings statment                                                                                                                                                                                                                 |
| holdingsStatementsForIndexes               | array           | Holdings record indexes statements                                                                                                                                                                                                                           |
| holdingsStatementsForIndexes/statement     | string          | Textual description of the holdings of indexes                                                                                                                                                                                                               |
| holdingsStatementsForIndexes/note          | string          | Note attached to a holdings statement                                                                                                                                                                                                                        |
| holdingsStatementsForIndexes/staffNote     | string          | Private note attached to a holdings statment                                                                                                                                                                                                                 |
| holdingsStatementsForSupplements           | array           | Holdings record supplements statements                                                                                                                                                                                                                       |
| holdingsStatementsForSupplements/statement | string          | textual description of the holdings of supplementary material                                                                                                                                                                                                |
| holdingsStatementsForSupplements/note      | string          | note attached to a holdings statement                                                                                                                                                                                                                        |
| holdingsStatementsForSupplements/staffNote | string          | Private note attached to a holdings statment                                                                                                                                                                                                                 |
| copyNumber                                 | string          | Item/Piece ID (usually barcode) for systems that do not use item records. Ability to designate the copy number if institution chooses to use copy numbers.                                                                                                   |
| numberOfItems                              | string          | Text (Number)                                                                                                                                                                                                                                                |
| receivingHistory                           | object          | Receiving history of holdings record                                                                                                                                                                                                                         |
| receivingHistory/displayType               | string          | Display hint. 1: Display fields separately. 2: Display fields concatenated                                                                                                                                                                                   |
| receivingHistory/entries                   | array           | Entries of receiving history                                                                                                                                                                                                                                 |
| receivingHistory/entries/publicDisplay     | boolean         | Defines if the receivingHistory should be visible to the public.                                                                                                                                                                                             |
| receivingHistory/entries/enumeration       | string          | This is the volume/issue number (e.g. v.71:no.6-2)                                                                                                                                                                                                           |
| receivingHistory/entries/chronology        | string          | Repeated element from Receiving history - Enumeration AND Receiving history - Chronology                                                                                                                                                                     |
| discoverySuppress                          | boolean         | records the fact that the record should not be displayed in a discovery system                                                                                                                                                                               |
| statisticalCodeIds                         | array           | List of statistical code IDs                                                                                                                                                                                                                                 |
| holdingsItems                              | array           | Items related to holdings record. This is a virtual field, accessible only when using mod-graphql.                                                                                                                                                           |
| bareHoldingsItems                          | array           | Items of bareHoldings. This is a virtual field, accessible only when using mod-graphql.                                                                                                                                                                      |
| holdingsInstance                           | object          | Instance of holding record. This is a virtual field, accessible only when using mod-graphql.                                                                                                                                                                 |
| tags                                       | object          | List of simple tags that can be added to an object                                                                                                                                                                                                           |
| tags/tagList                               | array           | List of tags                                                                                                                                                                                                                                                 |
| metadata                                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                                                                                                                                                           |
| metadata/createdDate                       | string          | Date and time when the record was created                                                                                                                                                                                                                    |
| metadata/createdByUserId                   | string          | ID of the user who created the record (when available)                                                                                                                                                                                                       |
| metadata/createdByUsername                 | string          | Username of the user who created the record (when available)                                                                                                                                                                                                 |
| metadata/updatedDate                       | string          | Date and time when the record was last updated                                                                                                                                                                                                               |
| metadata/updatedByUserId                   | string          | ID of the user who last updated the record (when available)                                                                                                                                                                                                  |
| metadata/updatedByUsername                 | string          | Username of the user who last updated the record (when available)                                                                                                                                                                                            |
| sourceId                                   | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/     |

## Documentation: [inventory_holdings_note_types](inventory_holdings_note_types.md)

### Source:

Module: mod-inventory-storage

Interface: /holdings-note-types

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          | unique ID of the holdings note type; a UUID                                                        |
| name                       | string          | name of the holdings note type                                                                     |
| source                     | string          | label indicating where the holdings note type entry originates from, i.e. 'folio' or 'local'       |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [inventory_holdings_sources](inventory_holdings_sources.md)

### Source:

Module: mod-inventory-storage

Interface: /holdings-sources

### Attributes:

| Property Name              | Property Type   | Property Description                                                                                                                                                                                                                                     |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id                         | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| name                       | string          | Name of the holdings records source                                                                                                                                                                                                                      |
| source                     | string          | The holdings records source                                                                                                                                                                                                                              |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                                                                                                                                                       |
| metadata/createdDate       | string          | Date and time when the record was created                                                                                                                                                                                                                |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                                                                                                                                                                                   |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                                                                                                                                                                             |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                                                                                                                                                                           |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                                                                                                                                                                              |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                                                                                                                                                                        |

## Documentation: [inventory_holdings_types](inventory_holdings_types.md)

### Source:

Module: mod-inventory-storage

Interface: /holdings-types

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          | unique ID of the holdings type; a UUID                                                             |
| name                       | string          | name of the holdings type                                                                          |
| source                     | string          | label indicating where the holdings type entry originates from, i.e. 'folio' or 'local'            |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [inventory_identifier_types](inventory_identifier_types.md)

### Source:

Module: mod-inventory-storage

Interface: /identifier-types

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          |                                                                                                    |
| name                       | string          | label for the identifier type                                                                      |
| source                     | string          | label indicating where the identifier type entry originates from, i.e. 'folio' or 'local'          |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [inventory_ill_policies](inventory_ill_policies.md)

### Source:

Module: mod-inventory-storage

Interface: /ill-policies

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          | unique ID of the ILL policy; UUID                                                                  |
| name                       | string          | name of the policy                                                                                 |
| source                     | string          | label indicating where the ILL policy entry originates from, i.e. 'folio' or 'local'               |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [inventory_instance_formats](inventory_instance_formats.md)

### Source:

Module: mod-inventory-storage

Interface: /instance-formats

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          |                                                                                                    |
| name                       | string          | label for the Instance format                                                                      |
| code                       | string          | distinct code for the Instance format                                                              |
| source                     | string          | origin of the Instance format record                                                               |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [inventory_instance_note_types](inventory_instance_note_types.md)

### Source:

Module: mod-inventory-storage

Interface: /instance-note-types

### Attributes:

| Property Name              | Property Type   | Property Description                                                                                                                                                                                                                                     |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id                         | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| name                       | string          | name of the Instance note type                                                                                                                                                                                                                           |
| source                     | string          | label indicating where the Instance note type entry originates from, i.e. 'folio' or 'local'                                                                                                                                                             |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                                                                                                                                                       |
| metadata/createdDate       | string          | Date and time when the record was created                                                                                                                                                                                                                |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                                                                                                                                                                                   |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                                                                                                                                                                             |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                                                                                                                                                                           |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                                                                                                                                                                              |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                                                                                                                                                                        |

## Documentation: [inventory_instance_relationship_types](inventory_instance_relationship_types.md)

### Source:

Module: mod-inventory-storage

Interface: /instance-relationship-types

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          |                                                                                                    |
| name                       | string          | label for the relationship type                                                                    |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [inventory_instance_relationships](inventory_instance_relationships.md)

### Source:

Module: mod-inventory-storage

Interface: /instance-storage/instance-relationships

### Attributes:

| Property Name              | Property Type   | Property Description                                                                                                                                                      |
|:---------------------------|:----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id                         | string          |                                                                                                                                                                           |
| superInstanceId            | string          | ID (a UUID) of the super-instance. References an Instance record                                                                                                          |
| subInstanceId              | string          | ID (a UUID) of the sub-instance. References an Instance record                                                                                                            |
| instanceRelationshipTypeId | string          | ID (a UUID) of the InstanceRelationshipType. References controlled vocabulary InstanceRelationshipTypes. Indicates the type of relationship between two Instance records. |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                                                                        |
| metadata/createdDate       | string          | Date and time when the record was created                                                                                                                                 |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                                                                                                    |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                                                                                              |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                                                                                            |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                                                                                               |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                                                                                         |

## Documentation: [inventory_instance_statuses](inventory_instance_statuses.md)

### Source:

Module: mod-inventory-storage

Interface: /instance-statuses

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          |                                                                                                    |
| code                       | string          | distinct code for an instance status                                                               |
| name                       | string          | label for the instance status                                                                      |
| source                     | string          | origin of an instance status record                                                                |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [inventory_instance_types](inventory_instance_types.md)

### Source:

Module: mod-inventory-storage

Interface: /instance-types

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          |                                                                                                    |
| name                       | string          | label for the resource type                                                                        |
| code                       | string          | distinct code for the resource type                                                                |
| source                     |                 | origin of a resource type record                                                                   |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [inventory_instances](inventory_instances.md)

### Source:

Module: mod-inventory-storage

Interface: /instance-storage/instances

### Attributes:

| Property Name                            | Property Type   | Property Description                                                                                                                                                                                                                                                                                                                                 |
|:-----------------------------------------|:----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id                                       | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/                                                                                             |
| _version                                 | integer         | Record version for optimistic locking                                                                                                                                                                                                                                                                                                                |
| hrid                                     | string          | The human readable ID, also called eye readable ID. A system-assigned sequential ID which maps to the Instance ID                                                                                                                                                                                                                                    |
| matchKey                                 | string          | A unique instance identifier matching a client-side bibliographic record identification scheme, in particular for a scenario where multiple separate catalogs with no shared record identifiers contribute to the same Instance in Inventory. A match key is typically generated from select, normalized pieces of metadata in bibliographic records |
| source                                   | string          | The metadata source and its format of the underlying record to the instance record. (e.g. FOLIO if it's a record created in Inventory; MARC if it's a MARC record created in MARCcat or EPKB if it's a record coming from eHoldings; CONSORTIUM-MARC or CONSORTIUM-FOLIO for sharing Instances).                                                     |
| title                                    | string          | The primary title (or label) associated with the resource                                                                                                                                                                                                                                                                                            |
| indexTitle                               | string          | Title normalized for browsing and searching; based on the title with articles removed                                                                                                                                                                                                                                                                |
| alternativeTitles                        | array           | List of alternative titles for the resource (e.g. original language version title of a movie)                                                                                                                                                                                                                                                        |
| alternativeTitles/alternativeTitleTypeId | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/                                                                                             |
| alternativeTitles/alternativeTitle       | string          | An alternative title for the resource                                                                                                                                                                                                                                                                                                                |
| alternativeTitles/authorityId            | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/                                                                                             |
| editions                                 | array           | The edition statement, imprint and other publication source information                                                                                                                                                                                                                                                                              |
| series                                   | array           | List of series titles associated with the resource (e.g. Harry Potter)                                                                                                                                                                                                                                                                               |
| series/value                             | string          | Series title value                                                                                                                                                                                                                                                                                                                                   |
| series/authorityId                       | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/                                                                                             |
| identifiers                              | array           | An extensible set of name-value pairs of identifiers associated with the resource                                                                                                                                                                                                                                                                    |
| identifiers/value                        | string          | Resource identifier value                                                                                                                                                                                                                                                                                                                            |
| identifiers/identifierTypeId             | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/                                                                                             |
| identifiers/identifierTypeObject         | object          | Information about identifier type, looked up from identifierTypeId                                                                                                                                                                                                                                                                                   |
| contributors                             | array           | List of contributors                                                                                                                                                                                                                                                                                                                                 |
| contributors/name                        | string          | Personal name, corporate name, meeting name                                                                                                                                                                                                                                                                                                          |
| contributors/contributorTypeId           | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/                                                                                             |
| contributors/contributorTypeText         | string          | Free text element for adding contributor type terms other that defined by the MARC code list for relators                                                                                                                                                                                                                                            |
| contributors/contributorNameTypeId       | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/                                                                                             |
| contributors/authorityId                 | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/                                                                                             |
| contributors/contributorNameType         | object          | Dereferenced contributor-name type                                                                                                                                                                                                                                                                                                                   |
| contributors/primary                     | boolean         | Whether this is the primary contributor                                                                                                                                                                                                                                                                                                              |
| subjects                                 | array           | List of subject headings                                                                                                                                                                                                                                                                                                                             |
| subjects/value                           | string          | Subject heading value                                                                                                                                                                                                                                                                                                                                |
| subjects/authorityId                     | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/                                                                                             |
| classifications                          | array           | List of classifications                                                                                                                                                                                                                                                                                                                              |
| classifications/classificationNumber     | string          | Classification (e.g. classification scheme, classification schedule)                                                                                                                                                                                                                                                                                 |
| classifications/classificationTypeId     | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/                                                                                             |
| classifications/classificationType       | object          | Dereferenced classification schema                                                                                                                                                                                                                                                                                                                   |
| publication                              | array           | List of publication items                                                                                                                                                                                                                                                                                                                            |
| publication/publisher                    | string          | Name of publisher, distributor, etc.                                                                                                                                                                                                                                                                                                                 |
| publication/place                        | string          | Place of publication, distribution, etc.                                                                                                                                                                                                                                                                                                             |
| publication/dateOfPublication            | string          | Date (year YYYY) of publication, distribution, etc.                                                                                                                                                                                                                                                                                                  |
| publication/role                         | string          | The role of the publisher, distributor, etc.                                                                                                                                                                                                                                                                                                         |
| publicationFrequency                     | array           | List of intervals at which a serial appears (e.g. daily, weekly, monthly, quarterly, etc.)                                                                                                                                                                                                                                                           |
| publicationRange                         | array           | The range of sequential designation/chronology of publication, or date range                                                                                                                                                                                                                                                                         |
| publicationPeriod                        | object          | Publication period                                                                                                                                                                                                                                                                                                                                   |
| publicationPeriod/start                  | integer         | Publication start year                                                                                                                                                                                                                                                                                                                               |
| publicationPeriod/end                    | integer         | Publication end year                                                                                                                                                                                                                                                                                                                                 |
| electronicAccess                         | array           | List of electronic access items                                                                                                                                                                                                                                                                                                                      |
| electronicAccess/uri                     | string          | uniform resource identifier (URI) is a string of characters designed for unambiguous identification of resources                                                                                                                                                                                                                                     |
| electronicAccess/linkText                | string          | The value of the MARC tag field 856 2nd indicator, where the values are: no information provided, resource, version of resource, related resource, no display constant generated                                                                                                                                                                     |
| electronicAccess/materialsSpecification  | string          | Materials specified is used to specify to what portion or aspect of the resource the electronic location and access information applies (e.g. a portion or subset of the item is electronic, or a related electronic resource is being linked to the record)                                                                                         |
| electronicAccess/publicNote              | string          | URL public note to be displayed in the discovery                                                                                                                                                                                                                                                                                                     |
| electronicAccess/relationshipId          | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/                                                                                             |
| instanceTypeId                           | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/                                                                                             |
| instanceFormatIds                        | array           | UUIDs for the unique terms for the format whether it's from the RDA carrier term list of locally defined                                                                                                                                                                                                                                             |
| instanceFormats                          | array           | List of dereferenced instance formats                                                                                                                                                                                                                                                                                                                |
| physicalDescriptions                     | array           | Physical description of the described resource, including its extent, dimensions, and such other physical details as a description of any accompanying materials and unit type and size                                                                                                                                                              |
| languages                                | array           | The set of languages used by the resource                                                                                                                                                                                                                                                                                                            |
| notes                                    | array           | Bibliographic notes (e.g. general notes, specialized notes)                                                                                                                                                                                                                                                                                          |
| notes/instanceNoteTypeId                 | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/                                                                                             |
| notes/note                               | string          | Text content of the note                                                                                                                                                                                                                                                                                                                             |
| notes/staffOnly                          | boolean         | If true, determines that the note should not be visible for others than staff                                                                                                                                                                                                                                                                        |
| administrativeNotes                      | array           | Administrative notes                                                                                                                                                                                                                                                                                                                                 |
| modeOfIssuanceId                         | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/                                                                                             |
| catalogedDate                            | string          | Date or timestamp on an instance for when is was considered cataloged                                                                                                                                                                                                                                                                                |
| previouslyHeld                           | boolean         | Records the fact that the resource was previously held by the library for things like Hathi access, etc.                                                                                                                                                                                                                                             |
| staffSuppress                            | boolean         | Records the fact that the record should not be displayed for others than catalogers                                                                                                                                                                                                                                                                  |
| discoverySuppress                        | boolean         | Records the fact that the record should not be displayed in a discovery system                                                                                                                                                                                                                                                                       |
| statisticalCodeIds                       | array           | List of statistical code IDs                                                                                                                                                                                                                                                                                                                         |
| sourceRecordFormat                       | string          | Format of the instance source record, if a source record exists (e.g. FOLIO if it's a record created in Inventory,  MARC if it's a MARC record created in MARCcat or EPKB if it's a record coming from eHoldings)                                                                                                                                    |
| statusId                                 | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/                                                                                             |
| statusUpdatedDate                        | string          | Date [or timestamp] for when the instance status was updated                                                                                                                                                                                                                                                                                         |
| tags                                     | object          | List of simple tags that can be added to an object                                                                                                                                                                                                                                                                                                   |
| tags/tagList                             | array           | List of tags                                                                                                                                                                                                                                                                                                                                         |
| metadata                                 | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                                                                                                                                                                                                                                                   |
| metadata/createdDate                     | string          | Date and time when the record was created                                                                                                                                                                                                                                                                                                            |
| metadata/createdByUserId                 | string          | ID of the user who created the record (when available)                                                                                                                                                                                                                                                                                               |
| metadata/createdByUsername               | string          | Username of the user who created the record (when available)                                                                                                                                                                                                                                                                                         |
| metadata/updatedDate                     | string          | Date and time when the record was last updated                                                                                                                                                                                                                                                                                                       |
| metadata/updatedByUserId                 | string          | ID of the user who last updated the record (when available)                                                                                                                                                                                                                                                                                          |
| metadata/updatedByUsername               | string          | Username of the user who last updated the record (when available)                                                                                                                                                                                                                                                                                    |
| holdingsRecords2                         | array           | List of holdings records                                                                                                                                                                                                                                                                                                                             |
| natureOfContentTermIds                   | array           | Array of UUID for the Instance nature of content (e.g. bibliography, biography, exhibition catalogue, festschrift, newspaper, proceedings, research report, thesis or website)                                                                                                                                                                       |

## Documentation: [inventory_institutions](inventory_institutions.md)

### Source:

Module: mod-inventory-storage

Interface: /location-units/institutions

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          |                                                                                                    |
| name                       | string          | name of location                                                                                   |
| code                       | string          | distinct code for location                                                                         |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [inventory_item_damaged_statuses](inventory_item_damaged_statuses.md)

### Source:

Module: mod-inventory-storage

Interface: /item-damaged-statuses

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          | unique ID of the item damage status; a UUID                                                        |
| name                       | string          | name of the item damage status                                                                     |
| source                     | string          | label indicating where the item damage status entry originates from, i.e. 'folio' or 'local'       |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [inventory_item_note_types](inventory_item_note_types.md)

### Source:

Module: mod-inventory-storage

Interface: /item-note-types

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          | unique ID of the item note type; a UUID                                                            |
| name                       | string          | name of the item note type                                                                         |
| source                     | string          | label indicating where the item note type entry originates from, i.e. 'folio' or 'local'           |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [inventory_items](inventory_items.md)

### Source:

Module: mod-inventory-storage

Interface: /item-storage/items

### Attributes:

| Property Name                              | Property Type   | Property Description                                                                                                                                                                                                                                                    |
|:-------------------------------------------|:----------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id                                         | string          | Unique ID of the item record                                                                                                                                                                                                                                            |
| _version                                   | integer         | Record version for optimistic locking                                                                                                                                                                                                                                   |
| hrid                                       | string          | The human readable ID, also called eye readable ID. A system-assigned sequential alternate ID                                                                                                                                                                           |
| holdingsRecordId                           | string          | ID of the holdings record the item is a member of.                                                                                                                                                                                                                      |
| formerIds                                  | array           | Previous identifiers assigned to the item                                                                                                                                                                                                                               |
| discoverySuppress                          | boolean         | Records the fact that the record should not be displayed in a discovery system                                                                                                                                                                                          |
| accessionNumber                            | string          | Also called inventar number                                                                                                                                                                                                                                             |
| barcode                                    | string          | Unique inventory control number for physical resources, used largely for circulation purposes                                                                                                                                                                           |
| effectiveShelvingOrder                     | string          | A system generated normalization of the call number that allows for call number sorting in reports and search results                                                                                                                                                   |
| itemLevelCallNumber                        | string          | Call Number is an identifier assigned to an item, usually printed on a label attached to the item. The call number is used to determine the items physical position in a shelving sequence, e.g. K1 .M44. The Item level call number, is the call number on item level. |
| itemLevelCallNumberPrefix                  | string          | Prefix of the call number on the item level.                                                                                                                                                                                                                            |
| itemLevelCallNumberSuffix                  | string          | Suffix of the call number on the item level.                                                                                                                                                                                                                            |
| itemLevelCallNumberTypeId                  | string          | Identifies the source of the call number, e.g., LCC, Dewey, NLM, etc.                                                                                                                                                                                                   |
| effectiveCallNumberComponents              | object          | Elements of a full call number generated from the item or holding                                                                                                                                                                                                       |
| effectiveCallNumberComponents/callNumber   | string          | Effective Call Number is an identifier assigned to an item or its holding and associated with the item.                                                                                                                                                                 |
| effectiveCallNumberComponents/prefix       | string          | Effective Call Number Prefix is the prefix of the identifier assigned to an item or its holding and associated with the item.                                                                                                                                           |
| effectiveCallNumberComponents/suffix       | string          | Effective Call Number Suffix is the suffix of the identifier assigned to an item or its holding and associated with the item.                                                                                                                                           |
| effectiveCallNumberComponents/typeId       | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/                |
| volume                                     | string          | Volume is intended for monographs when a multipart monograph (e.g. a biography of George Bernard Shaw in three volumes).                                                                                                                                                |
| enumeration                                | string          | Enumeration is the descriptive information for the numbering scheme of a serial.                                                                                                                                                                                        |
| chronology                                 | string          | Chronology is the descriptive information for the dating scheme of a serial.                                                                                                                                                                                            |
| yearCaption                                | array           | In multipart monographs, a caption is a character(s) used to label a level of chronology, e.g., year 1985.                                                                                                                                                              |
| itemIdentifier                             | string          | Item identifier number, e.g. imported from the union catalogue (read only).                                                                                                                                                                                             |
| copyNumber                                 | string          | Copy number is the piece identifier. The copy number reflects if the library has a copy of a single-volume monograph; one copy of a multi-volume, (e.g. Copy 1, or C.7.)                                                                                                |
| numberOfPieces                             | string          | Number of pieces. Used when an item is checked out or returned to verify that all parts are present (e.g. 7 CDs in a set).                                                                                                                                              |
| descriptionOfPieces                        | string          | Description of item pieces.                                                                                                                                                                                                                                             |
| numberOfMissingPieces                      | string          | Number of missing pieces.                                                                                                                                                                                                                                               |
| missingPieces                              | string          | Description of the missing pieces.                                                                                                                                                                                                                                      |
| missingPiecesDate                          | string          | Date when the piece(s) went missing.                                                                                                                                                                                                                                    |
| itemDamagedStatusId                        | string          | Item dame status id identifier.                                                                                                                                                                                                                                         |
| itemDamagedStatusDate                      | string          | Date and time when the item was damaged.                                                                                                                                                                                                                                |
| administrativeNotes                        | array           | Administrative notes                                                                                                                                                                                                                                                    |
| notes                                      | array           | Notes about action, copy, binding etc.                                                                                                                                                                                                                                  |
| notes/itemNoteTypeId                       | string          | ID of the type of note                                                                                                                                                                                                                                                  |
| notes/itemNoteType                         | object          | Type of item's note                                                                                                                                                                                                                                                     |
| notes/note                                 | string          | Text content of the note                                                                                                                                                                                                                                                |
| notes/staffOnly                            | boolean         | If true, determines that the note should not be visible for others than staff                                                                                                                                                                                           |
| circulationNotes                           | array           | Notes to be displayed in circulation processes                                                                                                                                                                                                                          |
| circulationNotes/id                        | string          | The id of the circulation note                                                                                                                                                                                                                                          |
| circulationNotes/noteType                  | string          | Type of circulation process that the note applies to                                                                                                                                                                                                                    |
| circulationNotes/note                      | string          | Text to display                                                                                                                                                                                                                                                         |
| circulationNotes/source                    | object          | The user who added/updated the note. The property is generated by the server and needed to support sorting. Points to /users/{id} resource.                                                                                                                             |
| circulationNotes/source/id                 | string          | The id of the user who added/updated the note. The user information is generated by the server and needed to support sorting. Points to /users/{id} resource.                                                                                                           |
| circulationNotes/source/personal           | object          | Personal information about the user                                                                                                                                                                                                                                     |
| circulationNotes/source/personal/lastName  | string          | The user's last name                                                                                                                                                                                                                                                    |
| circulationNotes/source/personal/firstName | string          | The user's first name                                                                                                                                                                                                                                                   |
| circulationNotes/date                      | string          | Date and time the record is added/updated. The property is generated by the server and needed to support sorting.                                                                                                                                                       |
| circulationNotes/staffOnly                 | boolean         | Flag to restrict display of this note                                                                                                                                                                                                                                   |
| status                                     | object          | The status of the item                                                                                                                                                                                                                                                  |
| status/name                                | string          | Name of the status e.g. Available, Checked out, In transit                                                                                                                                                                                                              |
| status/date                                | string          | Date and time when the status was last changed                                                                                                                                                                                                                          |
| materialTypeId                             | string          | Material type, term. Define what type of thing the item is.                                                                                                                                                                                                             |
| materialType                               | object          | Item's material type                                                                                                                                                                                                                                                    |
| permanentLoanTypeId                        | string          | The permanent loan type, is the default loan type for a given item. Loan types are tenant-defined.                                                                                                                                                                      |
| temporaryLoanTypeId                        | string          | Temporary loan type, is the temporary loan type for a given item.                                                                                                                                                                                                       |
| permanentLocationId                        | string          | Permanent item location is the default location, shelving location, or holding which is a physical place where items are stored, or an Online location.                                                                                                                 |
| permanentLocation                          | object          | The permanent shelving location in which an item resides                                                                                                                                                                                                                |
| temporaryLocationId                        | string          | Temporary item location is the temporarily location, shelving location, or holding which is a physical place where items are stored, or an Online location.                                                                                                             |
| temporaryLocation                          | object          | Temporary location, shelving location, or holding which is a physical place where items are stored, or an Online location                                                                                                                                               |
| effectiveLocationId                        | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/                |
| electronicAccess                           | array           | References for accessing the item by URL.                                                                                                                                                                                                                               |
| electronicAccess/uri                       | string          | uniform resource identifier (URI) is a string of characters designed for unambiguous identification of resources                                                                                                                                                        |
| electronicAccess/linkText                  | string          | the value of the MARC tag field 856 2nd indicator, where the values are: no information provided, resource, version of resource, related resource, no display constant generated                                                                                        |
| electronicAccess/materialsSpecification    | string          | materials specified is used to specify to what portion or aspect of the resource the electronic location and access information applies (e.g. a portion or subset of the item is electronic, or a related electronic resource is being linked to the record)            |
| electronicAccess/publicNote                | string          | URL public note to be displayed in the discovery                                                                                                                                                                                                                        |
| electronicAccess/relationshipId            | string          | relationship between the electronic resource at the location identified and the item described in the record as a whole                                                                                                                                                 |
| inTransitDestinationServicePointId         | string          | Service point an item is intended to be transited to (should only be present when in transit)                                                                                                                                                                           |
| statisticalCodeIds                         | array           | List of statistical code IDs                                                                                                                                                                                                                                            |
| purchaseOrderLineIdentifier                | string          | ID referencing a remote purchase order object related to this item                                                                                                                                                                                                      |
| tags                                       | object          | List of simple tags that can be added to an object                                                                                                                                                                                                                      |
| tags/tagList                               | array           | List of tags                                                                                                                                                                                                                                                            |
| metadata                                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                                                                                                                                                                      |
| metadata/createdDate                       | string          | Date and time when the record was created                                                                                                                                                                                                                               |
| metadata/createdByUserId                   | string          | ID of the user who created the record (when available)                                                                                                                                                                                                                  |
| metadata/createdByUsername                 | string          | Username of the user who created the record (when available)                                                                                                                                                                                                            |
| metadata/updatedDate                       | string          | Date and time when the record was last updated                                                                                                                                                                                                                          |
| metadata/updatedByUserId                   | string          | ID of the user who last updated the record (when available)                                                                                                                                                                                                             |
| metadata/updatedByUsername                 | string          | Username of the user who last updated the record (when available)                                                                                                                                                                                                       |
| holdingsRecord2                            | object          | Fake property for mod-graphql to determine record relationships.                                                                                                                                                                                                        |
| lastCheckIn                                | object          | Information about when an item was last scanned in the Inventory app.                                                                                                                                                                                                   |
| lastCheckIn/dateTime                       | string          | Date and time of the last check in of the item.                                                                                                                                                                                                                         |
| lastCheckIn/servicePointId                 | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/                |
| lastCheckIn/staffMemberId                  | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/                |

## Documentation: [inventory_libraries](inventory_libraries.md)

### Source:

Module: mod-inventory-storage

Interface: /location-units/libraries

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          |                                                                                                    |
| name                       | string          | name of the location                                                                               |
| code                       | string          | distinct code for the location                                                                     |
| campusId                   | string          | ID of the second-level location unit that the third-level unit belongs to                          |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [inventory_loan_types](inventory_loan_types.md)

### Source:

Module: mod-inventory-storage

Interface: /loan-types

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          |                                                                                                    |
| name                       | string          | label for the loan type                                                                            |
| source                     | string          | Origin of the loan type record, e.g. 'System', 'User', 'Consortium' etc.                           |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [inventory_locations](inventory_locations.md)

### Source:

Module: mod-inventory-storage

Interface: /locations

### Attributes:

| Property Name                                                  | Property Type   | Property Description                                                                               |
|:---------------------------------------------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                                                             | string          | id of this (shelf) location record as UUID.                                                        |
| name                                                           | string          | Name of the (shelf) location                                                                       |
| code                                                           | string          | Code of the (shelf) location, usually an abbreviation of the name.                                 |
| description                                                    | string          | Description of the (shelf) location.                                                               |
| discoveryDisplayName                                           | string          | Name of the (shelf) location to be shown in the discovery.                                         |
| isActive                                                       | boolean         | Whether this (shelf) location is active. Inactive (shelf) locations can no longer been used.       |
| institutionId                                                  | string          | The UUID of the institution, the first-level location unit, this (shelf) location belongs to.      |
| institution                                                    | object          | The institution, the first-level location unit, this (shelf) location belongs to.                  |
| campusId                                                       | string          | The UUID of the campus, the second-level location unit, this (shelf) location belongs to.          |
| campus                                                         | object          | The campus, the second-level location unit, this (shelf) location belongs to                       |
| libraryId                                                      | string          | The UUID of the library, the third-level location unit, this (shelf) location belongs to.          |
| library                                                        | object          | The library, the third-level location unit, this (shelf) location belongs to.                      |
| details                                                        | object          | Details about this (shelf) location.                                                               |
| primaryServicePoint                                            | string          | The UUID of the primary service point of this (shelf) location.                                    |
| primaryServicePointObject                                      | object          | A service point                                                                                    |
| primaryServicePointObject/id                                   | string          | Id of service-point object                                                                         |
| primaryServicePointObject/name                                 | string          | service-point name, a required field                                                               |
| primaryServicePointObject/code                                 | string          | service-point code, a required field                                                               |
| primaryServicePointObject/discoveryDisplayName                 | string          | display name, a required field                                                                     |
| primaryServicePointObject/description                          | string          | description of the service-point                                                                   |
| primaryServicePointObject/shelvingLagTime                      | integer         | shelving lag time                                                                                  |
| primaryServicePointObject/pickupLocation                       | boolean         | indicates whether or not the service point is a pickup location                                    |
| primaryServicePointObject/holdShelfExpiryPeriod                | object          | schema for time-period, which contains time interval 'duration' and the time unit                  |
| primaryServicePointObject/holdShelfExpiryPeriod/duration       | integer         | Duration interval                                                                                  |
| primaryServicePointObject/holdShelfExpiryPeriod/intervalId     | string          | Unit of time for the duration                                                                      |
| primaryServicePointObject/holdShelfClosedLibraryDateManagement | string          | enum for closedLibraryDateManagement associated with hold shelf                                    |
| primaryServicePointObject/staffSlips                           | array           | List of staff slips for this service point                                                         |
| primaryServicePointObject/staffSlips/id                        | string          | The ID of the staff slip                                                                           |
| primaryServicePointObject/staffSlips/printByDefault            | boolean         | Whether or not to print the staff slip by default                                                  |
| primaryServicePointObject/metadata                             | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| primaryServicePointObject/metadata/createdDate                 | string          | Date and time when the record was created                                                          |
| primaryServicePointObject/metadata/createdByUserId             | string          | ID of the user who created the record (when available)                                             |
| primaryServicePointObject/metadata/createdByUsername           | string          | Username of the user who created the record (when available)                                       |
| primaryServicePointObject/metadata/updatedDate                 | string          | Date and time when the record was last updated                                                     |
| primaryServicePointObject/metadata/updatedByUserId             | string          | ID of the user who last updated the record (when available)                                        |
| primaryServicePointObject/metadata/updatedByUsername           | string          | Username of the user who last updated the record (when available)                                  |
| servicePointIds                                                | array           | All service points that this (shelf) location has.                                                 |
| servicePoints                                                  | array           | List of dereferenced service points                                                                |
| metadata                                                       | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate                                           | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId                                       | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername                                     | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate                                           | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId                                       | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername                                     | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [inventory_material_types](inventory_material_types.md)

### Source:

Module: mod-inventory-storage

Interface: /material-types

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          |                                                                                                    |
| name                       | string          | label for the material type                                                                        |
| source                     | string          | origin of the material type record                                                                 |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [inventory_modes_of_issuance](inventory_modes_of_issuance.md)

### Source:

Module: mod-inventory-storage

Interface: /modes-of-issuance

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          |                                                                                                    |
| name                       | string          | label for the mode of issuance                                                                     |
| source                     | string          | label indicating where the mode of issuance entry originates from, i.e. 'rdamodeissue' or 'local'  |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [inventory_nature_of_content_terms](inventory_nature_of_content_terms.md)

### Source:

Module: mod-inventory-storage

Interface: /nature-of-content-terms

### Attributes:

| Property Name              | Property Type   | Property Description                                                                                                                                                                                                                                     |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id                         | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| name                       | string          | term for the nature of content                                                                                                                                                                                                                           |
| source                     | string          | label indicating where the term originates from, i.e. 'folio' or 'local'                                                                                                                                                                                 |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                                                                                                                                                       |
| metadata/createdDate       | string          | Date and time when the record was created                                                                                                                                                                                                                |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                                                                                                                                                                                   |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                                                                                                                                                                             |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                                                                                                                                                                           |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                                                                                                                                                                              |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                                                                                                                                                                        |

## Documentation: [inventory_service_points](inventory_service_points.md)

### Source:

Module: mod-inventory-storage

Interface: /service-points

### Attributes:

| Property Name                        | Property Type   | Property Description                                                                               |
|:-------------------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                                   | string          | Id of service-point object                                                                         |
| name                                 | string          | service-point name, a required field                                                               |
| code                                 | string          | service-point code, a required field                                                               |
| discoveryDisplayName                 | string          | display name, a required field                                                                     |
| description                          | string          | description of the service-point                                                                   |
| shelvingLagTime                      | integer         | shelving lag time                                                                                  |
| pickupLocation                       | boolean         | indicates whether or not the service point is a pickup location                                    |
| holdShelfExpiryPeriod                | object          | schema for time-period, which contains time interval 'duration' and the time unit                  |
| holdShelfExpiryPeriod/duration       | integer         | Duration interval                                                                                  |
| holdShelfExpiryPeriod/intervalId     | string          | Unit of time for the duration                                                                      |
| holdShelfClosedLibraryDateManagement | string          | enum for closedLibraryDateManagement associated with hold shelf                                    |
| staffSlips                           | array           | List of staff slips for this service point                                                         |
| staffSlips/id                        | string          | The ID of the staff slip                                                                           |
| staffSlips/printByDefault            | boolean         | Whether or not to print the staff slip by default                                                  |
| metadata                             | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate                 | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId             | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername           | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate                 | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId             | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername           | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [inventory_service_points_users](inventory_service_points_users.md)

### Source:

Module: mod-inventory-storage

Interface: /service-points-users

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          | The id of record as a UUID.                                                                        |
| userId                     | string          | Id of the user as a UUID.                                                                          |
| servicePointsIds           | array           | The list of service points a user is allowed to work at.                                           |
| defaultServicePointId      | string          | The id of the user's default service point as UUID.                                                |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [inventory_statistical_code_types](inventory_statistical_code_types.md)

### Source:

Module: mod-inventory-storage

Interface: /statistical-code-types

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          | unique ID of the statistical code type; a UUID                                                     |
| name                       | string          | name of a statistical code type                                                                    |
| source                     | string          | label indicating where the statistical code type entry originates from, i.e. 'folio' or 'local'    |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [inventory_statistical_codes](inventory_statistical_codes.md)

### Source:

Module: mod-inventory-storage

Interface: /statistical-codes

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          | unique ID of the statistical code; a UUID                                                          |
| code                       | string          | statistical code; a distinct label                                                                 |
| name                       | string          | name or description of a statistical code                                                          |
| statisticalCodeTypeId      | string          | a UUID referencing a statistical code type                                                         |
| source                     |                 | label indicating where the statistical code originates from, i.e. 'folio' or 'local'               |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [invoice_invoices](invoice_invoices.md)

### Source:

Module: mod-invoice-storage

Interface: /invoice-storage/invoices

### Attributes:

| Property Name              | Property Type   | Property Description                                                                                                                                                                                                                                                                                     |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id                         | string          | The UUID format string                                                                                                                                                                                                                                                                                   |
| accountingCode             | string          | Number that represents the vendor is an external accounting system which may include details like "Address code" in it. This is the number as stated on the invoice                                                                                                                                      |
| adjustments                | array           | List of invoice level adjustments. The adjustments can be pro-rated which are defined at the invoice level, but are applied to the invoice lines. A generic example is a shipping fee which should be spread out across all of the invoice lines so that all funds involved pay some portion of the fee. |
| adjustmentsTotal           | number          | Total amount which is sum of all invoice line adjustments and all non-prorated invoice level adjustments. This amount is always calculated by system.                                                                                                                                                    |
| approvedBy                 | string          | The UUID format string                                                                                                                                                                                                                                                                                   |
| approvalDate               | string          | Date the invoice was approved for processing                                                                                                                                                                                                                                                             |
| batchGroupId               | string          | UUID of the batch group to use when generating batch vouchers                                                                                                                                                                                                                                            |
| billTo                     | string          | The UUID format string                                                                                                                                                                                                                                                                                   |
| chkSubscriptionOverlap     | boolean         | IF TRUE the system will check if there is another invoice for this subscription and whether the dates overlap. IF the dates overlap, the system should issue an alert.                                                                                                                                   |
| cancellationNote           | string          | The reason of the invoice cancellation.                                                                                                                                                                                                                                                                  |
| currency                   | string          | Ideally this is the ISO code and not something the user defines                                                                                                                                                                                                                                          |
| enclosureNeeded            | boolean         | Indicates that an enclosure is needed                                                                                                                                                                                                                                                                    |
| exchangeRate               | number          | Exchange rate                                                                                                                                                                                                                                                                                            |
| exportToAccounting         | boolean         | This would keep the invoice from being feed into the batch process (i.e. not generate an external voucher/payment) but would still move values in the system. This might be defined by the vendor relationship and exposed for override on the invoice.                                                  |
| folioInvoiceNo             | string          | Invoice number in folio system                                                                                                                                                                                                                                                                           |
| invoiceDate                | string          | Invoice date                                                                                                                                                                                                                                                                                             |
| lockTotal                  | number          | Total amount which manually set by user. The calculated total must match this before the invoice can be approved                                                                                                                                                                                         |
| note                       | string          | Invoice note                                                                                                                                                                                                                                                                                             |
| paymentDue                 | string          | When this is required to be paid. Generally governed by the relationship with the Vendor                                                                                                                                                                                                                 |
| paymentDate                | string          | When the invoice was actually paid                                                                                                                                                                                                                                                                       |
| paymentTerms               | string          | Invoice payment terms                                                                                                                                                                                                                                                                                    |
| paymentMethod              | string          | Inherited from vendor record                                                                                                                                                                                                                                                                             |
| status                     | string          | Open: Record has been created, Reviewed: details have been verified, Approved: Funds are release, Paid: confirmation that funds have been exchanged and check number has been returned amounts are frozen, cancelled.                                                                                    |
|                            |                 | Note: invoices are never partially paid.                                                                                                                                                                                                                                                                 |
| source                     | string          | This does not denote a user ID but describes how the record was created. Eg. User, API, EDI                                                                                                                                                                                                              |
| subTotal                   | number          | Invoice amount before adjustments are applied. This is sum of all subTotal amounts of the corresponding invoice lines. This amount is always calculated by system.                                                                                                                                       |
| total                      | number          | The total amount is calculated "on the fly" of this invoice which is sum of subTotal and adjustmentsTotal. Must be the same with existed "lockTotal", when approve invoice.                                                                                                                              |
| vendorInvoiceNo            | string          | This is the number from the vendor's invoice, which is different from the folioInvoiceNo                                                                                                                                                                                                                 |
| disbursementNumber         | string          | The identifier for the physical transaction corresponding to a payment (Eg. Check #, EFT # etc.) Brought in from external source                                                                                                                                                                         |
| voucherNumber              | string          | Number generated by folio that will eventually identify the payment request sent out to external financial system.                                                                                                                                                                                       |
| paymentId                  | string          | The UUID format string                                                                                                                                                                                                                                                                                   |
| disbursementDate           | string          | Date payment was made from financial system (eg. corresponding check date)                                                                                                                                                                                                                               |
| poNumbers                  | array           | May or may not be provided; references the PO associated to the invoice                                                                                                                                                                                                                                  |
| vendorId                   | string          | The UUID format string                                                                                                                                                                                                                                                                                   |
| fiscalYearId               | string          | The UUID format string                                                                                                                                                                                                                                                                                   |
| accountNo                  | string          | The unique number of the organization account                                                                                                                                                                                                                                                            |
| manualPayment              | boolean         | This would keep the invoice from being feed into the batch process (Not generate a external voucher/payment) but would still move values in the system. Note: this is ideally defined by the vendor relationship and exposed for override on the invoice.                                                |
| acqUnitIds                 | array           | acquisition unit ids associated with this invoice                                                                                                                                                                                                                                                        |
| nextInvoiceLineNumber      | integer         | Number that will be used next time an invoice line is created                                                                                                                                                                                                                                            |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                                                                                                                                                                                                       |
| metadata/createdDate       | string          | Date and time when the record was created                                                                                                                                                                                                                                                                |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                                                                                                                                                                                                                                   |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                                                                                                                                                                                                                             |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                                                                                                                                                                                                                           |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                                                                                                                                                                                                                              |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                                                                                                                                                                                                                        |
| tags                       | object          | List of simple tags that can be added to an object                                                                                                                                                                                                                                                       |
| tags/tagList               | array           | List of tags                                                                                                                                                                                                                                                                                             |

## Documentation: [invoice_lines](invoice_lines.md)

### Source:

Module: mod-invoice-storage

Interface: /invoice-storage/invoice-lines

### Attributes:

| Property Name              | Property Type   | Property Description                                                                                                                                                                                                                                                                  |
|:---------------------------|:----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id                         | string          | The UUID format string                                                                                                                                                                                                                                                                |
| accountingCode             | string          | Pulled based on account number.                                                                                                                                                                                                                                                       |
| accountNumber              | string          | Account number that the vendor assigned                                                                                                                                                                                                                                               |
| adjustments                | array           | Defined in settings - the amount field will be editable and pro-rate toggle will be editable if enabled for that adjustment                                                                                                                                                           |
| adjustmentsTotal           | number          | Sum of all invoice line adjustments. This amount is always calculated by system.                                                                                                                                                                                                      |
| comment                    | string          | Free form commentary                                                                                                                                                                                                                                                                  |
| description                | string          | Title as captured in the Purchase Order Line. In the absence of a POL link this could be used to describe the POL                                                                                                                                                                     |
| fundDistributions          | array           | List of fund distributions                                                                                                                                                                                                                                                            |
| invoiceId                  | string          | The UUID format string                                                                                                                                                                                                                                                                |
| invoiceLineNumber          | string          | Sequentially generated and not editable by the user.                                                                                                                                                                                                                                  |
| invoiceLineStatus          | string          | Invoice line status                                                                                                                                                                                                                                                                   |
| poLineId                   | string          | The UUID format string                                                                                                                                                                                                                                                                |
| productId                  | string          | product identifier                                                                                                                                                                                                                                                                    |
| productIdType              | string          | The UUID corresponding to the type of product id                                                                                                                                                                                                                                      |
| quantity                   | integer         | quantity                                                                                                                                                                                                                                                                              |
| releaseEncumbrance         | boolean         | This is intended to not only release encumbrances but to indicate that this is the final invoice line for corresponding order line. This should take into account the fiscal year. We may release encumbrance for this FY but for on-going orders expect to encumber again next year. |
| subscriptionInfo           | string          | The user should use this field to provide info on the subscription (eg. which volumes are being invoiced). It is MANDATORY if the chk_subscription_overlap is FALSE AND there is no start date provided                                                                               |
| subscriptionStart          | string          | Subscription start date                                                                                                                                                                                                                                                               |
| subscriptionEnd            | string          | Subscription end date                                                                                                                                                                                                                                                                 |
| subTotal                   | number          | Invoice line amount before adjustments are applied                                                                                                                                                                                                                                    |
| total                      | number          | Invoice line total amount which is sum of subTotal and adjustmentsTotal. This amount is always calculated by system.                                                                                                                                                                  |
| referenceNumbers           | array           | Reference number items array                                                                                                                                                                                                                                                          |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                                                                                                                                                                                    |
| metadata/createdDate       | string          | Date and time when the record was created                                                                                                                                                                                                                                             |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                                                                                                                                                                                                                |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                                                                                                                                                                                                          |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                                                                                                                                                                                                        |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                                                                                                                                                                                                           |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                                                                                                                                                                                                     |
| tags                       | object          | List of simple tags that can be added to an object                                                                                                                                                                                                                                    |
| tags/tagList               | array           | List of tags                                                                                                                                                                                                                                                                          |

## Documentation: [invoice_voucher_lines](invoice_voucher_lines.md)

### Source:

Module: mod-invoice-storage

Interface: /voucher-storage/voucher-lines

### Attributes:

| Property Name              | Property Type   | Property Description                                                                                                                                       |
|:---------------------------|:----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| id                         | string          | The UUID format string                                                                                                                                     |
| amount                     | number          | Total amount of this voucher                                                                                                                               |
| externalAccountNumber      | string          | All distributions that come from funds with the same account number are grouped by voucher line                                                            |
| fundDistributions          | array           | List of fund distributions                                                                                                                                 |
| sourceIds                  | array           | UUID of invoice lines. There could be many invoice lines against a single voucher line. These are group on a voucher line based on External account number |
| subTransactionId           | string          | The UUID format string                                                                                                                                     |
| voucherId                  | string          | The UUID format string                                                                                                                                     |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                                                         |
| metadata/createdDate       | string          | Date and time when the record was created                                                                                                                  |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                                                                                     |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                                                                               |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                                                                             |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                                                                                |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                                                                          |

## Documentation: [invoice_vouchers](invoice_vouchers.md)

### Source:

Module: mod-invoice-storage

Interface: /voucher-storage/vouchers

### Attributes:

| Property Name              | Property Type   | Property Description                                                                                                                                                |
|:---------------------------|:----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id                         | string          | The UUID format string                                                                                                                                              |
| accountingCode             | string          | Number that represents the vendor is an external accounting system which may include details like "Address code" in it. This is the number as stated on the invoice |
| accountNo                  | string          | The unique number of the organization account                                                                                                                       |
| amount                     | number          | The amount that is actually paid                                                                                                                                    |
| batchGroupId               | string          | UUID of the batch group to use when generating batch vouchers                                                                                                       |
| disbursementNumber         | string          | The identifier for the physical transaction corresponding to a payment;Brought in from external source                                                              |
| disbursementDate           | string          | Date payment was made from financial system                                                                                                                         |
| disbursementAmount         | number          | The amount of the payment made outside of FOLIO                                                                                                                     |
| enclosureNeeded            | boolean         | Indicates that an enclosure is needed                                                                                                                               |
| invoiceCurrency            | string          | The currency in which invoice was originally defined                                                                                                                |
| invoiceId                  | string          | The UUID format string                                                                                                                                              |
| exchangeRate               | number          | Exchange rate used to generate transaction                                                                                                                          |
| exportToAccounting         | boolean         | Export this payment record to a financial system                                                                                                                    |
| status                     | string          | Status of the voucher                                                                                                                                               |
| systemCurrency             | string          | The currency in which the voucher was paid                                                                                                                          |
| type                       | string          | Indicates type of payment to account                                                                                                                                |
| voucherDate                | string          | The date the invoice status changes to approved                                                                                                                     |
| voucherNumber              | string          | Number generated by folio that will eventually identify the payment request sent out to external financial system.                                                  |
| vendorId                   | string          | The UUID format string                                                                                                                                              |
| vendorAddress              | object          | An address record                                                                                                                                                   |
| vendorAddress/addressLine1 | string          | The first line of this address                                                                                                                                      |
| vendorAddress/addressLine2 | string          | The second line of this address                                                                                                                                     |
| vendorAddress/city         | string          | The city for this address                                                                                                                                           |
| vendorAddress/stateRegion  | string          | The state or region for this address                                                                                                                                |
| vendorAddress/zipCode      | string          | The zip code for this address                                                                                                                                       |
| vendorAddress/country      | string          | The country for this address                                                                                                                                        |
| acqUnitIds                 | array           | acquisition unit ids associated with this voucher                                                                                                                   |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                                                                  |
| metadata/createdDate       | string          | Date and time when the record was created                                                                                                                           |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                                                                                              |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                                                                                        |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                                                                                      |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                                                                                         |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                                                                                   |

## Documentation: [notes](notes.md)

### Source:

Module: mod-notes

Interface: /notes

### Attributes:

| Property Name              | Property Type   | Property Description                                                                                                                                                                                                                                     |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id                         | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| typeId                     | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| type                       | string          | Type of note (configured in settings)                                                                                                                                                                                                                    |
| domain                     | string          | Domain associated with this note                                                                                                                                                                                                                         |
| title                      | string          | Note title                                                                                                                                                                                                                                               |
| content                    | string          | Content of the note                                                                                                                                                                                                                                      |
| status                     | string          | Status of note - applies when searching by link.id and status                                                                                                                                                                                            |
| creator                    | object          | User Display Information                                                                                                                                                                                                                                 |
| creator/lastName           | string          | Last name of the user                                                                                                                                                                                                                                    |
| creator/firstName          | string          | First name of the user                                                                                                                                                                                                                                   |
| creator/middleName         | string          | Middle name or initial of the user                                                                                                                                                                                                                       |
| updater                    | object          | User Display Information                                                                                                                                                                                                                                 |
| updater/lastName           | string          | Last name of the user                                                                                                                                                                                                                                    |
| updater/firstName          | string          | First name of the user                                                                                                                                                                                                                                   |
| updater/middleName         | string          | Middle name or initial of the user                                                                                                                                                                                                                       |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                                                                                                                                                       |
| metadata/createdDate       | string          | Date and time when the record was created                                                                                                                                                                                                                |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                                                                                                                                                                                   |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                                                                                                                                                                             |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                                                                                                                                                                           |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                                                                                                                                                                              |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                                                                                                                                                                        |
| links                      | array           | Collection of links to associated objects                                                                                                                                                                                                                |

## Documentation: [acquisition_method](acquisition_method.md)

### Source:

Module: mod-orders-storage

Interface: /orders-storage/acquisition-methods

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          | The UUID format string                                                                             |
| value                      | string          | The value of this acquisition method                                                               |
| source                     | string          | Source of acquisition method                                                                       |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [acquisitions_memberships](acquisitions_memberships.md)

### Source:

Module: mod-orders-storage

Interface: /acquisitions-units-storage/memberships

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          | UUID of this membership record                                                                     |
| userId                     | string          | The UUID of the user to associate with the acquisitions unit                                       |
| acquisitionsUnitId         | string          | The acquisition unit the user is a member of                                                       |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [acquisitions_units](acquisitions_units.md)

### Source:

Module: mod-orders-storage

Interface: /acquisitions-units-storage/units

### Attributes:

| Property Name              | Property Type   | Property Description                                                                                          |
|:---------------------------|:----------------|:--------------------------------------------------------------------------------------------------------------|
| id                         | string          | The UUID format string                                                                                        |
| name                       | string          | a name for this acquisitions unit                                                                             |
| isDeleted                  | boolean         | If true, the record is marked for deletion at some point. This prevents it from being assigned to any record. |
| protectCreate              | boolean         | if true, only members can create records associated with this acq unit.                                       |
| protectRead                | boolean         | if true, only members can read/view records associated with this acq unit.                                    |
| protectUpdate              | boolean         | if true, only members can update records associated with this acq unit.                                       |
| protectDelete              | boolean         | if true, only members can delete records associated with this acq unit.                                       |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)            |
| metadata/createdDate       | string          | Date and time when the record was created                                                                     |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                                        |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                                  |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                                |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                                   |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                             |

## Documentation: [po_alerts](po_alerts.md)

### Source:

Module: mod-orders-storage

Interface: /orders-storage/alerts

### Attributes:

| Property Name   | Property Type   | Property Description      |
|:----------------|:----------------|:--------------------------|
| id              | string          | UUID of this alert record |
| alert           | string          | the alert text            |

## Documentation: [po_lines](po_lines.md)

### Source:

Module: mod-orders-storage

Interface: /orders-storage/po-lines

### Attributes:

| Property Name                 | Property Type      | Property Description                                                                                                                        |
|:------------------------------|:-------------------|:--------------------------------------------------------------------------------------------------------------------------------------------|
| id                            | string             | The UUID format string                                                                                                                      |
| edition                       | string             | edition of the material                                                                                                                     |
| checkinItems                  | boolean            | if true this will toggle the Check-in workflow for details associated with this PO line                                                     |
| agreementId                   | string             | The UUID format string                                                                                                                      |
| acquisitionMethod             | string             | The UUID format string                                                                                                                      |
| automaticExport               | boolean            | if true then line will be marked as available to export in the EDIFACT format or other format                                               |
| alerts                        | array              | an array of alert record IDs                                                                                                                |
| cancellationRestriction       | boolean            | whether or not there are cancellation restrictions for this purchase order line                                                             |
| cancellationRestrictionNote   | string             | free-form notes related to cancellation restrictions                                                                                        |
| claims                        | array              | list of claims                                                                                                                              |
| collection                    | boolean            | whether or not this purchase order line is for a collection                                                                                 |
| contributors                  | array              | list of contributors to the material                                                                                                        |
| cost                          | object             | purchase order line cost record                                                                                                             |
| cost/listUnitPrice            | number             | The per-item list price for physical or resources of 'Other' order format                                                                   |
| cost/listUnitPriceElectronic  | number             | The e-resource per-item list price                                                                                                          |
| cost/currency                 | string             | An ISO currency code                                                                                                                        |
| cost/additionalCost           | number             | Lump sum that is added to the total estimated price - not affected by discount                                                              |
| cost/discount                 | number             | Percentage (0 to 100) or amount (positive number) that is subtracted from the list price time quantities calculation before additional cost |
| cost/discountType             | string             | Percentage or amount discount type                                                                                                          |
| cost/exchangeRate             | number             | Exchange rate                                                                                                                               |
| cost/quantityPhysical         | integer            | Quantity of physical items or resources of 'Other' order format in this purchase order line                                                 |
| cost/quantityElectronic       | integer            | Quantity of electronic items in this purchase order line                                                                                    |
| cost/poLineEstimatedPrice     | number             | The calculated total estimated price for this purchase order line: list price time quantities minus discount amount plus additional cost    |
| cost/fyroAdjustmentAmount     | number             | Adjustment amount if rollover was happen                                                                                                    |
| description                   | string             | description of the material                                                                                                                 |
| details                       | object             | purchase order line details                                                                                                                 |
| details/receivingNote         | string             | notes regarding receiving instructions                                                                                                      |
| details/isAcknowledged        | boolean            | Flag for acknowledge receiving note                                                                                                         |
| details/productIds            | array              | a list of product identifiers                                                                                                               |
| details/subscriptionFrom      | ['string', 'null'] | the start date of the subscription                                                                                                          |
| details/subscriptionInterval  | integer            | the subscription interval in days                                                                                                           |
| details/subscriptionTo        | ['string', 'null'] | the end date of the subscription                                                                                                            |
| donor                         | string             | the donor contributing to this purchase order line                                                                                          |
| eresource                     | object             | purchase order line e-resource details                                                                                                      |
| eresource/activated           | boolean            | whether or not this resource is activated                                                                                                   |
| eresource/activationDue       | integer            | number of days until activation, from date of order placement                                                                               |
| eresource/createInventory     | string             | Shows what inventory objects need to be created for electronic resource                                                                     |
| eresource/trial               | boolean            | whether or not this is a trial                                                                                                              |
| eresource/expectedActivation  | string             | expected date the resource will be activated                                                                                                |
| eresource/userLimit           | integer            | the concurrent user-limit                                                                                                                   |
| eresource/accessProvider      | string             | UUID of the access provider                                                                                                                 |
| eresource/license             | object             | purchase order line license record                                                                                                          |
| eresource/license/code        | string             | license code                                                                                                                                |
| eresource/license/description | string             | license description                                                                                                                         |
| eresource/license/reference   | string             | license reference                                                                                                                           |
| eresource/materialType        | string             | UUID of the material Type                                                                                                                   |
| eresource/resourceUrl         | string             | Electronic resource can be access via this URL                                                                                              |
| fundDistribution              | array              | Fund distribution records for this purchase order line                                                                                      |
| instanceId                    | string             | The UUID format string                                                                                                                      |
| isPackage                     | boolean            | Indicates that this POL is for a package                                                                                                    |
| locations                     | array              | Location records for this purchase order line                                                                                               |
| lastEDIExportDate             | string             | The last date when line was exported in the EDIFACT file                                                                                    |
| orderFormat                   | string             | The purchase order line format                                                                                                              |
| packagePoLineId               | string             | The UUID format string                                                                                                                      |
| paymentStatus                 | string             | Payment/Receipt status                                                                                                                      |
| physical                      | object             | purchase order line physical material details                                                                                               |
| physical/createInventory      | string             | Shows what inventory objects need to be created for physical resource                                                                       |
| physical/materialType         | string             | UUID of the material Type                                                                                                                   |
| physical/materialSupplier     | string             | UUID of the material supplier record                                                                                                        |
| physical/expectedReceiptDate  | ['string', 'null'] | vendor agreed date prior to the Receipt Due date item is expected to be received by                                                         |
| physical/receiptDue           | ['string', 'null'] | date item should be received by                                                                                                             |
| physical/volumes              | array              | list of volumes included to the physical material                                                                                           |
| poLineDescription             | string             | purchase order line description                                                                                                             |
| poLineNumber                  | string             | A human readable number assigned to this PO line                                                                                            |
| publicationDate               | string             | date (year) of the material's publication                                                                                                   |
| publisher                     | string             | publisher of the material                                                                                                                   |
| purchaseOrderId               | string             | The UUID format string                                                                                                                      |
| receiptDate                   | ['null', 'string'] | date the purchase order line was received                                                                                                   |
| receiptStatus                 | string             | The purchase order line receipt status                                                                                                      |
| renewalNote                   | string             | Renewal note for this purchase order line                                                                                                   |
| reportingCodes                | array              | a list of reporting codes associated with this purchase order line                                                                          |
| requester                     | string             | who requested this purchase order line                                                                                                      |
| rush                          | boolean            | whether or not this is a rush order                                                                                                         |
| selector                      | string             | who selected this material                                                                                                                  |
| source                        | string             | The source of the Order                                                                                                                     |
| tags                          | object             | List of simple tags that can be added to an object                                                                                          |
| tags/tagList                  | array              | List of tags                                                                                                                                |
| titleOrPackage                | string             | title of the material                                                                                                                       |
| vendorDetail                  | object             | purchase order line vendor details                                                                                                          |
| vendorDetail/instructions     | string             | special instructions for the vendor                                                                                                         |
| vendorDetail/noteFromVendor   | string             | free-form notes from the vendor                                                                                                             |
| vendorDetail/vendorAccount    | string             | the accound number on the vendor's end associated with this purchase order line                                                             |
| vendorDetail/referenceNumbers | array              | Reference number items array                                                                                                                |
| metadata                      | object             | Metadata about creation and changes to records, provided by the server (client should not provide)                                          |
| metadata/createdDate          | string             | Date and time when the record was created                                                                                                   |
| metadata/createdByUserId      | string             | ID of the user who created the record (when available)                                                                                      |
| metadata/createdByUsername    | string             | Username of the user who created the record (when available)                                                                                |
| metadata/updatedDate          | string             | Date and time when the record was last updated                                                                                              |
| metadata/updatedByUserId      | string             | ID of the user who last updated the record (when available)                                                                                 |
| metadata/updatedByUsername    | string             | Username of the user who last updated the record (when available)                                                                           |

## Documentation: [po_order_invoice_relns](po_order_invoice_relns.md)

### Source:

Module: mod-orders-storage

Interface: /orders-storage/order-invoice-relns

### Attributes:

| Property Name   | Property Type   | Property Description             |
|:----------------|:----------------|:---------------------------------|
| id              | string          | UUID of this relationship record |
| purchaseOrderId | string          | Purchase order id                |
| invoiceId       | string          | Invoice id                       |

## Documentation: [po_order_templates](po_order_templates.md)

### Source:

Module: mod-orders-storage

Interface: /orders-storage/order-templates

### Attributes:

| Property Name       | Property Type   | Property Description            |
|:--------------------|:----------------|:--------------------------------|
| id                  | string          | The UUID format string          |
| templateName        | string          | The order template name         |
| templateCode        | string          | The order template code         |
| templateDescription | string          | The order template description  |
| hiddenFields        | object          | Fields for hidden from end user |

## Documentation: [po_pieces](po_pieces.md)

### Source:

Module: mod-orders-storage

Interface: /orders-storage/pieces

### Attributes:

| Property Name     | Property Type   | Property Description                                                                                               |
|:------------------|:----------------|:-------------------------------------------------------------------------------------------------------------------|
| id                | string          | The UUID format string                                                                                             |
| caption           | string          | Volume/enumeration information                                                                                     |
| comment           | string          | Free form commentary                                                                                               |
| format            | string          | The format of the piece                                                                                            |
| itemId            | string          | The UUID format string                                                                                             |
| locationId        | string          | The UUID format string                                                                                             |
| poLineId          | string          | The UUID format string                                                                                             |
| titleId           | string          | The UUID format string                                                                                             |
| holdingId         | string          | The UUID format string                                                                                             |
| displayOnHolding  | boolean         | Whether or not receiving history should be displayed in holding record view                                        |
| enumeration       | string          | Enumeration is the descriptive information for the numbering scheme of a serial. Synchronized with inventory item. |
| chronology        | string          | Chronology is the descriptive information for the dating scheme of a serial. Synchronized with inventory item.     |
| discoverySuppress | boolean         | Records the fact that the record should not be displayed in a discovery system                                     |
| copyNumber        | string          | Copy number of the piece                                                                                           |
| receivingStatus   | string          | the status of this piece                                                                                           |
| supplement        | boolean         | Whether or not this is supplementary material                                                                      |
| receiptDate       | string          | Date that associated item is expected to arrive                                                                    |
| receivedDate      | string          | The date associated item is actually received                                                                      |

## Documentation: [po_purchase_orders](po_purchase_orders.md)

### Source:

Module: mod-orders-storage

Interface: /orders-storage/purchase-orders

### Attributes:

| Property Name              | Property Type   | Property Description                                                                                   |
|:---------------------------|:----------------|:-------------------------------------------------------------------------------------------------------|
| id                         | string          | The UUID format string                                                                                 |
| approved                   | boolean         | whether or not the purchase order has been approved                                                    |
| approvedById               | string          | The UUID format string                                                                                 |
| approvalDate               | string          | Date and time when purchase order was approved                                                         |
| assignedTo                 | string          | UUID of the user this purchase order his assigned to                                                   |
| billTo                     | string          | UUID of the billing address                                                                            |
| closeReason                | object          | purchase order closing reason record                                                                   |
| closeReason/reason         | string          | close reason description                                                                               |
| closeReason/note           | string          | free-form notes related to closing reason                                                              |
| dateOrdered                | string          | Date and time when purchase order was opened                                                           |
| manualPo                   | boolean         | if true, order cannot be sent automatically, e.g. via EDI                                              |
| notes                      | array           | free-form notes associated with this purchase order                                                    |
| poNumber                   | string          | A human readable ID assigned to this purchase order                                                    |
| poNumberPrefix             | string          | Purchase order number prefix                                                                           |
| poNumberSuffix             | string          | Purchase order number suffix                                                                           |
| orderType                  | string          | the purchase order type                                                                                |
| reEncumber                 | boolean         | indicates this purchase order should be re-encumbered each fiscal year. Only applies to ongoing orders |
| ongoing                    | object          | Ongoing details for Purchase Order                                                                     |
| ongoing/interval           | integer         | Renewal interval (in days)                                                                             |
| ongoing/isSubscription     | boolean         | Whether or not this is a subscription                                                                  |
| ongoing/manualRenewal      | boolean         | Whether or not this is a manual renewal                                                                |
| ongoing/notes              | string          | Notes associated with the Ongoing order                                                                |
| ongoing/reviewPeriod       | integer         | Time prior to renewal where changes can be made to subscription                                        |
| ongoing/renewalDate        | string          | The date this Ongoing PO's order lines were renewed                                                    |
| ongoing/reviewDate         | string          | Date when Order has to be reviewed                                                                     |
| shipTo                     | string          | UUID of the shipping address                                                                           |
| template                   | string          | The ID of the order template used for this order. Applies to both PO and POL                           |
| vendor                     | string          | UUID of the vendor record                                                                              |
| workflowStatus             | string          | Composite workflow status                                                                              |
| acqUnitIds                 | array           | acquisition unit ids associated with this purchase order                                               |
| nextPolNumber              | integer         | Number that will be used next time a purchase order line is created                                    |
| tags                       | object          | List of simple tags that can be added to an object                                                     |
| tags/tagList               | array           | List of tags                                                                                           |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)     |
| metadata/createdDate       | string          | Date and time when the record was created                                                              |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                                 |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                           |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                         |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                            |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                      |

## Documentation: [po_receiving_history](po_receiving_history.md)

### Source:

Module: mod-orders-storage

Interface: /orders-storage/receiving-history

### Attributes:

| Property Name       | Property Type   | Property Description                                                                                               |
|:--------------------|:----------------|:-------------------------------------------------------------------------------------------------------------------|
| id                  | string          | The UUID format string                                                                                             |
| caption             | string          | Volume/enumeration information                                                                                     |
| checkin             | boolean         | If true this piece is for the Check-in workflow                                                                    |
| chronology          | string          | Chronology is the descriptive information for the dating scheme of a serial. Synchronized with inventory item.     |
| comment             | string          | Free form commentary                                                                                               |
| dateOrdered         | string          | Date and time when purchase order was opened                                                                       |
| discoverySuppress   | boolean         | Records the fact that the record should not be displayed in a discovery system                                     |
| displayOnHolding    | boolean         | Whether or not receiving history should be displayed in holding record view                                        |
| enumeration         | string          | Enumeration is the descriptive information for the numbering scheme of a serial. Synchronized with inventory item. |
| copyNumber          | string          | Copy number of the piece                                                                                           |
| instanceId          | string          | The UUID format string                                                                                             |
| itemId              | string          | The UUID format string                                                                                             |
| locationId          | string          | The UUID format string                                                                                             |
| pieceFormat         | string          | The format of the piece                                                                                            |
| poLineId            | string          | The UUID format string                                                                                             |
| poLineNumber        | string          | A human readable number assigned to this PO line                                                                   |
| poLineReceiptStatus | string          | The purchase order line receipt status                                                                             |
| purchaseOrderId     | string          | The UUID format string                                                                                             |
| receiptDate         | string          | Date that this item is expected to arrive                                                                          |
| receivedDate        | string          | date received                                                                                                      |
| receivingNote       | string          | A note at the poLine level pertaining to receiving/check-in                                                        |
| receivingStatus     | string          | the status of this piece                                                                                           |
| supplement          | boolean         | Whether or not this is supplementary material                                                                      |
| title               | string          | Title of the instance this poLine is associated with                                                               |

## Documentation: [po_reporting_codes](po_reporting_codes.md)

### Source:

Module: mod-orders-storage

Interface: /orders-storage/reporting-codes

### Attributes:

| Property Name   | Property Type   | Property Description               |
|:----------------|:----------------|:-----------------------------------|
| id              | string          | UUID of this reporting code record |
| code            | string          | a reporting code                   |
| description     | string          | description of this reporting code |

## Documentation: [organization_addresses](organization_addresses.md)

### Source:

Module: mod-organizations-storage

Interface: /organizations-storage/addresses

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          | The UUID format string                                                                             |
| addressLine1               | string          | The first line of this address                                                                     |
| addressLine2               | string          | The second line of this address                                                                    |
| city                       | string          | The city for this address                                                                          |
| stateRegion                | string          | The state or region for this address                                                               |
| zipCode                    | string          | The zip code for this address                                                                      |
| country                    | string          | The country for this address                                                                       |
| isPrimary                  | boolean         | Used to set this address as primary for the contact                                                |
| categories                 | array           | The list of categories for this organization address                                               |
| language                   | string          | The language for this organization address                                                         |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [organization_categories](organization_categories.md)

### Source:

Module: mod-organizations-storage

Interface: /organizations-storage/categories

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          | The UUID format string                                                                             |
| value                      | string          | The value of this category                                                                         |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [organization_contacts](organization_contacts.md)

### Source:

Module: mod-organizations-storage

Interface: /organizations-storage/contacts

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          | The UUID format string                                                                             |
| prefix                     | string          | The prefix for this contact person                                                                 |
| firstName                  | string          | The first name of this contact person                                                              |
| lastName                   | string          | The last name of this contact person                                                               |
| language                   | string          | The preferred language for this contact person                                                     |
| notes                      | string          | The notes for this contact person                                                                  |
| phoneNumbers               | array           | The list of phone numbers for this contact person                                                  |
| emails                     | array           | The list of emails for this contact person                                                         |
| addresses                  | array           | The list of addresses for this contact person                                                      |
| urls                       | array           | The list of URLs for this contact person                                                           |
| categories                 | array           | The list of contact categories associated with this organization contact person                    |
| inactive                   | boolean         | Used to indicate that a contact is no longer active                                                |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [organization_emails](organization_emails.md)

### Source:

Module: mod-organizations-storage

Interface: /organizations-storage/emails

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          | The UUID format string                                                                             |
| value                      | string          | The value for this email                                                                           |
| description                | string          | The description for this email                                                                     |
| isPrimary                  | boolean         | Used to set this email as primary for the contact                                                  |
| categories                 | array           | The list of categories for this organization email                                                 |
| language                   | string          | The language for this organization email                                                           |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [organization_interfaces](organization_interfaces.md)

### Source:

Module: mod-organizations-storage

Interface: /organizations-storage/interfaces

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          | The UUID format string                                                                             |
| name                       | string          | The name of this interface                                                                         |
| uri                        | string          | The URI of this interface                                                                          |
| notes                      | string          | The notes for this interface                                                                       |
| available                  | boolean         | The availability setting for this interface                                                        |
| deliveryMethod             | string          | The delivery method for this interface                                                             |
| statisticsFormat           | string          | The format of the statistics for this interface                                                    |
| locallyStored              | string          | The locally stored location of this interface                                                      |
| onlineLocation             | string          | The online location for this interface                                                             |
| statisticsNotes            | string          | The notes regarding the statistics for this interface                                              |
| type                       | array           | Interface types                                                                                    |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [organization_organizations](organization_organizations.md)

### Source:

Module: mod-organizations-storage

Interface: /organizations-storage/organizations

### Attributes:

| Property Name                | Property Type      | Property Description                                                                                                                                                                                                                                    |
|:-----------------------------|:-------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id                           | string             | The UUID format string                                                                                                                                                                                                                                  |
| name                         | string             | The name of this organization                                                                                                                                                                                                                           |
| code                         | string             | The code for this organization                                                                                                                                                                                                                          |
| description                  | string             | The description for this organization                                                                                                                                                                                                                   |
| exportToAccounting           | boolean            | This would keep the invoice from being feed into the batch process (i.e. not generate an external voucher/payment) but would still move values in the system. This might be defined by the vendor relationship and exposed for override on the invoice. |
| status                       | string             | The status of this organization                                                                                                                                                                                                                         |
| organizationTypes            | array              | A list of organization types assigned to this organization                                                                                                                                                                                              |
| language                     | string             | The language for this organization                                                                                                                                                                                                                      |
| aliases                      | array              | The list of aliases for this organization                                                                                                                                                                                                               |
| addresses                    | array              | The list of addresses for this organization                                                                                                                                                                                                             |
| phoneNumbers                 | array              | The list of phone numbers for this organization                                                                                                                                                                                                         |
| emails                       | array              | The list of emails for this organization                                                                                                                                                                                                                |
| urls                         | array              | The list of URLs for this organization                                                                                                                                                                                                                  |
| contacts                     | array              | An array of contact record IDs                                                                                                                                                                                                                          |
| agreements                   | array              | The the list of agreements for this organization                                                                                                                                                                                                        |
| erpCode                      | string             | The ERP code for this organization                                                                                                                                                                                                                      |
| paymentMethod                | string             | The payment method for this organization                                                                                                                                                                                                                |
| accessProvider               | boolean            | The access provider for this organization                                                                                                                                                                                                               |
| governmental                 | boolean            | The setting to mark this organization as governmental                                                                                                                                                                                                   |
| licensor                     | boolean            | The setting to mark this organization as a licensor                                                                                                                                                                                                     |
| materialSupplier             | boolean            | The setting to mark this organization as a material supplier                                                                                                                                                                                            |
| vendorCurrencies             | array              | The list of currencies used by this organization                                                                                                                                                                                                        |
| claimingInterval             | integer            | The claim interval for this organization                                                                                                                                                                                                                |
| discountPercent              | number             | The discount percentage for this organization                                                                                                                                                                                                           |
| expectedActivationInterval   | integer            | The expected activation interval (in days) for this organization                                                                                                                                                                                        |
| expectedInvoiceInterval      | integer            | The expected invoice interval (in days) for this organization                                                                                                                                                                                           |
| renewalActivationInterval    | integer            | The revewal activation interval (in days) for this organization                                                                                                                                                                                         |
| subscriptionInterval         | integer            | The subscription interval (in days) for this organization                                                                                                                                                                                               |
| expectedReceiptInterval      | integer            | The receipt interval (in days) for this organization                                                                                                                                                                                                    |
| taxId                        | string             | The tax ID for this organization                                                                                                                                                                                                                        |
| liableForVat                 | boolean            | The setting to mark this organization liable to collect VAT                                                                                                                                                                                             |
| taxPercentage                | number             | The tax percentage value for this organization                                                                                                                                                                                                          |
| edi                          | object             | The EDI object for this organization (only applicable when isVendor is true)                                                                                                                                                                            |
| edi/vendorEdiCode            | string             | The organization code for this EDI                                                                                                                                                                                                                      |
| edi/vendorEdiType            | string             | The organization type for this EDI                                                                                                                                                                                                                      |
| edi/libEdiCode               | string             | The library code for this EDI                                                                                                                                                                                                                           |
| edi/libEdiType               | string             | The library type for this EDI                                                                                                                                                                                                                           |
| edi/prorateTax               | boolean            | The setting to prorate tax for this EDI                                                                                                                                                                                                                 |
| edi/prorateFees              | boolean            | The setting to prorate fees for this EDI                                                                                                                                                                                                                |
| edi/ediNamingConvention      | string             | The naming convention for this EDI                                                                                                                                                                                                                      |
| edi/sendAcctNum              | boolean            | The setting to send the account number for this EDI                                                                                                                                                                                                     |
| edi/supportOrder             | boolean            | The setting to support order for this EDI                                                                                                                                                                                                               |
| edi/supportInvoice           | boolean            | The setting to support invoice for this EDI                                                                                                                                                                                                             |
| edi/notes                    | string             | The notes for this EDI                                                                                                                                                                                                                                  |
| edi/ediFtp                   | object             | The FTP object for this EDI                                                                                                                                                                                                                             |
| edi/ediFtp/ftpFormat         | string             | The FTP format for this EDI                                                                                                                                                                                                                             |
| edi/ediFtp/serverAddress     | ['string', 'null'] | The server address for this EDI                                                                                                                                                                                                                         |
| edi/ediFtp/username          | string             | The login username for this EDI                                                                                                                                                                                                                         |
| edi/ediFtp/password          | string             | The login password for this EDI                                                                                                                                                                                                                         |
| edi/ediFtp/ftpMode           | string             | The FTP mode for this EDI                                                                                                                                                                                                                               |
| edi/ediFtp/ftpConnMode       | string             | The FTP connection mode for this EDI                                                                                                                                                                                                                    |
| edi/ediFtp/ftpPort           | integer            | The port for this EDI                                                                                                                                                                                                                                   |
| edi/ediFtp/orderDirectory    | string             | The order directory for this EDI                                                                                                                                                                                                                        |
| edi/ediFtp/invoiceDirectory  | string             | The invoice directory for this EDI                                                                                                                                                                                                                      |
| edi/ediFtp/notes             | string             | The notes for this EDI                                                                                                                                                                                                                                  |
| edi/ediJob                   | object             | The job object for this EDI                                                                                                                                                                                                                             |
| edi/ediJob/scheduleEdi       | boolean            | Activate the schedule for this EDI job                                                                                                                                                                                                                  |
| edi/ediJob/schedulingDate    | ['string', 'null'] | The date (MM/DD/YYYY) for this EDI job to start running                                                                                                                                                                                                 |
| edi/ediJob/time              | ['string', 'null'] | The time (h:mm A) for this EDI job                                                                                                                                                                                                                      |
| edi/ediJob/isMonday          | boolean            | The setting to run this EDI job on Mondays                                                                                                                                                                                                              |
| edi/ediJob/isTuesday         | boolean            | The setting to run this EDI job on Tuesdays                                                                                                                                                                                                             |
| edi/ediJob/isWednesday       | boolean            | The setting to run this EDI job on Wednesdays                                                                                                                                                                                                           |
| edi/ediJob/isThursday        | boolean            | The setting to run this EDI job on Thursdays                                                                                                                                                                                                            |
| edi/ediJob/isFriday          | boolean            | The setting to run this EDI job on Fridays                                                                                                                                                                                                              |
| edi/ediJob/isSaturday        | boolean            | The setting to run this EDI job on Saturdays                                                                                                                                                                                                            |
| edi/ediJob/isSunday          | boolean            | The setting to run this EDI job on Sundays                                                                                                                                                                                                              |
| edi/ediJob/sendToEmails      | string             | The comma delimited list of email addresses to notify when this EDI job runs                                                                                                                                                                            |
| edi/ediJob/notifyAllEdi      | boolean            | The setting to notify all receivers when this EDI job runs                                                                                                                                                                                              |
| edi/ediJob/notifyInvoiceOnly | boolean            | The setting to notify only the invoice receiver when this EDI job runs                                                                                                                                                                                  |
| edi/ediJob/notifyErrorOnly   | boolean            | The setting to notiry on the error receiver when this EDI job runs                                                                                                                                                                                      |
| edi/ediJob/schedulingNotes   | string             | The schedule notes for this EDI job                                                                                                                                                                                                                     |
| interfaces                   | array              | The list of interfaces assigned to this organization                                                                                                                                                                                                    |
| accounts                     | array              | The list of accounts for this organization                                                                                                                                                                                                              |
| isVendor                     | boolean            | Used to indicate that this organization is also a vendor                                                                                                                                                                                                |
| isDonor                      | boolean            | Used to designate whether this organization is a donor                                                                                                                                                                                                  |
| sanCode                      | string             | The SAN code for this organization address                                                                                                                                                                                                              |
| changelogs                   | array              | The list of changes applied to this organization                                                                                                                                                                                                        |
| acqUnitIds                   | array              | Acquisition unit UUIDs associated with this organization                                                                                                                                                                                                |
| tags                         | object             | List of simple tags that can be added to an object                                                                                                                                                                                                      |
| tags/tagList                 | array              | List of tags                                                                                                                                                                                                                                            |
| metadata                     | object             | Metadata about creation and changes to records, provided by the server (client should not provide)                                                                                                                                                      |
| metadata/createdDate         | string             | Date and time when the record was created                                                                                                                                                                                                               |
| metadata/createdByUserId     | string             | ID of the user who created the record (when available)                                                                                                                                                                                                  |
| metadata/createdByUsername   | string             | Username of the user who created the record (when available)                                                                                                                                                                                            |
| metadata/updatedDate         | string             | Date and time when the record was last updated                                                                                                                                                                                                          |
| metadata/updatedByUserId     | string             | ID of the user who last updated the record (when available)                                                                                                                                                                                             |
| metadata/updatedByUsername   | string             | Username of the user who last updated the record (when available)                                                                                                                                                                                       |

## Documentation: [organization_phone_numbers](organization_phone_numbers.md)

### Source:

Module: mod-organizations-storage

Interface: /organizations-storage/phone-numbers

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          | The UUID format string                                                                             |
| phoneNumber                | string          | The entire sequence of digits for this phone number                                                |
| categories                 | array           | The list of categories for this organization phone                                                 |
| type                       | string          | The type of this phone number                                                                      |
| isPrimary                  | boolean         | Used to set this phone number as primary for the contact                                           |
| language                   | string          | The language for this organization phone                                                           |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [organization_urls](organization_urls.md)

### Source:

Module: mod-organizations-storage

Interface: /organizations-storage/urls

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          | The UUID format string                                                                             |
| value                      | string          | The value for this URL                                                                             |
| description                | string          | The description for this URL                                                                       |
| language                   | string          | The language for this organization URL                                                             |
| isPrimary                  | boolean         | Used to set this url as primary for the contact                                                    |
| categories                 | array           | The list of categories for this organization URL                                                   |
| notes                      | string          | The notes for this organization URL                                                                |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [patron_blocks_user_summary](patron_blocks_user_summary.md)

### Source:

Module: mod-patron-blocks

Interface: /user-summary

### Attributes:

| Property Name                    | Property Type   | Property Description                                                                                                                                                                                                                                     |
|:---------------------------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id                               | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| _version                         | integer         | Record version for optimistic locking                                                                                                                                                                                                                    |
| userId                           | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| openLoans                        | array           | User's open loans                                                                                                                                                                                                                                        |
| openLoans/loanId                 | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| openLoans/dueDate                | string          | Due date of the loan                                                                                                                                                                                                                                     |
| openLoans/recall                 | boolean         | Indicates if the item was recalled                                                                                                                                                                                                                       |
| openLoans/itemLost               | boolean         | Indicates if the item associated with the loan is in status 'Aged to lost' or 'Declared lost'                                                                                                                                                            |
| openLoans/itemClaimedReturned    | boolean         | Indicates if the item associated with the loan is in status 'Claimed returned'                                                                                                                                                                           |
| openLoans/gracePeriod            | object          | Period of time, a number of minutes, hours, days, weeks or months                                                                                                                                                                                        |
| openLoans/gracePeriod/duration   | integer         | Duration of the period, number of times the interval repeats                                                                                                                                                                                             |
| openLoans/gracePeriod/intervalId | string          | Interval for the period, e.g. hours, days or weeks                                                                                                                                                                                                       |
| openFeesFines                    | array           | User's open fees/fines                                                                                                                                                                                                                                   |
| openFeesFines/feeFineId          | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| openFeesFines/feeFineTypeId      | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| openFeesFines/loanId             | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| openFeesFines/balance            | number          | Balance                                                                                                                                                                                                                                                  |
| metadata                         | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                                                                                                                                                       |
| metadata/createdDate             | string          | Date and time when the record was created                                                                                                                                                                                                                |
| metadata/createdByUserId         | string          | ID of the user who created the record (when available)                                                                                                                                                                                                   |
| metadata/createdByUsername       | string          | Username of the user who created the record (when available)                                                                                                                                                                                             |
| metadata/updatedDate             | string          | Date and time when the record was last updated                                                                                                                                                                                                           |
| metadata/updatedByUserId         | string          | ID of the user who last updated the record (when available)                                                                                                                                                                                              |
| metadata/updatedByUsername       | string          | Username of the user who last updated the record (when available)                                                                                                                                                                                        |

## Documentation: [perm_permissions](perm_permissions.md)

### Source:

Module: mod-permissions

Interface: /perms/permissions

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| permissionName             | string          | The unique name of the permission                                                                  |
| displayName                | string          | The human-readable name of the permission                                                          |
| id                         | string          | The globally unique (UUID) identifier for the permission                                           |
| description                | string          | A description of the permission                                                                    |
| tags                       | array           | A list of tags for searching                                                                       |
| subPermissions             | array           | A list of child permissions granted by this permission                                             |
| childOf                    | array           | A list of permissions that 'own' this permission                                                   |
| grantedTo                  | array           | A list of permission users to whom this permission has been granted                                |
| mutable                    | boolean         | Whether or not this permission changes at runtime                                                  |
| visible                    | boolean         | Whether or not this permission is visible to users                                                 |
| dummy                      | boolean         | Is this a temporary dummy permission                                                               |
| deprecated                 | boolean         | Indicates whether this permissions has been marked for deletion (soft deleted)                     |
| moduleName                 | string          | The name of the module (not including version) that defined this permission                        |
| moduleVersion              | string          | The version of the module that defined this permission                                             |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [perm_users](perm_users.md)

### Source:

Module: mod-permissions

Interface: /perms/users

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          | The primary key (UUID) of this permissionUser record                                               |
| userId                     | string          | A foreign key to the id field (UUID) of the user record in the users module                        |
| permissions                | array           | A list of permission names owned by this user                                                      |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [template_engine_template](template_engine_template.md)

### Source:

Module: mod-template-engine

Interface: /templates

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| id                         | string          | Template id                                                                                        |
| description                | string          | Template description                                                                               |
| outputFormats              | array           | Array of output formats                                                                            |
| templateResolver           | string          | Template engine name                                                                               |
| localizedTemplates         | object          | List of localized templates                                                                        |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [user_addresstypes](user_addresstypes.md)

### Source:

Module: mod-users

Interface: /addresstypes

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| addressType                | string          | A unique name for this address type                                                                |
| desc                       | string          | An explanation of this address type                                                                |
| id                         | string          | A UUID identifying this address type                                                               |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [user_departments](user_departments.md)

### Source:

Module: mod-users

Interface: /departments

### Attributes:

| Property Name              | Property Type   | Property Description                                                                                                                                                                                                                                     |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id                         | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| name                       | string          | The unique name of this department                                                                                                                                                                                                                       |
| code                       | string          | The unique code of this department                                                                                                                                                                                                                       |
| usageNumber                | integer         | Number of users that have this department                                                                                                                                                                                                                |
| source                     | string          | Origin of the department record, i.e. 'System' or 'User'                                                                                                                                                                                                 |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                                                                                                                                                       |
| metadata/createdDate       | string          | Date and time when the record was created                                                                                                                                                                                                                |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                                                                                                                                                                                   |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                                                                                                                                                                             |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                                                                                                                                                                           |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                                                                                                                                                                              |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                                                                                                                                                                        |

## Documentation: [user_groups](user_groups.md)

### Source:

Module: mod-users

Interface: /groups

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| group                      | string          | The unique name of this group                                                                      |
| desc                       | string          | An explanation of this group                                                                       |
| id                         | string          | A UUID identifying this group                                                                      |
| expirationOffsetInDays     | integer         | The default period in days after which a newly created user that belongs to this group will expire |
| source                     | string          | Origin of the group record, i.e. 'System' or 'User'                                                |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [user_proxiesfor](user_proxiesfor.md)

### Source:

Module: mod-users

Interface: /proxiesfor

### Attributes:

| Property Name              | Property Type   | Property Description                                                                               |
|:---------------------------|:----------------|:---------------------------------------------------------------------------------------------------|
| userId                     | string          | The id of the user for whom this proxy pertains                                                    |
| proxyUserId                | string          | The id of the user acting as the proxy                                                             |
| id                         | string          | A UUID identifying this proxy relationship                                                         |
| requestForSponsor          | string          | Can the user request a sponsor (yes/no)                                                            |
| createdDate                | string          | Deprecated                                                                                         |
| notificationsTo            | string          | Where notifications are sent                                                                       |
| accrueTo                   | string          | Where fees and fines accrue                                                                        |
| status                     | string          | Active or Inactive                                                                                 |
| expirationDate             | string          | The date this proxy relationship expires                                                           |
| metadata                   | object          | Metadata about creation and changes to records, provided by the server (client should not provide) |
| metadata/createdDate       | string          | Date and time when the record was created                                                          |
| metadata/createdByUserId   | string          | ID of the user who created the record (when available)                                             |
| metadata/createdByUsername | string          | Username of the user who created the record (when available)                                       |
| metadata/updatedDate       | string          | Date and time when the record was last updated                                                     |
| metadata/updatedByUserId   | string          | ID of the user who last updated the record (when available)                                        |
| metadata/updatedByUsername | string          | Username of the user who last updated the record (when available)                                  |

## Documentation: [user_users](user_users.md)

### Source:

Module: mod-users

Interface: /users

### Attributes:

| Property Name                     | Property Type   | Property Description                                                                                                                                                                                                                                     |
|:----------------------------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| username                          | string          | A unique name belonging to a user. Typically used for login                                                                                                                                                                                              |
| id                                | string          | A globally unique (UUID) identifier for the user                                                                                                                                                                                                         |
| externalSystemId                  | string          | A unique ID that corresponds to an external authority                                                                                                                                                                                                    |
| barcode                           | string          | The unique library barcode for this user                                                                                                                                                                                                                 |
| active                            | boolean         | A flag to determine if the user's account is effective and not expired. The tenant configuration can require the user to be active for login. Active is different from the loan patron block                                                             |
| type                              | string          | The class of user like staff or patron; this is different from patronGroup; it can store shadow, system user and dcb types also                                                                                                                          |
| patronGroup                       | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| departments                       | array           | A list of UUIDs corresponding to the departments the user belongs to, see /departments API                                                                                                                                                               |
| meta                              | object          | Deprecated                                                                                                                                                                                                                                               |
| proxyFor                          | array           | Deprecated                                                                                                                                                                                                                                               |
| personal                          | object          | Personal information about the user                                                                                                                                                                                                                      |
| personal/lastName                 | string          | The user's surname                                                                                                                                                                                                                                       |
| personal/firstName                | string          | The user's given name                                                                                                                                                                                                                                    |
| personal/middleName               | string          | The user's middle name (if any)                                                                                                                                                                                                                          |
| personal/preferredFirstName       | string          | The user's preferred name                                                                                                                                                                                                                                |
| personal/email                    | string          | The user's email address                                                                                                                                                                                                                                 |
| personal/phone                    | string          | The user's primary phone number                                                                                                                                                                                                                          |
| personal/mobilePhone              | string          | The user's mobile phone number                                                                                                                                                                                                                           |
| personal/dateOfBirth              | string          | The user's birth date                                                                                                                                                                                                                                    |
| personal/addresses                | array           | Physical addresses associated with the user                                                                                                                                                                                                              |
| personal/addresses/id             | string          | A unique id for this address                                                                                                                                                                                                                             |
| personal/addresses/countryId      | string          | The country code for this address                                                                                                                                                                                                                        |
| personal/addresses/addressLine1   | string          | Address, Line 1                                                                                                                                                                                                                                          |
| personal/addresses/addressLine2   | string          | Address, Line 2                                                                                                                                                                                                                                          |
| personal/addresses/city           | string          | City name                                                                                                                                                                                                                                                |
| personal/addresses/region         | string          | Region                                                                                                                                                                                                                                                   |
| personal/addresses/postalCode     | string          | Postal Code                                                                                                                                                                                                                                              |
| personal/addresses/addressTypeId  | string          | A universally unique identifier (UUID), this is a 128-bit number used to identify a record and is shown in hex with dashes, for example 6312d172-f0cf-40f6-b27d-9fa8feaf332f; the UUID version must be from 1-5; see https://dev.folio.org/guides/uuids/ |
| personal/addresses/primaryAddress | boolean         | Is this the user's primary address?                                                                                                                                                                                                                      |
| personal/preferredContactTypeId   | string          | Id of user's preferred contact type like Email, Mail or Text Message, see /addresstypes API                                                                                                                                                              |
| enrollmentDate                    | string          | The date in which the user joined the organization                                                                                                                                                                                                       |
| expirationDate                    | string          | The date for when the user becomes inactive                                                                                                                                                                                                              |
| createdDate                       | string          | Deprecated                                                                                                                                                                                                                                               |
| updatedDate                       | string          | Deprecated                                                                                                                                                                                                                                               |
| metadata                          | object          | Metadata about creation and changes to records, provided by the server (client should not provide)                                                                                                                                                       |
| metadata/createdDate              | string          | Date and time when the record was created                                                                                                                                                                                                                |
| metadata/createdByUserId          | string          | ID of the user who created the record (when available)                                                                                                                                                                                                   |
| metadata/createdByUsername        | string          | Username of the user who created the record (when available)                                                                                                                                                                                             |
| metadata/updatedDate              | string          | Date and time when the record was last updated                                                                                                                                                                                                           |
| metadata/updatedByUserId          | string          | ID of the user who last updated the record (when available)                                                                                                                                                                                              |
| metadata/updatedByUsername        | string          | Username of the user who last updated the record (when available)                                                                                                                                                                                        |
| tags                              | object          | List of simple tags that can be added to an object                                                                                                                                                                                                       |
| tags/tagList                      | array           | List of tags                                                                                                                                                                                                                                             |
| customFields                      | object          | Object that contains custom field                                                                                                                                                                                                                        |


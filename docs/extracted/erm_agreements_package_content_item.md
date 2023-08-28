---
title: erm_agreements_package_content_item
---
## Source:

Module: mod_agreements

Interface: package_content_item

## Attributes:

| Property Name    | Property Type   | Property Description                                                         |
|:-----------------|:----------------|:-----------------------------------------------------------------------------|
| id               |                 | ID of the package content item                                               |
| pci_pti_fk       |                 | ID of the platform_title_instance that the package_content_item is linked to |
| pci_pkg_fk       |                 | ID of the package that the package_content_item belongs to                   |
| pci_access_start |                 | The date on which a package_content_item was first accessible in a package   |
| pci_access_end   |                 | The date on which a package_content_item was last accessible in a package    |


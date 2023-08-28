---
title: users_departments_unpacked.sql
---
# Documentation: users_departments_unpacked.sql

## Attributes:

|   Attribute # | Attribute             | Type   | Source - Schema   | Source - Table   | Source - Attribute   | Source - Type   | Source - Multiple values   | Aggregation   | Description                                                            | Notes   |
|--------------:|:----------------------|:-------|:------------------|:-----------------|:---------------------|:----------------|:---------------------------|:--------------|:-----------------------------------------------------------------------|:--------|
|             1 | user_id               | uuid   |                   |                  |                      |                 |                            |               | User ID (Generated UUID) of the user associated with the department(s) |         |
|             2 | department_id         | uuid   |                   |                  |                      |                 |                            |               | Department ID (Generated UUID) of the department                       |         |
|             3 | department_ordinality | int8   |                   |                  |                      |                 |                            |               | The ordinality of the department(s) associated with a user             |         |
|             4 | department_name       | text   |                   |                  |                      |                 |                            |               | The display name of the department                                     |         |
|             5 | department_code       | text   |                   |                  |                      |                 |                            |               | The (user-supplied) code for the department                            |         |
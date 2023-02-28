Contributing
============

We appreciate submissions of  enhancements for the scripts and bug fixes.
All submissions will be considered as time allows. We ask your patience; 
it may require considerable time to decide whether a pull request will be accepted.

Please follow these guidelines when preparing a pull request.

##### Contents  
1\. [New contributors](#1-new-contributors)  
2\. [Commits and pull requests](#2-commits-and-pull-requests)  
3\. [Code review](#3-code-review)  
4\. [Documentation](#4-documentation)  
5\. [Testing](#5-testing)


1\. New contributors
--------------------

Before beginning work on a contribution, we recommend that you ask the
community in advance about the work you propose to do.  They may have
feedback that would save you time.

At present most contributors use the #folio channel in the
Metadb/LDP Slack workspace.

For bugs or specific technical proposals, use
[Issues](https://github.com/stdombek/folio_reporting_project_extracted_derived_tables/issues).


2\. Commits and pull requests
-----------------------------

### Making changes

All commits should be made in a "forked" repository, not in this
repository.

It is **strongly recommended** to create a new branch based on the
`main` branch, rather than committing directly to `main`.

### Commit description

Quoting roughly from the Git Reference Manual, Git commits are
documented with a short, one-line title which summarizes the changes,
followed by a more thorough, long description.  The title should be no
more than 75 characters.  It is important that at least the title be
filled in with a meaningful summary so that the Git history will be
readable.  Hyperlinks or other references such as "Fixes #" may be
included in the long description, but not in the title and not as a
substitute for a complete description of the changes.

3\. Code review
---------------

A pull request is reviewed by at least one other person than the
contributor before it can be merged.

If a review suggests expanding the scope of the changes to include
additional functionality, those changes do not have to be addressed in
the current pull request but may be handled in a separate, new pull
request.

4\. Documentation
-----------------
Please document the individual work steps in the script with a comment.

* If a new section is started, please leave a multi-line comment
* A single-line comment is sufficient for each statement within a section

Example:

    ###############################################################################
    #                                                                             #
    # Read data from postgres catalog                                             #
    #                                                                             #
    ###############################################################################

    # open database connection
    conn = psycopg2.connect(
                host     = hostname,
                dbname   = database,
                user     = username,
                password = pwd,
                port     = port_id)


5\. Testing
-----------

All enhancements or changes should be tested before they are submitted in a pull request.

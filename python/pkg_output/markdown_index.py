from pkg_output import mermaid

def create_markdown_index_file(table_names, combined, desired_columns):

    ###############################################################################
    #                                                                             #
    # Create index file for Markdown files                                        #
    #                                                                             #
    ###############################################################################

    # Content of the file
    
    content =   "---\n" + "title: Derived Table Documentation" + "\n---\n\n"

    # Create the files for each table inside the table list
    for tbl in table_names:

        """
        The loop go through the table name list. 
        To get the content for the specific table from the DataFrame, you have to compare 
        the table name from the table name list with the table name in the 
        DataFrame.
        """
        
        # Create a DataFrame for the content from the specific table
        tbl_df          = combined[desired_columns][combined.table == tbl]
        
        ###############################################################################
        #                                                                             #
        # Template                                                                    #
        #                                                                             #
        ###############################################################################     

        # Section header
        h2              = "## Documentation: " + "[" + tbl + "]" + "(" + tbl + ".md)" + "\n\n"
        
        # Section table
        h3              = "### Attributes:\n\n"
        markdown_table  = tbl_df.fillna('').to_markdown(index=False)

        # Section mermaid er diagram
        if mermaid.getMermaid_text(tbl) != '':

            mermaid_diagram = """\n\n### ER diagram\n\n```mermaid\n"""

            mermaid_diagram += mermaid.getMermaid_text(tbl)

            mermaid_diagram += """\n```"""
        
        else:

            mermaid_diagram = ''

        ###############################################################################
        #                                                                             #
        # Combine all components from template                                        #
        #                                                                             #
        ###############################################################################        

        content += h2 + h3 + markdown_table + mermaid_diagram + "\n\n"

    ###############################################################################
    #                                                                             #
    # Create file on system                                                       #
    #                                                                             #
    ############################################################################### 

    file_name = "../docs/derived/index.md"
    md_file   = open(file_name, "w")
    md_file.write(content)
    md_file.close()
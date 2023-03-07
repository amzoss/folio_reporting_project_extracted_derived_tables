def create_markdown_files(table_names, combined, desired_columns):

    ###############################################################################
    #                                                                             #
    # Markdown output as file for each table                                      #
    #                                                                             #
    ###############################################################################

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
        title           = "---\n" + "title: " + tbl   + ".sql" + "\n---\n"
        h1              = "# Documentation: " + tbl   + ".sql\n\n"
        
        # Section table
        h2              = "## Attributes:\n\n"
        markdown_table  = tbl_df.fillna('').to_markdown(index=False)

        # Section mermaid er diagram
        # ToDo
        mermaid_diagram = ''

        ###############################################################################
        #                                                                             #
        # Combine all components from template                                        #
        #                                                                             #
        ###############################################################################        

        markdown_output_string = title + h1 + h2 + markdown_table + mermaid_diagram

        ###############################################################################
        #                                                                             #
        # Create file on system                                                       #
        #                                                                             #
        ############################################################################### 

        file_name = "../Output/" + tbl + ".md"
        md_file   = open(file_name, "w")
        md_file.write(markdown_output_string)
        md_file.close()
from pkg_output import mermaid

def create_html_files(table_names, combined, desired_columns):
    
    ###############################################################################
    #                                                                             #
    # html output as file for each table                                          #
    #                                                                             #
    ###############################################################################

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
        html_header     =  "<!DOCTYPE html>"\
                           "<html lang='en'>"\
                           "<head>"\
                           "<title>" + tbl + ".sql</title>"\
                           "<meta charset='utf-8'>"\
                           "</head>"\
                           "<body>"
        
        header          =  "<h1>Documentation: " + tbl + ".sql</h1>"\
                           "<hr border='1'>"
        
        # Section table   
        html_table      = tbl_df.fillna('').to_html(index=False)

        # Section mermaid er diagram        
        if mermaid.getMermaid_text(tbl) != '':
        
            mermaid_diagram = """
            <!-- ER-diagramm with mermaid -->
            <h2>ER-diagram:</h2>
            <div class="mermaid">
            """
            mermaid_diagram += mermaid.getMermaid_text(tbl)

            mermaid_diagram += """
           </div>
           <!-- Script to generate the diagram -->
           <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
           <script>mermaid.initialize({startOnLoad:true});</script>
           """
        
        else:

            mermaid_diagram = ''

        # Section Footer
        footer          =  "</body></html>"

        ###############################################################################
        #                                                                             #
        # Combine all components from template                                        #
        #                                                                             #
        ###############################################################################        

        html_output_string = html_header + header + html_table + mermaid_diagram + footer

        ###############################################################################
        #                                                                             #
        # Create file on system                                                       #
        #                                                                             #
        ############################################################################### 

        file_name = "../docs/derived/" + tbl + ".html"
        html_file = open(file_name, "w")
        html_file.write(html_output_string)
        html_file.close()

from pkg_output import mermaid

def create_html_index_file(table_names, combined, desired_columns):

    ###############################################################################
    #                                                                             #
    # Create index file for HTML files                                        #
    #                                                                             #
    ###############################################################################

    # Content of the file

    title = "Derived Table Documentation"

    html_header     =  "<!DOCTYPE html>"\
                    "<html lang='en'>"\
                    "<head>"\
                    "<meta charset='utf-8'>"\
                    "<meta http-equiv='X-UA-Compatible' content='IE=edge'>"\
                    "<meta name='viewport' content='width=device-width, initial-scale=1'>"\
                    "<!-- Begin Jekyll SEO tag v2.8.0 -->"\
                    "<title>" + title + "</title>"\
                    "<meta name='generator' content='Jekyll v3.9.3' />"\
                    "<meta property='og:title' content='" + title + "' />"\
                    "<meta property='og:locale' content='en_US' />"\
                    "<meta name='description' content='Project to document extracted and derived tables' />"\
                    "<meta property='og:description' content='Project to document extracted and derived tables' />"\
                    "<meta property='og:site_name' content='folio_reporting_project_extracted_derived_tables' />"\
                    "<meta property='og:type' content='website' />"\
                    "<meta name='twitter:card' content='summary' />"\
                    "<meta property='twitter:title' content='" + title + "' />"\
                    "<script type='application/ld+json'>"\
                    "{'@context':'https://schema.org','@type':'WebPage','description':'Project to document extracted and derived tables','headline':'"+ title + "'}</script>"\
                    "<!-- End Jekyll SEO tag -->"\
                    "<link rel='stylesheet' href='../assets/main.css'>"\
                    "</head>"\
                    "<body>"\
                    "<header class='site-header' role='banner'>"\
                    "<div class='wrapper'><a class='site-title' rel='author' href='../'>folio_reporting_project_extracted_derived_tables</a><nav class='site-nav'>"\
                    "<input type='checkbox' id='nav-trigger' class='nav-trigger' />"\
                    "<label for='nav-trigger'>"\
                    "<span class='menu-icon'>"\
                        "<svg viewBox='0 0 18 15' width='18px' height='15px'>"\
                        "<path d='M18,1.484c0,0.82-0.665,1.484-1.484,1.484H1.484C0.665,2.969,0,2.304,0,1.484l0,0C0,0.665,0.665,0,1.484,0 h15.032C17.335,0,18,0.665,18,1.484L18,1.484z M18,7.516C18,8.335,17.335,9,16.516,9H1.484C0.665,9,0,8.335,0,7.516l0,0 c0-0.82,0.665-1.484,1.484-1.484h15.032C17.335,6.031,18,6.696,18,7.516L18,7.516z M18,13.516C18,14.335,17.335,15,16.516,15H1.484 C0.665,15,0,14.335,0,13.516l0,0c0-0.82,0.665-1.483,1.484-1.483h15.032C17.335,12.031,18,12.695,18,13.516L18,13.516z'/>"\
                        "</svg>"\
                    "</span>"\
                    "</label>"\
                    "<div class='trigger'><a class='page-link' href='../extracted/'>Extracted Table Documentation</a><a class='page-link' href='../derived/'>Derived Table Documentation</a></div>"\
                    "</nav></div>"\
                "</header>"\
                "<main class='page-content' aria-label='Content'>"
    header          =  "<h1 class='post-title'>" + title + "</h1>"\
                    "<hr border='1'>"\
                    "<div style='margin: 0 2em 0 2em;'>"
    
    content =   html_header + header

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
        h2              = "<h2>Documentation: " + "[" + tbl + "]" + "(" + tbl + ".html)" + "</h2>\n\n"
        
        # Section table
        h3              = "<h3>Attributes:</h3>\n\n"
        html_table  = tbl_df.fillna('').to_html(index=False)

        # Section mermaid er diagram
        if mermaid.getMermaid_text(tbl) != '':


            mermaid_diagram = """
            <!-- ER-diagramm with mermaid -->
            <h3>ER-diagram:</h3>
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
        footer          =   "</div></main>"\
                            "<footer class='site-footer h-card'>"\
                            "<data class='u-url' href='/folio_reporting_project_extracted_derived_tables/'></data>"\
                            "<div class='wrapper'>"\
                                "<h2 class='footer-heading'>folio_reporting_project_extracted_derived_tables</h2>"\
                                "<div class='footer-col-wrapper'>"\
                                "<div class='footer-col footer-col-1'>"\
                                    "<ul class='contact-list'>"\
                                    "<li class='p-name'>folio_reporting_project_extracted_derived_tables</li></ul>"\
                                "</div>"\
                                "<div class='footer-col footer-col-2'><ul class='social-media-list'></ul>"\
                            "</div>"\
                                "<div class='footer-col footer-col-3'>"\
                                    "<p>Project to document extracted and derived tables</p>"\
                                "</div>"\
                                "</div>"\
                            "</div>"\
                            "</footer>"\
                            "</body></html>"

        ###############################################################################
        #                                                                             #
        # Combine all components from template                                        #
        #                                                                             #
        ###############################################################################        

        content += h2 + h3 + html_table + mermaid_diagram + "\n\n" + footer

    ###############################################################################
    #                                                                             #
    # Create file on system                                                       #
    #                                                                             #
    ############################################################################### 

    file_name = "../docs/derived/index.html"
    md_file   = open(file_name, "w")
    md_file.write(content)
    md_file.close()
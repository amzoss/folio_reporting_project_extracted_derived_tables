import requests
import os.path

def getMermaid_text(tbl):  
    
    ###############################################################################
    #                                                                             #
    # Fetch mermaid text                                                          #
    #                                                                             #
    ###############################################################################    
    
    # Prepare string for the url source
    url      = 'https://raw.githubusercontent.com/stdombek/folio_reporting_project_extracted_derived_tables/main/data/mermaid/' + tbl + '.txt'

    # Fetch data from the server and save it in the object "response"
    response = requests.get(url)

    # If the connection is etablished and file exists
    if response.status_code == 200:

        # Write the data from the server in the local file
        file_name = "../data/mermaid/" + tbl + ".txt"
        mermaid_file  = open(file_name, "w")
        mermaid_file.write(response.text)
        mermaid_file.close() 

        # Create a String with the mermaid text from file
        mermaid_file_data = response.text

    # If the connection is not etablished or file not exists (fallback)
    else:

        # path
        file_name = "../data/mermaid/" + tbl + ".txt"

        # If file exists on system        
        if os.path.isfile(file_name):

            # Create a String with the mermaid text from file from the local file
            mermaid_file  = open(file_name, "r")
            mermaid_file_data     = ''
            for line in mermaid_file:
                mermaid_file_data += line
            mermaid_file.close()
        
        # If file doesn't exists on system
        else:

            mermaid_file_data = ''

    # Close the connection
    response.close()

    ###############################################################################
    #                                                                             #
    # return mermaid text                                                         #
    #                                                                             #
    ###############################################################################

    return mermaid_file_data

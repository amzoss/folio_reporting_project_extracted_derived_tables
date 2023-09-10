import os.path

def getMermaid_text(tbl):  
    
    ###############################################################################
    #                                                                             #
    # Fetch mermaid text                                                          #
    #                                                                             #
    ###############################################################################    
    
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

    ###############################################################################
    #                                                                             #
    # return mermaid text                                                         #
    #                                                                             #
    ###############################################################################

    return mermaid_file_data

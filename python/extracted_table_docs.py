"""
-------------------------------------------------------------------------------
extracted_table_docs.py

Author:         Angela Zoss <angela.zoss@duke.edu>
Description:    This script is intended to enable the documentation of  
                extracted tables. To do this, data is taken from RAML documents 
                and combined with manually created data.
-------------------------------------------------------------------------------
Copyright (C) 2018-2023 The Open Library Foundation

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
-------------------------------------------------------------------------------
"""
###############################################################################
#                                                                             #
# Load modules                                                                #
#                                                                             #
###############################################################################

import csv
import io
from io import StringIO
import os.path
import pandas as pd
import requests
import tabulate
import json

# Local packages
#from pkg_output import html, markdown

###############################################################################
#                                                                             #
# Set variables                                                               #
#                                                                             #
###############################################################################

# Set variables for holding data through various stages of retrival and parsing
csv_data    = None
newRows     = []
modName     = None
intName     = None
ldpName     = None
ramlURL     = None
exampleURL  = None
oneRAML     = {}
examples    = {}
urlLookup   = {}
ermProps    = None

###############################################################################
#                                                                             #
# Define functions                                                            #
#                                                                             #
###############################################################################

def create_markdown_files_extracted(table_names, full_df, desired_columns):

    combined_title  = "---\n" + "title: Extracted Table Documentation" + "\n---\n"
    combined_tables = combined_title



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

        headers         = full_df.loc[full_df['LDP Table Name'] == tbl,:].drop(columns=desired_columns).drop_duplicates()

        modName         = headers["Module Name"].to_string(index=False)
        intName         = headers["Interface Name"].to_string(index=False)
        
        # Create a DataFrame for the content from the specific table
        tbl_df          = full_df[desired_columns][full_df['LDP Table Name'] == tbl]
        
        ###############################################################################
        #                                                                             #
        # Template for individual pages                                               #
        #                                                                             #
        ###############################################################################     

        # Section header
        title           = "---\n" + "title: " + tbl + "\n---\n"
        
        # Section source
        h2_source       = "## Source:\n\n"
        p_source        = "Module: " + modName + "\n\n" + "Interface: " + intName + "\n\n"
        
        # Section table
        h2_attr         = "## Attributes:\n\n"
        markdown_table  = tbl_df.fillna('').to_markdown(index=False)


        ###############################################################################
        #                                                                             #
        # Template for combined page                                                  #
        #                                                                             #
        ###############################################################################     

        # Section header
        h2              = "## Documentation: [" + tbl   + "](" + tbl + ".md)\n\n"

        # Section source
        h3_source       = "### Source:\n\n"
        p_source        = "Module: " + modName + "\n\n" + "Interface: " + intName + "\n\n"
        
        # Section table
        h3_attr         = "### Attributes:\n\n"
        markdown_table  = tbl_df.fillna('').to_markdown(index=False)


        ###############################################################################
        #                                                                             #
        # Combine all components from templates                                       #
        #                                                                             #
        ###############################################################################        

        indiv_output_string = title + h2_source + p_source + h2_attr + markdown_table + "\n\n"

        combined_output_string = h2 + h3_source + p_source + h3_attr + markdown_table + "\n\n"

        ###############################################################################
        #                                                                             #
        # Create file on system                                                       #
        #                                                                             #
        ############################################################################### 

        combined_tables = combined_tables + combined_output_string
        
        file_name = "docs/extracted/" + tbl + ".md"
        md_file   = open(file_name, "w")
        md_file.write(indiv_output_string)
        md_file.close()
    
    full_file_name = "docs/extracted/index.md"
    full_md_file   = open(full_file_name, "w")
    full_md_file.write(combined_tables)
    full_md_file.close()

# TO DO: would be good to catch an exception for json.loads,
# but should it happen in this function? where this function
# gets called? both? maybe this doesn't need to be a function?

def getAllProps(ramlURL):

    # fetch the RAML data from the URL, parse it as JSON, then
    # extract and return the "properties" object

    url = ramlURL
    print("fetching URL: " + url)

    response = requests.get(url)

    #print(response)

    if response.status_code == 200:

        data = json.loads(response.text)
        #print(data)

        props = data["properties"]
        #print(props)
        return props        

    # If the TSV is not available
    else:
        
        # Show the error message for the user
        print("Oh, something went wrong! Cannot fetch RAML file from GitHub")
        print(response.status_code)

    # Close the connection
    response.close()


def grabERMdocs():

    #print("Grabbing ERM docs")

    # A special .tsv file was created to descript the ERM tables. Parse it into a dict
    # that can be used to look up the correct row information for each interface.

    ERMurl = 'https://raw.githubusercontent.com/folio-org/ldp-erm-doc/master/erm-reporting-data-dictionary.tsv'

    response = requests.get(ERMurl)

    # If the connection is established
    if response.status_code == 200:

        # Create a DataFrame with pandas for the data from the server
        erm_data = pd.read_csv(StringIO(response.text),delimiter='\t')
        #print(erm_data)

        grouped = erm_data.groupby('Internal Table')

        rowsByInterface = {}

        for name, group in grouped:
            rowsByInterface[name] = group

        #print(rowsByInterface['mod_agreements.subscription_agreement'])
        return rowsByInterface
        

    # If the TSV is not available
    else:
        
        # Show the error message for the user
        print("Oh, something went wrong! Cannot fetch ERM tsv file from GitHub")
        print(response.status_code)

    # Close the connection
    response.close()

def propsToRows(modName, intName, ldpName, props, ramlPath, prefix):

    # The JSON properties object is passed into this function, along with
    # other table information and an optional prefix. This function is
    # recursive, which means that nested properties can be parsed by 
    # calling the function from inside the function. The "prefix" argument
    # is used during recursion to keep track of what level the parser
    # is at.

    #print("propsToRows: " + ldpName + ", " + prefix)

    # create an array to store a row for each property
    propArray = []

    # iterate through the properties
    for prop in props:

        propName = prop

        #print(propName)
        
        # if this is a nested property, add the prefix to the name of the property
        if prefix != '':
            propName = prefix + '/' + propName

        propValue = props[prop]

        #print(propValue.get("$ref"))

        if propValue.get("$ref"):

            #print("Found a $ref, try to follow path")

            # Some schemas have references to common files stored elsewhere. An example is the
            # metadata object included in almost every FOLIO record.

            # If we find a $ref key in the property information, we should try to follow that
            # path to get the additional property information that is stored in that other file.

            # The path included in $ref might be relative to the schema's current location, so
            # we may need to generate the path to the $ref file from the original RAML URL.

            ramlDir = ramlPath[0:ramlPath.rindex("/")+1]
            refURL = ramlDir + propValue["$ref"]

            # However, if the $ref path includes "raml-util", that's pointing to another repository
            # just called folio-org/raml. We can discard most of the path info and just add the
            # final directory and file name to the default branch of the folio-org/raml repository.

            if propValue["$ref"].find("raml-util") != -1:
                # need to clean up extra path information, and then "raml-util" 
                # can be replaced with "https://raw.githubusercontent.com/folio-org/raml/raml1.0"
                refURL = propValue["$ref"].replace("../","").replace("../../","").replace("/raml-util","raml-util").replace("raml-util","https://raw.githubusercontent.com/folio-org/raml/raml1.0")
            
            print("fetching $ref URL: " + refURL)

            response = requests.get(refURL)

            # If the connection is established to refURL
            if response.status_code == 200:

                data = json.loads(response.text)

                #print(data)

                # If everything has gone well and we were able to fetch the property info from the
                # $ref and parse it as JSON, we can just use that data instead of the original
                # propValue data.
                propValue = data


            # If the refURL is not available
            else:
                
                # Show the error message for the user
                print("Oh, something went wrong! Cannot fetch $ref file from URL: " + refURL)
                print(response.status_code)

            # Close the connection
            response.close()

        propType = propValue.get("type")

        # build an array for the spreadsheet row, combining tab 1 info with the name, 
        # type, and description of the current property. add this row to the storage array.
        newRow = [[modName, intName, ldpName, propName, propType, propValue.get("description")]]
        #print(newRow)
        propArray.extend(newRow)
        
        # after creating a row for the property, check if it's an object or an array of objects.

        # for objects, find the nested properties object and start the process over again. The
        # result of that will be another array of arrays. Add that into the storage array, 
        # just like the top-level properties.
        # Note: not all objects have a nested properties object in these RAML files. The
        # object may reference another schema. In the API documentation, those references
        # are filled in and you see the nested properties, but in the source data on GitHub,
        # there might just be a reference.

        if propType == "object":
            if propValue.get("properties"):
                newPropArray = propsToRows(modName, intName, ldpName, propValue["properties"], ramlPath, propName)
                propArray.extend(newPropArray)
            
        elif propType == "array":

            # For arrays, look for a key named "items", and then look for "properties" in that key.
            # If you find another properties object, start the parsing over again. The
            # result of that will be another array of arrays. Add that into the storage array, 
            # just like the top-level properties.

            #print("propName: " + propName + "\npropValue Type: " + propValue["type"] + "\npropValue items: " + propValue["items"])
            #print("has properties? " + propValue.hasOwnProperty('items'))
            if propValue.get('items'):
                if propValue['items'].get('properties'):
                    itemProps = propValue["items"]["properties"]
                    newPropArray = propsToRows(modName, intName, ldpName, itemProps, ramlPath, propName)
                    propArray.extend(newPropArray)
                
    
    # After all of the loops are done, return the full array of arrays, which contain
    # all of the parse-able properties in individual rows.
    return propArray


###############################################################################
#                                                                             #
# Fetch csv data                                                              #
#                                                                             #
# TODO: change this to work with GitHub Actions, which should check out       #
#   a full copy of the repository                                             #
#                                                                             #
###############################################################################

csv_data = pd.read_csv("data/csv/RAMLdirectory.csv")
#print(csv_data)

# Call the grabERMdocs() function to pull data for ERM tables using
# a different method. Store the results in a variable called ermProps.

ermProps = grabERMdocs()

###############################################################################
#                                                                             #
# Fetch and parse RAML data using csv data                                    #
#                                                                             #
###############################################################################

#print("starting the parse")

# This function takes on the bulk of the work to retrieve the 
# schema information, parse it into a table, and push it to
# the second tab of the spreadsheet.

# There are many calls to Logger.log() to keep track of the 
# progress of the script. Just open the "Execution log" to 
# see the messages.


# First, grab the data from the first tab of the spreadsheet
# and store it in a variable called "rows".

for index, row in csv_data.iterrows():
    #print(row)

    # Loop through each schema from the CSV file
    print("starting RAML loop: " + str(index))
    
    # For each row, save the data from each column
    modName = row['Module']
    #print(modName)
    intName = row['Interface']
    #print(intName)
    ldpName = row['LDP table name']
    #print(ldpName)
    ramlURL = row['Schema URL']
    #print(ramlURL)
    exampleURL = row['Example URL']
    #print(exampleURL)
    
    apiUrl = row['Dev API URL']
    urlLookup[intName] = apiUrl
    
    #print(urlLookup);

    # if there is a row without a ramlURL, just skip it entirely
    if pd.notna(ramlURL):

        # if there is a row without an example URL, just leave that blank
        exampleJson = ''

        if pd.notna(exampleURL):
            response = requests.get(exampleURL)

            # If the connection is established to refURL
            if response.status_code == 200:

                exampleJson = response.text

            # If the refURL is not available
            else:
                
                # Show the error message for the user
                print("Oh, something went wrong! Cannot fetch example JSON from URL: " + exampleURL)
                print(response.status_code)

            # Close the connection
            response.close()                
        
        examples[ldpName] = exampleJson; 
        
        # Extract the properties from the RAML URL with a separate function and save
        # to a variable named "oneRAML". The properties will be in the form of a JSON object.
        #print("getting props")
        oneRAML = getAllProps(ramlURL)
        
        # Start building an array to store the properties in tabular form. This will
        # be an array of arrays, which is what is required to fill data into the second 
        # tab of the Google Sheet. The first element added to the array is a subheading 
        # row, which presents basic table info from the first spreadsheet tab. 
        
        #propArray = [[modName, intName, ldpName, '', '', '']]
        propArray = []
        
        # Call the propsToRows() function, which takes some of the information
        # from the first tab and the JSON object containing the properties and
        # returns the parsed data in an array of arrays.
        propRows = propsToRows(modName, intName, ldpName, oneRAML, ramlURL, '')
        
        # Add the tabular form of the properties to the same array with the subheading.
        propArray.extend(propRows)
        
        # Add the combined array of arrays to the growing array that stores the data from 
        # all of the various RAMLs.
        newRows.extend(propArray)
        
        print("ending RAML loop " + str(index) + " with newRows of length " + str(len(newRows)))

    
    elif modName == 'mod_agreements':

        # mod_agreements is different, so even though it doesn't have a URL, still look for data  
        
        # for each interface row, want to add a header to newRows,
        # pull out all the data rows from the TSV,
        # add those rows after header to newRows array
        
        # so, ermProps should be a dict where you can lookup all data rows
        # for an interface at once, but then rows should already be formatted for 
        # newRows
        
        #print(newRows)

        #newRows.extend([[modName, intName, ldpName, '', '', '']])

        #print(newRows)

        ermLookup = modName + '.' + intName
        
        newERMRows = ermProps[ermLookup]
        #print(newERMRows)
        
        for index, row in newERMRows.iterrows():
            newRows.extend([[modName, intName, ldpName, row['Column Name'], '', row['Data Element Description']]])
            

full_data = pd.DataFrame(newRows, columns=['Module Name', "Interface Name", "LDP Table Name", "Property Name", "Property Type",	"Property Description"])
#print(full_data)
#full_data.to_csv("docs/full_data.csv", index=False)

create_markdown_files_extracted(full_data['LDP Table Name'].unique(), full_data, ["Property Name", "Property Type",	"Property Description"])


###############################################################################
#                                                                             #
# Output                                                                      #
# Create files for each table                                                 #
#                                                                             #
###############################################################################

# html
#html.create_html_files(table_names, combined, desired_columns)

# markdown
#markdown.create_markdown_files(table_names, combined, desired_columns)


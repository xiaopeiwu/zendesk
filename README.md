# Zendesk ML Eng Coding Challenge 2021  
This is a simple Python command line tool to search for Zendesk data and return readable results. It is my solution to the Zendesk ML Eng coding challenge.  
  
This script was written in Python 3.8 and tested on macOS Linux. Ideally it should be run using Python 3.6+ in a Unix/Linux environment.
## Usage
1. Clone the repo  
2. Create a virtual env using Python 3. From your project directory, run  
`virtualenv --python=<path_to_your_python3> zendesk`  
   and activate the virtual env with  
   `source ./zendesk/bin/activate`
3. Install required packages using  
`pip install -r requirements.txt`
4. To search, use the `search` command. Specify a dataset to search on, a field to search for, and a value to search with using options. For example:  
`python zendesk.py search --data users --field _id --value 11`  
`python zendesk.py search -d tickets -f via -v web`   
`python zendesk.py search -d organizations -f name -v Bitrex`   
5. To search for empty values, the `--value` option can be omitted.
6. To list all searchable fields for a specific dataset, use the `fields` command. You can specify a dataset to list the fields, or the command will list fields for all datasets by default. For example:
`python zendesk.py fields` (will list fields for all datasets)  
`python zendesk.py fields -d users` (will list fields for users)  
7. Use the `--help` option to see the help docs when needed.  
`python zendesk.py` or `python zendesk.py --help` (will show the main help doc)  
`python zendesk.py [search|fields] --help` (will show the help docs for each command)   
   
## Assumptions  
- The `_id` field of all entities are not empty and unique.
- All timestamps are formatted in the ISO string format `yyyy-MM-dd'T'HH:mm:ss ZZ`. 
- For empty value searches, if an entity is missing a field, that field is presumed to be empty and a search for that field with an empty value will return said entity. For example, `python zendesk.py -d users -f email` will return users without an `email` field.
- For any associated entities, only the important identifiers are displayed (such as the name and Id of a user/organization and the subject and Id of a ticket). The printout of a returned result is a combination of the original data of that entity and the important identifiers of any associated entity, displayed in a readable format.


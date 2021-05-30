# Zendesk ML Eng Coding Challenge 2021  
This is a simple Python command line tool to search for Zendesk data and return readable results. It is my solution to the Zendesk ML Eng coding challenge.  
  
This script was written in Python 3.8 and tested on macOS Linux. Ideally it should be run using Python 3.6+ in a Unix/Linux environment.
## Usage
1. Clone the repo;  
2. Create a virtual environment using Python 3. From your project directory, run:  
`virtualenv --python=<path_to_your_python3> zendesk`  
   and activate the virtual env with:  
   `source ./zendesk/bin/activate`
3. Install required packages using:  
`pip install -r requirements.txt`
4. To search, use the `search` command. Specify a dataset to search on, a field to search for, and a value to search with, using the options `-d` `-f` and `-v` respectively. When the `-v` field is more than 1 word long, put it in double quotation marks. For example:  
`python zendesk.py search --data users --field _id --value 11`  
`python zendesk.py search -d tickets -f via -v web`   
`python zendesk.py search -d organizations -f tags -v "Rhode Island"`   
5. To search for empty values, the `-v` option can be empty or be omitted.
6. To list all searchable fields for a specific dataset, use the `fields` command. You can specify a dataset to list the fields, or the command will list fields for all datasets by default. For example:  
`python zendesk.py fields` (will list fields for all datasets)  
`python zendesk.py fields -d users` (will list fields for users)  
7. Use the `--help` option to see the help docs when needed.  
`python zendesk.py` or `python zendesk.py --help` (will show the main help doc)  
`python zendesk.py [search|fields] --help` (will show the help docs for each command)
8. To run the included tests, use the below command from the project directory:  
`python -m pytest tests --html=report.html`  
   This will generate a detailed test report that can be viewed in a browser.
   
## Assumptions  
- The `_id` field of all entities are not empty and unique.
- All timestamps are formatted in the ISO string format `yyyy-MM-dd'T'HH:mm:ss ZZ`. 
- For empty value searches, if an entity is missing a field, that field is presumed to be empty and a search for that field with an empty value will return said entity. For example, `python zendesk.py -d users -f email` will return users without an `email` field.
- For any associated entities, only the important identifiers are displayed (such as the name and Id of a user/organization and the subject and Id of a ticket). The printout of a returned result is a combination of the original data of that entity and the important identifiers of any associated entity, displayed in a readable format.

## Sample outputs
### Sample user search
- command used: `zendesk % python zendesk.py search -d users -f _id --value 13`
```Loading data...

Tickets data loaded from data/tickets.json
Users data loaded from data/users.json
Organizations data loaded from data/organizations.json

Searching users for _id with the value 12...

Found 1 result(s):

Id:                   12
Name:                 Watkins Hammond
Alias:                Mr Sally
Signature:            Don't Worry Be Happy!
Email:                sallyhammond@flotonic.com
Phone:                8144-293-283
Time zone:            United Kingdom
Locale:               en-AU
Organization:         Kindaloo
Organization Id:      110
Role:                 end-user
URL:                  http://initech.zendesk.com/api/v2/users/12.json
External Id:          38899b1e-89ca-43e7-b039-e3c88525f0d2
Tags:                 Bonanza, Balm, Fulford, Austinburg
Active:               False
Verified:             False
Shared:               False
Suspended:            False
Created at:           Thu, 21 Jul 2016 12:26 PM UTC-10:00
Last login at:        Sat, 29 Dec 2012  7:59 AM UTC-11:00
Submitted tickets:    
  - A Drama in Cayman Islands  (Id: be0f613a-e7f7-4833-9342-643b0d9b9fca)
  - A Catastrophe in New Zealand  (Id: c48bf827-fc45-4158-b7ce-70784509f562)
  - A Drama in Mauritius  (Id: 045b0fe9-8e17-4eec-af9c-cc00ce5b9ed1)
Assigned tickets:     
  - A Catastrophe in Macau  (Id: 35072cd7-e343-4d8e-a967-bbe32eb019cb)
  - A Drama in Germany  (Id: 774765fe-7123-4131-8822-e855d3cad14c)
  - A Nuisance in Namibia  (Id: 50f3fdbd-f8a6-481d-9bf7-572972856628)
```
## Sample ticket search
- command used: ``


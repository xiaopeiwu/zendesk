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
4. To search, use the `search` command. Specify a dataset to search on, a field to search for, and a value to search with, using the options `-d` `-f` and `-v` respectively. When the `-v` option contains whitespace, put it in quotation marks. For example:  
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
```
Loading data...

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
### Sample ticket search
- command used: `python zendesk.py search -d tickets -f assignee_id -v 29`
```
Loading data...

Tickets data loaded from data/tickets.json
Users data loaded from data/users.json
Organizations data loaded from data/organizations.json

Searching tickets for assignee_id with the value 29...

Found 2 result(s):

Id:                   6aac0369-a7e5-4417-8b50-92528ef485d3
Subject:              A Nuisance in Latvia
Priority:             urgent
Status:               hold
Description:          Laboris laborum culpa sit culpa minim ad laborum Lorem laboris aliqua tempor. Aliqua sit nisi deserunt eu quis ipsum incididunt aute excepteur cillum.
Organization name:    Noralex
Organization Id:      113
URL:                  http://initech.zendesk.com/api/v2/tickets/6aac0369-a7e5-4417-8b50-92528ef485d3.json
External Id:          0c2ba6c6-ea9a-4a58-ada4-bc72f3b9ff39
Tags:                 Washington, Wyoming, Ohio, Pennsylvania
Created at:           Wed, 15 Jun 2016 12:03 PM UTC-10:00
Due at:               Tue, 16 Aug 2016  5:52 AM UTC-10:00
Has incidents:        False
Via:                  chat
Submitter:            Daniel Agüilar (Id: 50)
Assignee:             Herrera Norman (Id: 29)


Id:                   ffe688cd-402f-4e37-8597-88b3811bbf46
Subject:              A Problem in Vatican City Ştate (Holy See)
Priority:             urgent
Status:               open
Description:          Ullamco enim id proident cillum tempor fugiat consequat non enim ad. Consectetur nostrud consequat deserunt consequat sit deserunt cillum esse eu ut fugiat.
Organization name:    Xylar
Organization Id:      104
URL:                  http://initech.zendesk.com/api/v2/tickets/ffe688cd-402f-4e37-8597-88b3811bbf46.json
External Id:          a264d753-d2c3-4f50-ba8f-299bf8070f67
Tags:                 District Of Columbia, Wisconsin, Illinois, Fédératéd Statés Of Micronésia
Created at:           Wed, 03 Feb 2016  5:47 AM UTC-11:00
Due at:               Sat, 06 Aug 2016  7:28 AM UTC-10:00
Has incidents:        False
Via:                  web
Submitter:            John Floyd (Id: 44)
Assignee:             Herrera Norman (Id: 29)
```

### Sample organization search
- command used: `python zendesk.py search -d organizations -f name -v Bitrex` 
```
Loading data...

Tickets data loaded from data/tickets.json
Users data loaded from data/users.json
Organizations data loaded from data/organizations.json

Searching organizations for name with the value Bitrex...

Found 1 result(s):

Id:                124
Name:              Bitrex
Details:           Non profit
URL:               http://initech.zendesk.com/api/v2/organizations/124.json
External Id:       15c21605-cbc6-440f-8da2-6e1601aed5fa
Tags:              Lott, Hunter, Beasley, Glass
Domain names:      unisure.com, boink.com, quinex.com, poochies.com
Created at:        Wed, 11 May 2016 12:16 PM UTC-10:00
Shared tickets:    True
Users:             
  - Francis Rodrigüez (Id: 19)
  - Russo Vincent (Id: 22)
  - Jennifer Gaines (Id: 39)
  - Harper Sandoval (Id: 45)
  - Spence Tate (Id: 54)
Tickets:           
  - A Nuisance in Egypt  (Id: 01731a8f-7c00-40ca-94a1-6b874abd1d17)
  - A Drama in Georgia  (Id: 31ec2df9-edaf-496e-b05a-ca6a75ddcc67)
  - A Drama in Germany  (Id: 774765fe-7123-4131-8822-e855d3cad14c)
  - A Catastrophe in Sierra Leone  (Id: 8ea53283-5b36-4328-9a78-f261ee90f44b)
  - A Catastrophe in Central African Republic  (Id: 5315f036-2bdd-4d6e-a356-fc6759c74351)
  - A Catastrophe in Belize  (Id: ba4feaec-47ac-483f-bc3d-2604f797e6f0)
  - A Problem in Marshall Islands  (Id: 9216c7b3-9a7b-40cb-8f96-56fca79520eb)
  - A Catastrophe in Tuvalu  (Id: 10378588-afec-443e-a0a5-6c707eb1c2e4)
  - A Problem in Saint Kitts and Nevis  (Id: a7b16a5c-76d9-4e60-aadc-33653b828173)
  - A Catastrophe in Netherlands Antilles  (Id: 7ef6cf9f-121d-41e7-832c-68d811da9379)
```

### When no results are found
- command used: `python zendesk.py search -d users -f name -v "Roger Federer"`
```
Loading data...

Tickets data loaded from data/tickets.json
Users data loaded from data/users.json
Organizations data loaded from data/organizations.json

Searching users for name with the value Roger Federer...

Sorry, no results found for this search.
```

### When the field provided is not valid for the specified dataset
- command used: `python zendesk.py search -d users -f id -v 11`
```
Loading data...

Tickets data loaded from data/tickets.json
Users data loaded from data/users.json
Organizations data loaded from data/organizations.json

Searching users for id with the value 11...

'id' is not a valid field for users.
You can search users with one of the below fields:
organization_id
created_at
active
tags
signature
suspended
timezone
phone
alias
shared
_id
url
locale
name
email
last_login_at
verified
role
external_id
```

### Listing searchable fields
- command used: `python zendesk.py fields -d organizations`
```
You can search tickets with one of the below fields:
url
description
external_id
_id
subject
has_incidents
type
assignee_id
tags
via
status
due_at
priority
submitter_id
created_at
organization_id
```
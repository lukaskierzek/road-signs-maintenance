## Road sign maintenance

This is a very early version of the project. This project is designed to support collection and management of information about damaged road signs.

## Backend

Backend is written in Django and Django Rest Framework.

## Frontend

Frontend will be written in Vue.js.

## Project status

*The following task list is not in particular order.*

- [x] Display a table with information,
- [x] Sign in capability,
- [ ] Display information about a particular region, locality, road sign and road signs for repair (*under development*),
- [ ] Modify information by a specific user (*under development*),
- [ ] Adding new task by a specific user (*under development*).

## Database diagram

!['Database diagram'](database_diagram.png 'Database diagram')

Explanation of the database:

- roadsign: Series (e.g. A-20), name (e.g. stop) and description of road sign (e.g. A stop sign),
- area: Area where there may be road signs, e.g., grocery shop,
- locality: Locality where there may be road sign, e.g., Some City,
- roadsignsforrepair: Road sign for repair with information about exact place where is the road sign, e.g., A road sign beside grocery shop on some street

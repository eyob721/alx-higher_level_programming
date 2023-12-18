# 0x0F. Python - Object-relational mapping

## Mandatory

[0-select_states.py](./0-select_states.py)

- This script takes 3 arguments:
  - mysql username
  - mysql password
  - database name
- For the purpose of this tasks, the arguments are not validated. And so the
 database name is assumed to be `hbtn_0e_0_usa` which has the table `states`.
- The sql file used to create the database `hbtn_0e_0_usa` can be found [here](./sql/0-select_states.sql).
- The script takes the 3 arguments and displays all the `states` from the
 database `hbtn_0e_0_usa`.

[1-filter_states.py](./1-filter_states.py)

- This script lists all states with a name that starts with `N`.

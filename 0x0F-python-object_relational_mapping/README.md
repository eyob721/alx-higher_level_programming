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

[2-my_filter_states.py](./2-my_filter_states.py)

- Unlike the previous scripts, this script takes 4 arguments
  - mysql username
  - mysql password
  - database name
  - state name
- It lists all the states with the given state name.

[3-my_safe_filter_states.py](./3-my_safe_filter_states.py)

- Building on the previous script, this one lists all the states with a given
 state name, while taking care of SQL Injections.

[4-cities_by_state.py](./4-cities_by_state.py)

- This script takes 3 arguments:
  - mysql username
  - mysql password
  - database name
- Database is taken to be `hbtn_0e_4_usa`, and the corresponding sql file can be
 found [here](./sql/4-cities_by_state.sql).
- It lists all the `cities` with their corresponding states from the
 database `hbtn_0e_4_usa`.

[5-filter_cities.py](./5-filter_cities.py)

- This script takes 4 arguments
  - mysql username
  - mysql password
  - database name
  - state name
- It lists all the `cities` that belong in the given state name.

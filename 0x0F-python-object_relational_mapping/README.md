# 0x0F. Python - Object-relational mapping

## Mandatory

[0-select_states.py](./0-select_states.py)

- This script lists all `states` from the database `hbtn_0e_0_usa`.
- The SQL file for the database can be find here: [`hbtn_0e_0_usa`](./sql/0-select_states.sql).
- Requirements:
  - The script should take 3 arguments: `mysql username`, `mysql password` and
    `database name` (no argument validation needed)
  - The module MySQLdb (`import MySQLdb`) must be used
  - The script should connect to a MySQL server running on `localhost` at port `3306`
  - Results must be sorted in ascending order by states.id
  - The code should not be executed when imported

[1-filter_states.py](./1-filter_states.py)

- This script lists all `states` with a name starting with `N` (upper N) from
  the database `hbtn_0e_0_usa`.
- Requirements are same as `0-select_states.py`.

[2-my_filter_states.py](./2-my_filter_states.py)

- This script takes in the state name as an argument (in addition to the mysql
  user, password and database) and displays all values in the states table
  of `hbtn_0e_0_usa` where name matches the argument.
- Usage: `./2-my_filter_states.py username password database state`
- Requirements are same as `0-select_states.py`.

[3-my_safe_filter_states.py](./3-my_safe_filter_states.py)

- In the previous task the state name was to be passed as an argument to the
  script. But this made the script vulnerable to SQL injection attack.
- This script builds on top of the previous script, but this one is safe from
  MySQL injections!
- Usage: `./3-my_safe_filter_states.py username password database state`

[4-cities_by_state.py](./4-cities_by_state.py)

- This script lists all cities from the database `hbtn_0e_4_usa`.
- The SQL file for the database find here: [`hbtn_0e_4_usa`](./sql/4-cities_by_state.sql)
- Requirements:
  - The script should take 3 arguments: `mysql username`, `mysql password` and
    `database name` (no argument validation needed)
  - The module MySQLdb (`import MySQLdb`) must be used
  - The script should connect to a MySQL server running on `localhost` at port `3306`
  - Results must be sorted in ascending order by cities.id
  - The method `execute()` method can only be used once
  - The code should not be executed when imported
- Usage: `./4-cities_by_state.py username password database`

[5-filter_cities.py](./5-filter_cities.py)

- This script, based on 4-cities_by_state.py, takes in the state name as an
  argument (in addition to the mysql user, password and database) and displays
  all cities of that state in the table `hbtn_0e_4_usa`.
- Additional Requirements:
  - The script must be SQL Injection safe
- Usage: `./5-filter_cities.py username password database state`

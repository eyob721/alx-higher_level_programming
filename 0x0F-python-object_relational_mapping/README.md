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

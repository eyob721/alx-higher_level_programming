# 0x0E. SQL - More queries

## Mandatory

[0-privileges.sql](./0-privileges.sql)

- A sql script that lists all privileges of the MySQL users `user_0d_1` and
  `user_0d_2` on your server (in localhost).

[1-create_user.sql](./1-create_user.sql)

- A sql script that creates user `user_0d_1`.
- Rules:
  - `user_0d_1` should have all privileges on the MySQL server
  - The `user_0d_1` password should be set to `user_0d_1_pwd`
  - If the user `user_0d_1` already exists, the script should not fail

[2-create_read_user.sql](./2-create_read_user.sql)

- A sql script that creates the database `hbtn_0d_2` and the user `user_0d_2`.
- Rules:
  - `user_0d_2` should have only `SELECT` privilege in the database `hbtn_0d_2`
  - The `user_0d_2` password should be set to `user_0d_2_pwd`
  - If the either the database `hbtn_0d_2` or the user `user_0d_2` already
    exists, the script should not fail

[3-force_name.sql](./3-force_name.sql)

- A sql script that creates the table force_name on your MySQL server.
- The database name must be passed as an argument to the mysql command

[4-never_empty.sql](./4-never_empty.sql)

- A sql script that creates the table id_not_null on your MySQL server.
- The database name must be passed as an argument to the mysql command

[5-unique_id.sql](./5-unique_id.sql)

- A sql script that creates the table unique_id on your MySQL server.
- The database name must be passed as an argument to the mysql command

[6-states.sql](./6-states.sql)

- A sql script that creates the database `hbtn_0d_usa` and the table `states`
  (in the database `hbtn_0d_usa`).

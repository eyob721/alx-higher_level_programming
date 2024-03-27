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

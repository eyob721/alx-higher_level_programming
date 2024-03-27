# 0x0D. SQL - Introduction

In this project we work with SQL queries, using MySQL.

To check the sql files you can do so like this:

- If you are using `auth_socket` as an authentication method:

```sh
cat example.sql | sudo mysql hbtn_0c_0
```

- or if you are using a password

```sh
cat example.sql | mysql -u root -p hbtn_0c_0
```

The database name we are using is named `hbtn_0c_0`, which can be passed to the
mysql command as an argument, as shown above. And you can also use any other
user other than `root`, provided that the user has sufficient privileges.

## Mandatory

[0-list_databases.sql](./0-list_databases.sql)

- A script that lists all databases of your MySQL server.

[1-create_database_if_missing.sql](./1-create_database_if_missing.sql)

- A script that creates a database named `hbtn_0c_0` in the MySQL server.

[2-remove_database.sql](./2-remove_database.sql)

- A script that deletes the database `hbtn_0c_0` from the MySQL server.

[3-list_tables.sql](./3-list_tables.sql)

- A script that lists all the tables of a database in the MySQL server.

[4-first_table.sql](./4-first_table.sql)

- A script that creates a table called `first_table` in the current database.
- The database name is passed as argument to the mysql command.

[5-full_table.sql](./5-full_table.sql)

- A script that prints the full description of the table `first_table` from the
  `hbtn_0c_0` database.

[6-list_values.sql](./6-list_values.sql)

- A script that prints all the rows from the table `first_table` of `hbtn_0c_0`
  database.

[7-insert_value.sql](./7-insert_value.sql)

- A script that inserts a new row into the table `first_table` of the
  `hbtn_0c_0` database.

[8-count_89.sql](./8-count_89.sql)

- A script that displays the number of records with id = 89 in the table
  `first_table` of `hbtn_0c_0` database.

[9-full_creation.sql](./9-full_creation.sql)

- A script that creates the table `second_table` in the database `hbtn_0c_0`
  and adds multiple rows.

[10-top_score.sql](./10-top_score.sql)

- A script that lists all the records of the table `second_table` of the
  database `hbtn_0c_0`.
- Requirements:
  - only the score and name columns should be displayed (in that order)
  - records should be ordered by score (top first)

[11-best_score.sql](./11-best_score.sql)

- A script that lists all the records with a score >= 10 in the table
  `second_table` of the database `hbtn_0c_0`.
- Requirements:
  - only the score and name columns should be displayed (in that order)
  - records should be ordered by score (top first)

[12-no_cheating.sql](./12-no_cheating.sql)

- A script that updates the score of `Bob` to `10` in the table `second_table`.

[13-change_class.sql](./13-change_class.sql)

- A script that removes all records with a score \<= 5  in the table `second_table`.

[14-average.sql](./14-average.sql)

- A script that computes the score average of all records in the table `second_table`.

[15-groups.sql](./15-groups.sql)

- A script that lists the number of records with the same score in the table
  `second_table`

[16-no_link.sql](./16-no_link.sql)

- Lists all the records of the table `second_table`
  - Requirements:
    - don't list rows with out a name value
    - only the score and the name column should be displayed (in that order)
    - records should be sorted in descending order

## Advanced

[100-move_to_utf8.sql](./100-move_to_utf8.sql)

- A script that converts the database `hbtn_0c_0`, and the table `first_table`,
  to UTF8(utf8mb4, collate utf8mb4_unicode_ci).

[101-avg_temperatures.sql](./101-avg_temperatures.sql)

- For this task and the following tasks a table dump [temperatures.sql](./import/temperatures.sql)
  is imported to `hbtn_0c_0` database.
- The script displays the average temperature (Fahrenheit) by city ordered
  by temperature (descending).

[102-top_city.sql](./102-top_city.sql)

- A script that displays the top 3 of cities temperatures during July(7) and
  August(8), ordered by temperature (descending).

[103-max_state.sql](./103-max_state.sql)

- A script that displays the max temperature of each state (ordered by State name).

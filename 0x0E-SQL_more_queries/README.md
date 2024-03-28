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

[7-cities.sql](./7-cities.sql)

- A sql script that creates the database `hbtn_0d_usa` and the table `cities`
  (in the database `hbtn_0d_usa`).

[8-cities_of_california_subquery.sql](./8-cities_of_california_subquery.sql)

- A sql script that lists all the cities of California that can be found in
  the database `hbtn_0d_usa`.
- The `states` table contains only one record where `name = California`, but
  the id can be different.
- Using `JOIN` is not allowed.

[9-cities_of_california_subquery.sql](./9-cities_by_state_join.sql)

- A sql script that lists all cities, along with thier corresponding state
  names, contained in the database `hbtn_0d_usa`.

[10-genre_id_by_show.sql](./10-genre_id_by_show.sql)

- A sql script that lists shows contained in hbtn_0d_tvshows that have at
  least one genre linked.
- Only one `SELECT` statement is allowed.
- The database name must be passed as an argument to the mysql command

[11-genre_id_all_shows.sql](./11-genre_id_all_shows.sql)

- A sql script that lists all shows contained in `hbtn_0d_tvshows` with their
  genre_id, including those that don't have a genre_id.
- Only one `SELECT` statement is allowed.
- The database name must be passed as an argument to the mysql command

[12-no_genre.sql](./12-no_genre.sql)

- A sql script that lists all shows contained in the `hbtn_0d_tvshows` database
  without a genre linked
- Only one `SELECT` statement is allowed.
- The database name must be passed as an argument to the mysql command

[13-count_shows_by_genre.sql](./13-count_shows_by_genre.sql)

- A sql script that lists all genres from `hbtn_0d_tvshows` and displays the
  number of shows linked to each.
- A genre which doesn't has any shows linked is not displayed.
- Only one `SELECT` statement is allowed.
- The database name must be passed as an argument to the mysql command

[14-my_genres.sql](./14-my_genres.sql)

- A sql script that uses the `hbtn_0d_tvshows` database to list all genres of
  the show Dexter.
- Only one `SELECT` statement is allowed.
- The database name must be passed as an argument to the mysql command

[15-comedy_only.sql](./15-comedy_only.sql)

- A sql that lists all Comedy shows in the database `hbtn_0d_tvshows`.
- Only one `SELECT` statement is allowed.
- The database name must be passed as an argument to the mysql command

-- A sql script that lists all cities, along with thier corresponding state
-- names, contained in the database `hbtn_0d_usa`.
SELECT    cities.id,
          cities.name,
          states.name
FROM      cities
INNER     JOIN states ON cities.state_id = states.id
ORDER BY  cities.id;

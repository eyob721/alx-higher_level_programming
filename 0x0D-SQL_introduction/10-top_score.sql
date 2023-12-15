-- Lists all the records of the table `second_table` of the database `hbtn_0c_0`
-- Requirements:
--    only the score and name columns should be displayed (in that order)
--    records should be ordered by score (top first)
SELECT
  score,
  name
FROM
  second_table
ORDER BY
  score DESC;

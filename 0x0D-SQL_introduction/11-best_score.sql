-- Lists all the records with a score >= 10 in the table `second_table` of the
-- database `hbtn_0c_0`
-- Requirements:
--    only the score and name columns should be displayed (in that order)
--    records should be ordered by score (top first)
SELECT
  score,
  name
FROM
  second_table
WHERE
  score >= 10
ORDER BY
  score DESC;

-- Lists all the records of the table `second_table`
-- Requirements:
--    - don't list rows with out a name value
--    - only the score and the name column should be displayed (in that order)
--    - records should be sorted in descending order
SELECT
  score,
  name
FROM
  second_table
WHERE
  name IS NOT NULL
ORDER BY
  score DESC;

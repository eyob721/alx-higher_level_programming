-- Lists all the records of the table `second_table` of the database `hbtn_0c_0`
-- It doesn't include rows without a name value, and the list is sorted
-- according to the score in descending order
SELECT    score,
          name
FROM      second_table
WHERE     name IS NOT NULL
ORDER BY  score DESC;

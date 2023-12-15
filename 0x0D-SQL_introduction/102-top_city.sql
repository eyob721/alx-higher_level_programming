-- Displays the top 3 of cities temperatures during July(7) and August(8),
-- ordered by temperature (descending)
SELECT
  city,
  avg(value) AS avg_temp
FROM
  temperatures
WHERE
  `month` IN (7, 8)
GROUP BY
  city
ORDER BY
  avg_temp DESC
LIMIT
  3;

-- Lists all shows from hbtn_0d_tvshows_rate by their rating
SELECT    title,
          sum(rate) AS rating
FROM      tv_shows
LEFT JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY  tv_shows.title
ORDER BY  rating DESC;

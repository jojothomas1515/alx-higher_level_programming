-- ratings
SELECT t.title, SUM(tsr.rate) AS rating
FROM tv_shows t
         INNER JOIN tv_show_ratings tsr ON t.id = tsr.show_id
GROUP BY t.title
ORDER BY rating DESC;

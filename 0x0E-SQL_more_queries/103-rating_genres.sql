-- ratings
SELECT name, SUM(tsr.rate) AS rating
FROM tv_shows t
         INNER JOIN tv_show_ratings tsr ON t.id = tsr.show_id
         INNER JOIN tv_show_genres tsg on t.id = tsg.show_id
         INNER JOIN tv_genres tg on tsg.genre_id = tg.id
GROUP BY name
ORDER BY rating DESC;

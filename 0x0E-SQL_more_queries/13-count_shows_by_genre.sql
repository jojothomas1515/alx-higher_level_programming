-- all shows with at least one genre
SELECT name 'genre', COUNT(title) AS number_of_shows
        FROM tv_genres tg
        JOIN tv_show_genres g ON tg.id = g.genre_id
        JOIN tv_shows t ON t.id = g.show_id
GROUP BY name
ORDER BY number_of_shows DESC;

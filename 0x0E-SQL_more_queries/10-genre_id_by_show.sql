-- all shows with at least one genre
SELECT title,
        genre_id
FROM tv_shows t,
        tv_show_genres g
WHERE t.id = g.show_id
ORDER BY t.id,
        g.genre_id ASC;

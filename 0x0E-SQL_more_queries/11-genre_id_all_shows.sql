-- all shows with at least one genre
SELECT title,
        genre_id
FROM tv_shows t
        LEFT JOIN tv_show_genres g
ON t.id = g.show_id
ORDER BY t.title ASC,
        g.genre_id ASC;

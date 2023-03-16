-- all shows with at least one genre
SELECT name
        FROM tv_genres tg
        JOIN tv_show_genres g ON tg.id = g.genre_id
        JOIN tv_shows t ON t.id = g.show_id
WHERE t.title = 'Dexter'
ORDER BY tg.name ASC;

-- all shows with at least one genre
SELECT title
        FROM tv_genres tg
        JOIN tv_show_genres g ON tg.id = g.genre_id
        JOIN tv_shows t ON t.id = g.show_id
WHERE tg.name = 'Comedy'
ORDER BY title ASC;

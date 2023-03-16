-- all shows with at least one genre
SELECT title, name
FROM tv_genres tg
        RIGHT JOIN tv_show_genres g ON tg.id = g.genre_id
        RIGHT JOIN tv_shows t ON t.id = g.show_id
ORDER BY title ASC, name ASC;

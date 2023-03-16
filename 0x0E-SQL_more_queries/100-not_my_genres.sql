-- all shows with at least one genre
SELECT DISTINCT tg.name
FROM tv_genres tg
        INNER JOIN tv_show_genres ts ON ts.genre_id = tg.id
        INNER JOIN tv_shows t ON t.id = ts.show_id
WHERE tg.name NOT IN (
                SELECT tg.name
                FROM tv_genres tg
                        INNER JOIN tv_show_genres ts ON ts.genre_id = tg.id
                        INNER JOIN tv_shows t ON t.id = ts.show_id
                WHERE t.title = 'Dexter'
        )
ORDER BY tg.name ASC;

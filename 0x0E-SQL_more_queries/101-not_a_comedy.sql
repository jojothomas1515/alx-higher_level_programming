-- all show without all
SELECT title
FROM tv_shows
WHERE title NOT IN (SELECT title
                    FROM tv_shows t
                             INNER JOIN tv_show_genres tsg ON t.id = tsg.show_id
                             INNER JOIN tv_genres tg ON tsg.genre_id = tg.id
                    WHERE tg.name = 'Comedy')
ORDER BY title;

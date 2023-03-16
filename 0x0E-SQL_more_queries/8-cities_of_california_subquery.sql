-- list the  of california
SELECT id,
        name
FROM cities c
where c.state_id = (
                SELECT id
                FROM states
                where name = 'California'
        )
ORDER BY id ASC;

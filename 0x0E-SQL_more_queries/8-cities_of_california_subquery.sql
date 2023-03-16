-- list the  of california
SELECT id,
        name
FROM cities c
where c.state_id IN (
                SELECT id
                FROM states s
                where s.name = 'California'
        )
ORDER BY id ASC;

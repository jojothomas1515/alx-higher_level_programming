-- city by state join
SELECT id,
        name,
        name
FROM cities c
        INNER JOIN states s
        ON c.state_id = s.id
ORDER BY id ASC;

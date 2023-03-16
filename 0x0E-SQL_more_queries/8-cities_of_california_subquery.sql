-- list the  of california
use hbtn_0d_usa;
SELECT id,
        name
FROM cities c
where c.state_id = (
                SELECT id
                FROM states s
                where s.name = 'California'
        )
ORDER BY id ASC;

-- city by state join
SELECT id,
        `cities`.name,
        `states`.name
FROM `cities` c
        INNER JOIN `states` s
        ON c.state_id = s.id
ORDER BY `cities`.id ASC;

-- number by score
SELECT score, COUNT(score) as 'number' GROUP BY score ORDER BY count(score) DESC;

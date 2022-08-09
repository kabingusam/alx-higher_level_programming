-- Script that lists all records of the table second_table
-- List sorted by descending score
SELECT 'score', 'name'
FROM 'second_table'
WHERE 'name' != ""
ORDER BY 'score' DESC

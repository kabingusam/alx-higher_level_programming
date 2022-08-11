-- Top 3 of cities with the highest temperature 
-- During July and August ordered by temperature (descending)
SELECT `city`, AVG(`value`) AS `avg_tmp`
FROM `temperatures`
WHERE `month` = 7 OR `month` = 8
GROUP BY `city`
ORDER BY `avg_tmp` DESC
LIMIT 3

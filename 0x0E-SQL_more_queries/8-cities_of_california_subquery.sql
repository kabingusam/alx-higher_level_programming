-- List all the cities of california that can be found in the database hbtn_0d_usa
-- Results ordered in ascending order by citites.id
SELECT  `name`, `id`
 FROM `cities`
    WHERE `state_id` IN
    (SELECT `id`
    FROM `states`
    WHERE `name` = "California")
 ORDER BY `id`;

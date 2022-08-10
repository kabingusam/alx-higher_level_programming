-- List all cities in the database hbtn_0d_usa
-- Results must be sorted in ascending order by cities.id
SELECT c.`id`,c.`name`,c.`status`
 FROM `cities` AS C
        INNER JOIN `states` AS s
        ON c.`state.id` = s.`id`
 ORDER BY c.`id`;

-- This script lists all the cities of California in the database hbtn_0d_usa.
-- It uses a subquery to find the state_id of California from the states table and then selects the corresponding cities from the cities table.
-- Results are sorted in ascending order by cities.id.

SELECT *
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id;

-- Write a SQL query to list all the cities of California in alphabetical order.
SELECT name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY cities.id ASC;

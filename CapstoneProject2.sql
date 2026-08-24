-- Names starting with "a"
SELECT * FROM Customers
WHERE name LIKE 'a%';

-- Names containing "or"
SELECT * FROM Customers
WHERE name LIKE '%or%';

-- Using AND
SELECT * FROM Customers
WHERE name LIKE 'a%'
AND name LIKE '%or%';

-- Grouping data
SELECT country, COUNT(*)
FROM Customers
GROUP BY country;

-- Filtering groups
SELECT country, COUNT(*)
FROM Customers
GROUP BY country
HAVING COUNT(*) > 1;
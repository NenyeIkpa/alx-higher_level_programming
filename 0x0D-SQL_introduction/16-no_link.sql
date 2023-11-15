-- list filtered columns from a database
-- when a specific condition is met
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;

-- displays the average temperature (Fahrenheit) by city
-- of top 3 cities with highest temp in july and august 
-- ordered by temperature (descending)
SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;

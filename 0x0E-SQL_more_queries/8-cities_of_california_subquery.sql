-- lists all cities in a given state
-- query to list cities in a state
SELECT id,name FROM cities
where state_id =(
	SELECT id FROM states
	WHERE name = 'California'
);

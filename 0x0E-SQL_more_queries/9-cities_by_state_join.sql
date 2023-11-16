-- lists all cities contained in database hbtn_0d_usa
-- each record displays cities.id - cities.name - states.name
SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id;

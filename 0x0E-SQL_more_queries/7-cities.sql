-- create database, with table and columns
-- should not fail if exists
-- id is primary key, autogenerated, unique and not null
-- state_id is foreign key, references states(id)
-- name cannot be null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
	id INT AUTO_INCREMENT PRIMARY KEY UNIQUE NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY(state_id) REFERENCES states(id)
	);

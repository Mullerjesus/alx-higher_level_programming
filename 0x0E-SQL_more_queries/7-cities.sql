-- creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on MySQL server
-- script creates db hbtn_0d_usa and the table cities
-- create db
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use db
USE hbtn_0d_usa
-- create table in db
CREATE TABLE IF NOT EXISTS cities (id INT UNIQUE AUTO_INCREMENT NOT NULL,
state_id INT NOT NULL,
name VARCHAR(255) NOT NULL,
PRIMARY KEY(id),
FOREIGN KEY(state_id) REFERENCES states(id));

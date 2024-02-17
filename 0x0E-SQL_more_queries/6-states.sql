-- script creates db hbtn_0d_usa and the table states
-- create db
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use db created
USE hbtn_0d_usa
-- create table in db
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(255) NOT NULL, PRIMARY KEY(id));

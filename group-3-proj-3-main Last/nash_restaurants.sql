-- Database: nash_restaurants_db

DROP DATABASE IF EXISTS nash_restaurants_db;

CREATE DATABASE nash_restaurants_db
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

-- Table schema

DROP TABLE IF EXISTS restaurant_info;
DROP TABLE IF EXISTS restaurant_categories; 

CREATE TABLE restaurant_info (
	name VARCHAR PRIMARY KEY NOT NULL,
	rating FLOAT NOT NULL,
	pricing FLOAT NOT NULL,
	number_of_reviews INT NOT NULL,
	location VARCHAR NOT NULL
	);

CREATE TABLE restaurant_categories (
	name VARCHAR PRIMARY KEY NOT NULL,
	category VARCHAR NOT NULL,
	location VARCHAR NOT NULL
	);

SELECT * FROM restaurant_info;
SELECT * FROM restaurant_categories;
-- state tables
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
use hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
        id INT NOT NULL AUTO_INCREMENT UNIQUE,
        name VARCHAR(256)
);

CREATE DATABASE db_brothers;
USE db_brothers;
CREATE TABLE tbl_brother (
	id INT NOT NULL,
	fname VARCHAR(60)
);
ALTER TABLE tbl_brother ADD PRIMARY KEY (id);
INSERT INTO tbl_brother(id, fname) VALUES (1, "dannel"), (2, "joel"), (3, "eitan");

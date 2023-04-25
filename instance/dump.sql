PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE user (
	id INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	email VARCHAR(150) NOT NULL, 
	password VARCHAR(150) NOT NULL, 
	blood_group TEXT NOT NULL, 
	age INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (email)
);
INSERT INTO user VALUES(1,'Suswin','suswin@gmail.com','sha256$Ge4dDojpfhPoolCx$9251140197d568c57e52c8836e3d53d3393868fb5656f88b5dc694fd01c10a99','A1+ve',21);
INSERT INTO user VALUES(2,'Saravanan','Saravanan@gmail.com','sha256$cm86B6P7w15pQJEq$e12c72f95bce79d44d94765de00f83716052d2cee9c021bea7edd1b53e36baaa','AB-ve',47);
CREATE TABLE plasma (
	id INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	email VARCHAR(150) NOT NULL, 
	contact_no INTEGER NOT NULL, 
	blood_group TEXT NOT NULL, 
	date_details VARCHAR NOT NULL, 
	address TEXT(200) NOT NULL, 
	details TEXT(4000) NOT NULL, 
	PRIMARY KEY (id)
);
COMMIT;

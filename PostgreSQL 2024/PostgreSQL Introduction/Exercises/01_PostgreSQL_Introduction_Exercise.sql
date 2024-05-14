CREATE TABLE minions
(
	id serial PRIMARY KEY NOT NULL,
	name VARCHAR(30),
	age integer
);

ALTER TABLE minions
RENAME TO minions_info;

ALTER TABLE minions_info
ADD COLUMN code CHAR(4),
ADD COLUMN task TEXT,
ADD COLUMN salary DECIMAL(8,3);

ALTER TABLE minions_info
RENAME COLUMN salary TO banana;

ALTER TABLE minions_info
ADD COLUMN email VARCHAR(20),
ADD COLUMN equipped BOOLEAN NOT NULL;

CREATE TYPE type_mood
AS ENUM
(
	'happy',
	'relaxed',
	'stressed',
	'sad'
);

ALTER TABLE minions_info
ADD COLUMN mood type_mood;

ALTER TABLE minions_info
ALTER COLUMN age SET DEFAULT 0,
ALTER COLUMN name SET DEFAULT '',
ALTER COLUMN code SET DEFAULT '';

ALTER TABLE minions_info
ADD CONSTRAINT unique_containt UNIQUE (id,email),
ADD CONSTRAINT banana_check CHECK(banana>0);

ALTER TABLE minions_info
ALTER COLUMN task TYPE VARCHAR(150);

ALTER TABLE minions_info
ALTER COLUMN equipped
DROP NOT NULL;

ALTER TABLE minions_info
DROP COLUMN age;

CREATE TABLE minions_birthdays
(
	id serial UNIQUE NOT NULL,
	name VARCHAR(50),
	date_of_birth date,
	age integer,
	present VARCHAR(100),
	party TIMESTAMPTZ
);

INSERT INTO minions_info(name, code, task, banana, email, equipped, mood)
VALUES
	('Mark', 'GKYA', 'Graphing Points', 3265.265, 'mark@minion.com', false, 'happy'),
	('Mel','HSK','Science Investigation',54784.996,'mel@minion.com',true,'stressed'),
	('Bob','HF','Painting',35.652,'bob@minion.com',true,'happy'),
	('Darwin','EHND','Create a Digital Greeting',321.958,'darwin@minion.com',false,'relaxed'),
	('Kevin','KMHD','Construct with Virtual Blocks',35214.789,'kevin@minion.com',false,'happy'),
	('Norbert','FEWB','Testing',3265.500,'norbert@minion.com',true,'sad'),
	('Donny','L','Make a Map',8.452,'donny@minion.com',true,'happy');

SELECT name,task,email,banana FROM public.minions_info;

TRUNCATE TABLE minions_info;

DROP TABLE minions_birthdays;

DROP DATABASE minions_db(FORCE);
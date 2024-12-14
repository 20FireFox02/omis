create table user_t
(
	id SERIAL PRIMARY KEY,
	name VARCHAR,
	description VARCHAR,
	avatar VARCHAR,
	password VARCHAR
);

create table wallet
(
	type VARCHAR,
	owner_id INTEGER,
	name VARCHAR,
	balance NUMERIC
);

create table auction
(
	id SERIAL PRIMARY KEY,
	name VARCHAR,
	st_d VARCHAR,
	en_d VARCHAR,
	st_b NUMERIC,
	creator VARCHAR,
	lotname VARCHAR,
	description VARCHAR
);

create table buyer_bet
(
	auc_id INTEGER,
	buyer_id INTEGER,
	bet NUMERIC
);
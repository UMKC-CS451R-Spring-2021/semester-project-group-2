create database commerce;
use commerce;

CREATE TABLE user(
id	INT NOT NULL,
email	VARCHAR(50),
f_name	VARCHAR(50),
l_name	VARCHAR(50),

PRIMARY KEY(id)
);

CREATE TABLE login(
login_id	INT NOT NULL auto_increment,
login_password	VARCHAR(50),
username	VARCHAR(50),
user_id	INT NOT NULL,

PRIMARY KEY(login_id),
FOREIGN KEY(user_id) REFERENCES user(id)
);

CREATE TABLE account(
account_id	INT NOT NULL,
balance	FLOAT,
user_id	INT NOT NULL,

PRIMARY KEY(account_id),
FOREIGN KEY(user_id) REFERENCES user(id)
);

CREATE TABLE transactions(
transaction_id	INT NOT NULL auto_increment,
balance	FLOAT,
processing_date	DATE,
amount	FLOAT,
description	VARCHAR(50),
type	VARCHAR(10),
account_id	INT,

PRIMARY KEY(transaction_id),
FOREIGN KEY(account_id) REFERENCES account(account_id)
);

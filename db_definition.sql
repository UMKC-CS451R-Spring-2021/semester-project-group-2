CREATE DATABASE commerce_data;
USE commerce_data;

CREATE TABLE transactions (
	transaction_id	INT NOT NULL auto-increment,
	account_number	INT,
	processing_date	DATE,
	balance	FLOAT,
	type VARCHAR(50),
	amount FLOAT,
	description VARCHAR(50),

	PRIMARY KEY(transaction_id)
);

CREATE INDEX index_transactions
ON transactions(processing_date);
create database commerce;
use commerce;

CREATE TABLE commerce_user(
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

CREATE TABLE user_account(
account_id	INT NOT NULL,
balance	FLOAT,
user_id	INT NOT NULL,

PRIMARY KEY(account_id),
FOREIGN KEY(user_id) REFERENCES user(id)
);

CREATE TABLE transactions(
transaction_id	INT NOT NULL auto_increment,
account_id	INT,
processing_date	DATE,
balance	FLOAT,
transaction_type	VARCHAR(10),
amount	FLOAT,
descr	VARCHAR(50),
location	VARCHAR(50),

PRIMARY KEY(transaction_id),
FOREIGN KEY(account_id) REFERENCES account(account_id)
);

CREATE TABLE notification_rules(
rule_id	INT NOT NULL auto_increment,
rule_type	INT NOT NULL,
set_rule	BOOL,
balance	FLOAT DEFAULT NULL,
location	VARCHAR(50) DEFAULT NULL,
amount	FLOAT DEFAULT NULL,
descr VARCHAR(50),
message	VARCHAR(100) DEFAULT NULL,

PRIMARY KEY(rule_id)
);

CREATE TABLE notifications(
notification_id	INT NOT NULL auto_increment,
transaction_id	INT,
account_id	INT,
processing_date	DATE,
balance	FLOAT,
transaction_type	VARCHAR(10),
amount	FLOAT,
descr	VARCHAR(50),
location	VARCHAR(50),
rule	INT,

PRIMARY KEY(notification_id),
FOREIGN KEY(rule) REFERENCES notification_rules(rule_type)
);

-- load data for transactions table
-- will need to update the path name 
LOAD DATA INFILE 'UMKC Project Data FS20.csv'
INTO TABLE transactions
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(account_id, processing_date, balance, transaction_type,
amount, descr);

-- create notification rule for low balance
INSERT INTO 'notification_rules'
(rule_type, set_rule, balance)
VALUES
(1, True, 25.00);

-- create notification rule for large amount
INSERT INTO 'notification_rules'
(rule_type, set_rule, amount)
VALUES
(2, True, 300.00);

-- create notification rule for out of state transactions
INSERT INTO 'notification_rules'
(rule_type, set_rule, location)
VALUES
(3, True, 'Missouri');

-- create notification rule for description 
INSERT INTO 'notification_rules'
(rule_type, set_rule, descr)
VALUES
(4, True, 'Payroll');







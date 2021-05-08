
use commerce_bank;

CREATE TABLE transactions(
transaction_id INT NOT NULL auto_increment,
account_id INT,
processing_date DATE,
balance FLOAT,
transaction_type VARCHAR(10),
amount FLOAT,
descr VARCHAR(50),

PRIMARY KEY(transaction_id)
);

CREATE TABLE balance_notif (
  account_id int NOT NULL,
  is_true varchar(1) NOT NULL,
  amount float DEFAULT NULL,
  PRIMARY KEY (account_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE deposit_notif (
  account_id int NOT NULL,
  is_true varchar(1) NOT NULL,
  PRIMARY KEY (account_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE withdrawal_notif (
  account_id int NOT NULL,
  is_true varchar(1) NOT NULL,
  amount float DEFAULT NULL,
  PRIMARY KEY (account_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


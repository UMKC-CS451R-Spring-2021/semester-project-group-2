DROP PROCEDURE IF EXISTS BalanceRule;

DELIMITER $$

CREATE PROCEDURE BalanceRule(IN t_id INT)
BEGIN
-- low balance rule is type 1
	SELECT set_rule
    INTO rule_on
    FROM notification_rules
    WHERE rule_type = 1;
    -- make sure rule is turned on before proceeding
	IF(rule_on IS True) THEN
		SELECT balance
        INTO current_balance
        FROM transactions
        WHERE transaction_id = t_id;
        
        SELECT balance 
        INTO balance_limit
        FROM notification_rules
        WHERE rule_type = 1;
        
        SELECT account_id, processing_date,
        balance, transaction_type, amount, descr,
        location, rule
        INTO i_account_id, i_processing_date,
        i_balance, i_transaction_type, i_amount, i_descr,
        i_location, i_rule
        FROM transactions
        WHERE transaction_id = t_id;
        
        IF(current_balance < balance_limit) THEN
			INSERT INTO notifications
            (transaction_id, account_id, processing_date,
            balance, transaction_type, amount, descr, 
            location, rule, message)
            VALUES
            (t_id, i_account_id, i_processing_date,
            i_balance, i_transaction_type, i_amount, 
            i_descr, i_location, 1,
            "Low balance notification");
            
		END IF;
	END IF;
END $$ 

DELIMITER ;


DROP PROCEDURE IF EXISTS AmountRule;

DELIMITER $$

CREATE PROCEDURE AmountRule(IN t_id INT)
BEGIN
-- amount rule is type 2
	SELECT set_rule
    INTO rule_on
    FROM notification_rules
    WHERE rule_type = 2;
    
    -- make sure the rule is turned on before proceeding
    IF(rule_on IS True) THEN
		SELECT amount 
        INTO current_amount
        FROM transactions
        WHERE transaction_id = t_id;
        
        SELECT amount
        INTO amount_limit
        FROM notification_rules
        WHERE rule_type = 2;
        
        SELECT account_id, processing_date,
        balance, transaction_type, amount, descr,
        location, rule
        INTO i_account_id, i_processing_date,
        i_balance, i_transaction_type, i_amount, i_descr,
        i_location, i_rule
        FROM transactions
        WHERE transaction_id = t_id;
        
        IF(current_amount > amount_limit) THEN
			INSERT INTO notifications
			(transaction_id, account_id, processing_date,
            balance, transaction_type, amount, descr, 
            location, rule, message)
            VALUES
            (t_id, i_account_id, i_processing_date,
            i_balance, i_transaction_type, i_amount, 
            i_descr, i_location, 2,
            "Transaction amount notification");
		END IF;
	END IF;
END $$

DELIMITER ;


DROP PROCEDURE IF EXISTS LocationRule;

DELIMITER $$

CREATE PROCEDURE LocationRule(IN t_id INT)
BEGIN
-- location rule is type 3
	SELECT set_rule
	INTO rule_on
	FROM notification_rules
	WHERE rule_type = 3;
    
	-- make sure the rule is turned on before proceeding
    IF(rule_on IS True) THEN
		SELECT location 
		INTO current_location
        FROM transactions
        WHERE transaction_id = t_id;
        
        SELECT location
        INTO allowed_location
        FROM notification_rules
        WHERE rule_type = 3;
        
        SELECT account_id, processing_date,
        balance, transaction_type, amount, descr,
        location, rule
        INTO i_account_id, i_processing_date,
        i_balance, i_transaction_type, i_amount, i_descr,
        i_location, i_rule
        FROM transactions
        WHERE transaction_id = t_id;
        
        IF(current_location <> allowed_location) THEN
			INSERT INTO notifications
			(transaction_id, account_id, processing_date,
            balance, transaction_type, amount, descr, 
            location, rule, message)
            VALUES
            (t_id, i_account_id, i_processing_date,
            i_balance, i_transaction_type, i_amount, 
            i_descr, i_location, 3,
            "Transaction location notification");
		END IF;
	END IF;
END $$

DELIMITER ;

DROP PROCEDURE IF EXISTS DescriptionRule;

DELIMITER $$

CREATE PROCEDURE DescriptionRule(IN t_id INT)
BEGIN
-- description rule is type 4
SELECT set_rule
	INTO rule_on
	FROM notification_rules
	WHERE rule_type = 4;
    
	-- make sure the rule is turned on before proceeding
    IF(rule_on IS True) THEN
		SELECT description 
		INTO current_description
        FROM transactions
        WHERE transaction_id = t_id;
        
        SELECT description
        INTO flagged_description
        FROM notification_rules
        WHERE rule_type = 4;
        
        SELECT account_id, processing_date,
        balance, transaction_type, amount, descr,
        location, rule
        INTO i_account_id, i_processing_date,
        i_balance, i_transaction_type, i_amount, i_descr,
        i_location, i_rule
        FROM transactions
        WHERE transaction_id = t_id;
        
        IF(current_description = flagged_description) THEN
			INSERT INTO notifications
			(transaction_id, account_id, processing_date,
            balance, transaction_type, amount, descr, 
            location, rule, message)
            VALUES
            (t_id, i_account_id, i_processing_date,
            i_balance, i_transaction_type, i_amount, 
            i_descr, i_location, 4,
            "Flagged description notification");
		END IF;
	END IF;
END $$

DELIMITER ;

        
        
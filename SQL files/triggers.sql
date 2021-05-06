DROP TRIGGER IF EXISTS CheckNotificationRules;

DELIMITER $$

CREATE TRIGGER CheckNotificationRules
AFTER INSERT
ON `transactions` FOR EACH ROW
BEGIN
	CALL BalanceRule(NEW.transaction_id);
    CALL LocationRule(NEW.transaction_id);
    CALL DescriptionRule(NEW.transaction_id);
    CALL AmountRule(NEW.transaction_id);
END $$

DELIMITER ;

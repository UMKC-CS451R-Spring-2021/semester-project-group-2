DROP TRIGGER IF EXISTS CheckNotificationRules;

DELIMITER $$

CREATE TRIGGER CheckNotificationRules
AFTER INSERT
ON 'transactions' FOR EACH ROW
BEGIN
	CALL BalanceRule(NEW.id);
    CALL LocationRule(NEW.id);
    CALL DescriptionRule(NEW.id);
    CALL AmountRule(NEW.id);
END $$

DELIMITER ;

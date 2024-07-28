-- Task 01

CREATE OR REPLACE FUNCTION fn_full_name (
	first_name VARCHAR(50),
	last_name VARCHAR(50)
) RETURNS VARCHAR(101)
AS
$$
DECLARE 
	full_name VARCHAR(101);
BEGIN
	full_name := INITCAP(LOWER(first_name)) || ' ' || INITCAP(LOWER(last_name));
	RETURN full_name; -- full_name is not really needed
END;
$$
LANGUAGE plpgsql;

-- Task 02

CREATE OR REPLACE FUNCTION fn_full_name (
	first_name VARCHAR(50),
	last_name VARCHAR(50)
) RETURNS VARCHAR(101)
AS
$$
DECLARE 
	full_name VARCHAR(101);
BEGIN
	full_name := INITCAP(LOWER(first_name)) || ' ' || INITCAP(LOWER(last_name));
	RETURN full_name; -- full_name is not really needed
END;
$$
LANGUAGE plpgsql;

-- Task 03

CREATE OR REPLACE FUNCTION fn_is_word_comprised (
	set_of_letters VARCHAR(50),
	word VARCHAR(50)
) RETURNS BOOLEAN
AS 
$$
BEGIN
	RETURN TRIM(LOWER(word), LOWER(set_of_letters)) = '';
END;
$$
LANGUAGE plpgsql;

-- Task 04

CREATE OR REPLACE FUNCTION fn_is_game_over (
	is_game_over BOOLEAN
) RETURNS TABLE (
	name VARCHAR(50),
	game_type_id INT,
	is_finished BOOLEAN
)
AS 
$$
BEGIN
	RETURN QUERY
	SELECT 
		g.name,
		g.game_type_id,
		g.is_finished
	FROM 
		games AS g
	WHERE 
		g.is_finished = is_game_over;
END;
$$
LANGUAGE plpgsql;

-- Task 05

CREATE OR REPLACE FUNCTION fn_difficulty_level (
	level INT
) RETURNS VARCHAR(50)
AS
$$
DECLARE 
	difficulty_level VARCHAR(50);
BEGIN
	IF level <= 40 THEN
		difficulty_level := 'Normal Difficulty';
	ELSIF level BETWEEN 41 AND 60 THEN
		difficulty_level := 'Nightmare Difficulty';
	ELSE
		difficulty_level := 'Hell Difficulty';
	END IF;
	
	RETURN difficulty_level;
END;
$$
LANGUAGE plpgsql;


SELECT 
	user_id, 
	level, 
	cash,
	fn_difficulty_level(level)
FROM
	users_games
ORDER BY
	user_id;	
	

-- Task 06

CREATE OR REPLACE FUNCTION fn_cash_in_users_games(
	game_name VARCHAR(50)
) RETURNS TABLE (
	total_cash NUMERIC
)
AS 
$$
BEGIN
	RETURN QUERY
	WITH ranked_games AS (
		SELECT
			cash,
			ROW_NUMBER() OVER (ORDER BY cash DESC) AS row_num
		FROM
			users_games AS ug
		JOIN
			games AS g
		ON 
			ug.game_id = g.id
		WHERE
			g.name = game_name
	)
	
	SELECT
		ROUND(SUM(cash), 2) AS total_cash
	FROM
		ranked_games AS rg
	WHERE
		rg.row_num % 2 <> 0;
END;
$$
LANGUAGE plpgsql;

-- Task 07

CREATE OR REPLACE PROCEDURE
	sp_retrieving_holders_with_balance_higher_than(
		searched_balance NUMERIC
	)
AS 
$$
DECLARE
	holder_info RECORD;
BEGIN
	FOR holder_info IN 
		SELECT
			ah.first_name || ' ' || ah.last_name AS full_name,
			SUM(balance) AS total_balance
		FROM
			account_holders AS ah
		JOIN
			accounts AS a
		ON
			a.account_holder_id = ah.id
		GROUP BY
			full_name
		HAVING
			SUM(balance) > searched_balance
		ORDER BY
			full_name
	LOOP
		RAISE NOTICE '% - %.', holder_info.full_name, holder_info.total_balance;
	END LOOP;
END;
$$
LANGUAGE plpgsql;


CALL sp_retrieving_holders_with_balance_higher_than(200000);

-- Task 08

CREATE OR REPLACE PROCEDURE sp_deposit_money(
	account_id INT,
	money_amount NUMERIC(4)
)
AS 
$$
BEGIN
	UPDATE
		accounts
	SET 
		balance = balance + money_amount
	WHERE 
		id = account_id;
END;
$$
LANGUAGE plpgsql;

-- Task 09

CREATE OR REPLACE PROCEDURE sp_withdraw_money(
	account_id INT,
	money_amount NUMERIC(4)
)
AS 
$$
DECLARE
	current_balance NUMERIC;
BEGIN
	current_balance := (SELECT balance FROM accounts WHERE id = account_id);
	
	IF money_amount <= current_balance THEN
		UPDATE
			accounts
		SET 
			balance = balance - money_amount
		WHERE 
			id = account_id;
	ELSE
		RAISE NOTICE 'Insufficient balance to withdraw %', money_amount;
	END IF;
END;
$$
LANGUAGE plpgsql;

-- Task 10

CREATE OR REPLACE PROCEDURE sp_transfer_money(
	sender_id INT,
	receiver_id INT,
	amount NUMERIC(4)
)
AS 
$$
DECLARE
	current_balance NUMERIC;
BEGIN
	CALL sp_withdraw_money(sender_id, amount);
	CALL sp_deposit_money(receiver_id, amount);
	
	SELECT balance INTO current_balance FROM accounts WHERE id = sender_id;
	
	IF current_balance < 0 THEN
		ROLLBACK;
	END IF;
END;
$$
LANGUAGE plpgsql;

-- Task 11

DROP PROCEDURE sp_retrieving_holders_with_balance_higher_than;

-- Task 12

CREATE TABLE logs (
	id SERIAL PRIMARY KEY,
	account_id INT,
	old_sum NUMERIC(20, 4),
	new_sum NUMERIC(20, 4)
);

CREATE OR REPLACE FUNCTION 
	trigger_fn_insert_new_entry_into_logs()
RETURNS TRIGGER AS
$$
BEGIN
	INSERT INTO 
		logs(account_id, old_sum, new_sum)
	VALUES
		(OLD.id, OLD.balance, NEW.balance);
	RETURN NEW;
END;
$$
LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER tr_account_balance_change
AFTER UPDATE OF
	balance 
ON 
	accounts
FOR EACH ROW
WHEN 
	(NEW.balance <> OLD.balance)
EXECUTE FUNCTION 
	trigger_fn_insert_new_entry_into_logs();

-- Task 13

CREATE TABLE IF NOT EXISTS notification_emails (
	id SERIAL PRIMARY KEY,
	recipient_id INT,
	subject VARCHAR(255),
	body TEXT
);

CREATE OR REPLACE FUNCTION 
	trigger_fn_send_email_on_balance_change()
RETURNS TRIGGER
AS
$$
BEGIN
	INSERT INTO
		notification_emails(recipient_id, subject, body)
	VALUES
		(
			NEW.account_id, 
			'Balance change for account: ' || NEW.account_id,
			'On ' || DATE(NOW()) || ' your balance was changed from ' || NEW.old_sum || ' to ' || NEW.new_sum || '.'
		);
		
	RETURN NEW;
END;
$$
LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER
	tr_send_email_on_balance_change
AFTER UPDATE ON 
	logs
FOR EACH ROW
WHEN
	(OLD.new_sum <> NEW.new_sum)
EXECUTE FUNCTION 
	trigger_fn_send_email_on_balance_change();
	
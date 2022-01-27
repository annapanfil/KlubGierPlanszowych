delimiter //
create function pesel_to_date (vPesel varchar(11))
	RETURNS date deterministic
		BEGIN
        IF CAST(substr(vPesel,3,2) AS UNSIGNED) < 20 THEN
			RETURN str_to_date(CONCAT('19',substr(vPesel, 1, 6)), '%Y%m%d');
		ELSE 
            RETURN str_to_date(CONCAT('20',substr(vPesel, 1, 2),substr(vPesel, 3, 1)-2,substr(vPesel, 4, 1),substr(vPesel, 5, 2)), '%Y%m%d');
        END IF;    
        END//
delimiter ;
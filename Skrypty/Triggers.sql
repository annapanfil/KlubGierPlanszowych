CREATE TRIGGER Usuwanie_czlonkow
	BEFORE DELETE ON Czlonkowie FOR EACH ROW
			DELETE from Czlonkowie_w_sekcjach WHERE pesel_czlonka = old.pesel;

DELIMITER //            
CREATE TRIGGER Usuwanie_eventow
	BEFORE DELETE ON Eventy FOR EACH ROW
		BEGIN
			DELETE FROM Turnieje WHERE event = old.id_eventu;
			DELETE FROM Sponsorowanie WHERE event = old.id_eventu;
        END//
DELIMITER ;

DELIMITER //
CREATE TRIGGER Usuwanie_uczestnikow_z_turnieju
	BEFORE DELETE ON Turnieje FOR EACH ROW
    BEGIN
		DELETE FROM Uczstnicy_turniejow where turniej = old.id_turnieju;
        DELETE FROM Gry_uzywanie where turniej = old.id_turnieju;
	END//
DELIMITER ;
    
CREATE TRIGGER Usuwanie_miejsc_z_turnieju
	BEFORE DELETE ON Uczestnicy_turniejow FOR EACH ROW
		DELETE FROM Miejsce_w_turnieju where uczestnik = old.id_uczestnika;        
        
CREATE TRIGGER Usuwanie_gier_z_egzemplarzem
	BEFORE DELETE ON Egzemplarz FOR EACH ROW
		DELETE FROM Gry_uzywanie where id_egzemplarza = old.id_egzemplarza;
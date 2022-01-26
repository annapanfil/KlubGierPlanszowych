CREATE TRIGGER Usuwanie_Czlonkow
	BEFORE DELETE ON czlonkowie FOR EACH ROW
			DELETE from Czlonkowie_w_sekcjach WHERE pesel_czlonka = old.pesel;

DELIMITER //            
CREATE TRIGGER Usuwanie_Eventow
	BEFORE DELETE ON Eventy FOR EACH ROW
		BEGIN
			DELETE FROM Turnieje WHERE event = old.id_eventu;
			DELETE FROM Sponsorowanie Turnieje WHERE event = old.id_eventu;
        END//
DELIMITER ;

DELIMITER //
CREATE TRIGGER Usuwanie_Uczestnikow_Z_Turnieju
	BEFORE DELETE ON Turnieje FOR EACH ROW
    BEGIN
		DELETE FROM Uczstnicy_turniejow where turniej = old.id_turnieju;
        DELETE FROM Gry_uzywanie where turniej = old.id_turnieju;
	END//
DELIMITER ;
    
CREATE TRIGGER Usuwanie_Miejsc_Z_Turnieju
	BEFORE DELETE ON Uczestnicy_turniejow FOR EACH ROW
		DELETE FROM Miejsce_w_turnieju where uczestnik = old.id_uczestnika;        
        
CREATE TRIGGER Usuwanie_Gier_Z_Egzemplarzem
	BEFORE DELETE ON Egzemplarz FOR EACH ROW
		DELETE FROM Gry_uzywanie where id_egzemplarza = old.id_egzemplarza;
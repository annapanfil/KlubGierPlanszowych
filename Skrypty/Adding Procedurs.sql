delimiter //
create procedure Sekcje_add(IN c_nazwa varchar(50))
		begin 
        INSERT into Sekcje(nazwa,data_utworzenia) values (c_nazwa,CURRENT_DATE);
        end//
delimiter ;

delimiter //
create procedure Czlonkowie_add(IN c_pesel INT(11), IN c_imie varchar(50), IN c_nazwisko varchar(50), IN c_data date)
		begin 
        INSERT into Czlonkowie(pesel,imie,nazwisko,data_urodzenia) values(c_pesel,c_imie,c_nazwisko,c_data);
        end//
delimiter ;

delimiter //
create procedure Czlonkowie_w_sekcjach_add(IN c_pesel INT(11), IN c_id_sekcji int(7)) 
		begin 
        INSERT into Czlonkowie_w_sekcjach values (c_pesel, c_id_sekcji, current_date());
        end//
delimiter ;

delimiter //
create procedure Placowki_add(IN c_adres varchar(100), IN c_czynsz float(7)) 
		begin 
        INSERT into Placowki values(c_adres,c_czynsz);
        end//
delimiter ;

delimiter //
create procedure Spotkania_add(IN c_data date,IN c_id_sekcji int(7),IN c_adres varchar(100)) 
		begin 
        INSERT INTO Spotkania(termin,id_sekcji,adres) values(c_data,c_id_sekcji,c_adres);
        end//
delimiter ;

delimiter //
create procedure Miejsca_add(IN c_adres varchar(100), IN c_czynsz float(7),IN c_capacity INT(7)) 
		begin 
        INSERT into Miejsca values(c_adres,c_czynsz,c_capacity);
        end//
delimiter ;

delimiter //
create procedure Eventy_add(IN c_nazwa varchar(50),IN c_data date,IN c_id_sekcji int(7),IN c_adres varchar(100)) 
		begin 
        insert into Eventy(nazwa,data,sekcja,adres) values (c_nazwa,c_data,c_id_sekcji,c_adres);
        end//
delimiter ;

delimiter //
create procedure Sponsorzy_add(IN c_nazwa varchar(50)) 
		begin 
       insert into Sponsorzy(nazwa) values (c_nazwa);
        end//
delimiter ;

delimiter //
create procedure Sponsorowanie_add(IN c_kwota FLOAT(7),IN c_id_sponsora int(7),IN c_id_eventu int(7))
		begin 
        insert into Sponsorowanie(kwota,sponsor,event) values (c_kwota,c_id_sponsora,c_id_eventu);
        end//
delimiter ;

delimiter //
create procedure Turnieje_add(IN c_nazwa varchar(50),IN c_id_eventu int(7),IN c_godzina time) 
		begin 
        insert into Turnieje(nazwa,event,godzina_rozpoczecia) values (c_nazwa,c_id_eventu,c_godzina);
        end//
delimiter ;

delimiter //
create procedure Uczestnicy_turniejow_add(IN c_imie varchar(50),IN c_nazwisko varchar(50),IN c_id_turnieju int(7)) 
		begin 
        insert into Uczestnicy_turniejow(imie,nazwisko,turniej) values (c_imie,c_nazwisko,c_id_turnieju);
        end//
delimiter ;

delimiter //
create procedure Miejsce_w_turnieju_add(IN c_numer_miejsca int(7),IN c_id_turnieju int(7),IN c_id_uczestnika int(7),IN c_nagroda varchar(100)) 
		begin 
        insert into Miejsce_w_turnieju values (c_numer_miejsca,c_id_turnieju,c_id_uczestnika,c_nagroda);
        end//
delimiter ;

delimiter //
create procedure Wydawcy_add(IN c_nazwa varchar(50)) 
		begin 
        insert into Wydawcy(nazwa) values (c_nazwa);
        end//
delimiter ;

delimiter //
create procedure Platformy_add(IN c_nazwa varchar(50)) 
		begin 
       insert into Platformy(nazwa) values (c_nazwa);
        end//
delimiter ;

delimiter //
create procedure Gry_add(IN c_nazwa varchar(50),IN c_cena int(7),IN c_id_wydawcy int(7))
		begin 
        insert into Gry(nazwa,cena,wydawca) values (c_nazwa,c_cena,c_id_wydawcy);
        end//
delimiter ;

delimiter //
create procedure Egzemplarz_add(IN c_id_gry int(7),IN c_id_sekcji int(7)) 
		begin 
        insert into Egzemplarz(id_gry,id_sekcji) values (c_id_gry,c_id_sekcji);
        end//
delimiter ;

delimiter //
create procedure Gry_komputerowe_add(IN c_id_gry int(7),IN c_id_platformy int(7)) 
		begin 
        insert into Gry_komputerowe values (c_id_gry,c_id_platformy);
        end//
delimiter ;

drop procedure Gry_komputerowe_add;

delimiter //
create procedure Gry_planszowe_add(IN c_id_gry int(7),IN c_waga FLOAT(3),IN c_min int(2),IN c_max int(2)) 
		begin 
        insert into Gry_planszowe values (c_id_gry,c_waga,c_min,c_max);
        end//
delimiter ;

delimiter //
create procedure Gry_uzywanie_add(IN c_id_egzemplarza int(7),IN c_id_turnieju int(7)) 
		begin 
        insert into Gry_uzywanie values(c_id_egzemplarza,c_id_turnieju);
        end//
delimiter ;


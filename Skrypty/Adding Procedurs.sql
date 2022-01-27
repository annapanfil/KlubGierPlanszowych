delimiter //
create procedure Sekcje_add(IN c_nazwa varchar(50))
		begin 
        INSERT into Sekcje(nazwa,data_utworzenia) values (c_nazwa,CURRENT_DATE);
        end//
delimiter ;

delimiter //
create procedure Czlonkowie_add(IN c_pesel varchar(11), IN c_imie varchar(50), IN c_nazwisko varchar(50))
		begin 
        INSERT into Czlonkowie(pesel,imie,nazwisko,data_urodzenia) values(c_pesel,c_imie,c_nazwisko,pesel_to_date(c_pesel));
        end//
delimiter ;

delimiter //
create procedure Czlonkowie_w_sekcjach_add(IN c_pesel INT(11), IN c_nazwa_sekcji varchar(50)) 
		begin 
        DECLARE c_id_sekcji int(7);
        SELECT id_sekcji into c_id_sekcji from Sekcje where nazwa=c_nazwa_sekcji;
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
create procedure Spotkania_add(IN c_data date,IN c_nazwa_sekcji varchar(50),IN c_adres varchar(100)) 
		begin 
        DECLARE c_id_sekcji int(7);
        SELECT id_sekcji into c_id_sekcji from Sekcje where nazwa=c_nazwa_sekcji;
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
create procedure Eventy_add(IN c_nazwa varchar(50),IN c_data date,IN c_nazwa_sekcji int(7),IN c_adres varchar(100)) 
		begin 
		DECLARE c_id_sekcji int(7);
        SELECT id_sekcji into c_id_sekcji from Sekcje where nazwa=c_nazwa_sekcji;
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
create procedure Sponsorowanie_add(IN c_kwota FLOAT(7),IN c_nazwa_sponsora varchar(50),IN c_nazwa_eventu varchar(50))
		begin 
        DECLARE c_id_sponsora INT(7);
        DECLARE c_id_eventu INT(7);
        select id_eventu into c_id_eventu from Eventy where nazwa = c_nazwa_eventu;
        select id_sponsora into c_id_sponsora from Sponsorzy where nazwa = c_nazwa_sponsora;
        insert into Sponsorowanie(kwota,sponsor,event) values (c_kwota,c_id_sponsora,c_id_eventu);
        end//
delimiter ;

delimiter //
create procedure Turnieje_add(IN c_nazwa varchar(50),IN c_nazwa_eventu varchar(50),IN c_godzina time) 
		begin 
		DECLARE c_id_eventu INT(7);
		select id_eventu into c_id_eventu from Eventy where nazwa = c_nazwa_eventu;
        insert into Turnieje(nazwa,event,godzina_rozpoczecia) values (c_nazwa,c_id_eventu,c_godzina);
        end//
delimiter ;

delimiter //
create procedure Uczestnicy_turniejow_add(IN c_imie varchar(50),IN c_nazwisko varchar(50),IN c_nazwa_turnieju varchar(50)) 
		begin
        DECLARE c_id_turnieju INT(7);
		select id_turnieju into c_id_turnieju from Turnieje where nazwa = c_nazwa_eventu;
        insert into Uczestnicy_turniejow(imie,nazwisko,turniej) values (c_imie,c_nazwisko,c_id_turnieju);
        end//
delimiter ;

delimiter //
#
create procedure Miejsce_w_turnieju_add(IN c_numer_miejsca int(7),IN c_nazwa_turnieju varchar(50),IN c_id_uczestnika int(7),IN c_nagroda varchar(100)) 
		begin
        DECLARE c_id_turnieju INT(7);
		select id_turnieju into c_id_turnieju from Turnieje where nazwa = c_nazwa_eventu;
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
create procedure Gry_add(IN c_nazwa varchar(50),IN c_cena int(7),IN c_nazwa_wydawcy varchar(50))
		begin 
        DECLARE c_id_wydawcy int(7);
        select id_wydawcy into c_id_wydawcy from Wydawcy where nazwa = c_nazwa_wydawcy;
        insert into Gry(nazwa,cena,wydawca) values (c_nazwa,c_cena,c_id_wydawcy);
        end//
delimiter ;

delimiter //
create procedure Egzemplarz_add(IN c_nazwa_gry varchar(50),IN c_nazwa_sekcji varchar(50)) 
		begin 
	DECLARE c_id_sekcji int(7);
        DECLARE c_id_gry int(7);
        SELECT id_gry into c_id_gry from Gry where nazwa = c_nazwa_gry; 
        SELECT id_sekcji into c_id_sekcji from Sekcje where nazwa=c_nazwa_sekcji;
        insert into Egzemplarz(id_gry,id_sekcji) values (c_id_gry,c_id_sekcji);
        end//
delimiter ;

delimiter //
create procedure Gry_komputerowe_add(IN c_nazwa varchar(50),IN c_cena float(4),IN c_nazwa_wydawcy varchar(50),IN c_nazwa_platformy varchar(50)) 
		begin 
        DECLARE c_id_gry int(7);
        DECLARE c_id_platformy int(7);
        call Gry_add(c_nazwa,c_cena,c_nazwa_wydawcy);
        SELECT id_gry into c_id_gry from Gry natural join Wydawcy where Gry.nazwa=c_nazwa; 
        SELECT id_platformy into c_id_platformy from Platformy where nazwa = c_nazwa_platformy;
        insert into Gry_komputerowe values (c_id_gry,c_id_platformy);
        end//
delimiter ;

drop procedure Gry_komputerowe_add;

delimiter //
create procedure Gry_planszowe_add(IN c_nazwa_gry varchar(50),IN c_cena float(4),IN c_nazwa_wydawcy varchar(50),IN c_waga FLOAT(3),IN c_min int(2),IN c_max int(2)) 
		begin 
	DECLARE c_id_gry int(7);
        call Gry_add(c_nazwa_gry,c_cena,c_nazwa_wydawcy);
        SELECT id_gry into c_id_gry from Gry natural join Wydawcy where Gry.nazwa=c_nazwa; 
        insert into Gry_planszowe values (c_id_gry,c_waga,c_min,c_max);
        end//
delimiter ;

delimiter //
create procedure Gry_uzywanie_add(IN c_id_egzemplarza int(7),IN c_nazwa_turnieju varchar(50)) 
		begin 
        DECLARE c_id_turnieju int(7);
        SELECT id_turnieju into c_id_turnieju from Turnieje where nazwa = c_nazwa_turnieju;
        insert into Gry_uzywanie values(c_id_egzemplarza,c_id_turnieju);
        end//
delimiter ;

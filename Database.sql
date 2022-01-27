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

CREATE TABLE Czlonkowie (
  pesel VARCHAR(11) PRIMARY KEY,
  imie VARCHAR(50) NOT NULL,
  nazwisko VARCHAR(50) NOT NULL,
  data_urodzenia DATE NOT NULL
);

CREATE TABLE  Sekcje(
  id_sekcji INT(7) PRIMARY KEY AUTO_INCREMENT,
  nazwa VARCHAR(50) NOT NULL,
  data_utworzenia DATE
);



CREATE TABLE Czlonkowie_w_sekcjach(
  pesel_czlonka VARCHAR(11) NOT NULL,
  id_sekcji INT(7) NOT NULL,
  data_dolaczenia DATE NOT NULL,
  #funkcja VARCHAR(50),
  PRIMARY KEY (pesel_czlonka, id_sekcji),
  FOREIGN KEY (pesel_czlonka) REFERENCES Czlonkowie(pesel),
  FOREIGN KEY (id_sekcji) REFERENCES Sekcje(id_sekcji)
);

CREATE TABLE Placowki(
  adres VARCHAR(100) PRIMARY KEY,
  czynsz FLOAT(7) NOT NULL
);

CREATE TABLE Spotkania(
  id_spotkania INT(7) PRIMARY KEY AUTO_INCREMENT,
  termin DATE NOT NULL,
  id_sekcji INT(7) NOT NULL,
  adres VARCHAR(100) NOT NULL,
  FOREIGN KEY (id_sekcji) REFERENCES Sekcje(id_sekcji),
  FOREIGN KEY (adres) REFERENCES Placowki (adres)
);

CREATE TABLE Miejsca(
  adres VARCHAR(100) PRIMARY KEY,
  cena_wynajmu FLOAT(7) NOT NULL,
  max_ilosc_osob INT(7)
);

CREATE TABLE Eventy(
  id_eventu INT(7) PRIMARY KEY AUTO_INCREMENT,  -- patrz [1]
  nazwa VARCHAR(100) NOT NULL,
  data DATE NOT NULL,
  sekcja int(7) NOT NULL,
  adres VARCHAR(100) NOT NULL,
  FOREIGN KEY (sekcja) REFERENCES Sekcje(id_sekcji),
  FOREIGN KEY (adres) REFERENCES Miejsca(adres)
);


CREATE TABLE Sponsorzy(
  id_sponsora INT(7) PRIMARY KEY AUTO_INCREMENT,
  nazwa VARCHAR(100) 
);

CREATE TABLE Sponsorowanie(
  id_sponsorowania INT(7) PRIMARY KEY AUTO_INCREMENT,
  kwota FLOAT(7) NOT NULL,
  sponsor int(7) NOT NULL,
  event INT(7) NOT NULL,
  FOREIGN KEY (sponsor) REFERENCES Sponsorzy(id_sponsora),
  FOREIGN KEY (event) REFERENCES Eventy(id_eventu)
);

CREATE TABLE Turnieje(
  id_turnieju INT(7) PRIMARY KEY AUTO_INCREMENT,
  nazwa VARCHAR(100) NOT NULL,
  event INT(7) NOT NULL,
  godzina_rozpoczecia TIME NOT NULL, 
  FOREIGN KEY (event) REFERENCES Eventy(id_eventu)
);

CREATE TABLE Uczestnicy_turniejow(
  id_uczestnika INT(8) PRIMARY KEY AUTO_INCREMENT,
  imie VARCHAR(50),
  nazwisko VARCHAR(50),
  turniej INT(7) NOT NULL,
  FOREIGN KEY (turniej) REFERENCES Turnieje(id_turnieju)
);

CREATE TABLE Miejsce_w_turnieju(
  numer_miejsca INT(4) NOT NULL,
  turniej INT(7) NOT NULL,
  uczestnik INT(8) NOT NULL,
  nagroda VARCHAR(100),
  PRIMARY KEY (numer_miejsca, turniej), -- id_uczestnika pomijam, bo te 2 i tak identyfikują miejsce
  FOREIGN KEY (turniej) REFERENCES Turnieje(id_turnieju),
  FOREIGN KEY (uczestnik) REFERENCES Uczestnicy_turniejow(id_uczestnika)
);

CREATE TABLE Wydawcy(
  id_wydawcy INT(7) PRIMARY KEY AUTO_INCREMENT,
  nazwa VARCHAR(100) 
);

CREATE TABLE Platformy(
  id_platformy INT(7) PRIMARY KEY AUTO_INCREMENT,
  nazwa VARCHAR(50) 
);

CREATE TABLE Gry(
  id_gry INT(7) PRIMARY KEY AUTO_INCREMENT,
  nazwa VARCHAR(100) NOT NULL,
  cena FLOAT(4),
  wydawca int(7) NOT NULL,
  FOREIGN KEY (wydawca) REFERENCES Wydawcy(id_wydawcy) 
);

CREATE TABLE Egzemplarz(
  id_egzemplarza INT(7) PRIMARY KEY AUTO_INCREMENT,
  id_gry INT(7),
  id_sekcji int(7),
  FOREIGN KEY (id_gry) REFERENCES Gry(id_gry),
  FOREIGN KEY (id_sekcji) REFERENCES Sekcje(id_sekcji)
);

CREATE TABLE Gry_komputerowe(
  id_gry INT(7) NOT NULL,
  platforma int(7) NOT NULL,
  FOREIGN KEY (id_gry) REFERENCES Gry(id_gry),
  FOREIGN KEY (platforma) REFERENCES Platformy(id_platformy)
);

CREATE TABLE Gry_planszowe(
  id_gry INT(7) NOT NULL,
  waga FLOAT(3),
  min_liczba_graczy INT(2),
  max_liczba_graczy INT(2),
  FOREIGN KEY (id_gry) REFERENCES Gry(id_gry)
);

CREATE TABLE Gry_uzywanie(
  id_egzemplarza INT(7) NOT NULL,
  turniej INT(7) NOT NULL,
  PRIMARY KEY(id_egzemplarza, turniej),
  FOREIGN KEY (id_egzemplarza) REFERENCES Egzemplarz(id_egzemplarza),
  FOREIGN KEY (turniej) REFERENCES Turnieje(id_turnieju) 
);

CREATE VIEW Sekcje_view AS
SELECT nazwa,data_utworzenia AS data , count(pesel_czlonka) as liczba_czlonkow 
FROM Sekcje left join Czlonkowie_w_sekcjach on Sekcje.id_sekcji = Czlonkowie_w_sekcjach.id_sekcji
group by nazwa;

CREATE VIEW Czlonkowie_view AS
SELECT * FROM Czlonkowie;

CREATE VIEW Spotkanie_view AS
SELECT Nazwa,termin AS data , adres
FROM Spotkania Natural join Sekcje;

CREATE VIEW Placowki_view AS
SELECT Placowki.adres,czynsz,count(id_spotkania) AS ilosc_spotkan
FROM Placowki left join Spotkania on Placowki.adres = Spotkania.adres
group by adres;

CREATE VIEW Egzemplarz_view AS
SELECT id_egzemplarza,Gry.nazwa as tytul , Sekcje.nazwa as Sekcja from Egzemplarz 
Inner join Sekcje on Egzemplarz.id_sekcji = Sekcje.id_sekcji 
Inner join Gry on Egzemplarz.id_gry = Gry.id_gry;

create view Gry_komputerowe_view as
SELECT Gry.nazwa as tytul , Gry.cena , Platformy.nazwa as platforma , Wydawcy.nazwa as wydawca
from Gry_komputerowe 
inner join Platformy on Gry_komputerowe.platforma = Platformy.id_platformy
inner join Gry on Gry_komputerowe.id_gry = Gry.id_gry
inner join Wydawcy on Gry.wydawca=Wydawcy.id_wydawcy;

create view Gry_planszowe_view as
SELECT Gry.nazwa as tytul , Gry.cena , waga, min_liczba_graczy , max_liczba_graczy , Wydawcy.nazwa as wydawca
from Gry_planszowe
inner join Gry on Gry_planszowe.id_gry = Gry.id_gry
inner join Wydawcy on Gry.wydawca=Wydawcy.id_wydawcy;

create view Platformy_view as
SELECT nazwa as platforma , count(id_gry) as liczba_gier
from Platformy
left join Gry_komputerowe on Gry_komputerowe.platforma = Platformy.id_platformy
group by id_platformy;

create view Wydawcy_view as
SELECT Wydawcy.nazwa as wydawca , count(id_gry) as liczba_gier
from Wydawcy
left join Gry on Gry.wydawca= Wydawcy.id_wydawcy
group by id_wydawcy;

create view Event_view as
SELECT Eventy.nazwa as event , Eventy.data , Sekcje.nazwa as sekcja , Eventy.adres , sum(Sponsorowanie.kwota) as 'suma sponsorowania', GROUP_CONCAT(Distinct Sponsorzy.nazwa SEPARATOR ', ') as sponsorzy
from Eventy
left join Sponsorowanie on Eventy.id_eventu = Sponsorowanie.event
inner join Sekcje on Eventy.sekcja= Sekcje.id_sekcji
left join Sponsorzy on Sponsorzy.id_sponsora=Sponsorowanie.sponsor
Group by Eventy.id_eventu;
CREATE view Miejsce_view as 
SELECT * from Miejsca;

Create view Sponsorzy_view as 
SELECT nazwa, count(distinct Sponsorowanie.event) 'ilosc sponsorowanych eventow', sum(Sponsorowanie.kwota) as 'suma sonsorowania'
from Sponsorzy
left join Sponsorowanie on Sponsorzy.id_sponsora = Sponsorowanie.sponsor
group by id_sponsora;

Create view Turnieje_view as 
SELECT Turnieje.nazwa as turniej , godzina_rozpoczecia , Eventy.nazwa , count(distinct Uczestnicy_turniejow.id_uczestnika) as 'ilosc uczestnikow',  GROUP_CONCAT(distinct Gry_uzywanie.id_egzemplarza SEPARATOR ', ') as 'id uzywanych gier'
From Turnieje 
inner join Eventy on Turnieje.event = Eventy.id_eventu
left join Uczestnicy_turniejow on Turnieje.id_turnieju = Uczestnicy_turniejow.turniej
left join Gry_uzywanie on Turnieje.id_turnieju = Gry_uzywanie.turniej
group by Turnieje.nazwa;


Create view Uczestnicy_turniejow_view as 
SELECT imie, nazwisko , id_uczestnika , Eventy.nazwa as event , Turnieje.nazwa as turniej
from Uczestnicy_turniejow
inner join Turnieje on Uczestnicy_turniejow.turniej = Turnieje.id_turnieju
inner join Eventy on Turnieje.event = Eventy.id_eventu;

Create view Miejsce_w_turnieju_view as
SELECT Uczestnicy_turniejow.imie , Uczestnicy_turniejow.nazwisko, Eventy.nazwa as event , Turnieje.nazwa as turniej , numer_miejsca as miejsce, nagroda
from Miejsce_w_turnieju
left join Uczestnicy_turniejow on Miejsce_w_turnieju.uczestnik = Uczestnicy_turniejow.id_uczestnika
inner join Turnieje on Uczestnicy_turniejow.turniej = Turnieje.id_turnieju
inner join Eventy on Turnieje.event = Eventy.id_eventu;


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
        
INSERT into Sekcje(nazwa,data_utworzenia) values ('Gry strategiczne',CURRENT_DATE);
INSERT into Sekcje(nazwa,data_utworzenia) values ('Gry karciane',CURRENT_DATE);
INSERT into Czlonkowie(pesel,imie,nazwisko,data_urodzenia) values('00111450469','Maria','Nowak','2000-11-14');
INSERT into Czlonkowie(pesel,imie,nazwisko,data_urodzenia) values('03072876315','Jan','Kowalski','2003-07-28');
INSERT into Czlonkowie(pesel,imie,nazwisko,data_urodzenia) values('04022912378','Janusz','Lewandowski','2004-02-29');
INSERT into Czlonkowie(pesel,imie,nazwisko,data_urodzenia) values('01010177711','Mikolaj','Malinowski','2001-01-01');
INSERT into Czlonkowie_w_sekcjach values ('00111450469', 2, current_date());
INSERT into Czlonkowie_w_sekcjach values ('04022912378', 2, current_date());
INSERT into Czlonkowie_w_sekcjach values ('01010177711', 2, current_date());
INSERT into Czlonkowie_w_sekcjach values ('01010177711', 1, current_date());
INSERT into Czlonkowie_w_sekcjach values ('03072876315', 1, current_date());
INSERT into Placowki values('Polna 46',700);
INSERT into Placowki values('Wiejska 80',400);
INSERT INTO Spotkania(termin,id_sekcji,adres) values('2022-01-19',1,'Polna 46');
INSERT INTO Spotkania(termin,id_sekcji,adres) values('2022-01-25',2,'Polna 46');
INSERT INTO Spotkania(termin,id_sekcji,adres) values('2021-12-17',1,'Wiejska 80');
INSERT into Miejsca values('Polna 46',700,50);
INSERT into Miejsca values('Głowna 17',2000,500);
insert into Eventy(nazwa,data,sekcja,adres) values ('Kokon 2077','2077-02-15',2,'Polna 46');
insert into Eventy(nazwa,data,sekcja,adres) values ('Event strategow','2023-07-16',1,'Głowna 17');
insert into Sponsorzy(nazwa) values ('Miasto poznan');
insert into Sponsorzy(nazwa) values ('MDK');
insert into Sponsorowanie(kwota,sponsor,event) values (500,1,1);
insert into Sponsorowanie(kwota,sponsor,event) values (700,1,2);
insert into Sponsorowanie(kwota,sponsor,event) values (100,1,1);
insert into Sponsorowanie(kwota,sponsor,event) values (2,2,1);
insert into Sponsorowanie(kwota,sponsor,event) values (5,2,2);
insert into Turnieje(nazwa,event,godzina_rozpoczecia) values ('Keyforgers',1,'15:00');
insert into Turnieje(nazwa,event,godzina_rozpoczecia) values ('Kosiarze',2,'13:00');
insert into Uczestnicy_turniejow(imie,nazwisko,turniej) values ('Piotr','Malecki',1);
insert into Uczestnicy_turniejow(imie,nazwisko,turniej) values ('Sebastian','Lewandowski',1);
insert into Uczestnicy_turniejow(imie,nazwisko,turniej) values ('Jan','Piotrowski',2);
insert into Uczestnicy_turniejow(imie,nazwisko,turniej) values ('Krzysztof','Terlecki',2);
insert into Uczestnicy_turniejow(imie,nazwisko,turniej) values ('Maja','Kasznia',2);
insert into Miejsce_w_turnieju values (1,1,2,'50 zl');
insert into Miejsce_w_turnieju values (1,2,5,'100 zl');
Insert into Wydawcy(nazwa) values ('Rebel');
Insert into Wydawcy(nazwa) values ('Nasza Ksiegarnia');
Insert into Wydawcy(nazwa) values ('Ubisoft');
insert into Platformy(nazwa) values ('Uplay');
insert into Platformy(nazwa) values ('Steam');
insert into Gry(nazwa,cena,wydawca) values ('Smoki',50,2);
insert into Gry(nazwa,cena,wydawca) values ('Kruki',50,2);
insert into Gry(nazwa,cena,wydawca) values ('Scythe',150,1);
insert into Gry(nazwa,cena,wydawca) values ('Keyforge',70,1);
insert into Gry(nazwa,cena,wydawca) values ('Assasin Creed',100,3);
insert into Gry(nazwa,cena,wydawca) values ('Rainbow Siegie',60,3);
insert into Egzemplarz(id_gry,id_sekcji) values (1,2);
insert into Egzemplarz(id_gry,id_sekcji) values (1,2);
insert into Egzemplarz(id_gry,id_sekcji) values (2,2);
insert into Egzemplarz(id_gry,id_sekcji) values (3,1);
insert into Egzemplarz(id_gry,id_sekcji) values (3,1);
insert into Egzemplarz(id_gry,id_sekcji) values (3,1);
insert into Egzemplarz(id_gry,id_sekcji) values (4,2);
insert into Egzemplarz(id_gry,id_sekcji) values (5,1);
insert into Egzemplarz(id_gry,id_sekcji) values (6,1);
insert into Gry_komputerowe values (5,1);
insert into Gry_komputerowe values (5,2);
insert into Gry_komputerowe values (6,1);
insert into Gry_planszowe values (1,0.3,2,5);
insert into Gry_planszowe values (2,0.4,2,2);
insert into Gry_planszowe values (3,3.1,1,5);
insert into Gry_planszowe values (4,0.6,2,2);
insert into Gry_uzywanie values(4,2);
insert into Gry_uzywanie values(6,2);
insert into Gry_uzywanie values(7,1);        

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
create procedure Eventy_add(IN c_nazwa varchar(50),IN c_data date,IN c_nazwa_sekcji varchar(50),IN c_adres varchar(100)) 
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
		select id_turnieju into c_id_turnieju from Turnieje where nazwa = c_nazwa_turnieju;
        insert into Uczestnicy_turniejow(imie,nazwisko,turniej) values (c_imie,c_nazwisko,c_id_turnieju);
        end//
delimiter ;

delimiter //
create procedure Miejsce_w_turnieju_add(IN c_numer_miejsca int(7),IN c_nazwa_turnieju varchar(50),IN c_id_uczestnika int(7),IN c_nagroda varchar(100)) 
		begin
        DECLARE c_id_turnieju INT(7);
		select id_turnieju into c_id_turnieju from Turnieje where nazwa = c_nazwa_turnieju;
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
        SELECT id_gry into c_id_gry from Gry where Gry.nazwa=c_nazwa; 
        SELECT id_platformy into c_id_platformy from Platformy where nazwa = c_nazwa_platformy;
        insert into Gry_komputerowe values (c_id_gry,c_id_platformy);
        end//
delimiter ;


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
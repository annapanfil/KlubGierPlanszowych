--------------------------------------------------------------------------------
-- TABELE

CREATE TABLE IF NOT EXISTS Czlonkowie (
  pesel VARCHAR(11) PRIMARY KEY,
  imie VARCHAR(50) NOT NULL,
  nazwisko VARCHAR(50) NOT NULL,
  data_urodzenia DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS Sekcje(
  nazwa VARCHAR(50) PRIMARY KEY,
  data_utworzenia DATE
);

CREATE TABLE IF NOT EXISTS Czlonkowie_w_sekcjach(
  pesel_czlonka VARCHAR(11) NOT NULL,
  nazwa_sekcji VARCHAR(50) NOT NULL,
  data_dolaczenia DATE NOT NULL,
  funkcja VARCHAR(50),
  PRIMARY KEY (pesel_czlonka, nazwa_sekcji),
  FOREIGN KEY (pesel_czlonka) REFERENCES Czlonkowie(pesel),
  FOREIGN KEY (nazwa_sekcji) REFERENCES Sekcje(nazwa)
);


CREATE TABLE IF NOT EXISTS Placowki(
  adres VARCHAR(100) PRIMARY KEY,
  czynsz FLOAT(7) NOT NULL
);

CREATE TABLE IF NOT EXISTS Spotkania(
  termin DATE NOT NULL,
  sekcja VARCHAR(50) NOT NULL,
  adres VARCHAR(100) NOT NULL,
  PRIMARY KEY (sekcja, adres),
  FOREIGN KEY (sekcja) REFERENCES Sekcje(nazwa),
  FOREIGN KEY (adres) REFERENCES Placowki (adres)
);

CREATE TABLE IF NOT EXISTS Miejsca(
  adres VARCHAR(100) PRIMARY KEY,
  cena_wynajmu FLOAT(7) NOT NULL,
  max_ilosc_osob INT(7)
);

CREATE TABLE IF NOT EXISTS Eventy(
  id_eventu INT(7) PRIMARY KEY AUTO_INCREMENT,  -- patrz [1]
  nazwa VARCHAR(100) NOT NULL,
  data DATE NOT NULL,
  sekcja VARCHAR(50) NOT NULL,
  adres VARCHAR(100) NOT NULL,
  FOREIGN KEY (sekcja) REFERENCES Sekcje(nazwa),
  FOREIGN KEY (adres) REFERENCES Miejsca(adres)
);


CREATE TABLE IF NOT EXISTS Sponsorzy(
  nazwa VARCHAR(100) PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS Sponsorowanie(
  kwota FLOAT(7) NOT NULL,
  sponsor VARCHAR(100) NOT NULL,
  event INT(7) NOT NULL,
  PRIMARY KEY (sponsor, event),
  FOREIGN KEY (sponsor) REFERENCES Sponsorzy(nazwa),
  FOREIGN KEY (event) REFERENCES Eventy(id_eventu)
);

CREATE TABLE IF NOT EXISTS Turnieje(
  id_turnieju INT(7) PRIMARY KEY AUTO_INCREMENT,
  nazwa VARCHAR(100) NOT NULL,
  event INT(7) NOT NULL,
  godzina_rozpoczecia TIME NOT NULL, 
  FOREIGN KEY (event) REFERENCES Eventy(id_eventu)
);

CREATE TABLE IF NOT EXISTS Uczestnicy_turniejow(
  id_uczestnika INT(8) PRIMARY KEY AUTO_INCREMENT,
  imie VARCHAR(50),
  nazwisko VARCHAR(50),
  turniej INT(7) NOT NULL,
  FOREIGN KEY (turniej) REFERENCES Turnieje(id_turnieju)
);

CREATE TABLE IF NOT EXISTS Miejsce_w_turnieju(
  numer_miejsca INT(4) NOT NULL,
  turniej INT(7) NOT NULL,
  uczestnik INT(8) NOT NULL,
  nagroda VARCHAR(100),
  PRIMARY KEY (numer_miejsca, turniej), -- id_uczestnika pomijam, bo te 2 i tak identyfikują miejsce
  FOREIGN KEY (turniej) REFERENCES Turnieje(id_turnieju),
  FOREIGN KEY (uczestnik) REFERENCES Uczestnicy_turniejow(id_uczestnika)
);

CREATE TABLE IF NOT EXISTS Wydawcy(
  nazwa VARCHAR(100) PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS Platformy(
  nazwa VARCHAR(50) PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS Gry(
  id_gry INT(7) PRIMARY KEY AUTO_INCREMENT,
  nazwa VARCHAR(100) NOT NULL,
  cena FLOAT(4),
  wydawca VARCHAR(100) NOT NULL,
  FOREIGN KEY (wydawca) REFERENCES Wydawcy(nazwa) 
);

CREATE TABLE IF NOT EXISTS Egzemplarz(
  id_egzemplarza INT(7) PRIMARY KEY AUTO_INCREMENT,
  id_gry INT(7),
  sekcja VARCHAR(50),
  FOREIGN KEY (id_gry) REFERENCES Gry(id_gry),
  FOREIGN KEY (sekcja) REFERENCES Sekcje(nazwa)
);

CREATE TABLE IF NOT EXISTS Gry_komputerowe(
  id_gry INT(7) NOT NULL,
  platforma VARCHAR(50) NOT NULL,
  FOREIGN KEY (id_gry) REFERENCES Gry(id_gry),
  FOREIGN KEY (platforma) REFERENCES Platformy(nazwa)
);

CREATE TABLE IF NOT EXISTS Gry_planszowe(
  id_gry INT(7) NOT NULL,
  waga FLOAT(3),
  min_liczba_graczy INT(2),
  max_liczba_graczy INT(2),
  FOREIGN KEY (id_gry) REFERENCES Gry(id_gry)
);

CREATE TABLE IF NOT EXISTS Gry_uzywanie(
  id_egzemplarza INT(7) NOT NULL,
  turniej INT(7) NOT NULL,
  PRIMARY KEY(id_egzemplarza, turniej),
  FOREIGN KEY (id_egzemplarza) REFERENCES Egzemplarz(id_egzemplarza),
  FOREIGN KEY (turniej) REFERENCES Turnieje(id_turnieju) 
);

-------------------------------------------------------------------------------
-- SEKWENCJE
-- Realizowane przez AUTO_INCREMENT, ponieważ mySQL nie posiada sekwencji
--------------------------------------------------------------------------------
-- FUNKCJE

 -- zwraca sumę kwot od sponsorów
CREATE OR REPLACE FUNCTION kwota_na_event(
  vid_eventu INT
) RETURNS INT
BEGIN
  DECLARE vKwota INT;
  SELECT SUM(kwota) INTO vKwota
  FROM Sponsorowanie
  WHERE event = vid_eventu;
  RETURN vKwota;
END;


 -- wstawia do tabeli członkowie datę urodzenia na podstawie podanego peselu
/*
CREATE OR REPLACE PROCEDURE data_ur_z_peselu
(IN vPesel VARCHAR)
AS
BEGIN
    DECLARE vDate DATE;
    IF CAST(substr(vPesel, 3, 2) AS INT) >= 21 THEN
       vDate := to_date( '20' || substr(vPesel, 1, 2) || cast(substr(vPesel, 3, 2) AS INT)-20 || substr(vPesel, 5, 2), 'yyyyMMdd');
       UPDATE Czlonkowie SET data_ur = vDate WHERE pesel = vPesel;
    ELSE
        vDate := to_date( '19' || substr(vPesel, 1, 6), 'yyyyMMdd');
        UPDATE Czlonkowie SET data_ur = vDate WHERE pesel = vPesel;
    END IF;
END;
*/

--------------------------------------------------------------------
-- INDEKSY
CREATE OR REPLACE INDEX miejsca_cena
ON Miejsca(cena_wynajmu);

CREATE OR REPLACE INDEX czlonkowie_nazwiska
ON Czlonkowie (nazwisko);

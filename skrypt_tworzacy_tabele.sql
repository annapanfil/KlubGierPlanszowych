--------------------------------------------------------------------------------
-- TABELE

CREATE TABLE Czlonkowie (
  pesel VARCHAR(11) PRIMARY KEY,
  imie VARCHAR(50) NOT NULL,
  nazwisko VARCHAR(50) NOT NULL,
  data_urodzenia DATE NOT NULL
);

CREATE TABLE Sekcje(
  nazwa VARCHAR(50) PRIMARY KEY,
  data_utworzenia DATE
);

CREATE TABLE Czlonkowie_w_sekcjach(
  pesel_czlonka VARCHAR(11) REFERENCES Czlonkowie(pesel) NOT NULL,
  nazwa_sekcji VARCHAR(50) REFERENCES Sekcje(nazwa) NOT NULL,
  data_dolaczenia DATE NOT NULL,
  funkcja VARCHAR(50),
  PRIMARY KEY (pesel_czlonka, nazwa_sekcji)
);

CREATE TABLE Placowki(
  adres VARCHAR(100) PRIMARY KEY,
  czynsz NUMBER(9,2) NOT NULL
);

CREATE TABLE Spotkania(
  termin DATE NOT NULL,
  sekcja VARCHAR(50) REFERENCES Sekcje(nazwa) NOT NULL,
  adres VARCHAR(100) REFERENCES Placowki(adres) NOT NULL,
  PRIMARY KEY (sekcja, adres)
);

CREATE TABLE Miejsca(
  adres VARCHAR(100) PRIMARY KEY,
  cena_wynajmu NUMBER(9,2) NOT NULL,
  max_ilosc_osob NUMBER(7)
);

CREATE TABLE Eventy(
  id_eventu NUMBER(7) PRIMARY KEY,  -- patrz [1]
  nazwa VARCHAR(100) NOT NULL,
  data DATE NOT NULL,
  sekcja VARCHAR(50) REFERENCES Sekcje(nazwa) NOT NULL,
  adres VARCHAR(100) REFERENCES Miejsca(adres) NOT NULL,
);

CREATE TABLE Sponsorzy(
  nazwa VARCHAR(100) PRIMARY KEY
);

CREATE TABLE Sponsorowanie(
  kwota NUMBER(9,2) NOT NULL,
  sponsor VARCHAR(100) REFERENCES Sponsorzy(nazwa) NOT NULL,
  event VARCHAR(100) REFERENCES Eventy(id_eventu) NOT NULL,
  PRIMARY KEY (sponsor, event)
);

CREATE TABLE Turnieje(
  id_turnieju NUMBER(7) PRIMARY KEY,
  nazwa VARCHAR(100) NOT NULL,
  event VARCHAR(100) REFERENCES Eventy(id_eventu) NOT NULL,
  godzina_rozpoczecia TIME NOT NULL, --albo DATETIME
);

CREATE TABLE Uczestnicy_turniejow(
  id_uczestnika NUMBER(8) PRIMARY KEY,
  imie VARCHAR(50),
  nazwisko VARCHAR(50),
  turniej VARCHAR(100) REFERENCES Turnieje(id_turnieju) NOT NULL,
);

CREATE TABLE Miejsce_w_turnieju(
  numer_miejsca NUMBER(4) NOT NULL,
  turniej VARCHAR(100) REFERENCES Turnieje(id_turnieju) NOT NULL,
  uczestnik NUMBER(8) REFERENCES Uczestnicy_turniejow(id_uczestnika) NOT NULL
  nagroda VARCHAR(100),
  PRIMARY KEY (numer_miejsca, turniej) -- id_uczestnika pomijam, bo te 2 i tak identyfikują miejsce
);

CREATE TABLE Wydawcy(
  nazwa VARCHAR(100) PRIMARY KEY
);

CREATE TABLE Platformy(
  nazwa VARCHAR(50) PRIMARY KEY
);

CREATE TABLE Egzemplarz(
  id_egzemplarza NUMBER(7) PRIMARY KEY,
  id_gry NUMBER(7) REFERENCES Gry(id_gry)
  sekcja VARCHAR(50) REFERENCES Sekcje(nazwa)
);

CREATE TABLE Gry(
  id_gry NUMBER(7) PRIMARY KEY,
  nazwa VARCHAR(100) NOT NULL,
  cena NUMBER(6,2),
  wydawca VARCHAR(100) REFERENCES Wydawcy(nazwa) NOT NULL
);

CREATE TABLE Gry_komputerowe(
  id_gry NUMBER(7) REFERENCES Gry(id_gry) NOT NULL,
  platforma VARCHAR(50) REFERENCES Platformy(nazwa) NOT NULL
);

CREATE TABLE Gry_planszowe(
  id_gry NUMBER(7) REFERENCES Gry(id_gry) NOT NULL,
  waga NUMBER(5,2),
  min_liczba_graczy NUMBER(2),
  max_liczba_graczy NUMBER(2)
);

CREATE TABLE Gry_uzywanie(
  id_egzemplarza NUMBER(7) REFERENCES Egzemplarz(id_egzemplarza) NOT NULL,
  turniej VARCHAR(100) REFERENCES Turnieje(id_turnieju) NOT NULL,
  PRIMARY KEY(id_egzemplarza, turniej)
);

-------------------------------------------------------------------------------
-- SEKWENCJE
CREATE SEQUENCE id_zrzutki START WITH 0 INCREMENT BY 1 MAXVALUE 9999999;
CREATE SEQUENCE id_eventu START WITH 0 INCREMENT BY 1 MAXVALUE 9999999;
CREATE SEQUENCE id_turnieju START WITH 0 INCREMENT BY 1 MAXVALUE 9999999;
CREATE SEQUENCE id_uczestnika START WITH 0 INCREMENT BY 1 MAXVALUE 9999999;
CREATE SEQUENCE id_gry START WITH 0 INCREMENT BY 1 MAXVALUE 9999999;
--------------------------------------------------------------------------------
-- FUNKCJE
CREATE OR REPLACE FUNCTION kwota_na_event(
  vid_eventu IN NUMBER
) -- zwraca sumę kwot od sponsorów
DECLARE
  vKwota NUMBER;
BEGIN
  SELECT SUM(kwota) INTO vKwota
  FROM Sponsorowanie
  WHERE event = vid_eventu;
  RETURN kwota;
END kwota_na_event;


CREATE OR REPLACE PROCEDURE data_ur_z_peselu
(vPesel IN VARCHAR2)
AS -- wstawia do tabeli członkowie datę urodzenia na podstawie podanego peselu
    vDate DATE;
BEGIN
    IF CAST(substr(vPesel, 3, 2) AS NUMBER) >= 21 THEN
       vDate := to_date( '20' || substr(vPesel, 1, 2) || cast(substr(vPesel, 3, 2) AS NUMBER)-20 || substr(vPesel, 5, 2), 'yyyyMMdd');
       UPDATE Czlonkowie SET data_ur = vDate WHERE pesel = vPesel;
    ELSE
        vDate := to_date( '19' || substr(vPesel, 1, 6), 'yyyyMMdd');
        UPDATE Czlonkowie SET data_ur = vDate WHERE pesel = vPesel;
    END IF;
END data_ur_z_peselu;

--------------------------------------------------------------------
-- INDEKSY
CREATE INDEX miejsca_cena
ON Miejsca(cena_wynajmu);

CREATE INDEX czlonkowie_nazwiska
ON Czlonkowie (nazwisko);

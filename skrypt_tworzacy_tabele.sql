-- Dodałam sztuczne klucze, żeby ułatwić joiny. Nie wiem tylko, czy wtedy nie tracimy identyfikacji
-- [1] https://solutioncenter.apexsql.com/sql-database-refactoring-techniques-replacing-a-natural-key-with-a-surrogate-key/

-- Czy adresy (i ogólnie varchary) są dobrymi kluczami? Na razie je zostawiłam
--[2] https://www.mssqltips.com/sqlservertip/5431/surrogate-key-vs-natural-key-differences-and-when-to-use-in-sql-server/

CREATE TABLE Czlonkowie (
  pesel VARCHAR(11) PRIMARY KEY,
  imie VARCHAR(50) NOT NULL,
  nazwisko VARCHAR(50) NOT NULL,
  data_urodzenia DATE NOT NULL --zmieniłam, bo wiek by trzeba aktualizować
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

CREATE TABLE Zrzutki(
  id_zrzutki NUMBER(7) PRIMARY KEY,
  cel VARCHAR(150) NOT NULL,
  cena NUMBER(8,2) NOT NULL,
  data_rozpoczecia DATE NOT NULL,
  sekcja VARCHAR(50) REFERENCES Sekcje(nazwa)
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

--wzorowane na lab Koszlajda transformacja pojazdy
CREATE TABLE Gry(
  id_gry NUMBER(7) PRIMARY KEY,
  nazwa VARCHAR(100) NOT NULL,
  cena NUMBER(6,2),
  wydawca VARCHAR(100) REFERENCES Wydawcy(nazwa) NOT NULL
);

CREATE TABLE Gry_komputerowe(
  id_gry NUMBER(7) REFERENCES Gry(id_gry) NOT NULL
);

CREATE TABLE Gry_planszowe(
  id_gry NUMBER(7) REFERENCES Gry(id_gry) NOT NULL,
  waga NUMBER(5,2),
  min_liczba_graczy NUMBER(2),
  max_liczba_graczy NUMBER(2)
);

--TODO: ograniczyć do gier komputerowych
CREATE TABLE Gry_platformy(
  id_gry NUMBER(7) REFERENCES Gry(id_gry) NOT NULL,
  platforma VARCHAR(50) REFERENCES Platformy(nazwa) NOT NULL,
  PRIMARY KEY (id_gry, platforma)
);

CREATE TABLE Gry_uzywanie(
  id_gry NUMBER(7) REFERENCES Gry(id_gry) NOT NULL,
  turniej VARCHAR(100) REFERENCES Turnieje(id_turnieju) NOT NULL,
  PRIMARY KEY(id_gry, turniej)
);

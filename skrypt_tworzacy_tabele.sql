CREATE TABLE Czlonkowie (
  pesel VARCHAR(11) PRIMARY KEY,
  imie VARCHAR(50) NOT NULL,
  nazwisko VARCHAR(50) NOT NULL,
  data_urodzenia DATE NOT NULL --zmieniłam, bo wiek by trzeba aktualizować
);

CREATE TABLE Sekcje(
  nazwa VARCHAR(50) PRIMARY KEY
);

CREATE TABLE Czlonkowie_w_sekcjach(
  pesel_czlonka VARCHAR(11) REFERENCES Czlonkowie(pesel) NOT NULL,
  nazwa_sekcji VARCHAR(50) REFERENCES Sekcje(nazwa) NOT NULL,
  data_dolaczenia DATE NOT NULL,
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
  data_rozpoczecia DATE NOT NULL
  sekcja VARCHAR(50) REFERENCES Sekcje(nazwa)
);

CREATE TABLE Miejsca(
  adres VARCHAR(100) PRIMARY KEY,
  cena_wynajmu NUMBER(9,2) NOT NULL,
  max_ilosc_osob NUMBER(7)
);

CREATE TABLE Eventy(
  nazwa VARCHAR(100) NOT NULL,
  sekcja VARCHAR(50) REFERENCES Sekcje(nazwa) NOT NULL, -- A może zwykła relacja, bez identyfikacji?
  data DATE NOT NULL,
  adres VARCHAR(100) REFERENCES Miejsca(adres) NOT NULL,
  PRIMARY KEY (nazwa, sekcja)
);

CREATE TABLE Sponsorzy(
  nazwa VARCHAR(100) PRIMARY KEY
);

CREATE TABLE Sponsorowanie(
  kwota NUMBER(9,2) NOT NULL,
  sponsor VARCHAR(100) REFERENCES Sponsorzy(nazwa) NOT NULL,
  event VARCHAR(100) REFERENCES Eventy(nazwa) NOT NULL,
  sekcja VARCHAR(50) REFERENCES Sekcje(nazwa) NOT NULL, --tu jest
  PRIMARY KEY (sponsor, event, sekcja)
);

-- podpina się do sekcji, mimo że powinno do eventów (patrz SBD1 wykł 5 sl. 15)
CREATE TABLE Turnieje(
  nazwa VARCHAR(100) NOT NULL,
  event VARCHAR(100) REFERENCES Eventy(nazwa) NOT NULL,
  sekcja VARCHAR(50) REFERENCES Sekcje(nazwa) NOT NULL, --i tu
  godzina_rozpoczecia TIME NOT NULL, --albo DATETIME
  PRIMARY KEY(nazwa, event, sekcja) -- może zamiast tego jakieś id turnieju?
);

CREATE TABLE Uczestnicy_turniejow(
  id_uczestnika NUMBER(8) PRIMARY KEY, -- nie wiem, czy tak nie tracimy identyfikacji, ale w sumie id jest jednoznaczne
  imie VARCHAR(50),
  nazwisko VARCHAR(50),
  turniej VARCHAR(100) REFERENCES Turnieje(nazwa) NOT NULL,
  event VARCHAR(100) REFERENCES Eventy(nazwa) NOT NULL,
  sekcja VARCHAR(50) REFERENCES Sekcje(nazwa) NOT NULL --tu też

  -- PRIMARY KEY(id_uczestnika, turniej, event, sekcja) --trzeba tak? Czy wystarczy id?
);

CREATE TABLE Miejsce_w_turnieju(
  numer_miejsca NUMBER(4) NOT NULL,
  turniej VARCHAR(100) REFERENCES Turnieje(nazwa) NOT NULL,
  event VARCHAR(100) REFERENCES Eventy(nazwa) NOT NULL,
  sekcja VARCHAR(50) REFERENCES Sekcje(nazwa) NOT NULL, --tu też
  id_uczestnika NUMBER(8) REFERENCES Uczestnicy_turniejow NOT NULL
  nagroda VARCHAR(100),
  PRIMARY KEY (numer_miejsca, turniej, event, sekcja, id_uczestnika)
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
  liczba_graczy NUMBER(2) --dodany
);

--TODO: ograniczyć do gier komputerowych
CREATE TABLE Gry_platformy(
  id_gry NUMBER(7) REFERENCES Gry(id_gry) NOT NULL,
  platforma VARCHAR(50) REFERENCES Platformy(nazwa) NOT NULL,
  PRIMARY KEY (id_gry, platforma)
);

CREATE TABLE Gry_uzywanie(
  id_gry NUMBER(7) REFERENCES Gry(id_gry) NOT NULL,
  turniej VARCHAR(100) REFERENCES Turnieje(nazwa) NOT NULL,
  event VARCHAR(100) REFERENCES Eventy(nazwa) NOT NULL,
  sekcja VARCHAR(50) REFERENCES Sekcje(nazwa) NOT NULL, --i tu
  PRIMARY KEY(id_gry, turniej, event, sekcja)
);

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
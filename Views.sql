CREATE VIEW Sekcje_view AS
SELECT Nazwa,data_utworzenia AS data , count(pesel_czlonka) as liczba_czlonkow 
FROM Sekcje Natural join czlonkowie_w_sekcjach
group by nazwa;

CREATE VIEW Czlonkowie_view AS
SELECT * FROM czlonkowie;

CREATE VIEW Spotkanie_view AS
SELECT Nazwa,termin AS data , adres
FROM spotkania Natural join sekcje;

CREATE VIEW Placowki_view AS
SELECT adres,czynsz,count(id_spotkania) AS ilosc_spotkan
FROM placowki Natural join spotkania
group by adres;

CREATE VIEW Egzemplarz_view AS
SELECT id_egzemplarza,gry.nazwa as tytul , sekcje.nazwa as sekcja from egzemplarz 
Inner join sekcje on egzemplarz.sekcja = sekcje.id_sekcji 
Inner join gry on egzemplarz.id_gry = gry.id_gry;

create view Gry_komputerowe_view as
SELECT gry.nazwa as tytul , gry.cena , platformy.nazwa as platforma , wydawcy.nazwa as wydawca
from gry_komputerowe 
inner join platformy on gry_komputerowe.platforma = platformy.id_platformy
inner join gry on gry_komputerowe.id_gry = gry.id_gry
inner join wydawcy on gry.wydawca=wydawcy.id_wydawcy;

create view Gry_planszowe_view as
SELECT gry.nazwa as tytul , gry.cena , waga, min_liczba_graczy , max_liczba_graczy , wydawcy.nazwa as wydawca
from gry_planszowe
inner join gry on gry_planszowe.id_gry = gry.id_gry
inner join wydawcy on gry.wydawca=wydawcy.id_wydawcy;

create view platformy_view as
SELECT nazwa as platforma , count(id_gry) as liczba_gier
from platformy
inner join gry_komputerowe on gry_komputerowe.platforma = platformy.id_platformy
group by id_platformy;

create view wydawcy_view as
SELECT wydawcy.nazwa as wydawca , count(id_gry) as liczba_gier
from wydawcy
inner join gry on gry.wydawca= wydawcy.id_wydawcy
group by id_wydawcy;

create view event_view as
SELECT eventy.nazwa as event , eventy.data , sekcje.nazwa as sekcja , eventy.adres , sum(sponsorowanie.kwota), GROUP_CONCAT(Distinct sponsorowanie.sponsor SEPARATOR ', ')
from eventy
inner join sponsorowanie on eventy.id_eventu = sponsorowanie.event
inner join sekcje on eventy.sekcja= sekcje.id_sekcji
Group by eventy.id_eventu;

CREATE view miejsce_view as 
SELECT * from miejsca;

Create view Sponsorzy_view as 
SELECT nazwa, count(distinct sponsorowanie.event), sum(sponsorowanie.kwota)
from sponsorzy
Inner join sponsorowanie on sponsorzy.id_sponsora = sponsorowanie.sponsor
group by id_sponsora;

Create view Turnieje_view as 
SELECT turnieje.nazwa as turniej , godzina_rozpoczecia , eventy.nazwa , count(uczestnicy_turniejow.id_uczestnika) ,  GROUP_CONCAT(gry_uzywanie.id_egzemplarza SEPARATOR ', ')
From turnieje 
inner join eventy on turnieje.event = eventy.id_eventu
Inner join uczestnicy_turniejow on turnieje.id_turnieju = uczestnicy_turniejow.turniej
Inner join gry_uzywanie on turnieje.id_turnieju = gry_uzywanie.turniej
group by turnieje.id_turnieju;

Create view Uczestnicy_turniejow_view as 
SELECT imie, nazwisko , id_uczestnika , eventy.nazwa as event , turnieje.nazwa as turniej
from uczestnicy_turniejow
inner join turnieje on uczestnicy_turniejow.turniej = turnieje.id_turnieju
inner join eventy on turnieje.event = eventy.id_eventu;

Create view Miejsce_w_turnieju_view as
SELECT uczestnicy_turniejow.imie , uczestnicy_turniejow.nazwisko, eventy.nazwa as event , turnieje.nazwa as turniej , numer_miejsca as miejsce, nagroda
from miejsce_w_turnieju
inner join uczestnicy_turniejow on miejsce_w_turnieju.uczestnik = uczestnicy_turniejow.id_uczestnika
inner join turnieje on uczestnicy_turniejow.turniej = turnieje.id_turnieju
inner join eventy on turnieje.event = eventy.id_eventu;





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

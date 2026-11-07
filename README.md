# Zadatak: priprema radnog okruženja

## AI upit

Napiši Python funkciju prosjecna_cijena za računanje prosječne cijene noćenja

## Nedostaci

- Funkcija ne uzima u obzir broj noćenja pri računanju prosječne cijene.
- Funkcija ne provjerava da li su unesene vrijednosti brojevi, pa može doći do greške ako se unese tekst ili None.
- Funkcija prihvata negativne cijene.
- Funkcija ne provjerava neuobičajeno visoke ili niske cijene koje mogu biti unesene greškom.
- Funkcija vraća 0 za praznu listu, iako nema podataka za računanje prosjeka.
- Rezultat se ne zaokružuje na dvije decimale.

# Mini projekat 1: refaktoring obrade rezervacija

## AI upiti

- (2) Refaktoriši sljedeći Python kod za obradu rezervacija koristeći klase i funkcije i SOLID principe S i D:
- (3) Dodaj Protocol za izvor podataka i za izvještavanje u prethodni kod
- (4) Napiši tri pytest testa sa zamjenskim izvorom podataka. Provjeri ukupnu cijenu, praznu listu i vrijednosti 239, 240 i 241.

## Ispravke generisanog koda

- U fajlu obrada_rezervacija.py dodata je provjera `if __name__ == "__main__"` da se kod ne izvršava pri importovanju.
- U fajlu obrada_rezervacija_protocol.py promijenila sam klasu ListaRezervacija da mogu sama unijeti rezervacije. Takođe sam podijelila posljednju liniju koda na više linija da bude jasnije.
- U fajlu test_obrada_rezervacija_protocol.py u klasu LazniIzvjestaj dodala sam __init__ sa početnim vrijednostima None, da testovi budu jasniji ako nešto ne radi.
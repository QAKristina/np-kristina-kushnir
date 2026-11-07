from obrada_rezervacija_protocol import Rezervacija, obradi_rezervacije


class LazniIzvor:
    def __init__(self, rezervacije):
        self.rezervacije = rezervacije

    def ucitaj_rezervacije(self):
        return self.rezervacije


class LazniIzvjestaj:
    def __init__(self):
        self.ukupno = None
        self.gosti = None

    def prikazi(self, ukupno, gosti):
        self.ukupno = ukupno
        self.gosti = gosti


def test_ukupna_cijena():
    izvor = LazniIzvor([
        Rezervacija("Ana", 3, 80),
        Rezervacija("Marko", 5, 65),
        Rezervacija("Ivana", 2, 120),
    ])
    izvjestaj = LazniIzvjestaj()

    obradi_rezervacije(izvor, izvjestaj)

    assert izvjestaj.ukupno == 805


def test_prazna_lista():
    izvor = LazniIzvor([])
    izvjestaj = LazniIzvjestaj()

    obradi_rezervacije(izvor, izvjestaj)

    assert izvjestaj.ukupno == 0
    assert izvjestaj.gosti == []


def test_granica_240():
    izvor = LazniIzvor([
        Rezervacija("Ana", 1, 239),
        Rezervacija("Marko", 1, 240),
        Rezervacija("Ivana", 1, 241),
    ])
    izvjestaj = LazniIzvjestaj()

    obradi_rezervacije(izvor, izvjestaj)

    assert izvjestaj.gosti == ["Marko", "Ivana"]
from typing import Protocol


class Rezervacija:
    def __init__(self, gost, noci, cijena_noci):
        self.gost = gost
        self.noci = noci
        self.cijena_noci = cijena_noci

    def ukupna_cijena(self):
        return self.noci * self.cijena_noci


class IzvorPodataka(Protocol):
    def ucitaj_rezervacije(self) -> list[Rezervacija]:
        ...


class Izvjestavanje(Protocol):
    def prikazi(self, ukupno, gosti):
        ...


class ListaRezervacija:
    #def ucitaj_rezervacije(self):
    #    return [
    #        Rezervacija("Ana", 3, 80),
    #        Rezervacija("Marko", 5, 65),
    #        Rezervacija("Ivana", 2, 120),
    #    ]
    def __init__(self, rezervacije):
        self.rezervacije = rezervacije

    def ucitaj_rezervacije(self):
        return self.rezervacije


class KonzolniIzvjestaj:
    def prikazi(self, ukupno, gosti):
        print(ukupno)
        print(gosti)


def ukupna_cijena_rezervacija(rezervacije):
    return sum(r.ukupna_cijena() for r in rezervacije)


def skupa_nocenja(rezervacije, granica=240):
    return [
        r.gost
        for r in rezervacije
        if r.ukupna_cijena() >= granica
    ]


def obradi_rezervacije(izvor: IzvorPodataka, izvjestaj: Izvjestavanje):
    rezervacije = izvor.ucitaj_rezervacije()
    ukupno = ukupna_cijena_rezervacija(rezervacije)
    gosti = skupa_nocenja(rezervacije)
    izvjestaj.prikazi(ukupno, gosti)


if __name__ == "__main__":
    rezervacije = [
        Rezervacija("Ana", 3, 80),
        Rezervacija("Marko", 5, 65),
        Rezervacija("Ivana", 2, 120),
    ]

    izvor = ListaRezervacija(rezervacije)
    izvjestaj = KonzolniIzvjestaj()

    obradi_rezervacije(izvor, izvjestaj)
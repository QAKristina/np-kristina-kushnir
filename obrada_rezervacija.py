class Rezervacija:
    def __init__(self, gost, noci, cijena_noci):
        self.gost = gost
        self.noci = noci
        self.cijena_noci = cijena_noci

    def ukupna_cijena(self):
        return self.noci * self.cijena_noci


def ukupna_cijena_rezervacija(rezervacije):
    return sum(r.ukupna_cijena() for r in rezervacije)


def skupa_nocenja(rezervacije, granica=240):
    return [
        r.gost
        for r in rezervacije
        if r.ukupna_cijena() >= granica
    ]

if __name__ == "__main__":
    rezervacije = [
        Rezervacija("Ana", 3, 80),
        Rezervacija("Marko", 5, 65),
        Rezervacija("Ivana", 2, 120),
    ]

    print(ukupna_cijena_rezervacija(rezervacije))
    print(skupa_nocenja(rezervacije))
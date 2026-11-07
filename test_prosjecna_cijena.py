from prosjecna_cijena import prosjecna_cijena


def test_prosjecna_cijena():
    assert prosjecna_cijena([80, 100, 120]) == 100


def test_prazna_lista():
    assert prosjecna_cijena([]) == 0
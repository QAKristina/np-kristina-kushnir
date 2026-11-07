def prosjecna_cijena(cijene):
    if not cijene:
        return 0

    return sum(cijene) / len(cijene)

print(prosjecna_cijena([]))
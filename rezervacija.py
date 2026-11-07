rezervacije = [
    {"gost": "Ana", "noci": 3, "cijena_noci": 80},
    {"gost": "Marko", "noci": 5, "cijena_noci": 65},
    {"gost": "Ivana", "noci": 2, "cijena_noci": 120},
]

# Eksplicitna petlja
ukupno = 0
for r in rezervacije:
    ukupno += r["noci"] * r["cijena_noci"]

# Ekvivalent pomoću izraza
iznosi = [r["noci"] * r["cijena_noci"] for r in rezervacije]
skupa_nocenja = [r["gost"] for r, i in zip (rezervacije, iznosi) if i >= 240]

print(ukupno, sum(iznosi))   # 805 805
print(skupa_nocenja)         # ['Ana', 'Marko', 'Ivana']
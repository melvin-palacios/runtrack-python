def e_finder():
    mot = input("entrez un mot ")
    special_characters = lettre
    if any(c in special_characters for c in mot):
        print("il y a la lettre", lettre)
    else:
        print("il n'y a pas la lettre", lettre)


lettre = input("choissisez la lettre ")
e_finder()
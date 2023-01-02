def e_finder() :
    mot = input("entrez un mot ")
    special_characters = "e"
    if any(c in special_characters for c in mot):
        print("il y a la lettre e")
    else:
        print("il n'y a pas la lettre e")
        e_finder()

e_finder()
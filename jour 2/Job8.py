def fonction(type, saison):
    if type == "fruits":
        if saison == "hiver":
            print("orange, mandarine et kiwi")
        elif saison == "ete":
            print("poire, fraise, cassis")
    elif type == "legume":
        if saison == "hiver":
            print("carotte, topinambour, endive")
        elif saison == "ete":
            print("artichaud, aubergine, navet")
    else:
        print("erreur")

fonction("fruits", "hiver")
fonction("fruits", "ete")
fonction("legume", "hiver")
fonction("legume", "ete")
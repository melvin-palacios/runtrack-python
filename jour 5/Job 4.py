def chiffrement(mot):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    trad = ""
    for i in mot:
        for j, a in enumerate(alpha):
            if i == a:
                trad += alpha[(j + 3) % 26]

        print(f"{i}", end="")
    print(f"    transformation ======>     {trad}")


chiffrement("bonjour")
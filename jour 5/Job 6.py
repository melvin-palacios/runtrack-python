def resultat(notes):
    results = []
    for note in notes:
        resultat = note
        for i in range(note, (note + 4)):
            if i % 5 == 0:
                resultat = i
        if resultat >= 40:
            results.append(f"felicitation {resultat}")
        elif resultat < 40:
            results.append(f"échec {resultat}")
    return results


print(resultat([87, 32, 65]))

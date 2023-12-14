def best_fit_translation(set1, set2, radius):
    # Calcul des moyennes theoriques et mesurees
    moyenne_positions_theorique = (sum(x for x, _ in set1) / len(set1), sum(y for _, y in set1) / len(set1))
    moyenne_positions_mesuree = (sum(x for x, _ in set2) / len(set2), sum(y for _, y in set2) / len(set2))

    # Calcul de la translation
    dx = moyenne_positions_mesuree[0] - moyenne_positions_theorique[0]
    dy = moyenne_positions_mesuree[1] - moyenne_positions_theorique[1]

    # Calcul de la distance totale d'erreur (optionnel)
    tupleSet=zip(set1, set2)                                                    # crée une paire de point en vue de l'iteration
    error = sum(
        ((x1 + dx - x2)**2 + (y1 + dy - y2)**2)**0.5                            #distance euclidienne
        for (x1, y1), (x2, y2) in tupleSet                                      #Iteration sur la paire de point
    )
    return dx, dy, error

# 0: dx = -8.821042783193036, dy = 10.9348002718707, error = 132.07265549803725
# 1: dx = -45.18462541475522, dy = 5.676944982870282, error = 76.81461551756885
# 2: dx = -39.25421866954025, dy = -17.12292926160717, error = 86.5880555773463
# 3: dx = -35.79687938273605, dy = -8.51657581973302, error = 177.13670245530716
# 4: dx = -35.97136902332346, dy = 8.330350250831202, error = 126.13936917058365
# 5: dx = -31.05455161750274, dy = -21.920560633293462, error = 240.91336477097133
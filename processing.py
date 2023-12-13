def best_fit_translation(set1, set2, radius):
    # Calcul des moyennes theoriques et mesurees
    moyenne_positions_theorique = (sum(x for x, _ in set1) / len(set1), sum(y for _, y in set1) / len(set1))
    moyenne_positions_mesuree = (sum(x for x, _ in set2) / len(set2), sum(y for _, y in set2) / len(set2))

    # Calcul de la translation
    dx = moyenne_positions_mesuree[0] - moyenne_positions_theorique[0]
    dy = moyenne_positions_mesuree[1] - moyenne_positions_theorique[1]

    # Calcul de la distance totale d'erreur (optionnel)
    error = sum(((x1 + dx - x2)**2 + (y1 + dy - y2)**2)**0.5 for (x1, y1), (x2, y2) in zip(set1, set2))

    return dx, dy, error
import numpy as np
from scipy.spatial.distance import cdist

def best_fit_translation(set1, set2, radius, learning_rate=0.01, iterations=1000):
    set1 = np.array(set1)
    set2 = np.array(set2)

    # Initialiser la translation à [0.0, 0.0]
    translation = np.array([0.0, 0.0])

    # Itérer pour effectuer la descente de gradient
    for _ in range(iterations):
        # Appliquer la translation aux points de set1
        translated = set1 + translation

        # Calculer les distances entre les points mesurés et les points de set2
        distances = cdist(translated, set2)

        # Trouver les indices des points les plus proches dans set2 pour chaque point mesuré
        nearest_indices = np.argmin(distances, axis=1) # point le plus proche dans set2 
        nearest_points = set2[nearest_indices]          

        # Calculer les gradients pour la descente de gradient
        gradients = translated - nearest_points

        # Mise à jour de la translation en utilisant le taux d'apprentissage
        translation -= learning_rate * np.mean(gradients, axis=0)

    # Calculer l'erreur finale
    final_translated = set1 + translation
    final_error = np.sum(np.linalg.norm(final_translated - set2[nearest_indices], axis=1))

    dx, dy = translation
    return dx, dy, final_error

# 0: dx = -5.294125781236383, dy = 17.259577931477455, error = 84.2787179306814
# 1: dx = -44.60873825880118, dy = 8.937428470352241, error = 131.0895595925738
# 2: dx = -34.874882789039724, dy = -25.159769904367376, error = 144.9465831354399
# 3: dx = -32.02567448697139, dy = -2.941254418455605, error = 82.14242214306465
# 4: dx = -32.43966632537116, dy = 14.663074192753554, error = 77.81893074395678
# 5: dx = -22.904588439715653, dy = -23.872861622587237, error = 76.70528558577386
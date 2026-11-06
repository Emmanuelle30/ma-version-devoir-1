import pandas as pd
import numpy as np


df = pd.read_csv("Base_Donnees_Finale.csv")

def var_es_empirique(r, alpha):
    """
    VaR et ES empiriques selon les définitions du cours.

    Paramètres
    ----------
    r : série de rendements
    alpha : niveau de risque (0.01 ou 0.05)

    Retour
    ------
    VaR, ES (positifs)
    """
    q_alpha = np.quantile(r, alpha)

    var = -q_alpha

    es = -np.mean(r[r <= q_alpha])

    return var, es

titres = ["CRSP", "APA", "ENB", "JBLU"]

resultats = []

for titre in titres:
    for alpha in [0.01, 0.05]:

        var, es = var_es_empirique(df[titre], alpha)

        resultats.append({
            "Titre": titre,
            "Alpha": alpha,
            "VaR": var,
            "ES": es,
            "VaR (%)": 100 * var,
            "ES (%)": 100 * es
        })

resultats = pd.DataFrame(resultats)

print(resultats.round(4))
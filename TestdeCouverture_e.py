import pandas as pd
import numpy as np
from scipy.stats import binom, norm


def test_couverture(r, var, p=0.05):

    r = np.asarray(r)
    var = np.asarray(var)

    # nombre de violations
    x = np.sum(r < var)

    n = len(r)

    # statistique s1
    s1 = (x - n*p) / np.sqrt(n*p*(1-p))

    # valeur-p exacte bilatérale
    proba_obs = binom.pmf(x, n, p)

    valeurs = np.arange(n + 1)

    p_value = np.sum(
        binom.pmf(valeurs, n, p)
        [binom.pmf(valeurs, n, p) <= proba_obs]
    )

    return {
        "n": n,
        "violations": x,
        "taux_observe": x / n,
        "s1": s1,
        "p_value": p_value
    }

base = pd.read_csv("Base_Donnees_Finale.csv")

Y = base["ENB"]

partie_b = pd.read_csv("VaR_ES_empiriques.csv")

VaR_emp = partie_b.loc[
    (partie_b["Titre"] == "ENB") &
    (partie_b["Alpha"] == 0.05),
    "VaR"
].iloc[0]


X = base["CRSP"]

beta, alpha = np.polyfit(X, Y, 1)

y_hat = alpha + beta * X

residus = Y - y_hat

sigma_mco = np.sqrt(
    np.var(residus, ddof=2)
)

z = norm.ppf(0.05)

VaR_mco = y_hat + z * sigma_mco


def test_couverture(r, var, p=0.05):

    x = np.sum(r < var)
    n = len(r)

    taux = x / n

    s1 = (
        x - n*p
    ) / np.sqrt(n*p*(1-p))


    p_inf = binom.cdf(x, n, p)

    p_sup = 1 - binom.cdf(x - 1, n, p)

    p_value = 2 * min(p_inf, p_sup)

    p_value = min(1, p_value)

    return pd.Series({
        "n": n,
        "Violations": x,
        "Taux observé": taux,
        "s1": s1,
        "Valeur-p": p_value
    })


resultat_emp = test_couverture(
    Y,
    np.repeat(VaR_emp, len(Y)),
    p=0.05
)


resultat_mco = test_couverture(
    Y,
    VaR_mco,
    p=0.05
)

print("\n===== VaR EMPIRIQUE =====")
print(resultat_emp)

print("\n===== VaR MCO-NORMALE =====")
print(resultat_mco)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def VaR_bootstrap(rendements, alpha, B=10000):

    rng = np.random.default_rng(12345)

    n = len(rendements)

    var_boot = np.zeros(B)

    for b in range(B):

        sample = rng.choice(
            rendements,
            size=n,
            replace=True
        )

        var_boot[b] = np.quantile(sample, alpha)

    return var_boot



df = pd.read_csv("Base_Donnees_Finale.csv")

APA = df["APA"].dropna().values


var_boot_01 = VaR_bootstrap(APA, 0.01)

var_boot_05 = VaR_bootstrap(APA, 0.05)

IC01_bas = np.percentile(var_boot_01, 2.5)
IC01_haut = np.percentile(var_boot_01, 97.5)

IC05_bas = np.percentile(var_boot_05, 2.5)
IC05_haut = np.percentile(var_boot_05, 97.5)

print("\n===== IC 95 % =====")
print(f"VaR 1 % : [{IC01_bas:.6f} ; {IC01_haut:.6f}]")
print(f"VaR 5 % : [{IC05_bas:.6f} ; {IC05_haut:.6f}]")

VaR01 = np.mean(var_boot_01)
VaR05 = np.mean(var_boot_05)

print("===== APA =====")
print(f"VaR 1% = {VaR01:.6f}")
print(f"VaR 5% = {VaR05:.6f}")

print(f"VaR 1% = {100*VaR01:.2f}%")
print(f"VaR 5% = {100*VaR05:.2f}%")



plt.figure(figsize=(10,6))

plt.hist(
    var_boot_05,
    bins=50,
    density=True,
    color="lightblue",
    edgecolor="black"
)

plt.axvline(
    VaR05,
    color="red",
    linewidth=3,
    label=f"VaR ponctuelle = {VaR05:.4f}"
)

plt.title("Distribution bootstrap de la VaR 5 % (APA)")
plt.xlabel("Estimations bootstrap de la VaR")
plt.ylabel("Densité")
plt.legend()
plt.grid(alpha=0.3)

plt.show()


ecart_type = np.std(var_boot_05, ddof=1)

IC_bas = np.percentile(var_boot_05, 2.5)
IC_haut = np.percentile(var_boot_05, 97.5)

print()
print("Incertitude de la VaR 5 %")
print(f"Écart-type : {ecart_type:.6f}")
print(f"IC 95 % : [{IC_bas:.6f} ; {IC_haut:.6f}]")
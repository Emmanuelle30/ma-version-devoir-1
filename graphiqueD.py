import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import norm

df = pd.read_csv("Base_Donnees_Finale.csv")

df["Date"] = pd.to_datetime(df["Date"])
df.set_index("Date", inplace=True)

Y = df["ENB"]
X = df["CRSP"]

beta, alpha = np.polyfit(X, Y, 1)

print("Alpha =", alpha)
print("Beta =", beta)

y_hat = alpha + beta * X

residus = Y - y_hat

sigma2_mco = np.var(residus, ddof=2)

print("Variance MCO =", sigma2_mco)

z = norm.ppf(0.05)

VaR_statique = y_hat + z * np.sqrt(sigma2_mco)

n = len(Y)

sigma2_t = np.zeros(n)

sigma2_t[0] = 0.5 * sigma2_mco

for t in range(1, n):

 sigma2_t[t] = (0.5 * sigma2_mco+ 0.5 * sigma2_t[t-1])
 

sigma_t = np.sqrt(sigma2_t)

VaR_dynamique = y_hat + z * sigma_t

plt.figure(figsize=(16,8))

plt.bar(
Y.index,
Y,
color="lightgray",
width=1,
alpha=0.7,
label="Rendements réels"
)

# VaR dynamique
plt.plot(
Y.index,
VaR_dynamique,
color="red",
linewidth=0.8,
label="VaR dynamique"
)

plt.plot(
Y.index,
VaR_statique,
color="blue",
linestyle="--",
linewidth=0.8,
label="VaR statique"
)

plt.title("Comparaison de la VaR statique et de la VaR dynamique")
plt.xlabel("Date")
plt.ylabel("Rendement")
plt.legend()
plt.grid(True, alpha=0.3)

plt.show()
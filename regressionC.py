import pandas as pd
import numpy as np

df = pd.read_csv("Base_Donnees_Finale.csv")

x = df["CRSP"].values
y = df["APA"].values


beta = np.cov(x, y, ddof=1)[0, 1] / np.var(x, ddof=1)
alpha = np.mean(y) - beta * np.mean(x)

# résidus
residus = y - (alpha + beta * x)

# écart-type résiduel
sigma = np.std(residus, ddof=2)

print("alpha =", alpha)
print("beta =", beta)
print("sigma =", sigma)
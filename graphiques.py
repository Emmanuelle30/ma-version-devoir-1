import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


base = pd.read_csv("Base_Donnees_Finale.csv")
base["Date"] = pd.to_datetime(base["Date"])

fig, ax = plt.subplots(figsize=(14,7))

ax.plot(base["Date"], abs(base["CRSP"]), label="CRSP")
ax.plot(base["Date"], abs(base["APA"]), label="APA")
ax.plot(base["Date"], abs(base["ENB"]), label="ENB")
ax.plot(base["Date"], abs(base["JBLU"]), label="JBLU")

ax.set_title(
    "Amplitude des rendements quotidiens et périodes de forte volatilité"
)

ax.set_xlabel("Date")
ax.set_ylabel("Valeur absolue du rendement")

ax.legend()
ax.grid(True)

plt.show()

import pandas as pd
import matplotlib.pyplot as plt


base = pd.read_csv("Base_Donnees_Finale.csv")
base["Date"] = pd.to_datetime(base["Date"])

# Création de 4 graphiques empilés
fig, axes = plt.subplots(
    4, 1,
    figsize=(14, 12),
    sharex=True
)


axes[0].plot(base["Date"], base["CRSP"], color="black")
axes[0].set_title(
    "Figure 1 - Rendement quotidien du marché CRSP pondéré par la valeur (avec dividendes)"
)
axes[0].set_ylabel("Rendement")
axes[0].grid(True, alpha=0.3)


axes[1].plot(base["Date"], base["APA"], color="blue")
axes[1].set_title(
    "Figure 2 - Rendement quotidien de APA Corporation"
)
axes[1].set_ylabel("Rendement")
axes[1].grid(True, alpha=0.3)


axes[2].plot(base["Date"], base["ENB"], color="green")
axes[2].set_title(
    "Figure 3 - Rendement quotidien d'Enbridge (ENB)"
)
axes[2].set_ylabel("Rendement")
axes[2].grid(True, alpha=0.3)


axes[3].plot(base["Date"], base["JBLU"], color="red")
axes[3].set_title(
    "Figure 4 - Rendement quotidien de JetBlue Airways (JBLU)"
)
axes[3].set_ylabel("Rendement")
axes[3].set_xlabel("Date")
axes[3].grid(True, alpha=0.3)


fig.suptitle(
    "Évolution des rendements quotidiens (2 décembre 2013 au 2 décembre 2022)",
    fontsize=16,
    fontweight="bold"
)

series = ["CRSP", "APA", "ENB", "JBLU"]

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.flatten()

for i, titre in enumerate(series):

    r = base[titre].dropna()

    mu = r.mean()
    sigma = r.std()

    # Histogramme
    axes[i].hist(
        r,
        bins=50,
        density=True,
        alpha=0.6,
        color="skyblue",
        edgecolor="black",
        label="Données observées"
    )

    # Courbe normale théorique
    x = np.linspace(r.min(), r.max(), 1000)
    y = norm.pdf(x, mu, sigma)

    axes[i].plot(
        x,
        y,
        color="red",
        linewidth=2,
        label="Loi normale"
    )

    axes[i].set_title(
        f"Distribution des rendements : {titre}"
    )

    axes[i].set_xlabel("Rendement")
    axes[i].set_ylabel("Densité")
    axes[i].grid(True, alpha=0.3)
    axes[i].legend()

plt.suptitle(
    "Histogrammes des rendements et comparaison avec la loi normale",
    fontsize=16,
    fontweight="bold"
)

plt.tight_layout()
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Base_Donnees_Finale.csv")
df["Date"] = pd.to_datetime(df["Date"])

actions = ["CRSP", "APA", "ENB", "JBLU"]

fig, axes = plt.subplots(2, 2, figsize=(14,8))

for ax, action in zip(axes.flatten(), actions):

    vol = df[action].rolling(30).std()

    ax.plot(df["Date"], vol, linewidth=1.2)
    ax.set_title(action)
    ax.grid(alpha=0.3)
    ax.set_ylabel("Volatilité")

plt.tight_layout()
plt.show()
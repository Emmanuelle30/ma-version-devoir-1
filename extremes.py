import pandas as pd

base = pd.read_csv("Base_Donnees_Finale.csv")

resultats = []

for titre in ["CRSP","APA", "ENB", "JBLU"]:

    # Plus forte baisse
    idx_min = base[titre].idxmin()

    resultats.append({
        "Titre": titre,
        "Type": "Plus forte baisse",
        "Date": base.loc[idx_min, "Date"],
        "Rendement": base.loc[idx_min, titre]
    })

    # Plus forte hausse
    idx_max = base[titre].idxmax()

    resultats.append({
        "Titre": titre,
        "Type": "Plus forte hausse",
        "Date": base.loc[idx_max, "Date"],
        "Rendement": base.loc[idx_max, titre]
    })

tableau_extremes = pd.DataFrame(resultats)

print(tableau_extremes)

tableau_extremes.to_csv(
    "Tableau_Extremes.csv",
    index=False
)
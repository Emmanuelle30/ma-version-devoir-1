import pandas as pd

base = pd.read_csv("Base_Donnees_Finale.csv")

stats = pd.DataFrame({
    "Moyenne": base[["CRSP","APA","ENB","JBLU"]].mean(),
    "Écart-type": base[["CRSP","APA","ENB","JBLU"]].std(),
    "Minimum": base[["CRSP","APA","ENB","JBLU"]].min(),
    "Maximum": base[["CRSP","APA","ENB","JBLU"]].max(),
    "Asymétrie": base[["CRSP","APA","ENB","JBLU"]].skew(),
    "Excès de kurtosis": base[["CRSP","APA","ENB","JBLU"]].kurt()
})

print(stats)
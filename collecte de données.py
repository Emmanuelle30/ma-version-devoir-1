import pandas as pd
import numpy as np


Market = pd.read_csv('Market.csv')
Stocks = pd.read_csv('APA-ENB-JBLU.csv')

Market["dlycaldt"] = pd.to_datetime(Market["dlycaldt"])
Stocks["DlyCalDt"] = pd.to_datetime(Stocks["DlyCalDt"])



Market = Market.rename(columns={
    "dlycaldt": "Date",
    "vwretd": "CRSP"
})



actions = Stocks.pivot_table(
    index="DlyCalDt",
    columns="Ticker",
    values="DlyRet",      
    aggfunc="first"
)

actions.reset_index(inplace=True)

actions.rename(
    columns={"DlyCalDt": "Date"},
    inplace=True
)



base_finale = pd.merge(
    Market,
    actions,
    how="inner",
    on="Date"
)

# 6. RECHERCHE DES ÉVÉNEMENTS > 10 %

for ticker in ["APA", "ENB", "JBLU"]:

    extreme = base_finale[
        base_finale[ticker].abs() > 0.10
    ]

    print(f"\n===== {ticker} =====")

    if extreme.empty:
        print("Aucun rendement > ±10 %")

    else:
        print(extreme[["Date", ticker]])


rendement_recherche = -0.178327

for ticker in [ "ENB"]:

    nb = np.isclose(
        base_finale[ticker],
        rendement_recherche,
        atol=1e-6
    ).sum()

    print(f"{ticker} : {nb} occurrence(s)")


base_finale.to_csv(
    "Base_Donnees_Finale.csv",
    index=False
)

print("\nBase_Donnees_Finale.csv créée.")
print(base_finale.head())
print(base_finale.shape)



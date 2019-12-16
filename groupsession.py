#%%
import pandas as pd

# %%
ufodf = pd.read_csv("ufoSightings.csv")



# %%
cleanufodf = ufodf.dropna(how = "any")
cleanufodf

# %%
castdurationpDF = cleanufodf.copy()
castdurationpDF["duration (seconds)"] = castdurationpDF.loc[:,"duration (seconds)"].astype(float)
castdurationpDF["duration (seconds)"].apply(type)



# %%
usaonly = castdurationpDF.loc[castdurationpDF["country"] == "us"]
usaonly

# %%
eachstate = usaonly.groupby(["state"])



# %%
groupbystatesum = usaonly.groupby(["duration (seconds)"]).sum()
groupbystatesum


# %%
groupbyaverage["average"] =  usaonly.groupby(["duration (seconds)"]).mean()


# %%
cityobj = usaonly.groupby(["city"])
citymean = cityobj["duration (seconds)"].mean()

# %%
locatesdf = usaonly.loc[cityobj["duration (seconds)"] > "1233"]]

# %%
pokemonDF = pd.read_csv("Pokemon.csv")

pokemonDF

# %%
groupbytype = pokemonDF.groupby(["Type 1"])
groupbytotalAvg = groupbytype["Total"].mean()
groupbytotalAvg.idxmax()



# %%
#best attack
groupbyattack = groupbytype["Defense"].mean()
groupbyattack.idxmax()


# %%
game = ["Attack", "Defense", "HP", "Sp. Atk","Sp. Def", "Speed", "Total" ]
bestPlayer = {}
for typeof in game:
    groupbyattack = groupbytype[typeof].mean()
    bestPlayer[typeof] = groupbyattack.idxmax()

print(bestPlayer)

# %%

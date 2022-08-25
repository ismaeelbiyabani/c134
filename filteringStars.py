import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('starWithGravity.csv')
print(df.head())
bools = []
for d in df.Distance:
    if d <= 100:
        bools.append(True)
    else:
        bools.append(False)
isDist = pd.Series(bools)
print(isDist.head())
starDist = df[isDist]
starDist.reset_index(inplace = True, drop = True)
print(starDist.head())
print(starDist.shape)
gravityBool = []
for g in starDist.Gravity:
    if g <= 350 and g >= 150:
        gravityBool.append(True)
    else:
        gravityBool.append(False)
isGravity = pd.Series(gravityBool)
finalStars = starDist[isGravity]
print(finalStars.head())
print(finalStars.shape)
finalStars.reset_index(inplace = True, drop = True)
print(finalStars.head())
finalStars.to_csv('filteredStars.csv')
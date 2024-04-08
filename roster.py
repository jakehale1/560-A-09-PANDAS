# https://goheels.com/sports/mens-basketball/roster
import pandas as pd

roster = {"RJ Davis", "Armando Bacot", "Seth Trimble"}

data = pd.DataFrame(roster, columns=["Player"])

print(data)



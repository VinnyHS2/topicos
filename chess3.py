import pandas as pd
from matplotlib import pyplot as plt

import os

if os.path.isfile("temp.txt"):
    os.remove("temp.txt")

columns = ["id", "turns", "victory_status", "winner", "white_rating", "black_rating", "moves", "opening_name", "opening_ply"]

jogos = pd.read_csv("gamesRated.csv", usecols=columns)

flag = 0

for index, row in jogos.iterrows():
    f = open("temp.txt", "w")
    f.write("[White Rating: " + str(row["white_rating"]) + "] \n")
    f.write("[Black Rating: " + str(row["black_rating"]) + "] \n")
    f.write("[Winner: " + str(row["winner"]) + "] \n")
    i = 0
    for s in row["moves"]:
        if s == ' ':
            flag = flag + 1
            if flag%2 == 1:
                row["moves"] = row["moves"][:i] + row["moves"][i+1:]
                i = i - 1
        i = i + 1 
    f.write("\n")
    f.write(row["moves"])
    f.write("\n")
    f.write("\n")
    flag = 0


    f.close()

os.system("python3 test.py")
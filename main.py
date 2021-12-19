import json
import pandas as pd
import re

with open("type_world.json", "r") as file:
    jsonified = file.read()
    datas = json.loads(jsonified)

with open("type_meta.json", "r") as file:
    jsonified = file.read()
    trait_data = json.loads(jsonified)
    traits = [x["nickname"] for x in trait_data]
    types = [x["type"][:4] for x in trait_data]

map_data = {}
for i in range(16):
    map_data.update({traits[i]: types[i]})

def mapper(string):
    others = string[10:]
    type = map_data[others]
    a_or_t = string[:9]
    if a_or_t == "Turbulent":
        type+="-T"
    if a_or_t == "Assertive":
        type+="-A"
    return type

countries = []
for country in datas:
    data = {}
    for i in range(32):
        name = country["names"][i]
        type_ = mapper(name)
        percentage = country["percentages"][i]
        data.update({type_: percentage})
    countries.append(data)

cols = list(countries[0].keys())
lists = {}
for col in cols:
    vals = []
    for country in countries:
        val = country[col]
        val = float(val[:-1])/100
        vals.append(val)
    lists.update({col: vals})

df = pd.DataFrame(lists, index = [x["country"] for x in datas])

df = df.rename_axis("Country")

df.to_csv("countries.csv")
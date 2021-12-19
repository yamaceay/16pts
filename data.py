import json
import pandas as pd

with open("type_meta.json", "r") as file:
    jsonified = file.read()
    type_data = json.loads(jsonified)

dataframe = []
for data in type_data:
    sections = data["sections"]
    series = {}
    for section in sections:
        series.update({section["name"]: section["content"]})
    dataframe.append(series)

lists = {}
cols = list(dataframe[0].keys())
for i in range(len(cols)):
    col = cols[i]
    vals = []
    for data in dataframe:
        val = data[col]
        vals.append(val)
    lists.update({col: vals})

df = pd.DataFrame(lists, index = [x["type"] for x in type_data])
df["Celebrities"] = [x["celebrities"] for x in type_data]
df["Description"] = [x["description"] for x in type_data]
df["Nickname"] = [x["nickname"] for x in type_data]
df["Definition"] = [x["definition"] for x in type_data]
indexes = []
for i in range(len(df.index)):
    index = df.index[i]
    index = index[:4]
    indexes.append(index)

df.index = indexes
df.to_csv("types.csv")
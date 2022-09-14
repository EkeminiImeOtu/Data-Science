import xml.etree.ElementTree as ET
import pandas as pd
cols = ["address", "description", "lat", "lng", "title"]
rows = []
tree=ET.parse("testing.xml")
root = tree.getroot()
for i in root:
    address = i.find("address").text
    description = i.find("description").text
    lat= i.find("lat").text
    lng = i.find("lng").text
    title = i.find("title").text

    rows.append({"address": address,
                 "description": description,
                 "lat": lat,
                 "lng": lng,
                 "title": title})

df = pd.DataFrame(rows, columns=cols)
print(df.head())
df.to_csv('ceramicpro.csv')
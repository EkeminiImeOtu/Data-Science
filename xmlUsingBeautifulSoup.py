import pandas as pd
from bs4 import BeautifulSoup as bs
content = []
cols=["url"]
rows=[]
# Read the XML file
with open("sitemap-profile-15.xml", "r", encoding='utf-8') as file:
    # Read each line in the file, readlines() returns a list of lines
    content = file.readlines()
    # Combine the lines in the list into a string
    content = "".join(content)
    bs_content = bs(content, "lxml")
    result = bs_content.find_all("loc")
    # print(result)
    for c in result:
        rows.append({"url": c})
        df = pd.DataFrame(rows, columns=cols)
        # print(df.head())
    # print(df.head())
    df.to_csv('sitemap15_15.csv',index=False)

    # # print(result)




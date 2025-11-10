import requests
import pandas as pd
import time

# initialization
url = "https://steamspy.com/api.php"
pages = 10

ID_list = []

for i in range(pages):
    # requesting
    params = {"request": "all", "page": str(i)}
    response = requests.get(url, params=params)

    # adding data to list
    ID_list = ID_list + list(response.json().keys())

    print(i+1, "/", pages) # tracking progress
    if i != pages-1:
        time.sleep(60)

# turning data into dataframe and saving
df = pd.DataFrame(ID_list)
df = df.rename(columns={0: "AppID"})
df.to_csv("../data/games_appid.csv")

import requests
import pandas as pd
import time

# initialization
url = "https://steamspy.com/api.php"
id_list = pd.read_csv("../data/games_appid.csv")
id_list = id_list["AppID"]

df = pd.DataFrame()
progress = 1

for i in id_list:
    try:
        # requesting data
        params = {"request": "appdetails", "appid": i}
        response = requests.get(url, params=params)

        # parsing
        game_data = response.json()
        tags = game_data.pop("tags")
        game_data = {**game_data, **tags}

        # adding info to data frame
        df = pd.concat([df, pd.DataFrame([game_data])])

    except Exception as e:
        print(f"Error at step {progress}, game AppID {i}: {e}")

    # tracking progress
    if progress % 100 == 0:
        print(progress, "/", len(id_list))

        # backup save
        if progress % 500 == 0:
            df.to_csv("../data/raw_game_data.csv")
            print("Data saved")

    progress += 1
    time.sleep(1)

df.to_csv("../data/raw_game_data.csv")

# Steam data gathering and analysis
Project gathers data about games from steam using SteamSpy API
Data has been cleaned and analysed in jupyter notebook.

## Goal 
The main focus of a project is to find correlation between genres, price, public opinion and 
in game online. Secondly we will analyse the changes in popularity of genres and games.

## Conclusion
* Online first-person shooters account for the highest number of downloads.
* A big percentage of games had no players in the last 2 weeks(26% in our sample).
* It is more optimal to have a stable casual audience, rather than having 
small group of dedicated players that play for a longer time through day.
* The most profitable tags are "Open World & RPG", "Action & Open World", and "Action & FPS"
* Free-to-play genre dominates in engagement.

## Project structure 
```
steam-data-gathering-and-analysis/
│
├── data/               # Folder for datasets
│   ├── processed_game_data.csv     # Clean game data ready for analysis
│   ├── games_appid.csv             # Contains list of AppIDs
│   └── raw_game_data.csv           # Contains detailed game data
│
├── src/                   # Source code
│   ├── data_preprocessing.py  # Script for cleaning and changing data
│   ├── game_id_scraper.py     # Script for collecting game IDs
│   └── game_data_scraper.py   # Script for collecting detailed game data 
│                              # with IDs from games_appid.csv
│
└── README.md 
```

## Usage 
```
# collecting games ID
python src/game_id_scraper.py   

# collecting games data
python src/game_data_scraper.py  

# cleaning data
python src/data_preprocessing.py
```

## Requirements 
Listed in requirements.txt  
Install them with:
```
pip install -r requirements.txt
```

## Contact
email: mkapravyj@gmail.com
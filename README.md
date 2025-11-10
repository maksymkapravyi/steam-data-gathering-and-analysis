# Steam data gathering and analysis
The goal of a project is to gather data about games on steam using SteamSpy API
for later analysis in jupyter notebook

## Goal 
The main focus of a project is to find correlation between genres, price, public opinion and 
in game online. Changes in game and genres trends will also be analysed

## Project structure 
```
steam-data-gathering-and-analysis/
│
├── data/               # Folder for datasets
│   ├── games_appid.csv    # Contains list of AppIDs
│   └── raw_game_data.csv  # Contains detailed game data
│
├── src/                   # Source code
│   ├── game_id_scraper.py     # Script for collecting game IDs
│   └── game_data_scraper.py   # Script for collecting detailed game data 
│                              # with IDs from games_appid.csv
│
├── venv/                  # Virtual environment (excluded)
└── README.md 
```

## Usage 
```
# collecting games ID
python src/game_id_scraper.py   

# collecting games data
python src/game_data_scraper.py  
```

## Requirements 
requests  
pandas  
time

## Notes
At the moment project consists only of scripts gathering data. 
Later data cleaning, engineering and analysis is going to be added.  
game_id_scraper.py has one-minute pauses between requests and
game_data_scraper.py has one-second pauses because of SteamSpy limitations

## Contact
email: mkapravyj@gmail.com
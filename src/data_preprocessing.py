import pandas as pd
import numpy as np

def get_second_largest_col(row):
    sorted_cols = row.sort_values(ascending=False).index
    return sorted_cols[1]

def main():
    df = pd.read_csv("../data/raw_game_data.csv")
    df = df.drop(columns=['Unnamed: 0'])

    game_info = df.iloc[:, :19]
    game_tags = df.iloc[:, 19:]

    game_info = game_info.drop(columns=['score_rank'])

    # Languages
    game_info.drop([3981], inplace=True)
    game_tags.drop([3981], inplace=True)
    game_info.loc[2565, 'languages'] = 'English, French, German'

    # Developer and publisher
    game_info.loc[game_info.developer.isna(), "developer"] = game_info.loc[game_info.developer.isna(), "publisher"]
    game_info.loc[game_info.publisher.isna(), "publisher"] = game_info.loc[game_info.publisher.isna(), "developer"]

    # Genres encoding
    game_info.genre = game_info.genre.fillna("")
    genres_encoded = pd.DataFrame()

    for i, value in game_info.genre.items():
        genres = value.split(", ")
        for g in genres:
            if g not in genres_encoded:
                genres_encoded[g] = 0
        genres_encoded.loc[i, genres] = 1

    genres_encoded = genres_encoded.fillna(0)

    # Languages encoding
    languages_encoded = pd.DataFrame()

    for i, value in game_info.languages.items():
        for noise in ["\r", "\n", "[b]", "*", "[/b]", ";"]:
            value = value.replace(noise, "")  # there are values that look like "Italian \r\n\r\n[b]*[/b]"
        value = value.strip()
        value = value.replace(" ,", ",")
        languages = list(set(value.split(", ")))

        for l in languages:
            if l not in languages_encoded:
                languages_encoded[l] = 0

        languages_encoded.loc[i, languages] = 1

    languages_encoded = languages_encoded.fillna(0)

    # Tags extracting
    game_tags = game_tags.fillna(0)
    tags_extracted = pd.DataFrame(game_tags.idxmax(axis="columns"))
    tags_extracted = tags_extracted.rename(columns={0: "first tag"})
    tags_extracted['second tag'] = game_tags.apply(get_second_largest_col, axis=1)

    # Creating feautes
    game_info['review_ratio '] = game_info['positive'] / game_info['positive'] + game_info['negative'] + 1
    game_info['popularity_change'] = game_info['average_2weeks'] - game_info['average_forever']
    game_info['price_change'] = game_info['initialprice'] - game_info['price']
    game_info['engagement_spread'] = game_info['average_forever'] / game_info['median_forever'] + 1
    game_info['language_count'] = languages_encoded.T.sum()

    game_info = game_info.drop(columns=['userscore', 'languages', 'genre', 'discount', 'median_2weeks'])

    #saving
    df = pd.concat([game_info, tags_extracted, languages_encoded, genres_encoded], axis=1)
    df.to_csv("../data/processed_game_data.csv")


if __name__ == "__main__":
    main()
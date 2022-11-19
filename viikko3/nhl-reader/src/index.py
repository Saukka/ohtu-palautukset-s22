import requests
from player import Player
from datetime import datetime
from player_stats import PlayerStats
from player_reader import PlayerReader

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    nationality = 'FIN'
    players = stats.top_scorers_by_nationality(nationality)

    print("Players from " + nationality + " " + str(datetime.now()))
    print('')

    for player in players:
        print(player)

if __name__ == "__main__":
    main()

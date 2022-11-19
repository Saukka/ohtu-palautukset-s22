import requests
from player import Player
from datetime import datetime

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'],
            player_dict['nationality'],
            player_dict['assists'],
            player_dict['goals'],
            player_dict['penalties'],
            player_dict['team'],
            player_dict['games'],
        )

        players.append(player)

    print("Players from FIN", datetime.now())
    print("")

    players.sort(key=get_stats, reverse = True)

    for player in players:
        if player.nationality == 'FIN':
            print(player)


def get_stats(player):
    return player.goals + player.assists


if __name__ == "__main__":
    main()
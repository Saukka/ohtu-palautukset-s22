from player_reader import PlayerReader
from player import Player

class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()
    
    def top_scorers_by_nationality(self, nationality):
        players = []
        
        for player in self.players:
            if (player.nationality == nationality):
                players.append(player)
        
        players.sort(key=get_stats, reverse = True)
        return players


def get_stats(self):
    return self.goals + self.assists
class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        if self.m_score1 == self.m_score2:
            if self.m_score1 > 3:
                return "Deuce"
            return self.get_name(self.m_score1) + "-All"

        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            return self.score_over_three()

        else:
            return self.get_name(self.m_score1) + "-" + self.get_name(self.m_score2)

    def score_over_three(self):
        minus_result = self.m_score1 - self. m_score2
        winning_player = "player1"
        if (minus_result < 0):
            winning_player = "player2"
            
        if (abs(minus_result) < 2):
            return "Advantage " + winning_player
        return "Win for " + winning_player

    def get_name(self, score):
        match score:
            case 0:
                return "Love"
            case 1:
                return "Fifteen"
            case 2:
                return "Thirty"
            case 3: 
                return "Forty"

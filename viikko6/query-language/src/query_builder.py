from matchers import *

class QueryBuilder():
    def __init__(self, matcher = All()):
        self.matcher = matcher

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self.matcher, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self.matcher, HasFewerThan(value, attr)))

    def playsIn(self, team):
        return QueryBuilder(And(self.matcher, PlaysIn(team)))

    def build(self):
        return self.matcher




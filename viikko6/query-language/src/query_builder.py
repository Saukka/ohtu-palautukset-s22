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

    def oneOf(self, m1, m2):
        return QueryBuilder(And(self.matcher, Or(m1, m2)))



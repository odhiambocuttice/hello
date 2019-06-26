class Team:

    goals = 2
    teammates = 0
    # method

    def __init__(self, firstname, position):
        self.firstname = firstname
        self.position = position

    def detials(self):
        return '{} {}'.format(self.firstname, self.position)

    @classmethod
    def goals_scored(cls, number):
        cls.goals = number

    # @staticmethod
    # def workday(day):
    #     if day.weekday() == 5 or day.weekday == 6:
    #         return False
    #     return True


class Club(Team):
    pass


# instances
player_1 = Team('oketch', 'goalkeeper')
player_3 = Team('shakes', 'striker')


club_player = Club('shakes', 'striker')

# instance variables
player_1.firstname = "oketch"
player_1.position = "goalkeeper"
Team.goals_scored = 5

player_1.goals = 3

print(player_1.position)

print(Team.goals_scored)

# class inheritance
print(club_player.position)
print(club_player.firstname)

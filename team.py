__author__ = 'Administrator'

class Team:
    """Represents a team in a fantasy league

    attributes: id, name, abbreviation, division, owners
    """

    def __init__(self, team_id):
        self.id = team_id
        self.owners = set()
        self.abbreviation = None
        self.division = None

    def add_owner(self, owner):
        self.owners.add(owner)
        if self is not owner.team:
            owner.team = self
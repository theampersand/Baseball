__author__ = 'Administrator'

class Owner:
    """Represents an owner of a team in a fantasy league

    attributes: id, name, team
    """

    def __init__(self, owner_id):
        self.id = owner_id
        self.name = None
        self.team = None

    def set_team(self, team):
        self.team = team
        if self not in team.owners:
            team.add_owner(self)
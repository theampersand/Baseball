__author__ = 'Administrator'

import requests
from lxml.html import document_fromstring, parse

owner_info_url = 'http://games.espn.go.com/flb/leaguesetup/ownerinfo?leagueId=54692'
cookies = dict([('SWID', '{9B885E8D-3D84-49B9-885E-8D3D8429B989}'), ('broadbandAccess', 'espn3-false%2Cnetworks-false'),
                ('DE2',
                 'dXNhO2luO2luZGlhbmFwb2xpczticm9hZGJhbmQ7NTs0OzQ7NTI3OzAzOS43ODM7LTA4Ni4wNDU7ODQwOzE1OzE0MDs2O3VzOw=='),
                ('id', 'c5a7bdc4e0000e2||t=1366235691|et=730|cs=002213fd48655c040886872e2b'),
                ('DS', 'Pzs7MDs7YXR0IHNlcnZpY2VzIGluYy47A'), ('BLUE',
                                                              'G9watzgXQpofPLGwUNyH19T5bGATMQzup902DtWcPI#2YNiib#8DC6m#lJ0OwNHfSs#ECuaWnFJKDqnvKVNAyMGKQ5OdTvlsSWVgf7nc0233rLW313dPnPRMK6m44tQkFXHJ7dXbMc$yA#UXsKfH3PhkZ0OK$aq9Zv5OsZvhU8CqBFtC#PYGlZlflTNiv0PXGW0va9sUIC#ttrxbxf4W5EgL9x$X6DZIwo1bd4S2QnzkAUx31P0#XxMoN0p#Xw6ELtSq$RjeJZyDy3DYtNv2Jg'),
                ('CRBLM', 'CBLM-001:'), ('RED',
                                         'AAAAAAAAEVavAAJUNm7xWUMuGBoIYTlQTu5LSgGU6dVhA/uprOS0lcbTMDqqyJlZJNDO4Q2mY3UKCzxvUlDSH5AXxOnY9uvBuM6TRwPVO5bXplikzVT3K4KCSidqyfKq4Pt2GwxZhoS6l04egIx47ATRxYEgiuvWRvRSdyR//0Vx0TZwcMUnxMbDieRmXljZlKEVaqRlrAhOSIi5Tg6D5hfiJTmxho4WEmndbvQISFGBiFXILS18QENuMmhxdg=='),
                ('userAB', '9'), ('CRBLM_LAST_UPDATE', '1366235692:{9B885E8D-3D84-49B9-885E-8D3D8429B989}')])


class OwnerPageProcessor:
    def process_owners_page(self):
        #owner_info_response = requests.get(owner_info_url, cookies=cookies)
        #self.owners_page = document_fromstring(owner_info_response.text)
        self.owners_page = parse('ownerinfo.html').getroot()

    def get_owners_rows(self, x):
        return x.get('style') is None


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


if __name__ == '__main__':
    processor = OwnerPageProcessor()
    processor.process_owners_page()
    owners = set()
    owner_rows = filter(processor.get_owners_rows, processor.owners_page.find_class('ownerRow'))
    for row in owner_rows:
        owner = Owner(row.get('id'))
        owner.name = row.get_element_by_id('ownerspan' + owner.id).text_content()
        owners.add(owner)
        #for owner in owners: print 'Owner name is ' + owner.name + " and owner id is " + owner.id
    team_ids = set()
    for row in owner_rows:
        team_ids.add(row.get('id')[:-2])
    teams = set()
    for id in team_ids:
        team = Team(id)
        this_team_element = processor.owners_page.get_element_by_id(id + "-0")
        team.abbreviation = this_team_element[1].text_content()
        team.name = this_team_element[2].text_content()
        team.division = this_team_element[3].text_content()
        teams.add(team)
    for t in teams:
        print 'team id is ' + t.id + ' and name is ' + t.name + ' and abbr is ' + t.abbreviation + ' and division is ' + t.division
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


class OwnerPageScraper:
    """Processes ElementTree of the owner info page on an ESPN fantasy baseball league
    can create sets of Owners and Teams and correlate them

    attributes: owners, teams
    """

    def __init__(self, owners_page_root):
        self.owners_page_root = owners_page_root
        self.owners = set()
        self.teams = set()
        self.owner_rows = filter(self.get_owners_rows, self.owners_page_root.find_class('ownerRow'))

    def get_owners_rows(self, x):
        return x.get('style') is None

    def scrape_owners_page(self):
        self.build_owners()
        self.build_teams()
        self.correlate_teams_and_owners()

    def build_owners(self):
        for row in self.owner_rows:
            owner = Owner(row.get('id'))
            owner.name = row.get_element_by_id('ownerspan' + owner.id).text_content()
            self.owners.add(owner)

    def build_teams(self):
        team_ids = set()
        for row in self.owner_rows:
            team_ids.add(row.get('id')[:-2])
        for id in team_ids:
            team = Team(id)
            this_team_element = self.owners_page_root.get_element_by_id(id + "-0")
            team.abbreviation = this_team_element[1].text_content()
            team.name = this_team_element[2].text_content()
            team.division = this_team_element[3].text_content()
            self.teams.add(team)
    def correlate_teams_and_owners(self):
        for team in self.teams:
            for owner in self.owners:
                if team.id == owner.id[:-2]:
                    team.add_owner(owner)


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
    owner_info_response = requests.get(owner_info_url, cookies=cookies)
    owners_page_root = document_fromstring(owner_info_response.text)
    #owners_page_root = parse('ownerinfo.html').getroot()
    scraper = OwnerPageScraper(owners_page_root)
    scraper.scrape_owners_page()
    #for owner in scraper.owners: print 'Owner name is ' + owner.name + " and owner id is " + owner.id
    for o in scraper.owners:
        print 'owner is ' + o.name + ' and team is ' + o.team.name
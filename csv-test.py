__author__ = 'Andrew Vincent Phillips'

import csv
import pprint

class Players:
    def __init__(self,input_file='zips-2013-data.csv' ):
        """Return a list ('player') of dict objects, taken from a Group Directory CSV file."""
        gd_extract = csv.DictReader(open(input_file))
        self.players = {row['playerid']:row for row in gd_extract}
    def print_players_names(self):
        for player in self.players.values():
            print(player['Name'])

if __name__ == '__main__':
    players = Players()
    #pprint.pprint(players.players)
    players.print_players()





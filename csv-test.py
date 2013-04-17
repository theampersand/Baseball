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
    def print_player_stats(self, player_name):
        for player in self.players.values():
            if player_name == player['Name']:
                selected_player = Player(player)
                selected_player.print_stat("Name")
                selected_player.print_stat("G")
                selected_player.print_stat("PA")
                selected_player.print_stat("AB")
                selected_player.print_stat("H")
                selected_player.print_stat("2B")
                selected_player.print_stat("3B")
                selected_player.print_stat("HR")
                selected_player.print_stat("R")
                selected_player.print_stat("RBI")
                selected_player.print_stat("BB")
                selected_player.print_stat("SO")
                selected_player.print_stat("HBP")
                selected_player.print_stat("SB")
                selected_player.print_stat("CS")
                selected_player.print_stat("AVG")
                selected_player.print_stat("OBP")
                selected_player.print_stat("SLG")
                selected_player.print_stat("OPS")
                selected_player.print_stat("wOBA")
                selected_player.print_stat("Fld")
                selected_player.print_stat("BsR")
                selected_player.print_stat("WAR")
    def print_top_player(self, stat):
        top_stat = 0
        top_player_id = 0
        for player in self.players.values():
            if float(player[stat]) > top_stat:
                top_stat = float(player[stat])
                top_player_id = player['playerid']
        top_player = self.players[top_player_id]
        print(top_player['Name'])

class Player:
    def __init__(self,stats):
        self.stats = stats
    def print_stat(self, stat_for_printing):
        print(stat_for_printing + ": " + '{:<25}'.format(self.stats[stat_for_printing]))

if __name__ == '__main__':
    players = Players()
    #pprint.pprint(players.players)
    #players.print_players_names()
    players.print_player_stats("Seth Smith")
    #players.print_top_player('HR')
    #players.print_top_player('OBP')
    #players.print_top_player('AVG')





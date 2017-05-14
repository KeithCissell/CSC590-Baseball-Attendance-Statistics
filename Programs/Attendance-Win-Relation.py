
# coding: utf-8

# In[1]:

import csv
import numpy
import matplotlib.pyplot as plt
from scipy.stats.stats import pearsonr
get_ipython().magic('matplotlib inline')


# In[2]:

# File names
teams_file = "Data//Teams.csv"

path = "Data//Retrosheet//GL"
startyr = 1970
endyr = 2016


# In[3]:

# Indicies
# game logs
teamx, vscorex, hscorex, parkx, attx  = 6, 9, 10, 16, 17

# teams_file
yrx, teamidx, gx, home_gx, wx, lx = 0, 2, 6, 7, 8, 9
team_namex, avg_attx = 40, 42


# In[4]:

def readcsv(fname):
    f = open(fname, 'r')
    reader = csv.reader(f)
    lines = list(reader)
    f.close()
    return lines


# In[5]:

class Team:
    def __init__(self, team, teamid, yr):
        self.team = team
        self.teamid = teamid
        self.year = yr
        self.avg_att = 0
        self.att_std = 0
        self.games = []
    def addGame(self, line):
        self.games.append(line)
    def calcStandardDeviation(self):
        game_att = []
        for g in range(0, len(self.games)):
            game = self.games[g]
            att = int(game[attx])
            game_att.append(att)
        std = numpy.std(game_att)
        self.att_std = std
    def setAvgAtt(self):
        num_games = len(self.games)
        total_att = 0
        for i in range(0, num_games):
            total_att += int(self.games[i][attx])
        self.avg_att = total_att / num_games
    def getAttDeviation(self, game):
        deviation = int(game[attx]) - self.avg_att
        return deviation
    def win(self, game):
        if game[hscorex] > game[vscorex]:
            return True
        else:
            return False


# In[6]:

def build_teamid_ref(lines):
    d = {}
    sortedLines = sorted(lines, key=lambda y: y[yrx], reverse=True)
    for line in sortedLines:
        teamid = line[teamidx]
        if teamid not in d:
            d[teamid] = line[team_namex]
    return d


# In[7]:

# builds a dictionary -> {year: {team_name: Team, ...}, ...}
def build_years_dict():
    # create the teamid dictionary for refference
    team_lines = readcsv(teams_file)
    team_ref = build_teamid_ref(team_lines[1:])
    
    years = {}
    for yr in range(startyr, (endyr + 1)):
        # add year to dict and initialize a dict for teams
        years[yr] = {}
        # gather game data for year
        yr_file = path + str(yr) + ".csv"
        games = readcsv(yr_file)
        for game in games:
            # validate data
            if game[attx] and int(game[attx]) > 0:
                # check if team is in team dict or not
                teamid = game[teamx]
                team_name = team_ref[teamid]
                if team_name not in years[yr]:
                    years[yr][team_name] = Team(team_name, teamid, yr)
                # add game data to proper team
                years[yr][team_name].addGame(game)
                    
    # calculate standard deviations of attendance
    for yr in years:
        for team in years[yr]:
            team = years[yr][team]
            team.calcStandardDeviation()
            team.setAvgAtt()
    
    return years


# In[17]:

# Analyzes game data to see if high attendance number translate to higher team performance
def supported_percentage(years):
    supported = 0
    games_analyzed = 0
    for y in years:
        year = years[y]
        for t in year:
            team = year[t]
            for g in range(0, len(team.games)):
                game = team.games[g]
                att_dev = team.getAttDeviation(game)
                # check if high/low attendance translates to win/loss
                if abs(att_dev) > team.att_std:
                    games_analyzed += 1
                    if att_dev > 0 and team.win(game):
                        supported += 1
                    elif att_dev < 0 and not team.win(game):
                        supported += 1
    # return the percentage of games that supports: high attendance -> high team performance
    preNormalized = (supported / games_analyzed) * 100
    pctSupported = (preNormalized - 50) * 2
    return round(pctSupported, 2)


# In[18]:

years = build_years_dict()


# In[19]:

sp = supported_percentage(years)
print("The relation of high/low attendance to win/loss of game is", sp, "% supported.")


# In[ ]:




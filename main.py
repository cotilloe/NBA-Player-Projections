#!/usr/bin/python3
from basketball_reference_web_scraper import client
from basketball_reference_web_scraper import data




'''
box_scores = client.player_box_scores(day=aDayAgo, month=cMonth, year=cYear)
print('***** BOX SCORES *****')
for box_score in box_scores[:10]:
  print(box_score)
'''
print('***** GAMES *****')
games = client.season_schedule(season_end_year=2020)
for game in games[:10]:
    print(game)

    
print("xxxxxxxxxxxxxxxxxxxxxxxx")
print("  ")
print("  ")
'''
print('***** ADVANCED SEASON TOTALS *****')
season_totals = client.players_advanced_season_totals(season_end_year=2019)
for total in season_totals[:10]:
  print(total)

print("  ")
print("  ")
print("xxxxxxxxxxxxxxxxxxxxxxxx")
print("xxxxxxxxxxxxxxxxxxxxxxxx")
print("  ")
print("  ")

print('***** SEASON TOTALS *****')
season_totals = client.players_season_totals(season_end_year=2019)
for total in season_totals[:10]:
  print(total)

print('***** TEAM BOX SCORES *****')
team_box_scores = client.team_box_scores(day=cDay, month=cMonth, year=cYear)
for total in team_box_scores[:10]:
  print(total)
'''

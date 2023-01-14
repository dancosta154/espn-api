def get_high_score():
    home_high_score = 0
    away_high_score = 0
    high_score = []
    
    for week in range(1,16):
        home_high_score = 0
        away_high_score = 0
        for i in range(5):
            if league.box_scores(week)[i].home_score > home_high_score:
                home_high_score = league.box_scores(week)[i].home_score
                home_team = str(league.box_scores(week)[i].home_team).strip('Team()')
            if league.box_scores(week)[i].away_score > away_high_score:
                away_high_score = league.box_scores(week)[i].away_score
                away_team = str(league.box_scores(week)[i].away_team).strip('Team()')
        high_score.append(f'Week {week}: {max((home_high_score, home_team), (away_high_score, away_team))}')

    return high_score

get_high_score()
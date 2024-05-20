from pymongo import MongoClient

username = "MD"
password = "datamining2024"

uri = f"mongodb+srv://{username}:{password}@datamining.ywf7foj.mongodb.net/?retryWrites=true&w=majority&appName=DataMining"

try:
    client = MongoClient(uri)
    print("Successfully connected to mongodb!")
except Exception as e:
    print(f"Couldn't connect to mongodb database: {e}")

db = client['sportmonks']
teams_collection = db['teams']

teams_information = dict()


def handle_team_lost(name, values):
    statistic_sentences = []

    all = values.get('all', [])
    home = values.get('home', [])
    away = values.get('away', [])

    if all != []:
        sentence = f"For a combined number of {all.get('count')} games, home and away, {name} has managed to lose {all.get('percentage')}% of them."
        statistic_sentences.append(sentence)

    if home != []:
        sentence = f"In {home.get('count')} home games, {name} has scored a lost in {home.get('percentage')}% of them."
        statistic_sentences.append(sentence)

    if away != []:
        sentence = f"In {away.get('count')} away games, {name} has scored a lost in {away.get('percentage')}% of them."
        statistic_sentences.append(sentence)

    return statistic_sentences


def handle_corners(name, values):
    statistic_sentences = []

    sentence = f"For a sample size of {values.get('count')} games, {name} was awarded, on average, {values.get('average')} corners per game."
    statistic_sentences.append(sentence)

    return statistic_sentences


def handle_goals_conceded(name, values):
    statistic_sentences = []

    all = values.get('all', [])
    home = values.get('home', [])
    away = values.get('away', [])

    if all != []:
        if all.get('first') != None:
            sentence = f"For a combined number of {all.get('count')} games, home and away, {name} has conceded an average of {all.get('average')} goals, in which the first tends to happend around the {all.get('first')} minute mark."
            statistic_sentences.append(sentence)
        else:
            sentence = f"For a combined number of {all.get('count')} games, home and away, {name} has conceded an average of {all.get('average')} goals."
            statistic_sentences.append(sentence)

    if home != []:
        if home.get('first') != None:
            sentence = f"In {home.get('count')} home games, {name} has conceded an average of {home.get('average')} goals, in which the first tends to occurr around the {home.get('first')} minute mark. This values equate to the fact that roughly {home.get('percentage')}% of {name}'s total number of conceded goals take place in home games."
            statistic_sentences.append(sentence)
        else:
            sentence = f"In {home.get('count')} home games, {name} has conceded an average of {home.get('average')} goals. This values equate to the fact that roughly {home.get('percentage')}% of {name}'s total number of conceded goals take place in home games."
            statistic_sentences.append(sentence)

    if away != []:
        if away.get('first') != None:
            sentence = f"In {away.get('count')} away games, {name} has conceded an average of {away.get('average')} goals, in which the first tends to occurr around the {away.get('first')} minute mark. This values equate to the fact that roughly {away.get('percentage')}% of {name}'s total number of conceded goals take place in away games."
            statistic_sentences.append(sentence)
        else:
            sentence = f"In {away.get('count')} away games, {name} has conceded an average of {away.get('average')} goals. This values equate to the fact that roughly {away.get('percentage')}% of {name}'s total number of conceded goals take place in away games."
            statistic_sentences.append(sentence)

    return statistic_sentences


def handle_dangerous_attacks(name, values):
    statistic_sentences = []

    sentence = f"In {name}'s {values.get('count')} attacks, {values.get('average')}% of them where considered to be dangerous attacks."
    statistic_sentences.append(sentence)

    return statistic_sentences


def handle_penalty_conversion_rate(name, values):
    statistic_sentences = []

    sentence = f"{name} has a penalty conversion rate of {values.get('conversion_rate_pct')}."
    statistic_sentences.append(sentence)

    return statistic_sentences


def handle_average_points_per_game(name, values):
    statistic_sentences = []

    sentence = f"{name} has managed to score an average of {values.get('average_points_per_game')} points per game."
    statistic_sentences.append(sentence)

    return statistic_sentences


def handle_team_wins(name, values):
    statistic_sentences = []

    all = values.get('all', [])
    home = values.get('home', [])
    away = values.get('away', [])

    if all != []:
        sentence = f"For a combined number of {all.get('count')} games, home and away, {name} has managed to win {all.get('percentage')}% of them."
        statistic_sentences.append(sentence)

    if home != []:
        sentence = f"In {home.get('count')} home games, {name} has scored a win in {home.get('percentage')}% of them."
        statistic_sentences.append(sentence)

    if away != []:
        sentence = f"In {away.get('count')} away games, {name} has scored a win in {away.get('percentage')}% of them."
        statistic_sentences.append(sentence)

    return statistic_sentences


def handle_shot_on_target_percentage(name, values):
    statistic_sentences = []

    sentence = f"{values.get('pct_shots_on_target')}% of {name}'s total shots are on target."
    statistic_sentences.append(sentence)

    return statistic_sentences


def handle_scoring_minutes(name, values):
    statistic_sentences = []

    _0_15 = values.get('0-15')
    _15_30 = values.get('15-30')
    _30_45 = values.get('30-45')
    _45_60 = values.get('45-60')
    _60_75 = values.get('60-75')
    _75_90 = values.get('75-90')

    sentence = f"{name} has scored {_0_15.get('count')} goals between minutes 0 and 15 in all their games, which correlates to {_0_15.get('percentage')}% of their total number of goals."
    statistic_sentences.append(sentence)

    sentence = f"{name} has scored {_15_30.get('count')} goals between minutes 15 and 30 in all their games, which correlates to {_15_30.get('percentage')}% of their total number of goals."
    statistic_sentences.append(sentence)

    sentence = f"{name} has scored {_30_45.get('count')} goals between minutes 30 and 45 in all their games, which correlates to {_30_45.get('percentage')}% of their total number of goals."
    statistic_sentences.append(sentence)

    sentence = f"{name} has scored {_45_60.get('count')} goals between minutes 45 and 60 in all their games, which correlates to {_45_60.get('percentage')}% of their total number of goals."
    statistic_sentences.append(sentence)

    sentence = f"{name} has scored {_60_75.get('count')} goals between minutes 60 and 75 in all their games, which correlates to {_60_75.get('percentage')}% of their total number of goals."
    statistic_sentences.append(sentence)

    sentence = f"{name} has scored {_75_90.get('count')} goals between minutes 75 and 90 in all their games, which correlates to {_75_90.get('percentage')}% of their total number of goals."
    statistic_sentences.append(sentence)

    return statistic_sentences


def handle_penalties(name, values):
    statistic_sentences = []

    sentence = f"{name} has successfully converted {values.get('scored')} penalties, while missing {values.get('missed')}. This equates to a conversion rate of {values.get('conversion_rate')}."
    statistic_sentences.append(sentence)

    return statistic_sentences


def handle_conceded_scoring_minutes(name, values):
    statistic_sentences = []

    _0_15 = values.get('0-15')
    _15_30 = values.get('15-30')
    _30_45 = values.get('30-45')
    _45_60 = values.get('45-60')
    _60_75 = values.get('60-75')
    _75_90 = values.get('75-90')

    sentence = f"{name} has conceded {_0_15.get('count')} goals between minutes 0 and 15 in all their games, which correlates to {_0_15.get('percentage')}% of their total number of conceded goals."
    statistic_sentences.append(sentence)

    sentence = f"{name} has conceded {_15_30.get('count')} goals between minutes 15 and 30 in all their games, which correlates to {_15_30.get('percentage')}% of their total number of conceded goals."
    statistic_sentences.append(sentence)

    sentence = f"{name} has conceded {_30_45.get('count')} goals between minutes 30 and 45 in all their games, which correlates to {_30_45.get('percentage')}% of their total number of conceded goals."
    statistic_sentences.append(sentence)

    sentence = f"{name} has conceded {_45_60.get('count')} goals between minutes 45 and 60 in all their games, which correlates to {_45_60.get('percentage')}% of their total number of conceded goals."
    statistic_sentences.append(sentence)

    sentence = f"{name} has conceded {_60_75.get('count')} goals between minutes 60 and 75 in all their games, which correlates to {_60_75.get('percentage')}% of their total number of conceded goals."
    statistic_sentences.append(sentence)

    sentence = f"{name} has conceded {_75_90.get('count')} goals between minutes 75 and 90 in all their games, which correlates to {_75_90.get('percentage')}% of their total number of conceded goals."
    statistic_sentences.append(sentence)

    return statistic_sentences


def handle_highest_rated_player(name, values):
    statistic_sentences = []

    player_name = values.get('player_name')
    rating = values.get('rating')

    sentence = f"{name} highest rated player, with a score of {rating}, is {player_name}."
    statistic_sentences.append(sentence)

    return statistic_sentences


def handle_players_footing(name, values):
    statistic_sentences = []

    right = values.get('right')
    left = values.get('left')

    sentence = f"{name} has a total of {left} left footed players and {right} right footed players."
    statistic_sentences.append(sentence)

    return statistic_sentences


def handle_ball_possession_percentage(name, values):
    statistic_sentences = []

    sentence = f"For a total of {values.get('count')} recorded games, {name} has on average {values.get('average')}% ball possession."
    statistic_sentences.append(sentence)

    return statistic_sentences


def handle_offsides(name, values):
    statistic_sentences = []

    sentence = f"In a total of {values.get('count')} games, {name} has had on average {values.get('average')} offsides per game."
    statistic_sentences.append(sentence)

    return statistic_sentences


def handle_fouls(name, values):
    statistic_sentences = []

    sentence = f"In a total of {values.get('count')} games, {name} has committed on average {values.get('average')} fouls per game."
    statistic_sentences.append(sentence)

    return statistic_sentences


def handle_cleansheets(name, values):
    statistic_sentences = []

    all = values.get('all', [])
    home = values.get('home', [])
    away = values.get('away', [])

    if all != []:
        sentence = f"For a combined number of {all.get('count')} games, home and away, {name} has managed to keep a clean sheet! This equates to {all.get('percentage')}% of all their games."
        statistic_sentences.append(sentence)

    if home != []:
        sentence = f"In {home.get('count')} home games, {name} has managed to keep a clean sheet. This equates to {home.get('percentage')}% of their home games."
        statistic_sentences.append(sentence)

    if away != []:
        sentence = f"In {away.get('count')} away games, {name} has managed to keep a clean sheet. This equates to {away.get('percentage')}% of their away games."
        statistic_sentences.append(sentence)

    return statistic_sentences


def handle_tackles(name, values):
    statistic_sentences = []

    sentence = f"In a total of {values.get('count')} games, {name} has made on average {values.get('average')} tackles per game."
    statistic_sentences.append(sentence)

    return statistic_sentences


def handle_shots(name, values):
    statistic_sentences = []

    total = values.get('total')
    on_target = values.get('on_target')
    off_target = values.get('off_target')
    inside_box = values.get('inside_box')
    outside_box = values.get('outside_box')
    blocked = values.get('blocked')
    average = values.get('average')

    sentence = f"In a total of {total} shots, {name} has made on average {average} shots per game."
    statistic_sentences.append(sentence)

    if on_target != None:
        sentence = f"In a total of {total} shots, {name} has made {on_target} shots on target."
        statistic_sentences.append(sentence)

    if off_target != None:
        sentence = f"In a total of {total} shots, {name} has made {off_target} shots off target."
        statistic_sentences.append(sentence)

    if inside_box != None:
        sentence = f"In a total of {total} shots, {name} has made {inside_box} shots inside the box."
        statistic_sentences.append(sentence)

    if outside_box != None:
        sentence = f"In a total of {total} shots, {name} has made {outside_box} shots outside the box."
        statistic_sentences.append(sentence)

    if blocked != None:
        sentence = f"In a total of {total} shots, {name} has made {blocked} shots that were blocked."
        statistic_sentences.append(sentence)

    return statistic_sentences


def handle_goals(name, values):
    statistic_sentences = []

    all = values.get('all', [])
    home = values.get('home', [])
    away = values.get('away', [])

    if all != []:
        if all.get('first') != None:
            sentence = f"For a combined number of {all.get('count')} games, home and away, {name} has managed to score an average of {all.get('average')} goals, in which the first goal tends to happen at the {all.get('first')} minute mark."
            statistic_sentences.append(sentence)
        else:
            sentence = f"For a combined number of {all.get('count')} games, home and away, {name} has managed to score an average of {all.get('average')} goals."
            statistic_sentences.append(sentence)

    if home != []:
        if home.get('first') != None:
            sentence = f"In {home.get('count')} home games, {name} has scored an average of {home.get('average')} goals, in which the first tends to occurr around the {home.get('first')} minute mark. This values equate to the fact that roughly {home.get('percentage')}% of {name}'s total number of scored goals take place in home games."
            statistic_sentences.append(sentence)
        else:
            sentence = f"In {home.get('count')} home games, {name} has scored an average of {home.get('average')} goals. This values equate to the fact that roughly {home.get('percentage')}% of {name}'s total number of scored goals take place in home games."
            statistic_sentences.append(sentence)

    if away != []:
        if away.get('first') != None:
            sentence = f"In {away.get('count')} away games, {name} has conceded an average of {away.get('average')} goals, in which the first tends to occurr around the {away.get('first')} minute mark. This values equate to the fact that roughly {away.get('percentage')}% of {name}'s total number of scored goals take place in away games."
            statistic_sentences.append(sentence)
        else:
            sentence = f"In {away.get('count')} away games, {name} has conceded an average of {away.get('average')} goals. This values equate to the fact that roughly {away.get('percentage')}% of {name}'s total number of scored goals take place in away games."
            statistic_sentences.append(sentence)

    return statistic_sentences


def handle_both_teams_to_score(name, values):
    statistic_sentences = []

    all = values.get('all', [])
    home = values.get('home', [])
    away = values.get('away', [])

    if all != []:
        sentence = f"For a combined number of {all.get('count')} games, home and away, {name} has managed to score and concede at least one goal."
        statistic_sentences.append(sentence)

    if home != []:
        sentence = f"In {home.get('count')} home games, {name} has scored and conceded at least one goal."
        statistic_sentences.append(sentence)

    if away != []:
        sentence = f"In {away.get('count')} away games, {name} has scored and conceded at least one goal."
        statistic_sentences.append(sentence)

    return statistic_sentences


def handle_failed_to_score(name, values):
    statistic_sentences = []

    all = values.get('all', [])
    home = values.get('home', [])
    away = values.get('away', [])

    if all != []:
        sentence = f"For a combined number of {all.get('count')} games, home and away, {name} has failed to score in {all.get('percentage')}% of them."
        statistic_sentences.append(sentence)

    if home != []:
        sentence = f"In {home.get('count')} home games, {name} has failed to score in {home.get('percentage')}% of them, which equates for {home.get('overall_percentage')}% of their total missed opportunities."
        statistic_sentences.append(sentence)

    if away != []:
        sentence = f"In {away.get('count')} away games, {name} has failed to score in {away.get('percentage')}% of them, which equates for {away.get('overall_percentage')}% of their total missed opportunities."
        statistic_sentences.append(sentence)

    return statistic_sentences


def handle_yellowcards(name, values):
    statistic_sentences = []

    player_name = values.get('player_name')

    if player_name != None:
        sentence = f"{name}'s player with the most yellow cards is {player_name} with {values.get('count')} yellow cards, which equate to {values.get('average')} yellow cards per game."
        statistic_sentences.append(sentence)

    return statistic_sentences


def handle_redcards(name, values):
    statistic_sentences = []

    player_name = values.get('player_name')

    if player_name != None:
        sentence = f"{name}'s player with the most red cards is {player_name} with {values.get('count')} red cards, which equate to {values.get('average')} red cards per game."
        statistic_sentences.append(sentence)

    return statistic_sentences


def handle_attacks(name, values):
    statistic_sentences = []

    sentence = f"{name} has a total of {values.get('count')} recorded attacks, which correlate to an average of {values.get('average')} attacks per game."
    statistic_sentences.append(sentence)

    return statistic_sentences


def handle_team_draws(name, values):
    statistic_sentences = []

    all = values.get('all', [])
    home = values.get('home', [])
    away = values.get('away', [])

    if all != []:
        sentence = f"{name} has scored {all.get('count')} draws."
        statistic_sentences.append(sentence)

    if home != []:
        sentence = f"{name} has scored {home.get('count')} draws in home games, which equates to {home.get('percentage')}% of all their draws."
        statistic_sentences.append(sentence)

    if away != []:
        sentence = f"{name} has scored {away.get('count')} draws in away games, which equates to {away.get('percentage')}% of all their draws."
        statistic_sentences.append(sentence)

    return statistic_sentences


def handle_shot_conversion_rate(name, values):
    statistic_sentences = []

    sentence = f"{name} has a conversion rate of {values.get('conversion_rate_pct')}"
    statistic_sentences.append(sentence)

    return statistic_sentences


def handle_statistic_details(team_name, stat_type, values):
    match stat_type:
        case "Team Lost":
            return handle_team_lost(team_name, values)

        case "Corners":
            return handle_corners(team_name, values)
    
        case "Goals Conceded":
            return handle_goals_conceded(team_name, values)

        case "Dangerous Attacks":
            return handle_dangerous_attacks(team_name, values)

        case "Penalty Conversion Rate":
            return handle_penalty_conversion_rate(team_name, values)

        case "Average Points Per Game":
            return handle_average_points_per_game(team_name, values)

        case "Team Wins":
            return handle_team_wins(team_name, values)

        case "Shot On Target Percentage":
            return handle_shot_on_target_percentage(team_name, values)

        case "Number Of Goals": # API has confusing information so we opted to ignore this data
            return []

        case "Yellowred Cards": # Duplicated information, therefore ignored
            return []

        case "Scoring Minutes":
            return handle_scoring_minutes(team_name, values)

        case "Penalties":
            return handle_penalties(team_name, values)

        case "Conceded Scoring Minutes":
            return handle_conceded_scoring_minutes(team_name, values)

        case "Highest Rated Player":
            return handle_highest_rated_player(team_name, values)

        case "Players Footing":
            return handle_players_footing(team_name, values)

        case "Most Injured Players": # API has incomplete information so we decided to ignore it
            return []

        case "Ball Possession %":
            return handle_ball_possession_percentage(team_name, values)

        case "Offsides":
            return handle_offsides(team_name, values)

        case "Fouls":
            return handle_fouls(team_name, values)

        case "Cleansheets":
            return handle_cleansheets(team_name, values)

        case "Tackles":
            return handle_tackles(team_name, values)

        case "Shots":
            return handle_shots(team_name, values)

        case "Goals":
            return handle_goals(team_name, values)

        case "Both Teams To Score":
            return handle_both_teams_to_score(team_name, values)

        case "Failed To Score":
            return handle_failed_to_score(team_name, values)

        case "Appearing Players": # API has incomplete information so we decided to ignore it
            return []

        case "Yellowcards":
            return handle_yellowcards(team_name, values)

        case "Redcards":
            return handle_redcards(team_name, values)

        case "Attacks":
            return handle_attacks(team_name, values)

        case "Team Draws":
            return handle_team_draws(team_name, values)

        case "Shot Conversion Rate":
            return handle_shot_conversion_rate(team_name, values)

        case "Most Substituted Players": # API has incomplete information so we decided to ignore it
            return []

        case _:
            print("Unknow statistic type found: ", stat_type)
            return []


def handle_statistics(team_name, statistics):
    global teams_information

    season_id = statistics.get('season_id')

    # To make sure we only include statistics from the "2023/2024" season to avoid
    # including dubious data due to the API's lack of season information
    if int(season_id) != 21825:
        return

    details = statistics.get('details')

    for detail in details:
        statistic_type = detail.get('type').get('name')
        values = detail.get('value')

        for detail_sentence in handle_statistic_details(team_name, statistic_type, values):
            teams_information[team_name].append(detail_sentence)


def handle_rivals(team_name, rivals):
    global teams_information

    for rival in rivals:
        rival_name = rival.get('name')
        founded = rival.get('founded')

        if founded != None:
            sentence = f"{rival_name}, a team founded in {founded}, has cultivated a rivalry with {team_name} since both teams tend to fight over the same league objectives in the portuguese championship."
            teams_information[team_name].append(sentence)
        else:
            sentence = f"{rival_name} has cultivated a rivalry with {team_name} since both teams tend to fight over the same league objectives in the portuguese championship."
            teams_information[team_name].append(sentence)
        


def handle_trophies(team_name, trophies):
    global teams_information

    if len(trophies) == 0:
        sentence = f"{team_name} has yet to win any trophy."
        teams_information[team_name].append(sentence)

    else:
        sentence = f"{team_name} has won a total of {len(trophies)} trophies."
        teams_information[team_name].append(sentence)

def handle_players(team_name, players):
    global teams_information

    for player in players:
        jersey_number = player.get('jersey_number')
        start = player.get('start')
        end = player.get('end')
        captain = player.get('captain')
        player_info = player.get('player')
        player_name = player_info.get('name')
        height = player_info.get('height')
        weight = player_info.get('weight')

        position = player.get('detailedposition')

        if jersey_number != None:
            jersey_number = int(jersey_number)

        if position != None:
            position_name = str(position.get('name')).lower()

            if height != None and weight != None:
                if jersey_number != None:
                    sentence = f"{player_name}, {height} tall and weighting {weight}, is a {position_name} for {team_name} with the {jersey_number} jersey number."
                    teams_information[team_name].append(sentence)
                else:
                    sentence = f"{player_name}, {height} tall and weighting {weight}, is a {position_name} for {team_name}."
                    teams_information[team_name].append(sentence)

            elif height != None:
                if jersey_number != None:
                    sentence = f"{player_name}, {height} tall, is a {position_name} for {team_name} with the {jersey_number} jersey number."
                    teams_information[team_name].append(sentence)
                else:
                    sentence = f"{player_name}, {height} tall, is a {position_name} for {team_name}."
                    teams_information[team_name].append(sentence)

            elif weight != None:
                if jersey_number != None:
                    sentence = f"{player_name}, weighting {weight}, is a {position_name} for {team_name} with the {jersey_number} jersey number."
                    teams_information[team_name].append(sentence)
                else:
                    sentence = f"{player_name}, weighting {weight}, is a {position_name} for {team_name}."
                    teams_information[team_name].append(sentence)

        else:
            if height != None and weight != None:
                if jersey_number != None:
                    sentence = f"{player_name}, {height} tall and weighting {weight}, plays for {team_name} with the {jersey_number} jersey number."
                    teams_information[team_name].append(sentence)
                else:
                    sentence = f"{player_name}, {height} tall and weighting {weight}, plays for {team_name}."
                    teams_information[team_name].append(sentence)

            elif height != None:
                if jersey_number != None:
                    sentence = f"{player_name}, {height} tall, plays for {team_name} with the {jersey_number} jersey number."
                    teams_information[team_name].append(sentence)
                else:
                    sentence = f"{player_name}, {height} tall, plays for {team_name}."
                    teams_information[team_name].append(sentence)

            elif weight != None:
                if jersey_number != None:
                    sentence = f"{player_name}, weighting {weight}, plays for {team_name} with the {jersey_number} jersey number."
                    teams_information[team_name].append(sentence)
                else:
                    sentence = f"{player_name}, weighting {weight}, plays for {team_name}."
                    teams_information[team_name].append(sentence)

        transfer = player.get('transfer')
        if transfer != None:
            transfer_date = transfer.get('date')
            amount = transfer.get('amount')
            from_team = transfer.get('from_team')

            if transfer_date != None and amount != None and from_team != None:
                sentence = f"{player_name} has been transfered from {from_team} to {team_name} on {transfer_date} for {amount} euros."
                teams_information[team_name].append(sentence)

        if start != None and end != None:
            sentence = f"{player_name}'s contract for {team_name} started in {start} and is valid until {end}."
            teams_information[team_name].append(sentence)

        if captain:
            sentence = f"{player_name} is the captain of {team_name}."
            teams_information[team_name].append(sentence)


try:
    teams_data = teams_collection.find()

    for team in teams_data:
        team_name = team.get('name')
        last_played_at = team.get('last_played_at')
        founded = team.get('founded')
        short_code = team.get('short_code', None)

        teams_information[team_name] = []

        for statistics in team.get('statistics', []):
            handle_statistics(team_name, statistics)

        rivals = team.get('rivals', [])
        handle_rivals(team_name, rivals)

        trophies = team.get('trophies', [])
        handle_trophies(team_name, trophies)

        players = team.get('players', [])
        handle_players(team_name, players)

except Exception as e:
    print("An error occurred when trying to access the teams collection: " + e)

file_name = "../Files/teams.txt"
with open(file_name, 'w',encoding='utf-8') as file:
    for team in teams_information:
        for sentence in teams_information[team]:
            file.write(sentence + '\n')
print("File ", file_name, "successfully created!")


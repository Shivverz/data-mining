from pymongo import MongoClient

username = "calcanhoto"
password = "admin"

uri = f"mongodb+srv://{username}:{password}@datamining.ywf7foj.mongodb.net/?retryWrites=true&w=majority&appName=DataMining"

try:
    client = MongoClient(uri)
    print("Conexão bem-sucedida ao MongoDB!")
except Exception as e:
    print(f"Erro ao conectar ao MongoDB: {e}")

db = client['sportmonks']
seasons_collection = db['seasons']

text_phrases = []

try:
    seasons_data = seasons_collection.find()

    for season in seasons_data:
        season_name = season.get('name')
        finished = season.get('finished', False)
        started = season.get('starting_at')
        ending = season.get('ending_at', "Not finished yet")
        
        teams = []
        for equipe in season.get('teams', []):
            name = equipe.get('name')
            founded = equipe.get('founded')
            if name and founded:
                info = (name, founded)
                teams.append(info)

        for statistic in season.get('statistics',[]):
            match statistic.get('statistic_type').get('name'):
                case 'Corners':
                    team_most_corners = statistic['value'].get('team_most_corners_name')
                    team_nr_corners = statistic['value'].get('count')
                    
                    frase = f"In Season {season_name} {team_most_corners} was the team with most corners with {int(team_nr_corners)}."
                    text_phrases.append(frase)
                case 'Attacks':
                    attacks_total = statistic['value'].get('count')
                    attacks_average = statistic['value'].get('average')
                                        
                    frase = f"In Season {season_name} the total number of attacks was {int(attacks_total)}."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the average number of attacks per match was {attacks_average}."
                    text_phrases.append(frase)
                case 'Dangerous Attacks':
                    dangerous_attacks_total = statistic['value'].get('count')
                    dangerous_attacks_average = statistic['value'].get('average')
                    
                    frase = f"In Season {season_name} the total number of dangerous attacks was {int(dangerous_attacks_total)}."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the average number of dangerous attacks per match was {dangerous_attacks_average}."
                    text_phrases.append(frase)
                case 'Season Matches':
                    total_matches = statistic['value'].get('total')
                    
                    frase = f"In Season {season_name} was {int(total_matches)} matches."
                    text_phrases.append(frase)
                case 'Matches Ended In Draw':
                    draw_matches = statistic['value'].get('count')
                    
                    frase = f"In Season {season_name} was {int(draw_matches)} matches ended in draw."
                    text_phrases.append(frase)
                case 'Number Of Goals':
                    total_goals = statistic['value'].get('total')
                    average_goals = statistic['value'].get('average')   

                    frase = f"In Season {season_name} the total number of goals was {int(total_goals)}."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the average total number of goals per match was {average_goals}."
                    text_phrases.append(frase)                      
                case 'Both Teams To Score':
                    both_t_score = statistic['value'].get('count')
                    both_t_score_percent = statistic['value'].get('percentage')
                    
                    frase = f"In Season {season_name} the total number of games where both teams scored was {int(both_t_score)}."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the percentage of games where both teams scored was {both_t_score_percent}."
                    text_phrases.append(frase) 
                case 'Cards':
                    yellowcards = statistic['value'].get('yellowcards')
                    redcards = statistic['value'].get('redcards')
                    yellowredcards = statistic['value'].get('yellowredcards')
                    average_yellowcards = statistic['value'].get('average_yellowcards')
                    average_redcards = statistic['value'].get('average_redcards')
                    average_yellowredcards = statistic['value'].get('average_yellowredcards')
                    
                    frase = f"In Season {season_name} the total number of yellowcards was {int(yellowcards)}."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the total number of redcards was {int(redcards)}."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the total number of yellowredcards was {int(yellowredcards)}."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the average number of yellowcards per match was {average_yellowcards}."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the average number of redcards per match was {average_redcards}."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the average number of yellowredcards per match was {average_yellowredcards}."
                    text_phrases.append(frase)                                        
                case 'Cleansheets':
                    cleansheets = statistic['value'].get('count')
                    cleansheets_percent = statistic['value'].get('percentage')
                    
                    frase = f"In Season {season_name} the total number of cleansheets was {int(cleansheets)}."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the percentage of cleansheets was {cleansheets_percent}."
                    text_phrases.append(frase) 
                case 'Scoring Minutes':
                    min_0_15 = statistic['value'].get('0-15', {}).get('count')
                    min_15_30 = statistic['value'].get('15-30', {}).get('count')
                    min_30_45 = statistic['value'].get('30-45', {}).get('count')
                    min_45_60 = statistic['value'].get('45-60', {}).get('count')
                    min_60_75 = statistic['value'].get('60-75', {}).get('count')
                    min_75_90 = statistic['value'].get('75-90', {}).get('count')
                    min_0_15_percent = statistic['value'].get('0-15', {}).get('percentage')
                    min_15_30_percent = statistic['value'].get('15-30', {}).get('percentage')
                    min_30_45_percent = statistic['value'].get('30-45', {}).get('percentage')
                    min_45_60_percent = statistic['value'].get('45-60', {}).get('percentage')
                    min_60_75_percent = statistic['value'].get('60-75', {}).get('percentage')
                    min_75_90_percent = statistic['value'].get('75-90', {}).get('percentage')
                    
                    frase = f"In Season {season_name} the number of goals scored in the first 15 minutes was {int(min_0_15)}."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the number of goals scored between 15 and 30 minutes was {int(min_15_30)}."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the number of goals scored between 30 and 45 minutes was {int(min_30_45)}."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the number of goals scored between 45 and 60 minutes was {int(min_45_60)}."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the number of goals scored between 60 and 75 minutes was {int(min_60_75)}."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the number of goals scored between 75 and 90 minutes was {int(min_75_90)}."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the number of goals scored in the first 15 minutes was {min_0_15_percent} percent of the total goals."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the number of goals scored between 15 and 30 minutes was {min_15_30_percent} percent of the total goals."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the number of goals scored between 30 and 45 minutes was {min_30_45_percent} percent of the total goals."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the number of goals scored between 45 and 60 minutes was {min_45_60_percent} percent of the total goals."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the number of goals scored between 60 and 75 minutes was {min_60_75_percent} percent of the total goals."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the number of goals scored between 75 and 90 minutes was {min_75_90_percent} percent of the total goals."
                    text_phrases.append(frase)
                case 'Goal Line':
                    over_data = statistic['value'].get('over', {})
                    over_4_5 = over_data.get('4_5', {}).get('count', {})
                    over_5_5 = over_data.get('5_5', {}).get('count', {})
                    over_6_5 = over_data.get('6_5', {}).get('count', {})
                    over_0_5 = over_data.get('0_5', {}).get('count', {})
                    over_1_5 = over_data.get('1_5', {}).get('count', {})
                    over_2_5 = over_data.get('2_5', {}).get('count', {})
                    over_3_5 = over_data.get('3_5', {}).get('count', {})
                    over_4_5_percent = over_data.get('4_5', {}).get('percentage', {})
                    over_5_5_percent = over_data.get('5_5', {}).get('percentage', {})
                    over_6_5_percent = over_data.get('6_5', {}).get('percentage', {})
                    over_0_5_percent = over_data.get('0_5', {}).get('percentage', {})
                    over_1_5_percent = over_data.get('1_5', {}).get('percentage', {})
                    over_2_5_percent = over_data.get('2_5', {}).get('percentage', {})
                    over_3_5_percent = over_data.get('3_5', {}).get('percentage', {})

                    under_data = statistic['value'].get('under', {})
                    under_4_5 = under_data.get('4_5', {}).get('count', {})
                    under_5_5 = under_data.get('5_5', {}).get('count', {})
                    under_6_5 = under_data.get('6_5', {}).get('count', {})
                    under_0_5 = under_data.get('0_5', {}).get('count', {})
                    under_1_5 = under_data.get('1_5', {}).get('count', {})
                    under_2_5 = under_data.get('2_5', {}).get('count', {})
                    under_3_5 = under_data.get('3_5', {}).get('count', {})
                    under_4_5_percent = under_data.get('4_5', {}).get('percentage', {})
                    under_5_5_percent = under_data.get('5_5', {}).get('percentage', {})
                    under_6_5_percent = under_data.get('6_5', {}).get('percentage', {})
                    under_0_5_percent = under_data.get('0_5', {}).get('percentage', {})
                    under_1_5_percent = under_data.get('1_5', {}).get('percentage', {})
                    under_2_5_percent = under_data.get('2_5', {}).get('percentage', {})
                    under_3_5_percent = under_data.get('3_5', {}).get('percentage', {})
                    
                    frase = f"In Season {season_name} the number of games with over 4.5 goals was {int(over_4_5)}."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the number of games with over 5.5 goals was {int(over_5_5)}."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the number of games with over 6.5 goals was {int(over_6_5)}."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the number of games with over 0.5 goals was {int(over_0_5)}."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the number of games with over 1.5 goals was {int(over_1_5)}."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the number of games with over 2.5 goals was {int(over_2_5)}."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the number of games with over 3.5 goals was {int(over_3_5)}."
                    text_phrases.append(frase)

                    frase = f"In Season {season_name} the number of games with under 4.5 goals was {int(under_4_5)}."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the number of games with under 5.5 goals was {int(under_5_5)}."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the number of games with under 6.5 goals was {int(under_6_5)}."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the number of games with under 0.5 goals was {int(under_0_5)}."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the number of games with under 1.5 goals was {int(under_1_5)}."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the number of games with under 2.5 goals was {int(under_2_5)}."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the number of games with under 3.5 goals was {int(under_3_5)}."
                    text_phrases.append(frase)

                    frase = f"In Season {season_name} the percentage of games with over 4.5 goals was {over_4_5_percent} percent."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the percentage of games with over 5.5 goals was {over_5_5_percent} percent."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the percentage of games with over 6.5 goals was {over_6_5_percent} percent."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the percentage of games with over 0.5 goals was {over_0_5_percent} percent."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the percentage of games with over 1.5 goals was {over_1_5_percent} percent."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the percentage of games with over 2.5 goals was {over_2_5_percent} percent."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the percentage of games with over 3.5 goals was {over_3_5_percent} percent."
                    text_phrases.append(frase)

                    frase = f"In Season {season_name} the percentage of games with under 4.5 goals was {under_4_5_percent} percent."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the percentage of games with under 5.5 goals was {under_5_5_percent} percent."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the percentage of games with under 6.5 goals was {under_6_5_percent} percent."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the percentage of games with under 0.5 goals was {under_0_5_percent} percent."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the percentage of games with under 1.5 goals was {under_1_5_percent} percent."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the percentage of games with under 2.5 goals was {under_2_5_percent} percent."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the percentage of games with under 3.5 goals was {under_3_5_percent} percent."
                    text_phrases.append(frase)

                case 'Win Percentage':
                    win_home_percent = statistic['value'].get('home')
                    win_away_percent = statistic['value'].get('away')
                    
                    frase = f"In Season {season_name} the home team won {win_home_percent} percent of the matches."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the away team won {win_away_percent} percent of the matches."
                    text_phrases.append(frase)
                case 'Defeat Percentage':
                    defeat_home_percent = statistic['value'].get('home')
                    defeat_away_percent = statistic['value'].get('away')
                    
                    frase = f"In Season {season_name} the home team lost {defeat_home_percent} percent of the matches."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} the away team lost {defeat_away_percent} percent of the matches."
                    text_phrases.append(frase)
                case 'Draw Percentage': 
                    draw_home_percent = statistic['value'].get('all')
                    
                    frase = f"In Season {season_name} the teams draw {draw_home_percent} percent of the matches."
                    text_phrases.append(frase)                     
                case 'Most Scored':
                    team_most_scored_data = statistic['value']
                    team_most_scored = team_most_scored_data.get('participant_name', {})
                    team_most_scored_count = team_most_scored_data.get('count', {})
                    team_most_scored_count_home = team_most_scored_data.get('home', {})
                    team_most_scored_count_away = team_most_scored_data.get('away', {})
                    
                    frase = f"In Season {season_name} the team that scored the most goals was {team_most_scored} with {int(team_most_scored_count)} goals."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} at home {team_most_scored} scored the most goals with {int(team_most_scored_count_home)} goals."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} away from home {team_most_scored} scored the most goals with {int(team_most_scored_count_away)} goals."
                    text_phrases.append(frase)
                case 'Most Conceded':
                    team_most_scored_data = statistic['value']
                    team_most_scored = team_most_scored_data.get('participant_name', {})
                    team_most_scored_count = team_most_scored_data.get('count', {})
                    team_most_scored_count_home = team_most_scored_data.get('home', {})
                    team_most_scored_count_away = team_most_scored_data.get('away', {})
                    
                    frase = f"In Season {season_name} the team that conceded the most goals was {team_most_scored} with {int(team_most_scored_count)} goals conceded."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} at home {team_most_scored} conceded the most goals with {int(team_most_scored_count_home)} goals conceded."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} away from home {team_most_scored} conceded the most goals with {int(team_most_scored_count_away)} goals conceded."
                    text_phrases.append(frase)
                case 'Most Scored Per Match':
                    team_most_scored = statistic['value']
                    average_away = team_most_scored.get('away')
                    average_home = team_most_scored.get('home')
                    team_name = team_most_scored.get('participant_name')
                    
                    frase = f"In Season {season_name} {team_name} scored an average of {average_home} goals per match at home."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} {team_name} scored an average of {average_away} goals per match away from home."
                    text_phrases.append(frase)
                case 'Most Conceded Per Match':
                    team_most_Conceded = statistic['value']
                    average_away = team_most_Conceded.get('away')
                    average_home = team_most_Conceded.get('home')
                    team_name = team_most_Conceded.get('participant_name')
                    
                    frase = f"In Season {season_name} {team_name} conceded an average of {average_home} goals per match at home."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} {team_name} conceded an average of {average_away} goals per match away from home."
                    text_phrases.append(frase)
                case 'Goal Topscorer':
                    player_name = statistic['value'].get('player_name')
                    player_nr_goals = statistic['value'].get('count')
                    
                    frase = f"In Season {season_name} the top goalscorer was {player_name} with {int(player_nr_goals)} goals."
                    text_phrases.append(frase)

                case 'Assist Topscorer':
                    player_name = statistic['value'].get('player_name')
                    player_nr_assists = statistic['value'].get('count')
                    
                    frase = f"In Season {season_name} the top assist provider was {player_name} with {int(player_nr_assists)} assists."
                    text_phrases.append(frase)
                case 'Card Topscorer':
                    player_name = statistic['value'].get('player_name')
                    player_nr_cards = statistic['value'].get('count')
                    
                    frase = f"In Season {season_name} the player with the most cards was {player_name} with {int(player_nr_cards)} cards."
                    text_phrases.append(frase)

                case 'Highest Rated Player':
                    player_name = statistic['value'].get('player_name')
                    player_rating = statistic['value'].get('rating')
                    
                    frase = f"In Season {season_name} the highest rated player was {player_name} with a rating of {player_rating}."
                    text_phrases.append(frase)          
                case 'Highest Rated Team':
                    team_name = statistic['value'].get('team_name')
                    team_rating = statistic['value'].get('rating')
                    
                    frase = f"In Season {season_name} the highest rated team was {team_name} with a rating of {team_rating}."
                    text_phrases.append(frase)
                case 'Referees':
                    total_referees = statistic['value'].get('total')
                    
                    frase = f"In Season {season_name} was a total of {int(total_referees)} referees."
                    text_phrases.append(frase)
                case 'Failed To Score':
                    team_name = statistic['value'].get('participant_name')
                    great_occasions_failed = statistic['value'].get('count')
                    
                    frase = f"In Season {season_name} {team_name} failed to score {int(great_occasions_failed)} significant occasions."
                    text_phrases.append(frase)
                case 'Shots':
                    total_shots = statistic['value'].get('total')
                    on_target = statistic['value'].get('on_target')
                    off_target = statistic['value'].get('off_target')
                    inside_box = statistic['value'].get('inside_box',0)
                    outside_box = statistic['value'].get('outside_box',0)
                    blocked_shots = statistic['value'].get('blocked',0)
                    average_shots_per_match = statistic['value'].get('average')
                    
                    if total_shots != None:
                        frase = f"In Season {season_name} the total number of shots taken was {int(total_shots)}."
                        text_phrases.append(frase)
                    frase = f"In Season {season_name} {int(on_target)} shots were on target."
                    text_phrases.append(frase)
                    frase = f"In Season {season_name} {int(off_target)} shots were off target."
                    text_phrases.append(frase)
                    if inside_box != None:
                        frase = f"In Season {season_name} {int(inside_box)} shots were taken from inside the box."
                        text_phrases.append(frase)
                    if outside_box != None:
                        frase = f"In Season {season_name} {int(outside_box)} shots were taken from outside the box."
                        text_phrases.append(frase)
                    if blocked_shots != None:
                        frase = f"In Season {season_name} {int(blocked_shots)} shots were blocked."
                        text_phrases.append(frase)
                    frase = f"In Season {season_name} the average number of shots per match was {average_shots_per_match}."
                    text_phrases.append(frase)

                                                
except Exception as e:
    print(f"Erro ao acessar os dados das temporadas: {e}")

finally:
    client.close()

file_name = "seasons.txt"
with open(file_name, 'w',encoding='utf-8') as file:
    for phrase in text_phrases:
        file.write(phrase + '\n')
print("Arquivo", file_name, "criado com sucesso!")



class WrongNumberOfPlayersError(Exception):
    pass

class NoSuchStrategyError(Exception):
    pass

def rps_game_winner(players):
    if len(players) != 2:
        raise WrongNumberOfPlayersError()
    
    vozmojniy_hod = ['R', 'P', 'S']
    player1_name, player1_hod = players[0]
    player2_name, player2_hod = players[1]

    if player1_hod not in vozmojniy_hod or player2_hod not in vozmojniy_hod:
        raise NoSuchStrategyError()
    
    if player1_hod == player2_hod:
        return f"{player1_name} {player1_hod}"

    if (player1_hod == 'R' and player2_hod == 'S') or \
       (player1_hod == 'S' and player2_hod == 'P') or \
       (player1_hod == 'P' and player2_hod == 'R'):
        return f"{player1_name} {player1_hod}"
    else:
        return f"{player2_name} {player2_hod}"
        

def safe_rps_game_winner(players):
    try:
        return rps_game_winner(players)
    except WrongNumberOfPlayersError:
        return "WrongNumberOfPlayersError"
    except NoSuchStrategyError:
        return "NoSuchStrategyError"


print(safe_rps_game_winner([['Ronaldo', 'R'], ['Pessi', 'S']]))
print(safe_rps_game_winner([['huligan', 'P'], ['pacan', 'A']]))
print(safe_rps_game_winner([['hehe', 'P'], ['haha', 'S'], ['huh', 'S']]))
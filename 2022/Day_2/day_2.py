round_score_key = {
    'win': 6,
    'tie': 3,
    'loss': 0
}
selection_score_key = {
    'X': 1,
    'Y': 2,
    'Z': 3
}
outcome_key = {
    'A': {'X': 'tie', 'Y': 'win', 'Z': 'loss'},
    'B': {'X': 'loss', 'Y': 'tie', 'Z': 'win'},
    'C': {'X': 'win', 'Y': 'loss', 'Z': 'tie'}
}

def get_game_data(infile):
    with open(infile, 'r') as fin:
        return [line.rstrip('\n').split(' ') for line in fin]

def main(infile):
    full_game = get_game_data(infile)
    score_total = 0
    for round in full_game:
        opponent_play, my_play = round[0], round[1]
        outcome = outcome_key[opponent_play][my_play]
        score_total += (round_score_key[outcome] + selection_score_key[my_play])

    print(score_total)

    
if __name__=="__main__":
    infile = 'strategy_guide.txt'
    main(infile)
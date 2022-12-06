#! python3


file_data="exemple.txt"
file_data="input01.txt"

"""
A for Rock          1
B for Paper         2
C for Scissors.     3


X
Y
Z

guide:
win = 6  + value (1-3)
Loss = 1  + 0
draw = value + opp.value

"""
# part 1
ROCK = 1
PAPER = 2
SCISSOR = 3

WIN = 6
LOSS = 0
DRAW = 3

table = {
    ('ROCK', 'ROCK') : DRAW,
    ('ROCK', 'PAPER') : WIN,
    ('ROCK', 'SCISSOR') : LOSS,

    ('PAPER', 'ROCK') : LOSS,
    ('PAPER', 'PAPER') : DRAW,
    ('PAPER', 'SCISSOR') : WIN,

    ('SCISSOR', 'ROCK') : WIN,
    ('SCISSOR', 'PAPER') : LOSS,
    ('SCISSOR', 'SCISSOR') : DRAW
}

value = {
    'ROCK' : 1,
    'PAPER' : 2,
    'SCISSOR' : 3
}


elem = {
    "A": "ROCK",
    "B": "PAPER",
    "C": "SCISSOR",
    "X": "ROCK",
    "Y": "PAPER",
    "Z": "SCISSOR",
}

scores = { 
    "A X": 2, # ROCK - ROCK
    "A Y": 8, # ROCK - PAPER
    "A Z": 3, # ROCK - SCISSOR

    "B X": 1, # PAPER - ROCK
    "B Y": 4, # PAPER - PAPER
    "B Z": 9, # PAPER - SCISSOR

    "C X": 7, # SCISSOR - ROCK
    "C Y": 2, # SCISSOR - PAPER
    "C Z": 6, # SCISSOR - SCISSOR
} 


roud_end = {
    'X': LOSS,
    'Y': DRAW,
    'Z': WIN
}

wining_shape = {
    'ROCK': 'PAPER',
    'SCISSOR': 'ROCK',
    'PAPER': 'SCISSOR'
}


def gess_shape (shape, result):
    if result == DRAW:
        return shape
    if result == WIN:
        return wining_shape[shape]      # type: ignore
    else:
        return wining_shape[wining_shape[shape]]   # type: ignore


if __name__ == "__main__":

    with open(file_data , 'r') as f:
        rounds = [line.strip("\n")  for line in f.readlines()]

        # print(rounds)
        total = 0
        total_part2 = 0
        for i, round in enumerate(rounds):
            opp , me = round.split()
            clef = (elem[opp], elem[me])
            game_result = table[clef]  # type: ignore
            score = value[elem[me]] + game_result

            status = me
            result_to_give = roud_end[status]
            my_shape = gess_shape( elem[opp], result_to_give)
            score_p2 =  value[my_shape] + result_to_give

            # score0 = scores[round]
            # print(f"{i} opp-me: {clef} score: {score} , score0: {score0} ")
            total += score
            total_part2 += score_p2
        print(f" total: {total}")
        print(f" total_part2: {total_part2}")

# part 1 result 9241
# part 2 14610
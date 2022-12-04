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

# def score(me, opp):
    # if me == "A" 
def win_or_loss(opp, me):
    result = 0
    if me == PAPER:
        if opp == ROCK:
            result = WIN
        elif opp == SCISSOR:
            result = LOSS 
        else:
            result = DRAW
 
    elif me == ROCK:
        if opp == SCISSOR:
            result = WIN
        elif opp == PAPER:
            result = LOSS 
        else:
            result = DRAW

    elif me == SCISSOR:
        if opp == PAPER:
            result = WIN
        elif opp == ROCK:
            result = LOSS 
        else:
            result = DRAW
    result += me
    return result

vals = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSOR,
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSOR,
}

if __name__ == "__main__":

    with open(file_data , 'r') as f:
        rounds =[line.strip("\n")  for line in f.readlines()]
    
        # print(rounds)
        total = 0
        for round in rounds:
            # print( round)
            round_opp, round_me  = round.split()
            me = vals[round_me]
            opp = vals[round_opp]
            # print(me, opp)
            score = win_or_loss(opp, me)
            print(f"{round}, score: {score}")
            total += score
        print(f" total: {total}")


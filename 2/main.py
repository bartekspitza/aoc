with open ('input.txt', 'r') as f:

    # X: Rock Y: Paper Z: Sciccors 
    # Win draw loss
    # x=loose, y=draw, z=win
    results = {
        'A': ['C', 'A', 'B'],
        'B': ['A', 'B', 'C'],
        'C': ['B', 'C', 'A'],
        }
    outcomes = ['X','Y','Z']
    asdf = ['A','B','C']
    scores = []
    score = 0
    for line in f.readlines():
        line = line.strip().split(' ')
        him = line[0]
        outcome = line[1]
        what_to_play = results[him][outcomes.index(outcome)]

        score += 3*outcomes.index(outcome)
        score += asdf.index(what_to_play) + 1
    
    print(score)

# Part 1
"""
with open ('input.txt', 'r') as f:

    # X: Rock Y: Paper Z: Sciccors 
    # Win draw loss
    asdf = {
        'X': ['C', 'A', 'B'],
        'Y': ['A', 'B', 'C'],
        'Z': ['B', 'C', 'A'],
        }
    scores = []
    score = 0
    for line in f.readlines():
        line = line.strip().split(' ')
        him = line[0]
        me = line[1]

        loss_score = asdf[me].index(him)
        if loss_score == 0:
            score += 6
        elif loss_score == 1:
            score += 3
        
        if me == 'X':score+=1
        if me == 'Y':score+=2
        if me == 'Z':score+=3
    
    print(score)
"""

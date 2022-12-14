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

with open('input.txt', 'r') as f:
    data = f.readlines()

    dataa = []
    curr = []
    for line in data:
        line = line.strip()

        if line == '':
            dataa.append(curr)
            curr = []
        else:
            curr.append(int(line))

print(max([sum(x) for x in dataa]))

def output(letter, line):
    with open (letter, 'a') as f:
        f.write(line)

with open('..\\data\\trainingset.txt', 'r') as f:
    for line in f.readlines():
        output(line[-2], line)

rock = 1
paper = 2
scissors = 3

win = 6
draw = 3
lose = 0

def getPoints(type):
    if (type == "A" or type == "X"):
        return rock
    if (type == "B" or type == "Y"):
        return paper
    if (type == "C" or type == "Z"):
        return scissors

def getResult(type):
    if (type == "X"):
        return lose
    if (type == "Y"):
        return draw
    if (type == "Z"):
        return win

def choose(enemy, result):
    if (result == draw):
        return enemy
    
    if (enemy == rock):
        if (result == win):
            return paper
        return scissors
    elif (enemy == paper):
        if (result == win):
            return scissors
        return rock
    elif (enemy == scissors):
        if (result == win):
            return rock
        return paper
    
    return 0

def playRound(enemy, you):
    if (enemy == you):
        return draw
    
    if (enemy == rock):
        if (you == paper):
            return win
    elif (enemy == paper):
        if (you == scissors):
            return win
    elif (enemy == scissors):
        if (you == rock):
            return win
    
    return 0

def part1(lines):
    sum = 0

    for line in lines:
        stripped = line.strip("\n")
        x = stripped.split(" ")
        you = getPoints(x[1])
        sum += playRound(getPoints(x[0]), you) + you

    print("Part 1: " + str(sum))

def part2(lines):
    sum = 0

    for line in lines:
        stripped = line.strip("\n")
        x = stripped.split(" ")
        result = getResult(x[1])
        enemy = getPoints(x[0])
        you = choose(enemy, result)
        sum += result + you

    print("Part 2: " + str(sum))


with open('day2/day2.txt') as f:
    lines = f.readlines()

    part1(lines)
    part2(lines)

    

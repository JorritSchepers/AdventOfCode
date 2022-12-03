def getTotals(lines):
    totals = []
    sum = 0
    
    for line in lines:
        line.strip('\n')
        try:
            sum += int(line)
        except:
            totals.append(sum)
            sum = 0

    return totals

def part1(lines):
    totals = getTotals(lines)

    print(max(totals))

def part2(lines):
    totals = getTotals(lines)
    
    totals.sort(reverse=1)

    print(totals[0] + totals[1] + totals[2])

with open('day1/day1.txt') as f:
    lines = f.readlines()
    lines.append("")

    part1(lines)
    part2(lines)

    

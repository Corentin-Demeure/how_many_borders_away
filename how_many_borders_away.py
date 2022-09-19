from ast import literal_eval

with open("borders.txt", "r") as f_in:
    borders = literal_eval("{" + ",".join(f_in) + "}")

def finder(genA):
    if genA == []:
        return genA
    else:
        genB = []
        away.append([])
        for country in genA:
            if not country in already_done:
                away[len(away) - 1].insert(0, country)
            already_done.append(country)
            for neighbor in borders[country]:
                if not neighbor in already_done and not neighbor in genB:
                    genB.append(neighbor)
        finder(genB)

origin = input('Enter any country: ')
away = []
already_done = []
finder([origin])
for line in away:
    print(f'{away.index(line)} borders to cross: {line}')


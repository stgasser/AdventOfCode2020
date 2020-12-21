from collections import Counter


def parse_input(filename):
    with open(filename) as f:
        inglist = f.read().splitlines()
        cooccurances = Counter()
        ing_occurances = Counter()
        al_occurances = Counter()
        for line in inglist:
            ingredients, allergens = line.split(' (')
            cooccurances += Counter((i, a) for i in ingredients.split(' ') for a in allergens[9:-1].split(', '))
            ing_occurances += Counter(ingredients.split(' '))
            al_occurances += Counter(allergens[9:-1].split(', '))
    al_dict = {}
    old = None
    while al_dict != old:
        old = al_dict.copy()
        for a in sorted(al_occurances, key=lambda a: al_occurances[a], reverse=True):
            for i in sorted(ing_occurances):
                if cooccurances[(i, a)] >= al_occurances[a] and i not in al_dict.values():
                    al_dict[a] = i
                    break
    return ing_occurances,  al_dict


def part1(ing_occurances, al_dict):
    return sum(ing_occurances[i] for i in ing_occurances if i not in al_dict.values())


def part2(ing_occurances, al_dict):
    return ','.join([i for a, i in sorted(al_dict.items())])


if __name__ == '__main__':
    data = parse_input('21.in')
    print("Solution to part 1:", part1(*data))
    print("Solution to part 2:", part2(*data))

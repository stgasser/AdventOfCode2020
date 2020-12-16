def split_bag(bag):
    b = bag.split(" ")
    return b[1] + " " + b[2], int(b[0])


def parse_input(filename):
    with open(filename) as f:
        lines = f.read().split(".\n")
        recipes = dict()
        for line in lines[:-1]:
            color, content = line.split(" bags contain ")
            content = [split_bag(bag) for bag in content.split(", ") if bag != "no other bags"]
            recipes[color] = dict(content)
        return recipes


def part1(recipes):
    ingredients = {'shiny gold'}
    visited = set()
    while ingredients:
        curr = ingredients.pop()
        visited.add(curr)
        for bag, content in recipes.items():
            if curr in content and bag not in visited:
                ingredients.add(bag)
    return len(visited) - 1


def part2(recipes):
    ingredients = {'shiny gold': 1}
    bagcnt = 0
    while ingredients:
        curr, qant = ingredients.popitem()
        bagcnt += qant
        for bag, amount in recipes[curr].items():
            ingredients[bag] = ingredients.get(bag, 0) + qant * amount
    return bagcnt - 1


if __name__ == '__main__':
    data = parse_input('7.in')
    print("Solution to part 1:", part1(data))
    print("Solution to part 2:", part2(data))

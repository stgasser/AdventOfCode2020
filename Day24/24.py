from collections import Counter


def parse_input(filename):
    with open(filename) as f:
        return f.read().splitlines()


def part1(seqs):
    movement = {'e': 1j, 'w': -1j, 'nw': 1 - 0.5j, 'ne': 1 + 0.5j, 'sw': -1 - 0.5j, 'se': -1 + 0.5j}
    tiles = []
    for seq in map(list, seqs.copy()):
        pos = 0
        while seq:
            d = seq.pop(0)
            if d in {'n', 's'}:
                d += seq.pop(0)
            pos += movement[d]
        tiles.append(pos)
    cnt = Counter(tiles)
    return sum(c % 2 == 1 for c in cnt.values())


def part2(seqs):
    movement = {'e': 1j, 'w': -1j, 'x': 1 - 0.5j, 'y': 1 + 0.5j, 'a': -1 - 0.5j, 'b': -1 + 0.5j}
    cnt = Counter(sum(map(lambda c: movement[c], seq.replace('nw', 'x').replace('ne', 'y').replace('sw', 'a').replace('se', 'b'))) for seq in seqs.copy())
    tiles = {pos for pos, n in cnt.items() if n % 2 == 1}
    dirs = movement.values()
    for _ in range(100):
        neighbor_cnt = Counter(pos + ds for pos in tiles for ds in dirs)
        new_tiles = {pos for pos, neighbors in neighbor_cnt.items() if neighbors == 2} - tiles
        tiles = new_tiles | {pos for pos in tiles if neighbor_cnt[pos] != 0 and neighbor_cnt[pos] <= 2}
    return len(tiles)


if __name__ == '__main__':
    data = parse_input('24.in')
    print("Solution to part 1:", part1(data))
    print("Solution to part 2:", part2(data))

import numpy as np
from collections import namedtuple
from itertools import product
from scipy.ndimage.filters import convolve


class Tile:
    def __init__(self, img, tid):
        self.img = img.astype(int)
        self.tid = tid
        self._recalculate_borders()
        self._hflip = False
        self._vflip = False

    def get_borders(self):
        return self.borders

    def share_borders(self, other):
        return (self.borders & other.borders) > set()

    def get_shared_border(self, other):
        for j, bo in enumerate(other._borders):
            for i, b in enumerate(self._borders):
                if b == bo:
                    return i, j

    def hflip(self, flip):
        if flip != self._hflip:
            self.img = self.img[::-1, :]
            self._hflip = flip

    def vflip(self, flip):
        if flip != self._vflip:
            self.img = self.img[:, ::-1]
            self._vflip = flip

    def rot90(self, k):
        self.img = np.rot90(self.img, k)

    def get_img(self):
        return self.img[1:-1, 1:-1]

    def _recalculate_borders(self):
        img = self.img
        # l, t, r, b , lh, tv, rh, bv
        tmp = [img[0, :], img[:, 0], img[-1, :], img[:, -1], img[0, ::-1], img[::-1, 0], img[-1, ::-1], img[::-1, -1]]
        self._borders = list(map(lambda arr: (arr * (2 ** np.arange(len(arr)))).sum(), tmp))
        self.borders = set(self._borders)


def parse_input(filename):
    with open(filename) as f:
        tiles_txt = f.read().split('\n\n')
        tiles = dict()
        for txt in tiles_txt:
            lines = txt.splitlines()
            tid = int(lines[0][-5:-1])
            tiles[tid] = Tile(np.array([list(line) for line in lines[1:]]) == '#', tid)
        return tiles


def part1(tiles):
    neighbors = dict()
    res = 1
    for tid in tiles:
        for tile in tiles.values():
            if tid == tile.tid:
                continue
            if tile.share_borders(tiles[tid]):
                neighbors[tid] = neighbors.get(tid, set()) | {tile.tid, }
        if len(neighbors[tid]) == 2:
            res *= tid
    return res


def part2(tiles):
    # find all the neighbors this is unnecessary
    neighbors = dict()
    for tid in tiles:
        for tile in tiles.values():
            if tid == tile.tid:
                continue
            if tile.share_borders(tiles[tid]):
                neighbors[tid] = neighbors.get(tid, set()) | {tile.tid, }

    Direction = namedtuple("Direction", ['left', 'right', 'top', 'bottom'])
    fringe = {list(tiles.keys())[0]}
    visited = set()
    while fringe:
        curr = fringe.pop()
        if curr in visited:
            continue
        visited.add(curr)
        c_tile = tiles[curr]
        l, r, t, b = -1, -1, -1, -1
        # find the correct orientation for all the neighboring tiles and add them to the fringe
        for tid in neighbors[curr]:
            tile = tiles[tid]
            for hflip, vflip, rot in product([False, True], [False, True], [1, 1, 1, 1]):
                # if it already was visited it has to be in the correct orientation
                if tid not in visited:
                    tile.hflip(hflip)
                    tile.vflip(vflip)
                    tile.rot90(rot)
                if np.all(tile.img[0, :] == c_tile.img[-1, :]):
                    r = tid
                    break
                if np.all(tile.img[-1, :] == c_tile.img[0, :]):
                    l = tid
                    break
                if np.all(tile.img[:, 0] == c_tile.img[:, -1]):
                    b = tid
                    break
                if np.all(tile.img[:, -1] == c_tile.img[:, 0]):
                    t = tid
                    break
                if tid in visited:
                    raise NotImplementedError("Tile already visited but not in correct orientation")
            fringe.add(tid)
        c_tile.nbs = Direction(l, r, t, b)
    # find top left corner
    start = -1
    for tile in tiles.values():
        if tile.nbs.top == -1 and tile.nbs.left == -1:
            start = tile.tid
    # actually stitch image together
    x, y = tiles[start].get_img().shape
    stitched = np.zeros((x * 12, y * 12), dtype=int)
    curcol = start
    colid = 0
    while curcol != -1:
        currow = curcol
        rowid = 0
        while currow != -1:
            stitched[rowid * x:rowid * x + x, colid * y:colid * y + y] = tiles[currow].get_img()
            currow = tiles[currow].nbs.right
            rowid += 1
        curcol = tiles[curcol].nbs.bottom
        colid += 1
    # Find pattern with convolutions and remove it from the water
    pattern = (np.array([list("                  # "),
                         list("#    ##    ##    ###"),
                         list(" #  #  #  #  #  #   ")]) == '#').astype(int)
    img = stitched.copy()
    water = stitched.copy()
    origin = ((pattern.shape[0] - 1) // 2, (pattern.shape[1] - 1) // 2)
    for _ in range(4):
        for pat in [pattern, pattern[::-1, :], pattern[:, ::-1], pattern[::-1, ::-1]]:
            monsters = convolve(img, pat[::-1, ::-1], mode='constant', origin=origin)
            pat_idx = np.argwhere(pat == 1)
            for i, j in np.argwhere(monsters == pat.sum()):
                for di, dj in pat_idx:
                    water[i + di, j + dj] = 0
        # have to rotate the water along with the image to keep the indices aligned
        img = np.rot90(img, 1)
        water = np.rot90(water, 1)
    return water.sum()


if __name__ == '__main__':
    data = parse_input('20.in')
    print("Solution to part 1:", part1(data))
    print("Solution to part 2:", part2(data))

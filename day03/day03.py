#!/usr/bin/python3

import re
import utils.input
import utils.grid

class Claim:
    id
    left = 0
    top = 0
    width = 0
    height = 0
    regex = '#(\d*) @ (\d*),(\d*): (\d*)x(\d*)'

    def __init__(self, string):
        match = re.search(self.regex, string)
        self.id = int(match.group(1))
        self.left = int(match.group(2))
        self.top = int(match.group(3))
        self.width = int(match.group(4))
        self.height = int(match.group(5))

    def xRange(self):
        return range(self.left, self.left + self.width)

    def yRange(self):
        return range(self.top, self.top + self.height)

def part1(input):
    claims = [Claim(i) for i in input]

    grid = utils.grid.grid(1000, 1000, 0)
    overclaimed = 0
    for claim in claims:
        for x in range(claim.left, claim.left + claim.width):
            for y in range(claim.top, claim.top + claim.height):
                grid.data[x][y] = grid.data[x][y] + 1
                if grid.data[x][y] == 2 :
                    overclaimed += 1

    print overclaimed

def hasOverlap(grid, claim):
    for x in claim.xRange():
        for y in claim.yRange():
            if grid.data[x][y] > 1:
                return True
    return False

def part2(input):
    claims = [Claim(i) for i in input]

    grid = utils.grid.grid(1000, 1000, 0)
    for claim in claims:
        for x in claim.xRange():
            for y in claim.yRange():
                grid.data[x][y] = grid.data[x][y] + 1

    for claim in claims:
        if not hasOverlap(grid, claim):
            print claim.id
            return




part2(utils.input.getInput())
#!/usr/bin/python3

import utils.input
import utils.grid


def calculateClosest(points, x, y):
    distances = {id: point.manhattanDistance(x,y) for id,point in enumerate(points)}
    minDistId = min(distances.keys(), key=(lambda k: distances[k]))
    numWithMinDist = sum(1 for x in distances.values() if x == distances[minDistId])
    return minDistId if numWithMinDist == 1 else '.'

def part1(input):
    points = [utils.grid.point2d.fromString(i) for i in input]
    maxX = max(points, key=lambda p: p.x).x
    maxY = max(points, key=lambda p: p.y).y
    grid = utils.grid.grid(maxX+2, maxY+1, -1)
    for x in range(grid.width):
        for y in range(grid.height):
            grid.data[x][y] = calculateClosest(points, x, y)

    # grid.draw()

    sums = {}
    invalid = set()
    for x in range(grid.width):
        for y in range(grid.height):
            val = grid.data[x][y]
            sums[val] = sums.get(val, 0) + 1
            if x == 0 or x == (grid.width - 1) or y == 0 or y == (grid.height - 1):
                invalid.add(val)
    sums.pop('.', None)
    for id in invalid:
        sums.pop(id, None)
    maxSizeKey = max(sums.keys(), key=(lambda k: sums[k]))
    print (sums[maxSizeKey])


def calculateSumDistances(points, x, y):
    sum = 0
    for point in points:
        sum += point.manhattanDistance(x, y)
    return sum

def part2(input):
    points = [utils.grid.point2d.fromString(i) for i in input]
    maxX = max(points, key=lambda p: p.x).x
    maxY = max(points, key=lambda p: p.y).y
    grid = utils.grid.grid(maxX+2, maxY+1, '.')
    inRangeCount = 0
    for x in range(grid.width):
        for y in range(grid.height):
            if calculateSumDistances(points, x, y) < 10000:
                inRangeCount += 1
                grid.data[x][y] = '#'

    grid.draw()
    print (inRangeCount)


part2(utils.input.getInput())
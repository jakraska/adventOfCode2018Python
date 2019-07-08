#!/usr/bin/python3

import utils.input
import utils.grid

import re

class Sky:

    def __init__(self, lights):
        self.lights = lights
        self.time = 0

    def getArea(self):
        return self.getWidth() * self.getHeight()

    def getHeight(self):
        minY = min(self.lights, key=lambda l: l.pos.y).pos.y
        maxY = max(self.lights, key=lambda l: l.pos.y).pos.y
        return  maxY - minY

    def getWidth(self):
        minX = min(self.lights, key=lambda l: l.pos.x).pos.x
        maxX = max(self.lights, key=lambda l: l.pos.x).pos.x
        return maxX - minX

    def draw(self):
        offsetX = 0 - min(self.lights, key=lambda l: l.pos.x).pos.x
        offsetY = 0 - min(self.lights, key=lambda l: l.pos.y).pos.y
        grid = utils.grid.grid(self.getWidth()+1, self.getHeight()+1, '.')
        for light in self.lights:
            grid.data[light.pos.x + offsetX][light.pos.y + offsetY] = '#'
        grid.draw()

    def tickForwards(self):
        for light in self.lights:
            light.pos.x += light.velocity.x
            light.pos.y += light.velocity.y
        self.time += 1

    def tickBackwards(self):
        for light in self.lights:
            light.pos.x -= light.velocity.x
            light.pos.y -= light.velocity.y
        self.time -= 1
class Light:

    def __init__(self, str):
        match = re.search('position=< ?(-?\d+), *(-?\d+)> velocity=< ?(-?\d+), *(-?\d+)>', str)
        self.pos = utils.grid.point2d(int(match.group(1)), int(match.group(2)))
        self.velocity = utils.grid.point2d(int(match.group(3)), int(match.group(4)))


def part1(input):
    lights = [Light(row) for row in input]
    sky = Sky(lights)

    lastArea = sky.getArea()
    sky.tickForwards()
    while sky.getArea() < lastArea:
        lastArea = sky.getArea()
        sky.tickForwards()

    sky.tickBackwards()
    sky.draw()
    print(sky.time)


part1(utils.input.getInput())
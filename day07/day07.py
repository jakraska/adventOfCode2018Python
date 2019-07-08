#!/usr/bin/python3

import utils.input
import re

class Step:

    def __init__(self, id):
        self.id = id
        self.complete = False
        self.requirements = []
        self.duration = ord(id) - 64 + 60
        self.duration_complete = 0
        self.in_progress = False

    def is_ready(self):
        for step in self.requirements:
            if not step.complete:
                return False
        return True

def parseSteps(input):
    steps = {}

    for row in input:
        match = re.search('Step (.) must be finished before step (.) can begin.', row)
        requirement = steps.get(match.group(1), Step(match.group(1)))
        step = steps.get(match.group(2), Step(match.group(2)))
        step.requirements.append(requirement)
        steps[step.id] = step
        steps[requirement.id] = requirement
    return steps

def part1(input):
    steps = parseSteps(input)
    order = ''
    while len(steps) > 0:
        for key in sorted(steps.keys()):
            step = steps[key]
            if step.is_ready():
                step.complete = True
                order = order + key
                steps.pop(key)
                break

    print(order)

def part2(input):
    steps = parseSteps(input)
    elves = [''] * 5
    time = 0
    while len(steps) > 0:
        time += 1
        # assign elf to task
        for elfId, current in enumerate(elves) :
            if current == '':
                for key in sorted(steps.keys()):
                    if not steps[key].in_progress and steps[key].is_ready():
                        steps[key].in_progress = True
                        elves[elfId] = key
                        break

        # work on tasks and complete them
        for elfId, current in enumerate(elves) :
            if current != '':
                step = steps[current]
                step.duration_complete += 1
                if step.duration_complete == step.duration:
                    step.complete = True
                    steps.pop(step.id)
                    elves[elfId] = ''
    print time


part2(utils.input.getInput())
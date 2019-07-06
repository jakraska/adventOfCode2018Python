#!/usr/bin/python3

import re
import utils.input


class Log:
    minute = None
    message = None

    def __init__(self, string):
        match = re.search('\[\d\d\d\d-\d\d-\d\d \d\d:(\d\d)\] (.*)', string)
        self.minute = int(match.group(1))
        self.message = match.group(2)


def fillGuardSleepHistory(sleepHistory, guardId, asleepMinute, awakeMinute):
    minutes = sleepHistory.get(guardId, [0]*60)
    for min in range(asleepMinute, awakeMinute):
        minutes[min] += 1
    sleepHistory[guardId] = minutes


def buildHistory(input):
    input = input.readlines()
    input.sort()
    logs = [Log(i) for i in input]
    sleepHistory = {}
    asleepMinute = None
    currentGuard = None
    for log in logs:
        if log.message == "falls asleep":
            asleepMinute = log.minute
        elif log.message == "wakes up":
            fillGuardSleepHistory(sleepHistory, currentGuard, asleepMinute, log.minute)
        else:
            currentGuard = re.search('Guard #(\d+) begins shift', log.message).group(1)
    return sleepHistory


def part1(input):
    sleepHistory = buildHistory(input)

    guardId = max(sleepHistory, key=lambda guardId: sum(sleepHistory[guardId]))
    maxAsleep = max(sleepHistory[guardId])
    maxAsleepMinute = sleepHistory[guardId].index(maxAsleep)
    print (int(guardId) * int(maxAsleepMinute))


def part2(input):
    sleepHistory = buildHistory(input)

    guardId = max(sleepHistory, key=lambda guardId: max(sleepHistory[guardId]))
    maxAsleep = max(sleepHistory[guardId])
    maxAsleepMinute = sleepHistory[guardId].index(maxAsleep)
    print (int(guardId) * int(maxAsleepMinute))


part2(utils.input.getInput())

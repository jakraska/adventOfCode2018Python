#!/usr/bin/python3

import utils.input

def fillDict(str):
    counts = {}
    for char in str:
        counts[char] = counts.get(char, 0) + 1
    return counts


def part1(input):
    containsTwo = 0
    containsThree = 0
    for row in input:
        counts = fillDict(row)
        containsTwo = containsTwo + 1 if (2 in counts.values()) else containsTwo
        containsThree = containsThree + 1 if (3 in counts.values()) else containsThree
    print(containsTwo * containsThree)
    return

def withinTwo(strA, strB):
    diff = 0
    for charA, charB in zip(strA, strB):
        if charA != charB:
            diff = diff+1
            if diff > 2:
                return False
    return True

def getMatching(strA, strB):
    matching = ""
    for charA, charB in zip(strA, strB):
        if charA == charB:
            matching = matching + charA
    return matching

def part2(input):
    for i, rowA in enumerate(input):
        for j in range(i+1, len(input)):
            if(withinTwo(rowA, input[j])):
                print(getMatching(rowA, input[j]))
                return



part2(utils.input.getInput())
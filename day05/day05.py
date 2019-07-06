#!/usr/bin/python3

import utils.input

def reacts(a, b):
    return abs(ord(a) - ord(b)) == 32


def reactFinalSize(input, ignore = None):
    final = []
    for char in input:
        if ignore is not None and char.lower() == ignore:
            pass
        elif len(final) > 0 and reacts(char, final[len(final) - 1]):
            final.pop()
        else:
            final.append(char)
    return len(final)


def part1(input):
    print(reactFinalSize(input))

def part2(input):
    letters = [char for char in "abcdefghijklmnopqrstuvwxyz"]
    minimumLetter = min(letters, key= lambda c: reactFinalSize(input, c))
    print(reactFinalSize(input, minimumLetter))




part2(utils.input.getInput().readlines()[0])
#!/usr/bin/python3

import itertools
import utils.input


def part1(input):
    val = 0
    for i in input:
        val += i

    print (val)


def part2(input):

    vals = {}
    val = 0
    for i in itertools.cycle(input):
        val += i
        if (vals.has_key(val)):
            print val
            break
        else:
            vals[val] = True


# part1(utils.input.getInputAsInts())
part2(utils.input.getInputAsInts())
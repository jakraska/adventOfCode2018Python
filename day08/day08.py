#!/usr/bin/python3

import utils.input
from collections import deque
class Node:

    def __init__(self, num_children, num_metadata):
        self.num_children = num_children
        self.num_metadata = num_metadata
        self.metadata = []
        self.children = []

    def sum_all_metadata(self):
        return sum(self.metadata) + sum(node.sum_all_metadata() for node in self.children if node)

    def get_value(self):
        if len(self.children) == 0:
            return sum(self.metadata)

        v = 0
        for idx in self.metadata:
            if 1 <= idx <= len(self.children):
                v += self.children[idx - 1].get_value()
        return v


def processInput(input):
    stack = []

    data = [int(i) for i in input.readline().split()]
    queue = deque(data)

    stack.append(Node(queue.popleft(), queue.popleft()))

    while len(queue) > 0:

        curNode = stack.pop()

        if curNode.num_children > len(curNode.children):
            # start a new child node
            child = Node(queue.popleft(), queue.popleft())
            curNode.children.append(child)
            stack.append(curNode)
            stack.append(child)  # child becomes current
        elif curNode.num_metadata > len(curNode.metadata):
            # add metadata
            curNode.metadata.append(queue.popleft())
            stack.append(curNode)

    return stack.pop()

def part1(input):

    root = processInput(input)
    print(root.sum_all_metadata())


def part2(input):
    root = processInput(input)
    print(root.get_value())

part2(utils.input.getInput())
#!/usr/bin/python3

import utils.input
from collections import deque


def findMaxScore(numPlayers, numMarbles):

    game = deque([0])
    players = deque(range(numPlayers))
    playerScores = [0] * numPlayers

    for m in range(1, numMarbles + 1):
        currPlayer = players.popleft()

        if m % 23 == 0 :
            game.rotate(-7)
            playerScores[currPlayer] += m + game.popleft()
            game.rotate(1)

        else:
            game.rotate(1)
            game.appendleft(m)

        players.append(currPlayer)



    return max(playerScores)


def part1():
    print(findMaxScore(477, 70851))

def part2():
    print(findMaxScore(477, 70851 * 100))

part2()
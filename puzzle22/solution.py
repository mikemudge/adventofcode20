from collections import deque
import itertools


def playGame(myCards, otherCards):
    round = 1
    while True:
        print("Round %d" % round)
        print(list(myCards))
        print(list(otherCards))
        a = myCards.popleft()
        b = otherCards.popleft()
        print("Player 1 plays %d" % a)
        print("Player 2 plays %d" % b)
        if a > b:
            # winners card first.
            myCards.append(a)
            myCards.append(b)
            print("Player 1 wins")
        else:
            # winners card first.
            otherCards.append(b)
            otherCards.append(a)
            print("Player 2 wins")
        if len(myCards) == 0 or len(otherCards) == 0:
            break

        round += 1


def part1():
    with open('input') as f:
        lines = f.readlines()
        lines = [l.rstrip() for l in lines]


        myCards = deque()
        otherCards = deque()

        cards = myCards
        for line in lines:
            print(line)
            if len(line) == 0:
                cards = otherCards
                continue
            if line[0:7] == "Player ":
                continue
            cards.append(int(line))

        playGame(myCards, otherCards)

        print(list(myCards))
        print(list(otherCards))

        total = 0
        print("Player 1")
        multiplier = len(otherCards) + len(myCards)
        for v in myCards:
            print(v, multiplier)
            total += multiplier * v
            multiplier -= 1
        print("Player 2")
        for v in otherCards:
            print(v, multiplier)
            total += multiplier * v
            multiplier -= 1

        print("Part 1:", total)


def playRecursiveGame(game, myCards, otherCards):
    round = 1
    print("=== Game %d ===" % game)
    subgame = game + 1
    visited = {}
    while True:

        print("Round %d  (Game %d) " % (round, game))
        print(list(myCards))
        print(list(otherCards))

        key = "-".join(map(str, list(myCards))) + ":" + "-".join(map(str, list(otherCards)))
        if key in visited:
            print("Already seen %s" % key)
            # take all the cards from player 2, so player 1 wins.
            while len(otherCards) > 0:
                myCards.append(otherCards.popleft())
            break
        visited[key] = True
        a = myCards.popleft()
        b = otherCards.popleft()
        print("Player 1 plays %d" % a)
        print("Player 2 plays %d" % b)
        if len(myCards) >= a and len(otherCards) >= b:
            print("Playing a sub-game to determine the winner...")
            cardsA = deque(itertools.islice(myCards, 0, a))
            cardsB = deque(itertools.islice(otherCards, 0, b))
            subgame = playRecursiveGame(subgame, cardsA, cardsB) + 1
            print("...anyway, back to game %d." % game)
            if len(cardsB) == 0:
                winner = 1
            else:
                winner = 2
        else:
            if a > b:
                winner = 1
            else:
                winner = 2

        if winner == 1:
            # winners card first.
            myCards.append(a)
            myCards.append(b)
            print("Player 1 wins")
        else:
            # winners card first.
            otherCards.append(b)
            otherCards.append(a)
            print("Player 2 wins")

        if len(myCards) == 0 or len(otherCards) == 0:
            break

        round += 1

    return subgame - 1

def part2():
    with open('input') as f:
        lines = f.readlines()
        lines = [l.rstrip() for l in lines]


        myCards = deque()
        otherCards = deque()

        cards = myCards
        for line in lines:
            print(line)
            if len(line) == 0:
                cards = otherCards
                continue
            if line[0:7] == "Player ":
                continue
            cards.append(int(line))

        game = 1
        playRecursiveGame(game, myCards, otherCards)

        print(list(myCards))
        print(list(otherCards))

        total = 0
        print("Player 1")
        multiplier = len(otherCards) + len(myCards)
        for v in myCards:
            print(v, multiplier)
            total += multiplier * v
            multiplier -= 1
        print("Player 2")
        for v in otherCards:
            print(v, multiplier)
            total += multiplier * v
            multiplier -= 1

        # Played 14052 games, Game 1 had a total of 793 rounds.
        print("Part 2:", total)


part1()
part2()

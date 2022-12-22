#! /usr/bin/env python
move_scores = {'X': 1, 'Y': 2, 'Z': 3}
win_map = {'A': 'Y', 'B': 'Z', 'C': 'X'}
draw_map = {'A': 'X', 'B': 'Y', 'C': 'Z'}
loss_map = {'A': 'Z', 'B': 'X', 'C': 'Y'}


def outcome(a, b):
    if (a == 'A' and b == 'X') or (a == 'B' and b == 'Y') or (a == 'C' and b == 'Z'):
        return 3
    if a == 'A':
        return 6 if b == 'Y' else 0
    elif a == 'B':
        return 6 if b == 'Z' else 0
    elif a == 'C':
        return 6 if b == 'X' else 0


def get_move(a, result):
    if result == 'X':
        return loss_map[a]
    elif result == 'Y':
        return draw_map[a]
    elif result == 'Z':
        return win_map[a]


def part1():
    with open('input.txt', 'r') as f:
        total_score = 0
        for line in f:
            [a, b] = line.split()
            total_score += outcome(a, b) + move_scores[b]
        print(total_score)


def part2():
    with open('input.txt', 'r') as f:
        total_score = 0
        for line in f:
            [a, result] = line.split()
            b = get_move(a, result)
            total_score += outcome(a, b) + move_scores[b]
        print(total_score)


if __name__ == '__main__':
    part2()

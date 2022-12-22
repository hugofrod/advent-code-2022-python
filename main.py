#! /usr/bin/env python
def get_priority(c):
    offset = 96 if c.islower() else 38
    return ord(c) - offset


def part1():
    with open('input.txt', 'r') as f:
        duplicate_priorities = []
        for line in f:
            line = line.strip('\n')
            middle_index = len(line) // 2
            first = line[:middle_index]
            second = line[middle_index:]
            for c in list(set(first)):
                if c in second:
                    duplicate_priorities.append(get_priority(c))
        print(sum(duplicate_priorities))


def part2():
    # TODO: INCOMPLETE SOLUTION
    with open('input.txt', 'r') as f:
        priorities = 0
        while True:
            l1 = f.readline()
            l2 = f.readline()
            l3 = f.readline()
            if not l1 or not l2 or not l3:
                break

            for c in ['a', 'b']:
                if c in l1 and c in l2 and c in l3:
                    priorities += get_priority(c)
                break

        print(sum(priorities))


if __name__ == '__main__':
    part1()

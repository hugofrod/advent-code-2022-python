#! /usr/bin/env python
def part1():
    highest_calories = 0
    current_calories = 0

    with open('./input.txt', 'r') as f:
        for line in f:
            if line == '\n':
                if current_calories > highest_calories:
                    highest_calories = current_calories
                current_calories = 0
            else:
                current_calories += int(line)
        print(highest_calories)


def part2():
    highest_calories = 0
    second_highest_calories = 0
    third_highest_calories = 0
    current_calories = 0

    with open('./input.txt', 'r') as f:
        for line in f:
            if line == '\n':
                if current_calories > highest_calories:
                    third_highest_calories = second_highest_calories
                    second_highest_calories = highest_calories
                    highest_calories = current_calories
                elif current_calories > second_highest_calories:
                    third_highest_calories = second_highest_calories
                    second_highest_calories = current_calories
                elif current_calories > third_highest_calories:
                    third_highest_calories = current_calories
                current_calories = 0
            else:
                current_calories += int(line)
        print(highest_calories + second_highest_calories + third_highest_calories)


if __name__ == '__main__':
    part2()

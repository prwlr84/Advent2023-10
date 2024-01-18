from input import input_string


grid = [list(line) for line in input_string.split('\n')]


def find_next_part(letter, direction, coordinates):
    print(len(coordinates), coordinates)
    r, c = coordinates
    legend = {
        'F': { 'left': [r + 1, c, 'down'], 'up': [r, c + 1, 'right']},
        '|': { 'up': [r - 1, c, 'up'], 'down': [r + 1, c, 'down']},
        'L': { 'left': [r - 1, c, 'up'], 'down': [r, c + 1, 'right']},
        '-': { 'right': [r, c + 1, 'right'], 'left': [r, c - 1, 'left']},
        'J': { 'right': [r - 1, c, 'up'], 'down': [r, c - 1, 'left']},
        '7': { 'right': [r + 1, c, 'down'], 'up': [r - 1, c, 'left']}
    }

    return legend[letter][direction]


def return_letter(r, c):
    return grid[r][c]


def find_first_part(start):
    r, c = start
    if grid[r + 1][c] in '|JL': return [grid[r + 1][c], [r + 1, c], 'down']
    if grid[r - 1][c] in '|F7': return [grid[r - 1][c], [r - 1, c], 'up']
    if grid[r][c + 1] in '-J7': return [grid[r + 1][c], [r + 1, c], 'right']
    if grid[r][c - 1] in '-FL': return [grid[r + 1][c], [r + 1, c], 'left']


def find_start_coordinates(lists):
    coordinates = None
    for r, sublist in enumerate(lists):
        for c, s in enumerate(sublist):
            if s == 'S':
                coordinates = [r, c]

    return coordinates


def get_furthest_point():
    start = find_start_coordinates(grid)
    letter, current, direction = find_first_part(start)
    print(letter, current, direction)
    steps = 0

    while current != start or steps < 16:
        r, c, direction = find_next_part(letter, direction, current)
        letter = return_letter(r, c)
        current = [r, c]
        steps += 1

    print(start, current, steps, 'XXXXXXXXXXXXXXXXXXXX')


if __name__ == '__main__':
    get_furthest_point()

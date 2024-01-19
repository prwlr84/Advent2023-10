from input import input_string


grid = [list(line) for line in input_string.split('\n')]


def find_next_tube(current_letter, input_direction, current_coordinates):
    r, c = current_coordinates
    if current_letter == 'S': return [r, c, 'Finish']
    legend = {
        'F': { 'left': [r + 1, c, 'down'], 'up': [r, c + 1, 'right']},
        '|': { 'up': [r - 1, c, 'up'], 'down': [r + 1, c, 'down']},
        'L': { 'left': [r - 1, c, 'up'], 'down': [r, c + 1, 'right']},
        '-': { 'right': [r, c + 1, 'right'], 'left': [r, c - 1, 'left']},
        'J': { 'right': [r - 1, c, 'up'], 'down': [r, c - 1, 'left']},
        '7': { 'right': [r + 1, c, 'down'], 'up': [r, c - 1, 'left']},
    }

    return legend[current_letter][input_direction]


def return_type(r, c):
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
    tube_type, current, direction = find_first_part(start)
    print(tube_type, current, direction)
    steps = 0

    while current != start or steps < 16:
        r, c, direction = find_next_tube(tube_type, direction, current)
        tube_type = return_type(r, c)
        current = [r, c]
        steps += 1

    print(round(steps/2))


if __name__ == '__main__':
    get_furthest_point()

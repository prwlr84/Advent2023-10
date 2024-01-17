from input import input_string


def parse_input(string):
    return [line.split() for line in string.split('\n')]


directions = {
    'F': [],
    '|': [],
    'L': [],
    '-': [],
    'J': [],
    '7': []
}


def get_furthest_point(string):
    print(parse_input(string))


if __name__ == '__main__':
    get_furthest_point(input_string)

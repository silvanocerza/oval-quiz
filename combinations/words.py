from itertools import product

def read_file(path):
    with open(path) as f:
        lines = [l.strip() for l in f.readlines()]

    current_test = 1
    try:
        total_tests = int(lines[0])
    except ValueError:
        raise ValueError('First line must contain the number of tests')
    test_cases = []

    current_line = 1
    while current_test <= total_tests:
        try:
            words_count = int(lines[current_line].split(' ')[0])
        except ValueError:
            raise ValueError(f' line {current_line} must contain the number of words for current test')
        from_line = current_line + 1
        to_line = from_line + words_count
        test_cases.append(lines[from_line:to_line])

        current_line = to_line

        current_test += 1

    return test_cases


def combinations(tests):
    for i, test in enumerate(tests):
        columns_count = len(test[0])
        if columns_count == 1:
            print(f'Case #{i+1}: -')
            continue

        columns = [set() for i in range(columns_count)]
        for word in test:
            for n, c in enumerate(word):
                columns[n].add(c)

        for w in product(*columns):
            word = ''.join(w)
            if not word in test:
                print(f'Case #{i+1}: {word}')
                break
        else:
            print(f'Case #{i+1}: -')


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: \n$ python words.py <path_to_file>")
        quit()
    tests = read_file(sys.argv[1])
    combinations(tests)


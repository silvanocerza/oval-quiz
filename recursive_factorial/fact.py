def fact(n: int):
    if n == 1:
        return n
    return n * fact(n - 1)


if __name__ == "__main__":
    import sys

    try:
        n = int(sys.argv[1])
    except (ValueError, IndexError):
        print("Usage: \n$ python fact.py <integer_number>")
        quit()

    print(fact(n))
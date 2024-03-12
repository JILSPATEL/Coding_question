def main():
    n = int(input("Enter The Number: "))

    c = 'R'
    x, y = 0, 0
    distance = 10

    while n > 0:
        if c == 'R':
            x += distance
            distance += 10
            c = 'U'
        elif c == 'U':
            y += distance
            distance += 10
            c = 'L'
        elif c == 'L':
            x -= distance
            distance += 10
            c = 'D'
        elif c == 'D':
            y -= distance
            distance += 10
            c = 'R'

        n -= 1

    print("Final position: ({}, {})".format(x, y))


if __name__ == "__main__":
    main()

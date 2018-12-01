def main():
    previous = set()
    value = 0
    previous.add(value)
    while True:
        with open('1.input') as f:
            for line in f:
                value += int(line)
                if value in previous:
                    print(value)
                    return
                previous.add(value)

main()

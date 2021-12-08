def main() -> None:
    with open("8_input.txt", "r") as f:
        result = 0
        for line in f.readlines():
            strings = line.split(" | ")
            output = strings[1].strip().split(" ")
            for out in output:
                if len(out) in (2, 4, 3, 7):
                    result += 1
        print(result)


if __name__ == "__main__":
    main()

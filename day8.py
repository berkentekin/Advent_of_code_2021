def main() -> None:
    with open("8_input.txt", "r") as f:
        result = 0
        for line in filter(lambda x: x != '\n', f.readlines()):
            for out in line.split(" | ")[1].strip().split(" "):
                result += 1 if len(out) in (2, 3, 4, 7) else 0
    print(result)


if __name__ == "__main__":
    main()

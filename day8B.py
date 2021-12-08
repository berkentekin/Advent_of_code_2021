def main() -> None:
    with open("8_input.txt", "r") as f:
        result = 0
        for line in f.readlines():
            if line == "\n":
                continue
            decodedict_str = {}
            decodedict_num = {}
            strings = line.split(" | ")
            input = strings[0].strip().split(" ")
            output = strings[1].strip().split(" ")
            outnum = []
            for istr in sorted(input, key=len):
                sorted_istr = "".join(sorted(istr))
                if len(istr) == 2:
                    decodedict_str[sorted_istr] = 1
                    decodedict_num[1] = set(istr)
                elif len(istr) == 3:
                    decodedict_str[sorted_istr] = 7
                    decodedict_num[7] = set(istr)
                elif len(istr) == 4:
                    decodedict_str[sorted_istr] = 4
                    decodedict_num[4] = set(istr)
                elif len(istr) == 5:
                    commons = decodedict_num[1].intersection(set(istr))
                    if len(commons) == 2:
                        decodedict_str[sorted_istr] = 3
                        decodedict_num[3] = set(istr)
                    else:
                        commons = decodedict_num[4].intersection(set(istr))
                        if len(commons) == 2:
                            decodedict_str[sorted_istr] = 2
                            decodedict_num[2] = set(istr)
                        elif len(commons) == 3:
                            decodedict_str[sorted_istr] = 5
                            decodedict_num[5] = set(istr)
                elif len(istr) == 6:
                    commons = decodedict_num[4].intersection(set(istr))
                    if len(commons) == 4:
                        decodedict_str[sorted_istr] = 9
                        decodedict_num[9] = set(istr)
                    else:
                        commons = decodedict_num[1].intersection(set(istr))
                        if len(commons) == 1:
                            decodedict_str[sorted_istr] = 6
                            decodedict_num[6] = set(istr)
                        elif len(commons) == 2:
                            decodedict_str[sorted_istr] = 0
                            decodedict_num[0] = set(istr)
                elif len(istr) == 7:
                    decodedict_str[sorted_istr] = 8
                    decodedict_num[8] = set(istr)
            for out in output:
                sorted_out = "".join(sorted(out))
                outnum.append(decodedict_str[sorted_out])
            currentNum = int("".join([str(x) for x in outnum]))
            result += currentNum
        print(result)


if __name__ == "__main__":
    main()

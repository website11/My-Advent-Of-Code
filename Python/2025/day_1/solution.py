# Part 1 Solution
if __name__ == "__main__":
    start = 50
    zero_count = 0
    with open("input.txt", "r") as f:
        items = f.read().splitlines()
        for item in items:
            if item[0] == "L":
                start -= int(item[1:])
                start = start % 100
                if start < 0:
                    start = 100 + start
                if start == 0:
                    zero_count += 1
            elif item[0] == "R":
                start += int(item[1:])
                start = start % 100
                if start > 99:
                    start = start + 100
                if start == 0:
                    zero_count += 1
            else:
                print(item)
    print(zero_count)


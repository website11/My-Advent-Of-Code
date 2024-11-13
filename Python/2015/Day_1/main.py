

def part_one(input_txt):
    up_count = input_txt.count("(")
    down_count = input_txt.count(")")
    return up_count - down_count

def part_two(input_txt):
    floor = 0
    for index, item in enumerate(input_txt):
        if item == "(":
            floor += 1
        else:
            floor -= 1

        if floor == -1:
            return index + 1

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_txt = f.read()
        results_1 = part_one(input_txt)
        print(results_1)
        results_2 = part_two(input_txt)
        print(results_2)
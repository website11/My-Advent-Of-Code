
def get_sur_area(l,w,h):
    surface_area = 2 * l * w + 2 * w * h + 2 * h * l
    return surface_area

def get_smallest_area(l,w,h):
    smallest = min([l*w, w*h, h*l])
    return smallest

def part_one(input_txt):
    total = 0
    to_add = input_txt.split("\n")
    for area in to_add:
        dim = area.split("x")
        l = int(dim[0])
        w = int(dim[1])
        h = int(dim[2])

        total += get_sur_area(l,w,h) + get_smallest_area(l,w,h)
    return total

def part_two(input_txt):
    total = 0
    to_add = input_txt.split("\n")
    for area in to_add:
        dim = area.split("x")
        l = int(dim[0])
        w = int(dim[1])
        h = int(dim[2])

        two_smallest = sorted([l,w,h])[:2]
        total += two_smallest[0] * 2 + two_smallest[1] * 2 + l * w * h
    return total

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_txt = f.read()
        results_1 = part_one(input_txt)
        print(results_1)
        results_2 = part_two(input_txt)
        print(results_2)

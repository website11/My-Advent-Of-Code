import re


# Part 1
def extract_calibration_values(line):
    # Use 're' to extract numbers
    numbers = re.findall(r'\d',line)
    if len(numbers) == 1:
        value = int(str(numbers[0]) + str(numbers[0]))
        return value
    else:
        value = int(str(numbers[0]) + str(numbers[-1]))
        return value


if __name__ == '__main__':
    total = 0
    input_text = "input-1.txt"
    with open('input-1.txt','r') as f:
        for line in f:
            total += extract_calibration_values(line)
    print(total)
def read_data(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]
  

def process_data(data):
    joltage = 0
    for line in data:
        largest = find_largest(line)
        joltage += int(largest)
    return joltage


def find_largest(line): # Possible to make viable for any number length by adding a parameter for the length I guess.
    number = []
    to_remove = len(line) - 12
    for char in line:
        while number and to_remove > 0 and number[-1] < char:
            number.pop()
            to_remove -= 1
        number.append(char)
    return ''.join(number[:12])


data = read_data('DAY_3/data.txt')
result = process_data(data)
print(result)
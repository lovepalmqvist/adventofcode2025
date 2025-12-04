def read_data(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]


def process_data(data):
    joltage = 0
    for line in data:
        second_largest = 0
        largest = 0
        for i in range(len(line)):
            char = line[i]
            if int(char) > largest:
                if i == len(line) - 1:
                    second_largest = int(char)
                else:
                    largest = int(char)
                    second_largest = 0
            elif int(char) > second_largest:
                second_largest = int(char)
        joltage += int(str(largest) + str(second_largest))
    return joltage


data = read_data('DAY_3/data.txt')
result = process_data(data)
print(result)
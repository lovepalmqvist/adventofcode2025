start = 50
size = 100

def read_data(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]

def process_data(data):
    num = start
    tot = 0
    for line in data:
        if line.startswith('L'):
            num = (num - int(line[1:])) % size
            if num == 0:
                tot += 1
        elif line.startswith('R'):
            num = (num + int(line[1:])) % size
            if num == 0:
                tot += 1
    return tot

data = read_data('data.txt')
result = process_data(data)
print(f"Final result: {result}")
start = 50
size = 100

def read_data(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]

def process_data(data):
    pos = start
    tot = 0
    for line in data:
        num = pos
      
        if line.startswith('L'):
            pos -= int(line[1:])
            passes = (num - 1) // size - (pos - 1) // size
          
        elif line.startswith('R'):
            pos += int(line[1:])
            passes = pos // size - num // size
            
        tot += passes
            
    return tot

data = read_data('data.txt')
result = process_data(data)
print(f"Final result: {result}")
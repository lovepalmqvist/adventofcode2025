def read_data(file_path):
    with open(file_path, 'r') as file:
        data = []
        for line in file:
            data.extend(line.strip().split(","))
        return data
      
      
def process_data(data):
    invalid = 0
    for entry in data:
        entry1, entry2 = entry.split("-")
        entry1_int, entry2_int = int(entry1), int(entry2)
        for i in range(entry1_int, entry2_int + 1):
            i_str = str(i)
            first, second = i_str[:len(i_str) // 2], i_str[len(i_str) // 2:]
            if first == second:
                invalid += i
    return invalid
  
  
data = read_data('DAY_2/data.txt')
result = process_data(data)
print(result)
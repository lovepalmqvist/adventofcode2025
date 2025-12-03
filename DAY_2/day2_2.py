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
            for j in range(1, len(i_str) // 2 + 1):
                if i_str[:j] * (len(i_str) // j) == i_str:
                    invalid += i
                    break
    return invalid
  
  
data = read_data('data.txt')
result = process_data(data)
print(result)
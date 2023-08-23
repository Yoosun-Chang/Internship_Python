def split_input(input_data):
    index = {}
    for line in input_data:
        for i in range(len(line)):
            for j in range(i + 1, len(line) + 1):
                substring = line[i:j]
                
                if substring not in index:
                    index[substring] = []
                index[substring].append(line)
    return index

def search(input_lines):
    search_target = input_lines[0]
    index = split_input(input_lines[1:])

    found_strings = set()
    if search_target in index:
        found_strings.update(index[search_target])

    return found_strings

input_data = []
while True:
    line = input("")
    if not line:
        break
    input_data.append(line)

search_results = search(input_data)
with open("output.txt", "w") as output_file:
    for result in search_results:
        output_file.write(result + "\n")

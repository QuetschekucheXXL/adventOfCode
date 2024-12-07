# Get the Input out of input6.txt
file_path = "input6.txt"
with open(file_path, "r") as file:
    puzzle_input = file.read().split("\n")
    #print("Printing the puzzle Input:")
    #print(puzzle_input)

    input = []
    for line in puzzle_input:
        #print("NEW LINE")
        #print(list(line))
        input.append(list(line))


# For the test I use the test data from the webpage
test_input = [
    ["....#....."],
    [".........#"],
    [".........."],
    ["..#......."],
    [".......#.."],
    [".........."],
    [".#..^....."],
    ["........#."],
    ["#........."],
    ["......#..."]
]

def turn_input_to_grid(input_list):
    input_to_grid = []
    for line in input_list:
        input_to_grid.append(list(line[0]))
    return input_to_grid

test_grid = turn_input_to_grid(test_input)
#grid = turn_input_to_grid(input)
print(f"Printing Grid:")
for line in test_grid:
    print(line)
for line in input:
    print(line)
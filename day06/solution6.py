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

# Printing the grids work. They are now a list of lists.
# each list consists of the characters as single entries in the list
#grid = turn_input_to_grid(input)
print(f"Printing Test-Grid:")
for line in test_grid:
    print(line)
#print(f"Printing Grid:")
#for line in input:
#    print(line)

def finding_starting_position(map_to_check):
    for line in map_to_check:
        if '^' in line:
            column = line.index('^')
            row = map_to_check.index(line)
    return [row, column]

def check_direction(guard_direction):
    # checks the direction the guard is currently facing in order to calculate the new position later
    if guard_direction == '^':
        return [-1,0]
    if guard_direction == '>':
        return [0,1]
    if guard_direction == 'v':
        return [1,0]
    if guard_direction == '<':
        return [0,-1]

def turn_90_degrees(guard_direction):
    # Turn the guard 90° when hitting an obstacle
    if guard_direction == '^':
        return '>'
    if guard_direction == '>':
        return 'v'
    if guard_direction == 'v':
        return '<'
    if guard_direction == '<':
        return '^'

def calculate_new_position(start, direction):
    result = []
    for i in range(0, len(start)):
        result.append(start[i] + direction[i])
    return result

def check_grid_at_new_position(map_to_check, initial_position, initial_direction):
    current_position = initial_position.copy()
    current_direction = initial_direction
    movement_count = {'^': 0, '>': 0, 'v': 0, '<': 0}

    while True:
        #calculate the next position
        next_position = calculate_new_position(current_position, check_direction(current_direction))

        #checking if next pos is out of bounds
        if next_position[0] < 0 or next_position[0] >= len(map_to_check) or next_position[1] < 0 or next_position[1] >= len(map_to_check[0]):
            print(f"Out of bounds at position {next_position}. Stopping.")
            break

        #chicking the content of the next position
        if map_to_check[next_position[0]][next_position[1]] == '#':
            # Turn 90 degrees clockwise
            current_direction = turn_90_degrees(current_direction)
            print(f"Encountered wall at {next_position}. Turning to {current_direction}.")
            continue

        #moving to the next position
        print(f"Moving to {next_position} in direction {current_direction}.")
        map_to_check[next_position[0]][next_position[1]] = current_direction
        current_position = next_position
        movement_count[current_direction] += 1

        # Print the grid after each move
        for line in map_to_check:
            print("".join(line))
        print()
    
    # Return the movement count
    return movement_count

def sum_moves(movements_dict):
    for line in test_grid:
        print(line)


#print(f"Starting Pos = Row {finding_starting_position(test_grid)[0]} and Column {finding_starting_position(test_grid)[1]}") #--> funktioniert
#print(check_direction(test_grid[6][4])) #--> Funktioniert

# Convert test_input to grid
test_grid = turn_input_to_grid(test_input)

# Find the starting position
start = finding_starting_position(input)
initial_direction = '^'  # The guard starts facing upwards

# Perform the navigation
movement_count = check_grid_at_new_position(input, start, initial_direction)

# Output the movement count
print("Final movement count:", movement_count)

count = 0
for line in input:
    for item in line:
        if item == '>' or item == 'v' or item == '<' or item == "^":
            count += 1
print(count)




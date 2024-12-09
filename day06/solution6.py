# Get the Input out of input6.txt
file_path = "input6.txt"
with open(file_path, "r") as file:
    puzzle_input = file.read().split("\n")
    #print("Printing the puzzle Input:")
    #print(puzzle_input)

    input = []
    for line in puzzle_input:
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
        # calculate the next position
        next_position = calculate_new_position(current_position, check_direction(current_direction))

        # checking if next pos is out of bounds
        if next_position[0] < 0 or next_position[0] >= len(map_to_check) or next_position[1] < 0 or next_position[1] >= len(map_to_check[0]):
            print(f"Out of bounds at position {next_position}. Stopping.")
            break

        # chicking the content of the next position
        if map_to_check[next_position[0]][next_position[1]] == '#':
            # Turn 90 degrees clockwise
            current_direction = turn_90_degrees(current_direction)
            print(f"Encountered wall at {next_position}. Turning to {current_direction}.")
            continue

        # moving to the next position
        print(f"Moving to {next_position} in direction {current_direction}.")
        map_to_check[next_position[0]][next_position[1]] = current_direction
        current_position = next_position
        movement_count[current_direction] += 1

        # Print the grid after each move
        #for line in map_to_check:
        #    print("".join(line))
        #print()
    
    # Return the movement count
    return movement_count

# Convert test_input to grid
test_grid = turn_input_to_grid(test_input)

# Find the starting position
start = finding_starting_position(input)
initial_direction = '^'  # The guard starts facing upwards

# Perform the navigation
movement_count = check_grid_at_new_position(input, start, initial_direction)

# Output the movement count
print("Final movement count:", movement_count)


# PART 1 SOLUTION IS HERE:
count = 0
for line in input:
    for item in line:
        if item == '>' or item == 'v' or item == '<' or item == "^":
            count += 1
print(count)

# PART 2 Functions

def simulate_with_zero(map_to_check, position, direction, test_pos):
    visited = set()
    current_pos = position
    current_direction = direction

    while True:
        # Record the current state (position + direction)
        state = (current_pos[0], current_pos[1], current_direction)
        if state in visited:
            print(f"Cycle detected at state: {state}")
            # Cycle detected
            return True
        visited.add(state)

        # Determine the next position and direction
        direction_vector = check_direction(current_direction)
        next_pos = calculate_new_position(current_pos, direction_vector)

        # Check bounds
        if not (0 <= next_pos[0] < len(map_to_check) and 0 <= next_pos[1] < len(map_to_check[0])):
            break  # Out of bounds, no cycle here

        # Check the next position
        if next_pos == test_pos:
            next_tile = '0'  # Pretend the test position has a '0'
        else:
            next_tile = map_to_check[next_pos[0]][next_pos[1]]

        if next_tile == '#':
            current_direction = turn_90_degrees(current_direction)  # Turn 90 degrees clockwise
        else:
            current_pos = next_pos  # Move forward

    return False


def find_all_cycle_positions(map_to_check, start_pos, start_direction):
    potential_positions = set()

    for row in range(len(map_to_check)):
        for col in range(len(map_to_check[0])):
            # Skip positions that are walls or already part of the map
            if map_to_check[row][col] != '.':
                continue

            # Simulate placing a '0' at this position
            if simulate_with_zero(map_to_check, start_pos, start_direction, (row, col)):
                potential_positions.add((row, col))

    return potential_positions

# Part 2 MAIN
# Initialize the map and starting position
test_grid = turn_input_to_grid(test_input)
start_pos = finding_starting_position(test_grid)
start_direction = '^'

# Find all positions that lead to infinite cycles
cycle_positions = find_all_cycle_positions(test_grid, start_pos, start_direction)

# Output the result
print(f"Total positions where '0' creates a cycle: {len(cycle_positions)}")
print("Positions:", cycle_positions)

print(test_grid)


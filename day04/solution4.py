
# 1. GETTING PUZZLE INPUT + CONSTRUCTING A MATRIX + SETTING A PATTERN TO FIND
file_path ="input4.txt"
with open(file_path, "r") as file:
    puzzle_input = file.read()

input_matrix = [list(row) for row in puzzle_input.split('\n')]

pattern_to_find = "MAS"


# 2. FUNCTION TO COUNT THE OCCURENCES OF THE PATTERN
#   Takes:
#       1) the input matrix that consists of a list of lines of the input where each line is a list of characters in that line
#       2) The word we are looking for in the puzzle_input
#   Returns:
#       The number of times the pattern was found
def count_occurences_pattern(input_matrix, pattern_to_find):
    rows = len(input_matrix)
    cols = len(input_matrix[0])
    pattern_length  = len(pattern_to_find)
    count = 0

    # Setting up the directions we need to check in for each character in the matrix
    directions_to_check = [
        (0, 1),     # Nach rechts gehen
        (0, -1),    # Nach links gehen
        (1, 0),     # Nach unten gehen
        (-1, 0),    # Nach oben gehen
        (1, 1),     # Nach rechts-unten gehen
        (1, -1),    # Nach links-unten gehen
        (-1, 1),    # Nach rechts-oben gehen
        (-1, -1),   # Nach links-oben gehen
    ]

    # HELPER: Checks whether the parttern exists in the different directions
    def check_direction(row, column, direction_row_step, direction_column_step):
        for i in range(pattern_length):
            new_row_index, new_column_index = row + direction_row_step * i, column + direction_column_step * i
            if not (0 <= new_row_index < rows and 0 <= new_column_index < cols) or input_matrix[new_row_index][new_column_index] != pattern_to_find[i]:
                return False
        return True

    # HELPER: Do this for each cell of the matrix
    for row in range(rows):
        for col in range(cols):
            for direction_row_step, direction_column_step in directions_to_check:
                if check_direction(row, col, direction_row_step, direction_column_step):
                    count += 1

    return count

# PART 2 HERE
#   Takes:
#       1) the input matrix that consists of a list of lines of the input where each line is a list of characters in that line
#       2) The word we are looking for in the puzzle_input
#   Returns:
#       The number of times the X-MAS pattern was found
def count_occurences_pattern_in_x_shape(input_matrix, pattern_to_find):
    rows = len(input_matrix)
    cols = len(input_matrix[0])
    count = 0

    # Directions for PART 2 
    directions_to_check_Xshape = [
        (1, 1),     # Nach unten-rechts gehen
        (1, -1),    # Nach unten-link gehen
        (-1, 1),    # Nach oben-rechts gehen
        (-1, -1),   # Nach oben-links gehen
    ]

    # PART 2 - HELPER: Checks whether the X-MAS pattern exists in the X-Form
    def check_x_shape(row, col):
        print(f"Checking center A at ({row}, {col})")
        # Check diagonals
        # Bottom-right (1,1) and top-left (-1,-1)
        # Bottom-left (1,-1) and top-right (-1,1)
        
        # Check positions for "M" and "S" in diagonals
        # We'll check two pairs of diagonals:
        # - (bottom-right, top-left)
        # - (bottom-left, top-right)

        positions = [
            (row + 1, col + 1),    # Bottom-right
            (row - 1, col - 1),    # Top-left
            (row + 1, col - 1),    # Bottom-left
            (row - 1, col + 1),    # Top-right
        ]
        
        # Ensure the positions are within bounds
        if all(0 <= r < rows and 0 <= c < cols for r, c in positions):
            chars = [input_matrix[r][c] for r, c in positions]
            print(f"Found chars: {chars}")
            
            # Check for valid 'X' shape: two diagonals with "M" and "S" in either order
            if (
                ((chars[0] == 'M' and chars[1] == 'S') or (chars[0] == 'S' and chars[1] == 'M')) and
                ((chars[2] == 'M' and chars[3] == 'S') or (chars[2] == 'S' and chars[3] == 'M'))
                ):
                return True
        return False

    # Loop through the entire grid and check for the "A"s and then the X-MAS pattern
    for row in range(1, rows - 1):  # Start from 1 to avoid edge issues
        for col in range(1, cols - 1):  # Start from 1 to avoid edge issues
            if input_matrix[row][col] == 'A':  # Check only the "A"s
                if check_x_shape(row, col):
                    count += 1
    return count

# END --> GETTING THE COUNT
#result = count_occurences_pattern(input_matrix, pattern_to_find)
result2 = count_occurences_pattern_in_x_shape(input_matrix, pattern_to_find)
print(result2)




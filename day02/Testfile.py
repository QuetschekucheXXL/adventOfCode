test = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9]
]


# the actual function doing the counting by using the other 3 helpers
def count_of_safe_reports(list_of_reports):
    number_of_safe_reports = 0
    not_safe = 0
    for item in list_of_reports:
        if is_safe(item):
            number_of_safe_reports += 1
        else:
            not_safe += 1
    print(f"Not safe: {not_safe}")
    return number_of_safe_reports

# helper to check whether it is strictly increasing
def is_strictly_increasing(numbers):
    if all(x < y for x, y in zip(numbers, numbers[1:])):
        return True

# helper to check whether it is strictly decreasing
def is_strictly_decreasing(numbers):
    if all(x > y for x, y in zip(numbers, numbers[1:])):
        return True
    
# helper that determines whether the distances are fine
def is_distance_ok(numbers):
    check = 0
    for i in range(0, len(numbers) - 1):
        # for each number beginning with the first check if the absulote value of the differnece between it and the next number is between the specified thresholds
        if (abs(numbers[i] - numbers[i+1]) >= 1) and (abs(numbers[i] - numbers[i+1]) <= 3):
            check += 1
    # if the check was successfull for each pair of numbers it will be as high as the length of the list -1
    return (check == len(numbers)-1)

def is_safe(numbers):
    # use helper 1 and 2 in step one to determine if the list of numbers is sorted or not
    if is_strictly_increasing(numbers) or is_strictly_decreasing(numbers):
        # if it is sorted use helper 3 to check if the distance is actually valid among all indices
        if is_distance_ok(numbers):
            return True
    return False



# get the input 
file_path = "input2_a.txt"

list_of_reports = []

with open (file_path, "r") as file:
    for line in file:
        # Opening the input file, extracting the lines as a list for each line and storinng those lists of ints in a report list
        numbers = [int(num) for num in line.strip().split()]
        list_of_reports.append(numbers)

safe_reports = count_of_safe_reports(list_of_reports)
print(f"Safe: {safe_reports}")
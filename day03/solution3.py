# The Idea I have would be to:
# 1. get all mul(*,*) instances and safe them in a list
# 2. iterate over the list and see if there are even more to filter out
# 3. Sum up the multiplications for the valid list

import re

# INSERT HERE PART 1
pattern = r"\bmul\((-?\d+),\s*(-?\d+)\)"

# accepts the list of tuples from the valid mul-instances iterates over it and transforms the strings into ints an sums the result of each multiplication
def evaluate_mul_instances(mul_list):
    multi = 0
    for instance in mul_list:
        int1, int2 = map(int, instance)
        result = int1 * int2
        multi += result
    return multi

# GET INPUT
file_path = "input3.txt"
with open (file_path, "r") as file:
    input = file.read().replace("\n", "")

# SEARCH FOR PATTERNS OF mul(int1, int2) and store it in a list of tuples with onyl the numbers
matches = re.findall(pattern, input)

# GET THE FINAL RESULT
sum = evaluate_mul_instances(matches)
print(sum)


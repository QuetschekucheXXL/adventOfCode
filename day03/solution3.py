# PART 1
# The Idea I have would be to:
# 1. get all mul(*,*) instances and safe them in a list
# 2. iterate over the list and see if there are even more to filter out
# 3. Sum up the multiplications for the valid list

# PART 2
# I know want to also include a pattern to check for do() and don't() to set a boolean that is initially true.
# When iterating over my found expressions I know want to check the flag for true and false
# true mean the mul can be calculated and sumed up, false means to skip this instance
# if I reach a do() or don't() I want to change the flag accordingly

import re

# added the first part before the "|" for part two --> I now get tuples of three "restricion, int1, int2"
pattern = r"(\b(?:do|don't)\(\))|mul\((-?\d+),\s*(-?\d+)\)" 

# accepts the list of tuples from the valid mul-instances iterates over it and transforms the strings into ints an sums the result of each multiplication
def evaluate_mul_instances(mul_list):
    # added the flag "include" for part 2
    include = True
    multi = 0
    for instance in mul_list:
        # new: setting flag include and checking for it before calculating
        if instance[0] == "do()":
            include = True
        elif instance[0] == "don't()":
            include = False
        if include and instance[1] and instance[2]:
            int1, int2 = map(int, (instance[1], instance[2]))
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


file_path = "task1.txt"

left_side = []
right_side = []

with open (file_path, "r") as file:
    #reading the file and storing the values in two lists. The left side in one an the right side in one:
    for line in file:
        numbers = line.strip().split()
        if len(numbers) == 2:
            left_side.append(int(numbers[0]))
            right_side.append(int(numbers[1]))
    #now that I have two lists I want to sort them in ascendnding order
    sorted_left = sorted(left_side)
    sorted_right = sorted(right_side)
    #now that I have two sorted lists I can loop over them and sum the differneceof each index
    total = 0
    for number in range(0, len(sorted_left)):
        toSum = sorted_left[number] - sorted_right[number]
        #and sum the difference between the two numbers up to a total
        if toSum < 0:
            total += toSum * -1
        else:
            total += toSum
    print(total)

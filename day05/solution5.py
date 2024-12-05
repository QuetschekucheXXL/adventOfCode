# Get the input
file_path ="input5.txt"
with open(file_path, "r") as file:
    puzzle_input = file.read().split("\n\n")
    input_for_ordering_rules = puzzle_input[0].split("\n")
    input_for_updates = puzzle_input[1].split("\n")


    # Creating a List of Ordering Rules where each rule is a list of two elements of the ordering rule
    ordering_rules = []
    for item in input_for_ordering_rules:
        ordering_rules.append(list(map(int, item.split("|"))))
    

    # Creating a list of updates where each update is a list of ints representing the pages to be checked
    updates = []
    for item in input_for_updates:
        updates.append(list(map(int, item.split(","))))
    
    test_updates = [
        [75,47,61,53,29],
        [97,61,53,29,13],
        [75,29,13],
        [75,97,47,61,53],
        [61,13,29],
        [97,13,75,29,47]
    ]

    test_orders = [
        [47,53],
        [97,13],
        [97,61],
        [97,47],
        [75,29],
        [61,13],
        [75,53],
        [29,13],
        [97,29],
        [53,29],
        [61,53],
        [97,53],
        [61,29],
        [47,13],
        [75,47],
        [97,75],
        [47,61],
        [75,61],
        [47,29],
        [75,13],
        [53,13]
    ]

    # FUNCTION FOR PART 1
    def is_update_correct(test_orders, line_of_update):
        for i in range(0, len(line_of_update)-1):
            count_of_wrong_orders = 0
            for order in test_orders:
                if line_of_update[i] == order[1]:
                    slice_of_update_to_check = line_of_update[i+1:]
                    if order[0] in slice_of_update_to_check:
                        count_of_wrong_orders += 1
                        return False
                    else:
                        pass
        return True
    
    # FUNCTION FOR PART 2 --> gets one wrong update line at a time together with the ordering rules and needs to correct the line
    def corrective_actions(ordering_rules, line_of_wrong_updates):
        corrected_update_line = line_of_wrong_updates.copy()
        should_restart = True
        #print(f"Should restart is: {should_restart}")
        while should_restart:
            should_restart = False
            #print("I am in WHILE")
            for i in range(0, len(corrected_update_line) - 1):
                for order in ordering_rules:
                    if corrected_update_line[i] == order[1]:
                        slice_to_check = corrected_update_line[i+1:]
                        if order[0] in slice_to_check:
                            should_restart = True
                            #print(f"Order number {order[0]} found after {corrected_update_line[i]} but should come before!")
                            index_to_change = slice_to_check.index(order[0])
                            #print(index_to_change)
                            number_to_change = slice_to_check.pop(index_to_change)
                            #print(f"Number to take from Slice: {number_to_change}")
                            #print(f"slice after number is removed: {slice_to_check}")
                            corrected_update_line = corrected_update_line[:i] + [number_to_change] + [corrected_update_line[i]] + slice_to_check
                            #print(corrected_update_line)
                            #print(f"Should restart is: {should_restart}")
        return corrected_update_line        

            
    # MAIN PART 
    sum_of_middle_page_numbers = 0
    list_of_wrong_updates = []

    #PART 1
    for line in updates:
        if is_update_correct(ordering_rules, line):
            sum_of_middle_page_numbers += line[(len(line) // 2)]
        if not is_update_correct(ordering_rules, line):
            list_of_wrong_updates.append(line)
    print(sum_of_middle_page_numbers)
    print(f"There are {len(list_of_wrong_updates)} wrong updates")
    


    #PART 2
    list_of_corrected_updates = []
    for line in list_of_wrong_updates:
        # uses the orders and one line of the list of wrong updates which in turn is a list of numbers to be checked
        #print(f"CHECKING LINE: {line}")
        #print(f"APPENDING LINE: {corrective_actions(ordering_rules, line)}")
        list_of_corrected_updates.append(corrective_actions(ordering_rules, line))

    sum_of_corrected = 0
    for line in list_of_corrected_updates:
        sum_of_corrected += line[(len(line) // 2)]
    print(sum_of_corrected)
    
    
    
    
    # CHECKS
    #print(sum_of_middle_page_numbers) #--> for Part 1 this was 4637
    #print(list_of_wrong_updates)
    print(f"number of corrected updates: {len(list_of_corrected_updates)}")

    # CHECKS
    #print(ordering_rules) --> fine = list of two ints each
    #print(updates) # --> is fine should be a list of ints at this point
    #print(len(ordering_rules)) #--> = 1176 checks with the lines of the input5.txt
    #print(len(updates)) #--> = 190 checks with the lines of the input5.txt
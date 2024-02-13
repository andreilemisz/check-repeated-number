# Create a function that identify if a list contains more than one duplicated number
# and returns that first duplicated number the second time it appears
single_numbers = [] # list to contain the numbers that appear the first time in the list
repeated_numbers = [] # list that contain the repeated numbers from the main list
set_list = None # variable to copy the list in a set formate to check the size of the list

problem_list = [
    
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    
]

def answer(big_list):
    
    for individual_list in big_list:
        
        set_list = set(individual_list)
        
        if len(set_list) == len(individual_list):
            print("There is no duplicate numbers in the list:")
            print(individual_list)
        else:
            single_numbers = []
            repeated_numbers = []
            for numbers in individual_list:
                if numbers in single_numbers:
                    repeated_numbers.append(numbers)
                else:
                    single_numbers.append(numbers)
            
            print("There are duplicated numbers in the list:")
            print(individual_list)
            print("And the answer to the question is:", repeated_numbers[0])
        print()

answer(problem_list)
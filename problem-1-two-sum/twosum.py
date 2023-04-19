"""Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
I explained the intuition behind my solution here:
https://samueladebayo.com/leetcode-blind75-day-1-two-sum-problem-with-hash-tables-in-python

"""

def two_sum(input_list: list, target_int:int):
    # Create a hash table or dictionary that maps each integer to its index location
    cache = {el:en for en, el in enumerate(input_list)}

    # Iterate over the input list and check for the sum of two integers that equals the target value
    for en, int_1 in enumerate(input_list):
        if (target_int - int_1) in input_list:
            # Check that the two integers are not the same
            if cache[target_int - int_1] != en:
                # Return the indices of the two integers that add up to the target value
                return [cache[int_1], cache[target_int-int_1]]

    # Return an empty list if no two integers add up to the target value
    return []

# Example usage
list_1 = [2, 3, 6, 9]
print(two_sum(list_1, 9))  # Output: [0, 1]



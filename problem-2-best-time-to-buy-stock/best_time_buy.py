"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and
choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""


def maximum_profit_buy(input_list: list):
    # Check if the input list is empty
    if len (input_list) == 0:
        return 0

    # Initialize the minimum price and maximum profit seen so far
    minimum_price = input_list[0]
    maximum_profit_seen = 0

    # Traverse through the input list
    for price in input_list:
        # Update the minimum price seen so far
        if price < minimum_price:
            minimum_price = price
        else:
            # Calculate the profit that can be made by selling at the current price
            profit = price - minimum_price
            # Update the maximum profit seen so far if the current profit is greater
            if profit > maximum_profit_seen:
                maximum_profit_seen = profit

    # Return the maximum profit seen so far
    return maximum_profit_seen


# prices = [7, 1, 5, 3, 6, 4]
prices = [1, 2, 3, 7, 4, 3]
print (maximum_profit_buy (prices))


print (maximum_profit_buy ([7,6,4,3,1]))
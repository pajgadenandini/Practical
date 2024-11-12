# Function to solve the 0/1 Knapsack Problem using Dynamic Programming
def knapsack_dp(weights, values, n, m):
    # Create a DP table with (n+1) rows and (m+1) columns, initialized to 0
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    # Fill the DP table
    for i in range(1, n+1):
        for w in range(1, m+1):
            if weights[i-1] <= w:  # If the current item can fit in the knapsack
                dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w - weights[i-1]])  # Include or exclude the item
            else:
                dp[i][w] = dp[i-1][w]  # Exclude the item
    
    # The result is the value in the bottom-right corner of the DP table
    return dp[n][m], dp

# Main function to take input and solve the problem
def knapsack():
    n = int(input("Enter the number of items: "))  # Number of items
    weights = []
    values = []
    
    # Input weights and values of items
    for i in range(n):
        weight = int(input(f"Enter weight of item {i+1}: "))
        value = int(input(f"Enter value of item {i+1}: "))
        weights.append(weight)
        values.append(value)
    
    m = int(input("Enter the capacity of the knapsack: "))  # Capacity of the knapsack
    
    # Call the DP knapsack function
    max_value, dp_table = knapsack_dp(weights, values, n, m)
    
    # Display the DP Table
    print("\nDynamic Programming Table:")
    for row in dp_table:
        print(" ".join(map(str, row)))
    
    print(f"\nThe maximum value that can be obtained is: {max_value}")

# Run the knapsack function
knapsack()


















































# Enter the number of items: 4
# Enter weight of item 1: 2
# Enter value of item 1: 12
# Enter weight of item 2: 1
# Enter value of item 2: 10
# Enter weight of item 3: 3
# Enter value of item 3: 20
# Enter weight of item 4: 2
# Enter the capacity of the knapsack: 5        

# Dynamic Programming Table:
# 0 0 0 0 0 0
# 0 0 12 12 12 12
# 0 10 12 22 22 22
# 0 10 12 22 30 32
# 0 10 15 25 30 37

# The maximum value that can be obtained is: 37
# Time Complexity: O(n * m), where n is the number of items and m is the knapsack capacity. We fill a table of size (n+1) x (m+1).
# Space Complexity: O(n * m) for storing the DP table.
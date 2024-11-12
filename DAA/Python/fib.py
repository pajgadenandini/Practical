# Recursive Fibonacci function with step count
def fibonacci_recursive(n, steps=[0]):
    if n <= 1:
        steps[0] += 1  # Base case counts as one step
        return n
    steps[0] += 1  # Each function call counts as a step
    return fibonacci_recursive(n - 1, steps) + fibonacci_recursive(n - 2, steps)

# Iterative Fibonacci function with step count
def fibonacci_iterative(n):
    if n <= 1:
        return n, 1  # Base case with 1 step

    prev, curr = 0, 1
    steps = 2  # Initial step for the two starting values

    for i in range(2, n + 1):
        prev, curr = curr, prev + curr
        steps += 1  # Each calculation counts as a step

    return curr, steps

# Get input from the user
n = int(input("Enter the position of Fibonacci number: "))

# Recursive calculation
steps_recursive = [0]  # Using a list to keep count as a reference
fib_recursive = fibonacci_recursive(n, steps_recursive)
print(f"Recursive: The {n}th Fibonacci number is: {fib_recursive}")
print(f"Total steps taken (recursive): {steps_recursive[0]}")

# Iterative calculation
fib_iterative, steps_iterative = fibonacci_iterative(n)
print(f"Iterative: The {n}th Fibonacci number is: {fib_iterative}")
print(f"Total steps taken (iterative): {steps_iterative}")

















# Complexity Analysis
# Recursive Approach:

# Time Complexity: 
# 𝑂(2^𝑛), due to redundant calculations.
# Space Complexity: 
# 𝑂(𝑛), due to recursion stack depth.
# Iterative Approach:

# Time Complexity: 
# 𝑂(𝑛), as each number up to n is calculated once.
# Space Complexity: 
# 𝑂(1)
# if we only track the last two values in the sequence.
from tabulate import tabulate

class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value
        self.ratio = value / weight  # value-to-weight ratio

def fractional_knapsack(items, capacity):
    # Sort items by the value-to-weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)
    
    total_value = 0  # Total value of knapsack
    knapsack = []    # To store items in the knapsack
    remaining_capacity = capacity  # Track remaining capacity of the knapsack

    for item in items:
        if item.weight <= remaining_capacity:
            # If the item can be fully added
            knapsack.append((item.name, item.weight, item.value, 1.0))  # 1.0 means fully taken
            total_value += item.value
            remaining_capacity -= item.weight
        else:
            # If the item can only be partially added
            fraction = remaining_capacity / item.weight
            knapsack.append((item.name, remaining_capacity, item.value * fraction, fraction))
            total_value += item.value * fraction
            remaining_capacity = 0  # Knapsack is full
            break  # No more items can be added

    return total_value, knapsack

# Dynamic input
n = int(input("Enter the number of items: "))
items = []
for i in range(n):
    name = input(f"Enter name of item {i + 1}: ")
    weight = float(input(f"Enter weight of item {i + 1}: "))
    value = float(input(f"Enter value of item {i + 1}: "))
    items.append(Item(name, weight, value))

capacity = float(input("Enter the capacity of the knapsack: "))

# Get the result of fractional knapsack
total_value, knapsack = fractional_knapsack(items, capacity)

# Prepare the knapsack table data
knapsack_data = {
    'Item': [x[0] for x in knapsack],
    'Weight Taken': [x[1] for x in knapsack],
    'Value Taken': [x[2] for x in knapsack],
    'Fraction Taken': [x[3] for x in knapsack]
}

# Create the knapsack table
knapsack_table = tabulate(knapsack_data, headers='keys', tablefmt='grid', showindex=False)

# Display the knapsack table with borders
print("\nItems Taken in Knapsack (with fractions):")
print(knapsack_table)

print(f"\nTotal value in Knapsack: {total_value}")









































































# time complexity - o(nlogn) - sorting and iterating it is O(n) total is O(nlogn)
# space-O(n) to store the list of item
# Enter the number of items: 3
# Enter name of item 1: i1
# Enter weight of item 1: 18
# Enter value of item 1: 25
# Enter name of item 2: i2
# Enter weight of item 2: 15
# Enter value of item 2: 24
# Enter name of item 3: i3
# Enter weight of item 3: 10
# Enter value of item 3: 15
# Enter the capacity of the knapsack: 20

# Items Taken in Knapsack (with fractions):
# +--------+----------------+---------------+------------------+      
# | Item   |   Weight Taken |   Value Taken |   Fraction Taken |      
# +========+================+===============+==================+      
# | i2     |             15 |          24   |              1   |      
# +--------+----------------+---------------+------------------+      
# | i3     |              5 |           7.5 |              0.5 |      
# +--------+----------------+---------------+------------------+      

# Total value in Knapsack: 31.5
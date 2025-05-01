# Day 3 - Python Lists and Loops
# Author: Sateesh Kumar
# Date: 2025-05-01
# Description: Print a list of AI tools multiple times based on user input.

# Create a list of AI tools
tool_names = ['Python', 'NumPy', 'Pandas']

# Get user input on how many times to repeat the list
no_of_times = int(input("How many times do you want to repeat the list? "))

# Initialize counter
start_num = 1
end_num = no_of_times

# Outer loop controls how many times the list should repeat
while start_num <= end_num:
    # Inner loop prints each tool name
    for tool in tool_names:
        print(f"I am learning {tool}")
    
    # Move to the next repetition
    start_num += 1

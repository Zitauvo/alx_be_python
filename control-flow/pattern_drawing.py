# pattern_drawing.py

# Step 1: Ask user for size
size = int(input("Enter the size of the pattern: "))

# Step 2: Validate input
while size <= 0:
    size = int(input("Please enter a positive integer: "))

# Step 3: Initialize row counter
row = 0

# Step 4: Loop through rows
while row < size:
    # Step 5: Print stars for each column
    for col in range(size):
        print("*", end="")
    # Step 6: Move to the next line
    print()
    row += 1


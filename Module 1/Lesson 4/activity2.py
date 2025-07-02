# Python program to print star pattern based on a number of rows
# Get the number of rows from user
n = int(input("Enter the number of rows: "))
# Outer loop for each row
for i in range(1, n+1):
    # Inner loop for each column in the row
    for i in range(i):
        # Print star end with space instead of new line
        print('*', end=' ')
        # After each row, print a new line
    print()
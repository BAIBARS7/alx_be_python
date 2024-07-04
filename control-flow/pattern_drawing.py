# Prompting user for pattern size
size = int(input("Enter the size of the pattern: "))

# Drawing the pattern
row = 0
while row < size:
    col = 0
    while col < size:
        print("*", end="")
        col += 1
    print()  # Move to the next line after completing the row
    row += 1

# Get the dimensions of the 2D list from the user
num_rows = int(input("Enter the number of rows: "))
num_cols = int(input("Enter the number of columns: "))

# Initialize an empty 2D list
matrix = []

# Iterate over rows
for i in range(num_rows):
    # Initialize an empty row
    row = []
    # Iterate over columns
    for j in range(num_cols):
        # Get user input for each element and append it to the row
        element = int(
            input("Enter element for row {} column {}: ".format(i+1, j+1)))
        row.append(element)
    # Append the row to the matrix
    matrix.append(row)

max_ones_row = -1  # Initialize to -1 indicating no row has been found yet
max_ones_count = 0

# Iterate over the rows
for i in range(num_rows):
    # Count the number of 1's in the current row
    ones_count = matrix[i].count(1)
    # Update max_ones_row if the current row has more 1's than the previous max
    if ones_count > max_ones_count:
        max_ones_row = i
        max_ones_count = ones_count

if max_ones_row != -1:
    print("Row number {} has the maximum number of 1's.".format(max_ones_row + 1))
else:
    print("There are no rows with 1's in the matrix.")

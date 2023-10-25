def rotate(matrix, direction):
    if direction == "clockwise":
        # Check if the desired rotation is clockwise.
        
        # To rotate a matrix clockwise, first transpose it. Transposing a matrix means that its rows become columns and vice versa.
        transposed_matrix = list(map(list, zip(*matrix)))

        # Then, reverse each row of the transposed matrix to complete the clockwise rotation.
        rotated_matrix = [list(reversed(row)) for row in transposed_matrix]
    elif direction == "counter-clockwise":
        # Check if the desired rotation is counterclockwise.
        
        # To rotate a matrix counterclockwise, first transpose it in the same way as for clockwise rotation.
        transposed_matrix = list(map(list, zip(*matrix)))

        # Then, reverse the order of rows to complete the counterclockwise rotation.
        rotated_matrix = list(reversed(transposed_matrix))
    else:
        # If an invalid direction is provided, raise a ValueError with a specific error message.
        raise ValueError("Invalid rotation direction. Use 'clockwise' or 'counter-clockwise'.")
    
    # Return the rotated matrix.
    return rotated_matrix

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

clockwise_rotation = rotate(matrix, "clockwise")
counter_clockwise_rotation = rotate(matrix, "counter-clockwise")

print("Clockwise rotation:")
for row in clockwise_rotation:
    print(row)

print("\nCounter-clockwise rotation:")
for row in counter_clockwise_rotation:
    print(row)

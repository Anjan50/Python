# Function to rotate a string to the left
def rotate_string_left(input_string, positions):
    # Calculate the length of the input string
    length = len(input_string)
    
    # Use slicing to rotate the string to the left
    rotated_string = input_string[positions % length:] + input_string[:positions % length]
    
    return rotated_string

# Function to rotate a string to the right
def rotate_string_right(input_string, positions):
    # Calculate the length of the input string
    length = len(input_string)
    
    # Use slicing to rotate the string to the right
    rotated_string = input_string[-(positions % length):] + input_string[:-(positions % length)]
    
    return rotated_string

# Example usage:
original_string = "abcdef"
positions_to_rotate = 2

# Rotate the string to the left
rotated_left = rotate_string_left(original_string, positions_to_rotate)

# Rotate the string to the right
rotated_right = rotate_string_right(original_string, positions_to_rotate)

# Print the original and rotated strings
print("Original String:", original_string)
print("Rotated String (left):", rotated_left)
print("Rotated String (right):", rotated_right)

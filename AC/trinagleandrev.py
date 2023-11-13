def print_combined_triangle(height):
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

    for i in range(height, 0, -1):
        spaces = " " * (height - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

# Example usage:
height = 5
print_combined_triangle(height)

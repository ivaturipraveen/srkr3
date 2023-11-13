from itertools import permutations

def generate_permutations(elements):
    # Use permutations from itertools
    permuted_list = list(permutations(elements))
    
    # Print each permutation
    for perm in permuted_list:
        print(perm)

# Example usage:
elements = [1, 2, 3]
print("Original List:", elements)

print("\nPermutations:")
generate_permutations(elements)

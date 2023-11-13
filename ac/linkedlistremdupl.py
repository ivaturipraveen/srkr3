linked_list = [1, 2, 2, 3, 4, 4, 5]
unique_values = []

for item in linked_list:
    if item not in unique_values:
        unique_values.append(item)

print("Linked List after Removing Duplicates:")
print(unique_values)

original_array = [2, 8, 9, 48, 8, 22, -12, 2]

new_array = []
seen_values = set()

for num in original_array:
    if num > 5:
        new_value = num + 2
        if new_value not in seen_values:
            new_array.append(new_value)
            seen_values.add(new_value)

print("Original array:", original_array)
print("New array:     ", new_array)

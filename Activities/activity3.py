def insert_at(arr, index, value):
    # Add a placeholder to increase the list size
    arr.append(None)

    # Shift elements to the right
    for i in range(len(arr) - 1, index, -1):
        arr[i] = arr[i - 1]

    # Insert the new value
    arr[index] = value
    return arr

# My inputs
numbers = [10, 20, 30, 40]
print(insert_at(numbers, 2, 25))
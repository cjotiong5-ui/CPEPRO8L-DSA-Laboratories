def find_max(arr): # defining arr

    # Giving maximum a task where to start
    maximum = arr[0]
    for i in range(len(arr)): 
        if arr[i] > maximum: 
            maximum = arr[i]
            return maximum


arr = [15, 8, 42, 19, 3]
print(f"Maximum Number is: {find_max(arr)}")
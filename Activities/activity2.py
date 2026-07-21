def binary_search(arr, target): #defining variables
    # adding value to the left and right
    left = 0
    right = len(arr) -1
    
    #looping
    while left <= right:
        #adding value to the midpoint
        midpoint = (left + right) // 2       
        
        if arr[midpoint] == target:
            return midpoint
        elif arr[midpoint] < target:
            left = midpoint + 1
        else :  
            right = midpoint - 1
    return -1

numbers = [10, 20, 30, 40, 50, 60]
print(binary_search(numbers, 50))
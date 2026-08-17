def recursive_binary_search(arr, low, high, target):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid

    if arr[mid] > target:
        return recursive_binary_search(arr, low, mid - 1, target)

    return recursive_binary_search(arr, mid + 1, high, target)


if __name__ == "__main__":
    data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

    test_targets = [23, 56, 50, 2, 91]

    for target_val in test_targets:
        result = recursive_binary_search(
            data,
            0,
            len(data) - 1,
            target_val
        )
        print(f"Target: {target_val} -> Index: {result}")

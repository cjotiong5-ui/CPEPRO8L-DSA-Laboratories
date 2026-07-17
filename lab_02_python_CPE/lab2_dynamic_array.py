import ctypes

class DynamicArray:
    def __init__(self):
        self.size = 0          # number of elements currently stored
        self.capacity = 1      # current allocated capacity
        self.array = self._make_array(self.capacity)

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError(f"indices must be integers, not {type(index).__name__}")
        if index < 0 or index >= self.size:
            raise IndexError(f"index {index} out of range (size={self.size})")
        return self.array[index]

    def append(self, element):
        # Grow the backing store before it overflows.
        if self.size == self.capacity:
            self._resize(2 * self.capacity)

        self.array[self.size] = element
        self.size += 1

    def _resize(self, new_capacity):
        print(f"[RESIZE] capacity {self.capacity} -> {new_capacity} "
              f"(triggered at size={self.size})")

        new_array = self._make_array(new_capacity)
        for i in range(self.size):
            new_array[i] = self.array[i]

        self.array = new_array
        self.capacity = new_capacity

    def _make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()


# Testing script
if __name__ == "__main__":
    arr = DynamicArray()
    for i in range(10):
        arr.append(i)
        print(f"Appending {i} | Size: {len(arr)} | Capacity: {arr.capacity} "
              f"| Element at index {i}: {arr[i]}")
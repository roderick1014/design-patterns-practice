'''

    Design Pattern 8: Structure Patterns - Facade.

'''

# Python arrays are dynamic by default, but this is an example of resizing.
class Array:

    def __init__(self):
        self.capacity = 2
        self.length = 0
        self.arr = [0] * 2 # Array of capacity = 2

    # Insert n in the last position of the array.
    def pushback(self, n):
        if self.length == self.capacity:
            self.resize()
    
        # insert at next empty position.
        self.arr[self.length] = n
        self.length += 1

    def resize(self):
        
        # Create new array of double capacity.
        self.capacity = 2 * self.capacity
        newArr = [0] * self.capacity

        for idx in range(self.length):
            newArr[idx] = self.arr[idx]
        
        self.arr = newArr

if __name__ == '__main__':
    arr = Array()
    print(f'Array length: {len(arr.arr)}')  # Array length: 2, arr.length = 0
    arr.pushback(3)
    print(f'Array length: {len(arr.arr)}')  # Array length: 2, arr.length = 1
    arr.pushback(4)
    print(f'Array length: {len(arr.arr)}')  # Array length: 2, arr.length = 2
    arr.pushback(5)
    # The capacity of the defined Array is doubled.
    print(f'Array length: {len(arr.arr)}')  # Array length: 4, arr.length = 3
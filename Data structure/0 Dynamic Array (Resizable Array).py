class DynamicArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        if self.capacity > 0:
            self.arr = []
        else:
            raise Exception("capacity must be more than 0")

    def get(self, i: int) -> int:
        try:
            return self.arr[i]
        except:
            raise Exception("invalid index")

    def set(self, i: int, n: int) -> None:
        try:
            self.arr[i] = n
        except:
            raise Exception("invalid index")

    def pushback(self, n: int) -> None:
        if self.getSize() == self.getCapacity():
            self.resize()
            self.arr.append(n)
        else:
            self.arr.append(n)

    def popback(self) -> int:
        if self.getSize != 0:
            return self.arr.pop()

    def resize(self) -> None:
        self.capacity *= 2

    def getSize(self) -> int:
        return len(self.arr)

    def getCapacity(self) -> int:
        return self.capacity


"""
Input:
    [
        "Array", 1, "getSize", "getCapacity", 
        "pushback", 1, "getSize", "getCapacity",
        "pushback", 2, "getSize", "getCapacity", "get", 1, 
        "set", 1, 3, "get", 1, "popback", "getSize", "getCapacity"
    ]

Output:
    [null, 0, 1, null, 1, 1, null, 2, 2, 2, null, 3, 3, 1, 2]
"""
arr = DynamicArray(1)
print(arr.getSize(), arr.getCapacity())
arr.pushback(1)
print(arr.getSize(), arr.getCapacity())
arr.pushback(2)
print(arr.getSize(), arr.getCapacity(), arr.get(1))
arr.set(1, 3)
print(arr.get(1), arr.popback(), arr.getSize(), arr.getCapacity())

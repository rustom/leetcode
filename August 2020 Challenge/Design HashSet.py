class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.insides = []
        

    def add(self, key: int) -> None:
        if key not in self.insides:
            self.insides.append(key)

    def remove(self, key: int) -> None:
        if key in self.insides:
            self.insides.remove(key)
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.insides: 
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(6)
obj.remove(4)
obj.add(17)
param_3 = obj.contains(14)
print(param_3)
print(obj.insides)
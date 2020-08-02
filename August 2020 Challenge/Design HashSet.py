class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.insides = set()

    def add(self, key: int) -> None:
        if key not in self.insides:
            self.insides.add(key)

    def remove(self, key: int) -> None:
        if key in self.insides:
            self.insides.remove(key)
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.insides
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
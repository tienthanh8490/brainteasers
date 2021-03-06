# https://leetcode.com/problems/insert-delete-getrandom-o1/submissions/

import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.table:
            return False
        self.table[val] = True
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.table:
            return False
        del self.table[val]
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        k = random.choice(list(self.table))
        return k


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
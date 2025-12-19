import random


class RandomizedSet:

    def __init__(self):
        self.randomizedSet = {}
        self.listOfIntegers = []

    def insert(self, val: int) -> bool:
        if self.randomizedSet.get(val) == None:
            self.listOfIntegers.append(val)
            self.randomizedSet[val] = len(self.listOfIntegers) - 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if self.randomizedSet.get(val) != None:
            index = self.randomizedSet.get(val)
            if index == (len(self.listOfIntegers) - 1):
                self.listOfIntegers.pop()
                self.randomizedSet.pop(val)
                return True
            else:
                self.listOfIntegers[index] = self.listOfIntegers[-1]
                self.randomizedSet[self.listOfIntegers[-1]] = index
                self.listOfIntegers.pop()
                self.randomizedSet.pop(val)
                return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.listOfIntegers)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
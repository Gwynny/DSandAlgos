class HandcraftedArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def __str__(self):
        return str(self.__dict__)

    def get(self, index):
        return self.data[index]

    def append(self, new_element):
        self.data[self.length] = new_element
        self.length += 1

    def pop(self):
        item = self.data[self.length]
        del self.data[self.length]
        self.length -= 1
        return item

    def insert(self, index, new_element):
        for i in list(range(index, self.length))[::-1]:
            self.data[i + 1] = self.data[i]
        self.data[index] = new_element
        self.length += 1

    def delete(self, index):
        for i in range(index, self.length-1):
            self.data[i] = self.data[i + 1]
        del self.data[self.length-1]
        self.length -= 1


myList = HandcraftedArray()

myList.append(0)
myList.append(2)
myList.append(4)
myList.append(6)
print(myList)
myList.insert(2, 5)
print(myList)
myList.delete(3)
print(myList)

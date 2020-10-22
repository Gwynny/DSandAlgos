from Arrays.python_array import HandcraftedArray
from Arrays.MergeSortedArrays import MergeSortedArrays

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

print(MergeSortedArrays([0, 3, 4, 31], [3, 4, 6, 30]))

# INSTRUCTIONS
''''
Tartiblangan kvadratlar
Bo'sh bo'lmagan va o'sish tartibida saralangan butun sonlar arrayini qabul qiluvchi funksiya yozing. 
Funksiya har bir sonning kvadratini hisoblablasin. Natija ham o‘sish tartibida qaytarilsin.

Misol uchun
array = [1, 2, 3, 5, 6, 8, 9]
Kutilgan natija
[1, 4, 9, 25, 36, 64, 81]'''

# CODE
# my_version          O(nlogn)
def sortedSquaredArray(array):                   
  squared = [] 
  for i in array:
    i *= i
    squared.append(i)
  return sorted(squared)

# pythonic_version
def sortedSquaredArray(array):
  return sorted(map(lambda x: x**2, array))

# version 3
def sortedSquaredArray(array):
  return sorted([i**2 for i in array])

# two_pointer version (best version)  O(n)
def sortedSquaredArray(array):
    n = len(array)
    result = [0] * n        # create empty result array of same size
    left, right = 0, n - 1  # left starts at 0, right starts at last index
    
    for i in range(n - 1, -1, -1):  # fill result from RIGHT to LEFT
        if abs(array[left]) > abs(array[right]):
            result[i] = array[left] ** 2
            left += 1       # move left pointer right
        else:
            result[i] = array[right] ** 2
            right -= 1      # move right pointer left
    
    return result
  
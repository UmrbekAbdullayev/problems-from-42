# INSTRUCTIONS

# Ikki Son Yig‘indisi
# Sizga butun sonlardan iborat array va targetSum beriladi. Arraydagi ikki turli son yig‘indisi targetSum'ga teng bo‘lsa, ularni o‘sish tartibida qaytaradigan funksiya yozing.
# Agar bunday juftlik bo‘lmasa, bo‘sh array qaytaring.
# 💡 Eslatma: Sonlar turli bo'lsin, bitta sondan ikki marta foydalanib bo‘lmaydi.

# Faqat bitta juftlik mavjud deb faraz qiling.

# Misol uchun
# array = [3, 5, -4, 8, 11, 1, -1, 6]
# targetSum = 10
# Kutilgan natija
# [-1, 11] // sonlar o‘sish tartibida


# CODE
def twoNumberSum(array, targetSum):
  seen = set()
  for i in array:
    rem = targetSum - i
    if rem in seen:
      return sorted([i, rem])
    seen.add(i)  
  return [] 



# conclusions to draw:

# for i in list:  ---> i is an item in the list
# for i in range(len(list)):  ---> i is an index of an item in the list
# for index, value in enumerate(list):   ---> gives the index and item together

# for i in array():  O(n2)
# for i in set():    O(1)
# looking for an item in set is faster because set uses hash tables under the hood, while in array item is searched one by one

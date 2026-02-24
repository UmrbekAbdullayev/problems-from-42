# INSTRUCTIONS
'''Ketma-ket qism
Ikkita butun sonlardan iborat array beriladi. Ikkinchi array birinchining ketma-ket qismi ekanini aniqlovchi funksiya yozing.

Ketma-ket qism — bu elementlari tartib bilan uchraydigan, lekin yonma-yon bo‘lishi shart bo‘lmagan qator.

Masalan, [1, 3, 4] sonlari [1, 2, 3, 4] arrayining ketma-ket qismi hisoblanadi, [2, 4] ham shunday. Shuningdek, bitta son yoki arrayning o‘zi ham ketma-ket qism bo‘lishi mumkin.

Misol uchun
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
Kutilgan natija
true'''

# CODE
def isValidSubsequence(array, sequence):
  index = 0
  for item in array:
    if index == len(sequence):
      break
    if item == sequence[index]:
      index += 1
  return index == len(sequence)  

''' What can I learn from this code: to prove if list is sublist of another bigger one,
 we have to loop through the first, bigger list, if an item of the bigger list is in the smaller list,
 we compare the next item of the bigger list to the next item of the smaller list by increasing index of smaller list
  Once index == len(sequence) which means all items in the smaller list exists in the bigger list,
   so we break and go out of loop, return True '''    
  


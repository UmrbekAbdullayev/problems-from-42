# INSTRUCTIONS
'''Nollarni orqaga surish
Berilgan sonlar ro'yxatidagi nollarni ro'yxat orqasiga o'tkazing, lekin boshqa elementlar ketma-ketligi buzilmasin.

 Imkon qadar kamroq amal bajaring.
 Qo'shimcha xotiradan foydalanmang - amallarni ro'yxat ustida bajaring.

Misol 1:
 Kiritish: nums = [0,1,0,3,12]
 Natija: [1, 3, 12, 0, 0]
 Misol 1:
 Kiritish: nums = [0]
 Natija: [0]'''

# CODE
def moveZeroes(nums: list) -> list:
  for i in nums:
    if i != 0:
      continue
    else:
      nums.remove(i)
      nums.append(i)

  return nums  
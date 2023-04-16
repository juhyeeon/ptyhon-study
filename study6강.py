# 1번문제
# class Calculator:
#     def __init__(self):
#         self.value=0

#     def add(self, val):
#         self.value+= val
    
# class UpgradeCalculator(Calculator):


#     def minus(self, val):
#         self.value-= val
# cal=UpgradeCalculator()
# cal.add(10)
# cal.minus(7)
# print(cal.value)

# 2번문제
# class Calculator:
#     def __init__(self):
#         self.value=0

#     def add(self, val):
#         self.value+= val
# class MaxLimitCalculator(Calculator):
#     def add(self,val):
#         self.value += val
#         if self.value > 100:
#             self.value=100
# cal=MaxLimitCalculator()
# cal.add(50)
# cal.add(60)
# print(cal.value)

# 3번문제
# print(all([1,2,abs(-3)-3]))

# print(cpr(ord('a'))=='a')
# >>>true

# 4번문제
# print(list(filter(lambda x:x>0 , [1,-2,3,-5,8,-3])))

# 5번문제
# print(int('0xea', 16))

# 6번문제
# print(list(map(lambda a: a*3, [1,2,3,4])))

# 7번문제
# a=[-8,2,7,5,-3,5,0,1]
# print(max(a)+min(a))

# 8번문제 round사용 
# print(round(17/3,4))

# 9번문제
# 보류
# import sys
# numbers = sys.argv[1:]
# result=0
# for number in numbers:
#     result += int(number)
# print(result)

# 10번문제
# 보류

# 11번문제
# 보류

# 12번문제
# import time
# print(time.strftime("%Y/%m/%d %H:%M:%S"))

# 13번문제
# sorted는 기존 리스트는 건드리지 않고, 정렬된 새로운 리스트를 리턴
# sort는 아무것도 리턴하지 않고, 기존 리스트를 정렬
# import random
# lotto = sorted(random.sample(range(1,45),6))
# print(lotto)
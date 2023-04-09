# 1번 문제
# def is_odd(number):
#     if number%2==1:
#         return True
#     else:
#         return False
# print(is_odd(4))

# 2번문제
# def avg_numbers(*args):
#     result=0
#     for i in args:
#         result += i
#     return result / len(args)
# print(avg_numbers(1, 2))

# 3번문제
# input1= int(input("첫번째 숫자를 입력하세요."))
# input2= int(input("두번째 숫자를 입력하세요."))

# total=(input1+input2)
# print("두 수의 합은 %s 입니다" % total)

# 5번 문제
# f1= open("text.txt","w", encoding="UTF-8")
# f1.write("Life is too short")
# f1.close()

# f2= open("text.txt","r")
# print(f2.read())
# f2.close()

# 6번 문제
# user_input= input("저장할 내용을 입력하세요")
# f= open("text.txt","a", encoding="UTF-8")
# f.write(user_input)
# f.write("\n")
# f.close()

# 7번문제
# f=open("text.txt", 'r', encoding="UTF-8")
# body=f.read()
# f.close()
# body=body.replace("java", "python")
# f= open("text.txt", "w", encoding="UTF-8")
# f.write(body)
# f.close()


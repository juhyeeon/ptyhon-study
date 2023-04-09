# 함수의 기본 구조
# def sum(a,b):
#     result=a+b
#     return result
# print(sum(1,2))

# 입력값 없이도 출력이 됀다
# def say():
#     return 'HI'
# print(say())

# 출력값 없이도 출력이 됀다.
# def sum(a,b):
#     print("%d,%d의 합은 %d입니다." %(a,b,a+b))
# print(sum(1,2))    

# 입력도 출력도 없는 함수
# def say():
#     print('HI')
# print(say())

# 여러개의 입력값을 받는 함수
# def sum_many(*args):
#     sum=0
#     for i in args:  
#         sum=sum+i <--여기에 *args에 입력받은 모든값을 더함
#     return sum
# print(sum_many(4,5,6))

# def print_kwargs(**kwargs):
#     for k in kwargs.keys():
#         if(k == "name"):
#             print("당신의 이름은:" + k)
# print(print_kwargs(name="int 조수", b="2"))

# 함수의 결과 값은 언제나 하나
# def sum_and_mul(a,b):
#     return a+b,a*b
# print(sum_and_mul(1,2))

# 매개변수에서 초기값 미리 설정하기 (순서를 맞춰서 정렬해야됌)
# def say_myslef(name,old,man=True):
#     print("나의 이름은 %s 입니다." %name)
#     print("나이는 %d 입니다" %old)
#     if man:
#         print("남자입니다")
#     else:
#         print("여자입니다.")
# say_myslef("백주현",20)    

# 함수안에서 선언된 변수의 효력범위
# a=1
# def vartest(a):  이 안에서 쓰인 변수는 지역변수라고 해서 임시변수같은 개념
#     a=a+1         함수안에 있는 변수는 함수 안에서만 쓰인다.
# vartest(a)
# print(a)
# 함수안에서 선언된 변수 변경하는 방법1
# a=1
# def vartest(a):
#     a=a+1
#     return a
# a=vartest(a)
# print(a)
# 방법2
# a=1
# def vartest():
#     global a
#     a=  a+1
# vartest()
# print(a)

# (lambda) 함수를 간단하게 표현하는 방법                 def add(a,b):
# add= lambda a, b: a+b                     ==              return a+b
# result=add(3,4)                        동일하다       result=add(3,4)
# print(result)                                         print(resulrt)

# mylist=[lambda a,b:a+b, lambda a,b:a*b]
# print(mylist[1](1,2))



# 파일 읽고 쓰기
# 파일 생성하기 ("w")
# f=open("새파일.txt","w")
# f.close()

# f=open("C:\ps\새파일.txt","w",encoding="UTF-8")
# for i in range(1,11):
#     data="%d번째 줄입니다.\n" %i
#     f.write(data)
# f.close()

# 파일 읽기모드("r")  readline()함수
# f=open("새파일.txt", "r", encoding="UTF-8")
# line=f.readline()
# print(line)
# f.close()
# 모든줄 읽기 while 사용
# f=open("새파일.txt","r", encoding="UTF-8")
# while True:
#     line=f.readline()
#     if not line: break
#     print(line)
# f.close()
# 모든줄 읽기 readlines사용
# f=open("새파일.txt", "r", encoding="UTF-8")
# lines=f.readlines()
# for line in lines:
#     print(line)
# f.close()

# read()함수 내용을 통째로 가져옴
# f=open("새파일.txt", "r" , encoding="UTF-8")
# data=f.read()
# print(data)
# f.close()

# 파일에 새로운 내용 추가하기 ("a")
# f=open("새파일.txt","a", encoding="UTF-8")
# for i in range(11,20):
#     data="%d번째 줄입니다\n" %i
#     f.write(data)
# f.close()

# with문을 사용하면 .close()사용하지 않아도 됌
# with open("새파일.txt", "w") as f:
#     f.write("Life is to short, you need python")
#과제 11
a = list(map(int, input('숫자 5개를 입력하시오: ').split()))
a.append(input('문자 1개를 입력하시오: '))
print(a)

#과제 12
a = list(map(int, input('숫자 5개를 입력하시오: ').split()))
del a[-2:]
print(a)

#과제 13
a = list(map(int, input('숫자 5개를 입력하시오: ').split()))

for index, value in enumerate(a, start = 101):
    print(index, value)

#과제 14
a = [10, 20, 30, 40, 30, 20, 10]
result = a.count(20)

print(result)

#과제 15
a = list(map(int, input('숫자 10개를 입력하시오: ').split()))
a.sort()

print("최저값: ", a[0])
print("최고값: ", a[-1])

#과제 16
a = list(map(int, input('숫자 10개를 입력하시오: ').split()))
a.sort()
print(sum(a[1:-1]))

#과제 17
a = [10, 20, 30, 40, 30, 20, 10]
a.remove(20)
a.remove(20)
print(a)

#과제 18
a = list(i for i in range(1, 6))
print(a)

#과제 19
a = [i for i in range(1, 21) if i % 2 == 1]
print(a)

#과제 20
a1, a2 = map(int, input('정수 두 개를 입력하시오: ').split())

if 1 <= a1 <= 20 and 10 <= a2 <= 30 and a1 < a2:
    b = [2 ** i for i in range(a1, a2 + 1)]

del b[1]
del b[-2]

print(b)

#과제 21
a = input("'Hello, world!'를 입력하시오: ")
a = a.replace('Hello', 'Hi')
print(a)

#과제 22
a = input('문자 4개를 입력하시오: ')
a = "/".join(a)
print(a)

#과제 23
a = input('본인의 성을 영어로 입력하시오: ').lower().rjust(10)
print(a)

#과제 24
a = list(map(int, input('세미콜론으로 구분하여 입력하시오: ').split(';')))
a.sort(reverse=True)

for b in a:
    print(str(b).rjust(9))
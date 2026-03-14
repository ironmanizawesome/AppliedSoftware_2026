def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
#재귀호출 구조를 이용한 팩토리얼 계산
num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")
def check_even(n): 
    if num % 2 == 0:
        return True
    return False

num = int(input("Enter a number: "))

if check_even(num):
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

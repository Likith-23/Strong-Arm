number = int(input("INPUT A NUMBER"))
digits = len(str(number))
result = 0
temp = number
while temp > 0:
    digit = temp%10
    result += digit ** digits
    temp //= 10
if number == result:
    print("ITS AN ARMSTRONG NUMBER")
else:
    print("ITS NOT AN ARMSTRONG NUMBER")
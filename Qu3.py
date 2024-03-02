# Python program to check armstrong number use three digit number.

userNum = (input("Enter three digit numbers : "))
numberOfDigit = len(userNum)
armstrongNum = 0

for num in userNum:
    num = int(num)
    armstrongNum += (num ** numberOfDigit)

if (armstrongNum == int(userNum)):
    print(userNum,"is","Armstrong Number :",armstrongNum)
else:
    print(userNum,"is not","Armstrong Number :",armstrongNum)

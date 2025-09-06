# Sum of range of natural number starting from 1

num = int(input("Enter the last number in the range: "))

sum = 0

for i in range(1, num+1):
    sum = sum + i

    print("\n Sum = ", sum)

# write a program that will ask user to enter a number and then calculate and output its factorial number.
input = int(input('Enter a number: '))
factorial = 1
for i in range(1, input + 1):
    factorial = factorial * i
print(f'The factorial of {input} is {factorial}')

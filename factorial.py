# To find the factorial of input number

def fact(n):
    if n <= 1:
        return 1
    else:
        return (n * fact(n-1))

number = int(input("Enter a number: "))

print("Factorial of {}! = {}".format(number, fact(number)))

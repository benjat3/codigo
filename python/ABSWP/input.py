def collatz(number):
             print(str(number), end=' ')
             comparar = number % 2 #0 si es par, 1 si es impar
             if comparar == 0: #Si number es par 
                 number = number // 2
             else:
                 number = 3 * number + 1
             return(number)

print("Enter a number")
try:
    number = int(input())
    while number != 1:
        number = collatz(number)

except ValueError:
    print("Enter an integer number")



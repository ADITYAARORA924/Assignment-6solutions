n=int(input("Enter a number"))
#defining the function
def perfect_number(n):
    sum = 0
    for x in range(1 , n):
        if n % x == 0:
            sum += x
if sum == n  :
    print("The number is perfect")
else :
    print("The numbr isn't perfect")
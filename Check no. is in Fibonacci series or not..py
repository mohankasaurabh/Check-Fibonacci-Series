#user take single input or multipul input with (,) 
def fibo(n):
    a = 0
    b = 1
    while a <= n:
        if n == a:
            return str(n) + " " + "is a Fibonacci Number"
        a, b = b, a + b
    return str(n) + " " + "is not a Fibonacci Number"

def fun():
    try:
        n = list(map(int,input("Enter a single/series of number: ").split(",")))
        for i in n:
            print(fibo(i))
    except:
        print("Invalid Input, Please give comma e.g: 1,2,3,4")

#call the function
fun()
def fib(n):
    """recursive solution to fibonacci"""
    if n <= 1:
        return n
    else: 
        return (fib(n - 1) + fib(n - 2))

nterms = int(input("Enter number of terms: >>> "))

if nterms <= 0:
    print("Error. Please, enter an integer above 0.")
else:
    print("Fibonacci Sequence: ")
    for num in range(nterms):
        print(fib(num))


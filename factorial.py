def factorial(n):
    if(n == 1 or n == 0):
        return 1
    else:
        return(n * factorial(n-1))

if __name__ == "__main__":
    n = 24
    
    # factorial through recursion
    print(factorial(n))

    # factorial through brute force method
    factorial_val = 1
    for i in range(1, n+1):
        factorial_val *= i
    print(factorial_val)

from functools import cache, lru_cache

# @cache # stores all the previous values
@lru_cache(maxsize=5) # storing last 5 values 
def fib(n):
    return (n if n <= 1 else fib(n-1) + fib(n-2))

def main():
    for i in range(400):
        print(i, fib(i))
    print("done")

if __name__ == "__main__":
    main()

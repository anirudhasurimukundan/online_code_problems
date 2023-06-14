def fibonacci_series(length, fib_series):
    for i in range(2, length):
        fib_series[i] = fib_series[i-1] + fib_series[i-2]
    return fib_series

if __name__ == "__main__":

    fib_series_length = 10

    fib_series = [0] * fib_series_length
    fib_series[0] = 0
    fib_series[1] = 1

    print(fibonacci_series(fib_series_length, fib_series))

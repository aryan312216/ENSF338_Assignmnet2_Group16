import time
import matplotlib.pyplot as plt


def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)


def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        memo[n] = n
    else:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]


numbers = list(range(36))
list_original = []
list_memo = []
for i in numbers:
    start_time = time.time()
    func(i)
    list_original.append(time.time() - start_time)
    
    start_time = time.time()
    fib_memo(i)
    list_memo.append(time.time() - start_time)


plt.plot(numbers, list_original, label='Original function')
plt.plot(numbers, list_memo, label='Memoized function')
plt.legend()
plt.xlabel(' Fibonacci number')
plt.ylabel('Time (seconds)')
plt.show()

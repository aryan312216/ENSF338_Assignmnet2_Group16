def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        memo[n] = n
    else:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]
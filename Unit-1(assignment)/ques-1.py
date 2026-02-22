# Name = Anveshna | Roll no. = 2501010130
# Assignment: Unit 1 (Factorial & Fibonacci Analysis)
# <=================CODE STARTS========================>

def get_factorial(n):
    """Recursive Factorial: Time O(n)"""
    if n <= 1:
        return 1
    return n * get_factorial(n - 1)

def fib_naive(n):
    """Naive Fibonacci: Time O(2^n)"""
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)

def fib_memoized(n, memo=None):
    """Memoized Fibonacci: Time O(n)"""
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memoized(n - 1, memo) + fib_memoized(n - 2, memo)
    return memo[n]

def main():
    print("--- PART 1: RECURSION ---")
    
    # Taking user input instead of fixed numbers
    val = int(input("Enter a number to calculate Factorial and Fibonacci: "))

    # 1. Factorial
    print(f"\nFactorial of {val}: {get_factorial(val)}")
    
    # 2. Fibonacci Comparison
    print(f"\nComputing Fibonacci({val})...")
    print(f"Memoized Result (Fast): {fib_memoized(val)}")
    
    # Warning for Naive: If val is too high (e.g., > 35), it will freeze the computer
    if val > 30:
        print("Note: Skipping Naive version for high input to avoid system hang.")
    else:
        print(f"Naive Result (Slow):  {fib_naive(val)}")

if __name__ == "__main__":
    main()
# <=================CODE ENDS==========================>
# Complexity Analysis: Factorial & Fibonacci

## 1. Recursive Factorial
**Recurrence Relation:** $T(n) = T(n-1) + O(1)$

| Complexity | Analysis |
| :--- | :--- |
| **Time Complexity** | **O(n)** |
| **Space Complexity** | **O(n)** |

### Justification:
* **Time:** The function makes exactly $n$ recursive calls (from $n$ down to $1$). Each call performs a single multiplication, which is a constant time operation $O(1)$.
* **Space:** Each recursive call adds a new frame to the system stack. Since the recursion depth is $n$, it consumes linear space.

---

## 2. Fibonacci Sequence (Naive vs. Memoized)

### A. Naive Recursion
**Recurrence Relation:** $T(n) = T(n-1) + T(n-2) + O(1)$

| Complexity | Analysis |
| :--- | :--- |
| **Time Complexity** | **O(2ⁿ)** (Exponential) |
| **Space Complexity** | **O(n)** |

**Why is it inefficient?**
The naive approach is inefficient due to **Overlapping Subproblems**. When calculating $fib(n)$, the algorithm builds a full binary recursion tree where it recalculates the same values multiple times. 
* *Example:* To find $fib(5)$, the algorithm calculates $fib(3)$ twice, $fib(2)$ three times, and $fib(1)$ five times. This redundancy grows exponentially as $n$ increases.



### B. Memoized Recursion (Top-Down DP)
**Recurrence Relation:** $T(n) = T(n-1) + O(1)$

| Complexity | Analysis |
| :--- | :--- |
| **Time Complexity** | **O(n)** (Linear) |
| **Space Complexity** | **O(n)** |

**Why is it efficient?**
Memoization stores the result of each subproblem in a cache (dictionary/array). When a subproblem is encountered again, the result is returned instantly in $O(1)$ time. This collapses the exponential tree into a linear path of $n$ unique calls.
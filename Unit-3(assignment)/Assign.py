# Name = Anveshna
# Course = B.Tech CSE Core 
# Section = A
# Roll no. = 2501010130
# Unit 3 Assignment: Sorting Algorithms & Performance Analysis
# Submitted to = Deepak Kaushik Sir
# <==========================================================>

import time
import random
import sys

# Increase recursion limit for deep Merge/Quick sort calls on large datasets
sys.setrecursionlimit(20000)

# 1. INSERTION SORT 
def insertion_sort(arr):
    # O(n^2) worst case, but O(n) for nearly sorted data [cite: 49, 293]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# 2. MERGE SORT 
def merge_sort(arr):
    # Divide and Conquer approach [cite: 51, 298]
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]: # Maintains stability [cite: 298, 300]
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# 3. QUICK SORT 
def quick_sort(arr):
    # Performance depends heavily on pivot choice [cite: 53, 302]
    if len(arr) <= 1:
        return arr
    
    # Using middle element as pivot to avoid O(n^2) on sorted data 
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# 4. BENCHMARK HARNESS 
def run_benchmark():
    # Requirements: Sizes 1000, 5000, 10000 [cite: 57, 313]
    sizes = [1000, 5000, 10000]
    data_types = ["Random", "Sorted", "Reverse"]
    
    print(f"{'Algorithm':<15} | {'Size':<6} | {'Type':<8} | {'Time (s)':<10}")
    print("-" * 50)

    for size in sizes:
        # Generate the three required datasets [cite: 313, 319]
        base_data = {
            "Random": [random.randint(0, size) for _ in range(size)],
            "Sorted": list(range(size)),
            "Reverse": list(range(size, 0, -1))
        }

        for d_type, original_list in base_data.items():
            # Test each algorithm
            for name, sort_func in [("Insertion", insertion_sort), 
                                    ("Merge", merge_sort), 
                                    ("Quick", quick_sort)]:
                
                # Copy input before sorting to ensure fair test [cite: 316]
                test_list = original_list.copy()
                
                start = time.perf_counter()
                sort_func(test_list)
                end = time.perf_counter()
                
                print(f"{name:<15} | {size:<6} | {d_type:<8} | {end-start:.6f}")

# <==================== LAB REPORT SUMMARY ====================>
"""
STABILITY & IN-PLACE NOTES[cite: 319]:
- Insertion Sort: Stable, In-place.
- Merge Sort: Stable, Out-of-place (requires O(n) extra memory).
- Quick Sort: Unstable, In-place (O(log n) stack memory).

VIVA POINTS[cite: 136, 316]:
1. Insertion sort is fastest on 'Sorted' data because it performs zero swaps.
2. Quick sort worst-case occurs when the pivot consistently divides the 
   array into 0 and n-1 elements (e.g., sorted data with end-pivot).
3. Merge sort is the most consistent for large datasets due to its 
   guaranteed O(n log n) time complexity.
"""

if __name__ == "__main__":
    run_benchmark()
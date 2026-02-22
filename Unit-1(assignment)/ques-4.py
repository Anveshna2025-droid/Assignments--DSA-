# Name = Anveshna | Roll no. = 2501010130
# Assignment: Unit 1 - Tower of Hanoi
# <=============CODE STARTS======================>

# THEORY & COMPLEXITY ANALYSIS:
# -----------------------------
# 1. Recurrence Relation: T(n) = 2T(n-1) + 1
# 2. Time Complexity: O(2ⁿ) - Exponential
#    - Every additional disk doubles the number of moves required.
# 3. Space Complexity: O(n) - Linear
#    - Based on the maximum depth of the recursion stack.

# MANUAL TRACE FOR N = 3 (A=Source, B=Aux, C=Dest):
# -------------------------------------------------
# Step 1: Move Disk 1 from A to C
# Step 2: Move Disk 2 from A to B
# Step 3: Move Disk 1 from C to B
# Step 4: Move Disk 3 from A to C  <-- Midpoint (Largest Disk)
# Step 5: Move Disk 1 from B to A
# Step 6: Move Disk 2 from B to C
# Step 7: Move Disk 1 from A to C




def solve_hanoi(n, src, aux, dest, move_count=[0]):
    # Solves Hanoi and tracks steps.
    # Using a list for move_count to keep it mutable across recursive calls.
    
    if n == 1:
        move_count[0] += 1
        print(f"Step {move_count[0]}: Move Disk 1 from {src} to {dest}")
        return

    # Move n-1 disks from Source to Aux
    solve_hanoi(n - 1, src, dest, aux, move_count)

    # Move the actual nth disk
    move_count[0] += 1
    print(f"Step {move_count[0]}: Move Disk {n} from {src} to {dest}")

    # Move n-1 disks from Aux to Dest
    solve_hanoi(n - 1, aux, src, dest, move_count)

def main():
    print("=== TOWER OF HANOI RECURSIVE SOLVER ===")
    try:
        n = int(input("Enter number of disks: "))
        if n < 1:
            print("Please enter a positive integer.")
            return

        print(f"\nSolution for {n} disks:")
        print("-" * 35)
        
        counter = [0]
        solve_hanoi(n, 'Peg A', 'Peg B', 'Peg C', counter)
        
        print("-" * 35)
        print(f"Total Moves (2^{n} - 1) = {counter[0]}")
        
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
# <=============CODE ENDS===================>
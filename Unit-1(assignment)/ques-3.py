# Name = Anveshna | Roll no. = 2501010130
# Assignment: Unit 1 - Tower of Hanoi
# <==============CODE STARTS===========================>

def tower_of_hanoi(n, source, auxiliary, destination):
    # Recursive function to solve Tower of Hanoi.
    # n: Number of disks
    # source: The starting peg (A)
    # auxiliary: The middle peg (B)
    # destination: The target peg (C)
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return 1
    
    # Step 1: Move n-1 disks from Source to Auxiliary
    count1 = tower_of_hanoi(n-1, source, destination, auxiliary)
    
    # Step 2: Move the nth (largest) disk to Destination
    print(f"Move disk {n} from {source} to {destination}")
    
    # Step 3: Move n-1 disks from Auxiliary to Destination
    count2 = tower_of_hanoi(n-1, auxiliary, source, destination)
    
    return count1 + 1 + count2

def main():
    print("--- PART 2: TOWER OF HANOI ---")
    
    n = int(input("Enter number of disks (N=3 for manual trace): "))
    
    print(f"\nMove Sequence for N={n}:")
    print("-" * 30)
    total_moves = tower_of_hanoi(n, 'A', 'B', 'C')
    print("-" * 30)
    print(f"Total moves required: {total_moves}")

if __name__ == "__main__":
    main()
# <===============CODE ENDS==========================>
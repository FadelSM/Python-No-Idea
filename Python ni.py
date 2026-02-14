import sys

def solve():
    # Read n and m
    try:
        line1 = sys.stdin.readline().split()
        if not line1:
            return
        n, m = map(int, line1)
        
        # Read the main array
        array = list(map(int, sys.stdin.readline().split()))
        
        # Read set A and set B
        # Converting these to sets is vital for O(1) lookup time
        set_a = set(map(int, sys.stdin.readline().split()))
        set_b = set(map(int, sys.stdin.readline().split()))
        
        happiness = 0
        
        # Calculate happiness
        for num in array:
            if num in set_a:
                happiness += 1
            elif num in set_b:
                happiness -= 1
                
        print(happiness)
        
    except EOFError:
        pass

if __name__ == "__main__":
    solve()

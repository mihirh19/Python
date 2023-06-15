T = int(input())  # Read the number of test cases

for _ in range(T):
    N, B = map(int, input().split())  # Read N and B
    A = list(map(int, input().split()))  # Read the array elements
    
    found = False  # Initialize found as false
    
    for i in range(N-1):
        for j in range(i+1, N):
            if (A[i] & A[j]) == B:  # Check if the bitwise AND equals B
                found = True
                break
        
        if found:
            break
    
    if found:
        print("YES")
    else:
        print("NO")

N = int(input("Enter the number of stars: "))

# Pattern 1  
for i in range(0, N):                  # Time Complexity: O(N^2)
    for j in range(0, N):              # Space Complexity: O(1)
        print("*",end="")
    print("")
      

for i in range(0, N):                  # Time Complexity: O(N)
    print("*" * N)                     # Space Complexity: O(1)
    i = i + 1


# Pattern 2
for i in range(0, N): 
    for j in range(0, i + 1):          # Time Complexity: O(N^2)  
        print("*",end="")              # Space Complexity: O(1)
    print("")  
 


for i in range(1, N+1):                # Time Complexity: O(N)
    print("*" * i)                     # Space Complexity: O(1)
    i = i + 1


# Pattern 3
for i in range(1,N+1):
    for j in range(1, i+1):              # Time Complexity: O(N^2)
        print(j, end="")               # Space Complexity: O(1)
    print("") 
    


# Pattern 4
for i in range(1,N+1):
    for j in range(1, i + 1):          # Time Complexity: O(N^2)
        print(i, end="")               # Space Complexity: O(1)
    print("")


# Pattern 5
for i in range(0, N):
    for j in range(0, N - i):          # Time Complexity: O(N^2)
        print("*", end="")             # Space Complexity: O(1)
    print("")


for i in range(N, 0, -1):              # Time Complexity: O(N)
    print("*" * i)                     # Space Complexity: O(1)
    i = i - 1   


# Pattern 6
for i in range(N,0,-1):                # Time Complexity: O(N^2)
    for j in range(1, i + 1):          # Space Complexity: O(1)
        print(j, end="")
    print("")


# Pattern 7
for i in range(1, N + 1):
    for j in range(1, N - i + 1):      # Time Complexity: O(N^2)
        print(" ", end="")             # Space Complexity: O(1)
    for j in range(1, 2 * i):
        print("*", end="")
    print("")


# Pattern 8
for i in range(N, 0, -1):
    for j in range(1, N - i + 1):      # Time Complexity: O(N^2)
        print(" ", end="")             # Space Complexity: O(1)
    for j in range(1, 2 * i):
        print("*", end="")
    print("")


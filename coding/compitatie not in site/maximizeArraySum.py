# You are given an array A consisting of N elements and an integer K. You can perform the following operation on the array any number of times(including zero).

# Choose an element from A. Let us denote it by Ai.
# Choose a positive integer Y. 
# Change Ai to Ai XOR Y.
# The sum of all the Y's used in the operations should not be greater than K.

# Task

# Your task is to calculate the maximum sum of all the elements of array A after applying the operations.

# Example

# Assumptions

# N = 3
# K = 7
# A = [2, 4, 3]
# Approach

# In the first operation, choose the second element and Y = 3. Change 4 to 4 XOR 3, which would be 7. The updated array would be A = [2, 7, 3]
# In the second operation, choose the first element and Y = 4. Change 2 to 2 XOR 4, which would be 6. The updated array would be A = [6, 7, 3]
# The sum of all the Y's used is 7, which is not greater than K. Hence, the maximum sum of the array we could get would be 16. 

# Function description

# Complete the solve function provided in the editor. This function takes the following parameter and returns the answer:

# N: Represents the size of the array.
# K: Represents the number K according to the problem statement
# A: Represents an array of integers of size N
# Input format

# Note: This is the input format that you must use to provide custom input (available above the Compile and Test button).

# The first line contains an integer T denoting the number of test cases. T also denotes the number of times you have to run the solve function on a different set of inputs.
# For each test case:
# The first line contains an integer N denoting the size of the array.
# The second line contains an integer K.
# The third line contains N space-separated integers denoting the array A.
# Output format

# For each test case, print the answer on a new line.

# Constraints

# 1≤T≤10

# 1≤N≤105

# 1≤K≤1018

# 1≤A[i]≤1012

# Code snippets (also called starter code/boilerplate code)

# This question has code snippets for C, CPP, Java, and Python.

# Sample input 1
# Copy
# 2558 7 1 8 2569 7 7 4 3
# Sample output 1
# Copy
# 3136
# Explanation
# The first line represents the number of test cases, T = 2

# The first test case

# Given

# N = 5
# K = 5
# A = [8, 7, 1, 8, 2]
# Approach

# In the second operation, choose the first element and Y = 5. Change 8 to 8 XOR 5, which would be 13. The updated array would be A = [13, 7, 1, 8, 2]
# The sum of all the Y's used is 5, which is not greater than K. Hence, the maximum sum of the array we could get would be 31. 

# The second test case

# Given

# N = 5
# K = 6
# A = [9, 7, 7, 4, 3]
# Approach

# In the first operation, choose the fourth element and Y = 2. Change 4 to 4 XOR 2, which would be 6. The updated array would be A = [9, 7, 7, 6, 3]
# In the second operation, choose the fifth element and Y = 4. Change 3 to 3 XOR 4, which would be 7. The updated array would be A = [9, 7, 7, 6, 7]
# The sum of all the Y's used is 6, which is not greater than K. Hence, the maximum sum of the array we could get would be 36. 


def func(num,list_len):
    # returns all possible combinations which creates the num
    dm = [None]*(num+1)
    for i in range(num+1): 
        dm[i] = [[i]]

    for i in range(1,num+1):
        for j in range(1,num+1):
            if i+j <= num:
                for k in dm[i]:
                    v = k.copy()
                    v.append(j)
                    dm[i+j].append(v.copy())

    ans = set()
    for v in dm[-1]:
        v.sort()
        ans.add(tuple(v))

    ans = [list(x) for x in ans]

    # ans = [x for x in ans if len(x)<=list_len]

    return ans


def get_max_sum(arr,num):
    ans = func(num,len(arr))

    max_sum = float("-inf")

    for a in ans:
        aux = arr.copy()
        for i in range(len(a)):
            index = i%len(aux)
            aux[index] = aux[index] ^ a[i]
        max_sum = max(max_sum,sum(aux))

    print(max_sum)

T = 3
a = [[2, 4, 3],[8,7,1,8,2],[9,7,7,4,3]]
n = [7,5,6]
for i in range(T):
    get_max_sum(a[i],n[i])



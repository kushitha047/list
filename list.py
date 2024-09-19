***
Write a program to print the given list in reverse order.
Sample Input:
10 20 30 40 50
Sample Output:
50 40 30 20 10 
***
# Read the list elements from the input line
elements = list(map(int, input().split()))

# Reverse the list
reversed_elements = elements[::-1]

# Print the reversed list elements space-separated followed by "program"
print(" ".join(map(str, reversed_elements)), "program")

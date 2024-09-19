***
Write a program to create a list and display it. 
Input format:
Input consist of n+1 integers
First integer corresponds to the size of the list
Next n inputs corresponds to the elements in the list 
Output format: 
Output is an integer list
Sample Input
4 
1
2
3
4
Output
1 2 3 4
***
# Read the size of the list
size = int(input())

# Initialize an empty list
elements = []

# Read the next `size` number of elements and append them to the list
for _ in range(size):
    element = int(input())
    elements.append(element)

# Print the list elements space-separated followed by "program"
print(" ".join(map(str, elements)), "program")

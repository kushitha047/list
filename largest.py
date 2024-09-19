***
Write a Python Program to find the largest number in a list
Input & Output Format:
Input consists of one list and one integer.
First input consists of a size of a list.
Second inputs corresponds to the size of the list.
Output consists of the largest element.
Sample Input:
5
1
2
3
6
5
Sample Output:
6
***
# Read the size of the list
size = int(input())

# Initialize an empty list
elements = []

# Read the next `size` number of elements and append them to the list
for _ in range(size):
    element = int(input())
    elements.append(element)

# Find the largest number in the list
largest_number = max(elements)

# Print the largest number followed by "program"
print(largest_number, "program")

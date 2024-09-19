***
Write a Python Program to find the smallest number in a list
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
1
***
# Read the size of the list
size = int(input())

# Initialize an empty list
elements = []

# Read the next `size` number of elements and append them to the list
for _ in range(size):
    element = int(input())
    elements.append(element)

# Find the smallest number in the list
smallest_number = min(elements)

# Print the smallest number followed by "program"
print(smallest_number, "program")

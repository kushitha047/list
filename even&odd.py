***
)Write a Python Program to put the even and odd elements in a list into two different lists.
Input format:
Input consists of one integer and one list.
First input consists of the size of the list.
Second input consists of the elements based on the size.
Output format:
Output consists of two lists.
First list consists of all the even numbers in the list.
Second list consists of all the odd numbers in the list.
Sample Input:
5
1
2
3
6
5
Sample Output:
The even list [2, 6]
The odd list [1, 3, 5]
***
# Read the size of the list
size = int(input())

# Initialize an empty list to store the elements
elements = []

# Read the next `size` number of elements and append them to the list
for _ in range(size):
    element = int(input())
    elements.append(element)

# Separate the elements into even and odd lists
even_list = [x for x in elements if x % 2 == 0]
odd_list = [x for x in elements if x % 2 != 0]

# Print the results in the required format
print("The even list", even_list)
print("The odd list", odd_list)

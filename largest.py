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
size = int(input())
elements = []
for _ in range(size):
    element = int(input())
    elements.append(element)
largest_number = max(elements)
print(largest_number, "program")

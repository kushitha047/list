***
Write a program to sort the given list and print it.
Sample Input:
30 20 10 50 40
Sample Output:
10 20 30 40 50 
***
elements = list(map(int, input().split()))
sorted_elements = sorted(elements)
print(" ".join(map(str, sorted_elements)), "program")

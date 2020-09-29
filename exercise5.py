# Given two list generate a new one that contains all common elements in the two list, witouth duplicate
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
c = [element for element in a if element in b and element not in c]

print(c)

# Write a program (function!) that takes a list and returns a new list that contains 
# all the elements of the first list minus all the duplicates.

# Extras:

# Write two different functions to do this - one using a loop and constructing a list, 
# and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.
list = ["Michele", "Robin", "Sara", "Michele"]
def removeDuplicates(list):
    return set(list)

def removeDuplicates_list(list):
    newList = []
    for  x in range(len(list)):
        if list[x] not in newList:
            newList.append(list[x])

    return newList

if __name__ == "__main__":
    print(removeDuplicates(list))
    print(removeDuplicates_list(list))


#create a list of characters
list1 = ['u', 'm', 'e', 'r']

#print("character: ",char_list[0])

# strings --> lists
# so the characters of string --> characters in list

# Print each character of the list using a loop
x = 0
for char in list1:
    print(list1[x])
    x +=1

# Print the size of list
print("size of list1: ", x)

# Concatenate two lists together without using a function
list2 = ['k', 'h', 'a', 'n']
concatenated_lists = print("concatenated list: ",list1 + list2)

# print reversed list
print("Reversed list:", list(reversed(list1)))
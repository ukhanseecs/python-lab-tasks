string_input = input("first string: ")
count =0
# Print each character of a string using a loop

for letter in string_input:
    print(letter)
    count += 1

# Print the size of a string
print("size of string: ",count)

# Concatenate two strings together without using a function
string_input2 = input("second string: ")
concatenated_string = print(string_input + "",string_input2)

# print reversed string
def reversed_string(string_input):
    result= ""
    for char in string_input:
        result = char + result
    return result

reversed_string = reversed_string(string_input)
print("reversed string = ", reversed_string)

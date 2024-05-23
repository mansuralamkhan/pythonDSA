def reverse_string(str):

    reverse_string = str[::-1]

    return reverse_string

print("Input your string")
input_string = input()
reversed_string_output = reverse_string(input_string)
print("Reversed string", reversed_string_output)
new = reversed_string_output[::-1]
print(new)
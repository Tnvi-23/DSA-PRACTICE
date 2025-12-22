def reverse_string(s):
    result = ""
    for char in s:
        result = char + result
    return result

text = input("Enter string: ")
print(reverse_string(text))   # ivnaT
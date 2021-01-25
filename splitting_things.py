panagram = "The quick brown fox jumps over the lazy dog"
other = " elephant"

print(panagram)
print(other)
separators = "."

new_string = separators.join(panagram)
print(new_string)

split_string= new_string.split()
print(split_string)

for index, value in enumerate(split_string):
    print(index + 1)
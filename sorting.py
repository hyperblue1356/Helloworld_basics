pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)
print(letters)
numbers = [1.4, 2.5, 5.6, 4.3, 3.8]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

numbers.sort()
print(numbers)

missing_letter = sorted("The quick brown fox jumped over the lazy dog",
                        key=str.casefold)
print(missing_letter)
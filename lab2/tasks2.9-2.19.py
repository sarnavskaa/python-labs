# task nr 2.9


word = input("enter some word: ")
line = input("enter line: ")

first_letters = ''
last_letters = ''
words = []
words_sum = 0
max_len = 0
max_word_len = ''

if len(line) > 0:
    words = line.split()

for single_word in words:

    if max_len <= len(single_word):
        max_len = len(single_word)
        max_word_len = single_word

    words_sum += len(single_word)
    first_letters += single_word[0]
    last_letters += single_word[len(single_word) - 1]

print()

# task nr 2.10
print("TASK 2.10 result: ", end='')
print("your line has %d words" % len(words))

# task nr 2.11
check_word = word.split()  # check if entered word is single word
if len(word) > 0 and check_word.__len__() == 1:
    print("TASK 2.11 result: ", end='')
    for character in range(0, len(word) - 1):
        print(word[character], end='_')
    print(word[len(word) - 1])

# task nr 2.12
print("TASK 2.12 result: ", end='')
print("first letters word: %s" % first_letters)
print("\t\t\t\t  last letters word: %s" % last_letters)

# task nr 2.13
print("TASK 2.13 result: ", end='')
print("words sum is %d " % words_sum)

# task nr 2.14
print("TASK 2.14 result: ", end='')
print("the longest word is %s and length of it is %d" % (max_word_len, max_len))

# task nr 2.15
array = [12, 23, 1, 33, 45, 20]
result = ''
print("\nTASK 2.15 test array:", array)
for num in array:
    result += "".join(str(num))
assert result == "12231334520"
print("TASK 2.15 result: ", end='')
print(result, end='')

# task nr 2.16
test_line = "text which is contain GvR"
print("\n\nTASK 2.16 this is test line to check replace function before changes: ", test_line)
if test_line.__contains__("GvR"):
    test_line = test_line.replace("GvR", "Guido van Rossum")
    assert test_line == "text which is contain Guido van Rossum"
    print("TASK 2.16 result: ", end='')
    print("this is line after replacement:", test_line)


# task nr 2.17
print("\nTASK 2.17 result: ", end='')
print("words are sorted alphabetically:", sorted(words))
print("\t\t\t\t  words sorted by length:", sorted(words, key=len))

# task nr 2.18
value = 1230000045902
value2 = 12301
value3 = 12
print("\nTASK 2.18 eg values is %d, %d, %d " % (value, value2, value3))
print("TASK 2.18 result: ", end='')
print("test value1 contains %d zeroes" % str(value).count("0"))
print("\t\t\t\t  test value2 contains %d zeroes" % str(value2).count("0"))
print("\t\t\t\t  test value3 contains %d zeroes" % str(value3).count("0"))

# task nr 2.19

"""def countOccurences(str, char):
    a = str.split(" ")
    count = 0
    for i in range(0, len(a)):
        if (char == a[i]):
            count = count + 1
    return count
str = "tejaa "
char = "portal"
print(countOccurences(str, char))"""
def countOccurences(str, word):

    # split the string by spaces in a
    a = str.split(" ")

    # search for pattern in a
    count = 0
    for i in range(0, len(a)):

        # if match found increase count
        if (word == a[i]):
           count = count + 1

    return count

# Driver code
str ="teja got in conference with teja "
word ="teja"
print(countOccurences(str, word))
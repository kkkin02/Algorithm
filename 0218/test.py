def pal(word):
    l = len(word)
    while l > 1:
        if word[0] != word[-1]:
            return False
        l -= 2
        word = word[1:-1]
    return True

string = 'asdfdsa'
word = string[1:6]
print(pal(word))
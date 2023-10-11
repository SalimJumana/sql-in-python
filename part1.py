# test if a word is a palindrome
def is_palindrome(word):
    word = word.strip().lower()
    rev_word = reversed(word)

    if list(word) == list(rev_word):
        print(True)
    else:
        print(False)

is_palindrome("Apple ")

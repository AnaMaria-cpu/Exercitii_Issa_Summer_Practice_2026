# 5. Write a function that checks whether a string contains special characters (\r, \t, \n, \a, \b, \f, \v)
def check_sc(text: str):
    special_char=['\r', '\t', '\n', '\a', '\b', '\f', '\v']
    for char in text:
        if char in special_char:
            return True
    return False



print(check_sc('hello\\\r world'))
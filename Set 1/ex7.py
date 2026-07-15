# 7. Write a function that receives a char_len integer and a variable number of strings
# and checks that each two neighboring strings follow the following rule:
# the second string starts with the last char_len characters of the first string (like the word game pheasant).
def check_fazan(char_len, *cuvinte):
    for i in range(len(cuvinte) - 1):
        final_cuv_before = cuvinte[i][-char_len:]
        inceput_cuv_after = cuvinte[i+1][:char_len]
        if final_cuv_before != inceput_cuv_after:
            return False

    return True


print(check_fazan(3, 'ana', 'analog', 'logaritm'))
print(check_fazan(2, 'sare', 'remiza', 'ana'))

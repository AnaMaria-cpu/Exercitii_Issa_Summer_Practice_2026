# 6. Write a function that converts a string of characters written in UpperCamelCase into snake_case.
def camel_to_snake(text):
    string_converted = ''

    for i in range(len(text)):
        letter = text[i]

        if letter.isupper() and i != 0:
            string_converted= string_converted + "_"

        string_converted = string_converted + letter.lower()

    return string_converted


print(camel_to_snake('AnaMaria'))


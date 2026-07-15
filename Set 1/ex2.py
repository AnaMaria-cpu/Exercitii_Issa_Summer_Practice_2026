# 2. Write a function that calculates how many vowels are in a string.

def nr_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    contor = 0
    for i in text:
        if i in vowels:
            contor += 1
    return contor


text = 'hanna montana'

print(f' Number of vowels in -{text}- is {nr_vowels(text)}')

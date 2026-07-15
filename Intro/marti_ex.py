# 5.	Print how many digits does 2^1024 have.
# HINT: Convert to string and check the length of the string.
#
a5 = 2 ** 1024
a5 = str(a5)
nr_of_digits = len(a5)
print('\n Exercise 5')
print(f' 2^1024 has {nr_of_digits} digits.')


# 6.	Write a function that takes 3 numeric arguments and
# return the highest one without using the max() function.

def maxim_number(a: int, b: int, c: int) -> int:
    maximum = a
    if b > maximum:
        maximum = b
    if c > maximum:
        maximum = c
    return maximum


print('\n Exercise 6')
print(f' The highest is maxim_number(5, 2, 3)')


# 7.	Write a function that takes 3 arguments.
# The first 2, "x" and "y" are numbers.
# The 3rd, "op" is a string that is one of "+", "-", "/", "*".
# Return the operation denoted by "op" computed on "x" and "y".
# E.g. If “op” is "+" return the sum of "x" and "y".
# HINT: Use "elif".

def select_operation(x, y, op):
    """
    Return the operation denoted by "op" computed on "x" and "y".
     E.g. If “op” is "+" return the sum of "x" and "y".
    """
    if op == '+':
        return str(x + y)
    elif op == '-':
        return str(x - y)
    elif op == '*':
        return str(x * y)
    elif op == '/':
        if y == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return str(x / y)
    else:
        raise ValueError('The operator must be one of: "+", "-", "*", "/".')


x = 5
y = 7
op = '-'
print('\n Exercise 7')
print(f' The result of {x} {op} {y} is {select_operation(x, y, op)}')


# 8.	Write a function that takes 1 numeric argument and checks
# if it is a palindrome.

def check_palindrome(num_arg: int) -> bool:
    num_arg = str(num_arg)
    if num_arg == num_arg[::-1]:
        return True
    else:
        return False


num_arg = 515
print('\n Exercise 8')
print(f' The affirmation that "{num_arg} is a palindrome" is {check_palindrome(num_arg)}')


# 9.	Write a function that takes 1 numeric argument and checks if it is a prime
def check_prime(nr: int) -> bool:
    """Return True if number is prime."""
    if nr < 2:
        return False
    divisor = 2
    while divisor ** 2 <= nr:
        if nr % divisor == 0:
            return False
        divisor += 1
    return True


nr = 23
print('\n Exercise 9')
if check_prime(nr):
    print(f'The number {nr} is prime.')
else:
    print(f'The number {nr} is not prime.')


# 10.	Write a function that takes 1 list argument
# and prints its elements using a for loop.
def fct_print(lista: list):
    """Print the list."""
    print('\n Exercise 10')
    print(f'The list: {lista}')
    print(f'The elements: ')
    for num in lista:
        print(num, end=' ')


lista = [2, 3, 4, 7, 233, 9, 564]
fct_print(lista)

# 11. Write a function that takes 1 list of numbers as an argument and
# returns the mean and geometric mean of the largest and smallest element.
print('\n \n Exercise 11')


def fxt_mean_geom(lista_nr: list):
    """Calculate the mean/geometric mean of lista_nr."""
    if len(lista_nr) == 0:
        raise ValueError("The list cannot be empty.")
    l = len(lista_nr)
    smallest = min(lista_nr)
    highest = max(lista_nr)

    media = (smallest + highest) / 2
    print(f' The media of {smallest} and {highest} is: {media}')

    geom = (smallest * highest) ** (1 / 2)
    print(f' The geometric mean of {smallest} and {highest} is: {geom}')


fxt_mean_geom(lista)


# 12.Write a function that takes 1 list of numbers as an argument and returns the largest
# element in the 1st half of the list and the smallest element in the 2nd half of the list.
# HINT: Use min(), max(), slicing.
def fct_slicing(lista12: list):
    """ The function returns the largest element in the 1st half of the list and the smallest element in the 2nd half of the list."""
    if len(lista12) < 2:
        raise ValueError("The list must contain at least two elements.")
    # For an odd - sized list, the middle element is included in the second half.
    middle = len(lista12) // 2
    first_half = lista12[:middle]
    second_half = lista12[middle:]
    return max(first_half), min(second_half)


lista12 = [1, 89, 34, 10, 2, 7, 8, 45, 3]
print('\n Exercise 12')
print(f' The highest of the first half and the smallest of the second half are : {fct_slicing(lista12)}')


# 13. Write a function that takes 1 list of numbers as an argument and returns
# another list containing only the palindromes with an even number of digits.
# HINT: Use what you made/learned for exercises 3 and 6.
def even_digit_palindromes(values: list):
    """
    Return a list containing only non-negative integer palindromes
    with an even number of digits.
    """
    result = []

    for value in values:
        if check_palindrome(value) and len(str(value)) % 2 == 0:
            result.append(value)

    return result

lista13=[1,3,3443,22,656,90]

print('\n Exercise 13')
print(lista13)
print(f'Non-negative integer palindromes with an even number of digits are : {even_digit_palindromes(lista13)}')


# 14. Write a function that takes 1 list of numbers as an argument, calculates the positions of the smallest and largest elements,
# and returns the sublist between the smallest and largest elements.
# WARNING: Be careful in case the largest element appears before the smallest one.
# HINT: Use min(), max(), list methods, slicing.
def take_sublist(listaa: list):
    if len(listaa) == 0:
        raise ValueError("The list cannot be empty.")
    smallest14 = min(listaa)
    highest14 = max(listaa)
    contor = 0
    sublist = []
    for num in listaa:
        contor += 1
        if num == smallest14:
            contor_mic = contor
        if num == highest14:
            contor_mare = contor
    if contor_mic < contor_mare:
        sublist = listaa[contor_mic:contor_mare-1]
    else :
        sublist = lista[contor_mare:contor_mic-1]
    return sublist
print('\n Exercise 14')
print(lista)
print(f' The smallest number is {min(lista)} and the highest is {max(lista)}')
print(f' The sublist between the smallest and highest numbers is : {take_sublist(lista)}')

# 15. Write a function that takes a list of lists of numbers, representing a square matrix and returns
# a list containing the elements of the main diagonal sorted in descending order.
def sorted_main_diagonal(matrix: list):
    """
    :param matrix: list of lists of numbers representing a square matrix
    :return: a list containing the elements of the main diagonal sorted in descending order
    """
    size = len(matrix)

    if size == 0:
        return []

    for row in matrix:
        if len(row) != size:
            raise ValueError("The matrix must be square.")

    diagonal = []

    for i in range(size):
        diagonal.append(matrix[i][i])

    return sorted(diagonal, reverse=True)
example_matrix = [
    [4, 2, 3],
    [1, 9, 5],
    [7, 8, 6]
]

print("\n Exercise 15:", sorted_main_diagonal(example_matrix))
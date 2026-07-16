# Fie un dictionar global
# {
#    "+": lambda a, b: a + b,
#    "*": lambda a, b: a * b,
#    "/": lambda a, b: a / b,
#    "%": lambda a, b: a % b
# }
# Sa se construiasca o functie apply_operator(operator, a, b) care va aplica peste a si b regula specificata de dictionarul global.
# Sa se implementeze astfel incat, in cazul adaugarii unui operator nou, sa nu fie necesara modificarea functiei.
#

operators = {
    "+": lambda a, b: a + b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "%": lambda a, b: a % b
}


def apply_operator(operator, a, b):
    if operator in operators:
        return operators[operator](a, b)

    return "Invalid operator"


print(apply_operator("+", 10, 5))
print(apply_operator("^", 10, 5))
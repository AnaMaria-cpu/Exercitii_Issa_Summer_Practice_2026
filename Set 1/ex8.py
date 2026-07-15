# 8. Given a string that represents a polynomial
# (Ex: "3x ^ 3 + 5x ^ 2 - 2x - 5") and a number (int or float).
# Evaluate the polynomial for the given value.

def eval_polynom(polynom,x):
    polynom = polynom.replace(' ', '')
    polynom = polynom.replace('-','+-')
    termeni = polynom.split("+")
    rezultat = 0

    for termen in termeni:
        if termen == "":
            continue

        if "x" in termen:
            parti = termen.split("x")
            coeficient_text = parti[0]

            if coeficient_text == "":
                coeficient = 1
            elif coeficient_text == "-":
                coeficient = -1
            else:
                coeficient = float(coeficient_text)

            if "^" in termen:
                exponent = int(termen.split("^")[1])
            else:
                exponent = 1

            rezultat = rezultat + coeficient * x ** exponent
        else:
            rezultat = rezultat + float(termen)

    return rezultat

print(eval_polynom("3x ^ 3 + 5x ^ 2 - 2x - 5", 2))
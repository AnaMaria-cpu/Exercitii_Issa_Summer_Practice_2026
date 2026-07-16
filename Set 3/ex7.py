# Fie un dictionar global definit asemanator cu cel de la ex6, cu deosebirea ca
# functiile date ca valori ale dictionarului poate primi orice combinatie de parametri.
# Sa se scrie o functie apply_function care primeste ca parametru numele unei operatii si
# aplica functia corespunzatoare peste argumentele primite.
# Sa se implementeze astfel incat, in cazul adaugarii unei functii noi, sa nu fie necesara modificarea functiei apply_function.
# Un exemplu de dictionar global ar putea fi urmatorul:
# {
#    "print_all": lambda *a, **k: print(a, k),
#    "print_args_commas": lambda *a, **k: print(a, k, sep=", "),
#    "print_only_args": lambda *a, **k: print(a),
#    "print_only_kwargs": lambda *a, **k: print(k)
# }

functions = {
    "print_all": lambda *a, **k: print(a, k),
    "print_args_commas": lambda *a, **k: print(a, k, sep=", "),
    "print_only_args": lambda *a, **k: print(a),
    "print_only_kwargs": lambda *a, **k: print(k)
}


def apply_function(function_name, *args, **kwargs):
    if function_name in functions:
        return functions[function_name](*args, **kwargs)

    return "Invalid function"


apply_function("print_all", 1, 2, 3, name="Ana")
apply_function("print_only_args", 10, 20, 30)
apply_function("print_only_kwargs", city="Iasi", age=21)

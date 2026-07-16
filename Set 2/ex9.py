# 9.Să se scrie o funție ce va ordona o listă de tuple de string-uri în funcție de al 3-lea caracter al celui de-al 2-lea element din tuplă.
# Exemplu: [('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]
def third_character(item):
    return item[1][2]
def sort_tuples(values):
    return sorted(values, key=third_character)
values = [("abc", "bcd"), ("abc", "zza")]
print(sort_tuples(values))
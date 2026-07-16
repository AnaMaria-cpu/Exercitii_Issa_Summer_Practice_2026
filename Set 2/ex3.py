# 3.	Fie un tuplu (x,y) reprezentarea unui punct intr-un sistem cartezian.
# Sa se scrie o functie care primeste ca parametru o lista de puncte si
# returneaza o lista de tuple (a,b,c) unice care reprezinta
# dreptele unice determinate de acele puncte ( (a,b,c) corespunde dreptei ax + by + c = 0).


def cmmdc(x, y):
    x = abs(x)
    y = abs(y)

    while y != 0:
        rest = x % y
        x = y
        y = rest

    return x


def normalize_line(a, b, c):
    common_divisor = cmmdc(a, b)
    common_divisor = cmmdc(common_divisor, c)

    if common_divisor != 0:
        a = a // common_divisor
        b = b // common_divisor
        c = c // common_divisor

    if a < 0 or (a == 0 and b < 0):
        a = -a
        b = -b
        c = -c

    return (a, b, c)


def unique_lines(points):
    lines = []

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x1 = points[i][0]
            y1 = points[i][1]
            x2 = points[j][0]
            y2 = points[j][1]

            if x1 == x2 and y1 == y2:
                continue

            a = y1 - y2
            b = x2 - x1
            c = x1 * y2 - x2 * y1

            line = normalize_line(a, b, c)

            if line not in lines:
                lines.append(line)

    return lines


points = [(0, 0), (1, 1), (2, 2), (0, 1)]
print(unique_lines(points))

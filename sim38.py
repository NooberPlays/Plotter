def f(x):
    return -0.00002 * x ** 6 + 0.0011 * x ** 5 - 0.024 * x ** 4 + 0.24 * x ** 3 - 0.8 * x ** 2 - x + 10

def simpson_3_8(a, b, n):
    h = (b - a) / n
    area = 0

    for i in range(n):
        x0 = a + i * h
        x1 = x0 + h / 3
        x2 = x0 + 2 * h / 3
        x3 = x0 + h

        area += (h / 8) * (f(x0) + 3 * f(x1) + 3 * f(x2) + f(x3))

    return area

# Solicitar entrada al usuario
a = float(input("Set a value for 'a': "))
b = float(input("Set a value for 'b': "))
n = int(input("How many segments (must be pair): "))

# Calcular y mostrar el área aproximada bajo la curva
area_aproximada = simpson_3_8(a, b, n)
print("The approximate area under the curve is:", area_aproximada)

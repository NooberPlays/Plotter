def f(x):
    #Define function 
    return -0.00002 * x ** 6 + 0.0011 * x ** 5 - 0.024 * x ** 4 + 0.24 * x ** 3 - 0.8 * x ** 2 - x + 10

def simpson_1_3(a, b, n):
    h = (b - a) / n
    x = a

    area = f(x)
    x += h

    for i in range(1, n):
        if i % 2 == 0:
            area += 2 * f(x)
        else:
            area += 4 * f(x)
        x += h

    area += f(x)
    area *= h / 3

    return area

#Set intervals
a = float(input("Set a value for 'a': "))
b = float(input("Set a value for 'b': "))
n = int(input("How many segments (must be pair): "))

#Usage
area_aproximada = simpson_1_3(a, b, n)
print("The approximate area under the curve is:", area_aproximada)

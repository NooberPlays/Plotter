import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle, RegularPolygon
from scipy.integrate import quad

def plot_function_with_pattern(func, x_range, y_range, base_size, shape="rectangle", include_touching=True, start_x=None, start_y=None):
    fig, ax = plt.subplots()
    x = np.linspace(x_range[0], x_range[1], 1000)
    y = func(x)

    ax.plot(x, y)

    # Calculate number of figures that fit inside function
    num_figures = 0
    if start_x is None:
        start_x = x_range[0]
    if start_y is None:
        start_y = y_range[0]


    for x_i in np.arange(start_x, x_range[1], base_size):
        for y_i in np.arange(start_y, y_range[1], base_size):
            if func(x_i) >= y_i:
                # Check if the figure is touching the function
                touching = func(x_i + base_size/2) >= y_i or func(x_i + base_size/2) >= y_i + base_size or func(x_i) >= y_i + base_size/2 or func(x_i + base_size) >= y_i + base_size/2
                if include_touching or not touching:
                    # Create shape patch
                    if shape == "rectangle":
                        facecolor = 'red' if not include_touching else 'green'
                        patch = Rectangle((x_i, y_i), base_size, radius=base_size, facecolor=facecolor)
                    elif shape == "triangle":
                        facecolor = 'red' if not include_touching else 'green'
                        patch = RegularPolygon((x_i+base_size/2, y_i), 3, radius=base_size/np.sqrt(3), orientation=0, facecolor=facecolor)
                    elif shape == "square":
                        facecolor = 'red' if not include_touching else 'green'
                        patch = RegularPolygon((x_i+base_size/2, y_i+base_size/2), 4, radius=base_size/np.sqrt(2), orientation=np.pi/4, facecolor=facecolor)
                    elif shape == "hexagon":
                        facecolor = 'red' if not include_touching else 'green'
                        patch = RegularPolygon((x_i+base_size/2, y_i), 6, radius=base_size/np.sqrt(3), orientation=np.pi/2, facecolor=facecolor)
                    ax.add_patch(patch)
                    num_figures += 1

    plt.show()

    # Calculate integral of the function
    integral, _ = quad(func, x_range[0], x_range[1])

    # Subtract the amount of figures touching the function if include_touching is False
    if not include_touching:
        num_figures -= int(integral / base_size**2)
        total = num_figures*-1
        print(f"{total} {shape}(s) are inside the function and NOT TOUCHING the function. The base size was {base_size} unit(s) with x range of: {x_range} and y range of: {y_range}. The area of the function is {integral:.4f}.")
    elif include_touching:
        print(f"{num_figures} {shape}(s) are inside the function and TOUCHING the function. The base size was {base_size} unit(s) with x range of: {x_range} and y range of: {y_range}. The area of the function is {integral:.4f}.")

# Example usage
def func(x):
    return -0.00002*x**6 + 0.0011*x**5 -0.024 *x**4 + 0.24*x**3 -0.8*x**2 -x + 10

plot_function_with_pattern(func, x_range=(0, 19.308), y_range=(0, 17.55), base_size=1, shape="hexagon", include_touching=True)
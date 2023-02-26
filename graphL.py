"""
This code is actually functioning but there are some modifications to be made:

1.- The "include_touching=True" does not seem to work correctly and counts the same figures.
2.- Figures need to be placed in such a way so that each figure is touching at least 2 vertices from another figure.
3.- Find a way to start the patch placement where I decide to
4.- Change the color of the figures touching and outside the function to red
"""
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
                # Create shape patch
                if shape == "rectangle":
                    patch = Rectangle((x_i, y_i), base_size, base_size, facecolor='green')
                elif shape == "triangle":
                    patch = RegularPolygon((x_i+base_size/2, y_i), 3, base_size/np.sqrt(3), orientation=0, facecolor='green')
                elif shape == "square":
                    patch = RegularPolygon((x_i+base_size/2, y_i+base_size/2), 4, base_size/np.sqrt(2), orientation=np.pi/4, facecolor='green')
                elif shape == "hexagon":
                    patch = RegularPolygon((x_i+base_size/2, y_i), 6, base_size/np.sqrt(3), orientation=np.pi/2, facecolor='green')
                # Add patch to plot
                ax.add_patch(patch)
                num_figures += 1
            elif include_touching and func(x_i) == y_i:
                # Create shape patch with transparency
                if shape == "rectangle":
                    patch = Rectangle((x_i, y_i), base_size, base_size, facecolor='red')
                elif shape == "triangle":
                    patch = RegularPolygon((x_i+base_size/2, y_i), 3, base_size/np.sqrt(3), orientation=0, facecolor='red')
                elif shape == "square":
                    patch = RegularPolygon((x_i+base_size/2, y_i+base_size/2), 4, base_size/np.sqrt(2), orientation=np.pi/4, facecolor='red')
                elif shape == "hexagon":
                    patch = RegularPolygon((x_i+base_size/2, y_i), 6, base_size/np.sqrt(3), orientation=np.pi/2, facecolor='red')
                # Add patch to plot
                ax.add_patch(patch)
                num_figures += 1

    plt.show()

    # Calculate integral of the function
    integral, _ = quad(func, x_range[0], x_range[1])

    print(f"{num_figures} {shape}(s) fit inside the function. The base size was {base_size} unit(s) with x range of: {x_range} and y range of: {y_range}. The area of the function is {integral:.4f}.")

# Example usage
def func(x):
    return -0.00002*x**6 + 0.0011*x**5 -0.024 *x**4 + 0.24*x**3 -0.8*x**2 -x + 10

plot_function_with_pattern(func, x_range=(0, 19.308), y_range=(0, 17.55), base_size=1, shape="hexagon", include_touching=True)

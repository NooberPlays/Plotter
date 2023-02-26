import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

def plot_function_with_pattern(func, x_range, y_range, base_size, include_touching=True):
    fig, ax = plt.subplots()
    x = np.linspace(x_range[0], x_range[1], 1000)
    y = func(x)

    ax.plot(x, y)

    # Calculate number of figures that fit inside function
    num_figures = 0
    for x_i in np.arange(x_range[0], x_range[1], base_size):
        for y_i in np.arange(y_range[0], y_range[1], base_size):
            if func(x_i) <= y_i:
                # Create rectangle patch
                rect = Rectangle((x_i, y_i), base_size, base_size)
                # Add patch to plot
                ax.add_patch(rect)
                num_figures += 1
            elif include_touching and func(x_i) == y_i:
                # Create rectangle patch with transparency
                rect = Rectangle((x_i, y_i), base_size, base_size, alpha=0.5)
                # Add patch to plot
                ax.add_patch(rect)
                num_figures += 1

    plt.show()
    print(f"{num_figures} figures fit inside the function. The base size was {base_size} with x range of: {x_range} and y range of: {y_range}")

# Example usage
def func(x):
    return -0.00002*x**6 + 0.0011*x**5 -0.024*x**4 + 0.24*x**3 -0.8*x**2 -x + 10

plot_function_with_pattern(func, x_range=(0, 19.308), y_range=(0, 17.55), base_size=1, include_touching=True)

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle, RegularPolygon
from scipy.integrate import quad

def plot_function_with_pattern(func, x_range, y_range, base_size=1,  num_vertices=4, face_col='green', edge_col='black'):
    shape_dict = {
        3: {    # triangle
            'radius': base_size/np.sqrt(3),
            'orientation': 0,
            'rotation': np.pi,  # rotation every two columns
            'y_offset': base_size/(2*np.sqrt(3)),  # y_offset every two columns
            'base_step_x': base_size/2,
            'base_step_y': np.sqrt(3)*base_size/2
        },
        4: {    # square
            'radius': base_size/np.sqrt(2),
            'orientation': np.pi/4
        },
        6: {    # hexagon
            'radius': base_size/2,
            'orientation': np.pi/2,
            'y_offset': np.sqrt(3)*base_size/4,  # y_offset every two columns
            'base_step_x': 3*base_size/4,
            'base_step_y': np.sqrt(3)*base_size/2
        }
    }
    if not num_vertices in shape_dict:
        print(f"Error: polygon with {num_vertices} vertices are not supported.")
        return
    
    fig, ax = plt.subplots()
    x = np.linspace(x_range[0], x_range[1], 1000)
    y = func(x)

    ax.plot(x, y)

    num_figures = 0
    base_step_x = shape_dict[num_vertices].get('base_step_x', base_size)
    base_step_y = shape_dict[num_vertices].get('base_step_y', base_size)
    radius = shape_dict[num_vertices]['radius']
    orientation = shape_dict[num_vertices]['orientation']
    y_start = shape_dict[num_vertices].get('y_offset', base_size/2) # align height of the first shape base with 0

    for i, x_i in enumerate(np.arange(x_range[0], x_range[1], base_step_x)):
        y_offset = y_start
        orient = orientation
        if (i % 2 != 0):
            y_offset += shape_dict[num_vertices].get('y_offset', 0)
            orient += shape_dict[num_vertices].get('rotation', 0)
        for y_i in np.arange(y_range[0] + y_offset, y_range[1] + y_offset, base_step_y):
            patch = RegularPolygon((x_i, y_i), num_vertices, radius=radius, orientation=orient, fc=face_col, ec=edge_col)
            if patch.contains_point((x_i, func(x_i)), radius=1e-9):  # omitting radius triggers a mpl bug
                ax.add_patch(patch)
                num_figures += 1
                break  
            else:
                ax.add_patch(patch)
                num_figures += 1

    # Calculate integral of the function
    integral, _ = quad(func, x_range[0], x_range[1])

    # Subtract the amount of figures touching the function if include_touching is False
    print(f"{num_figures} polygons with {num_vertices} vertices are inside the function or touching the function. The base size was {base_size} unit(s) with x range of: {x_range} and y range of: {y_range}. The area of the function is {integral:.4f}.")
    
    plt.show()

# Example usage
def func(x):
    return -0.00002*x**6 + 0.0011*x**5 -0.024 *x**4 + 0.24*x**3 -0.8*x**2 -x + 10

plot_function_with_pattern(func, x_range=(0, 19.308), y_range=(0, 17.55), base_size=.01, num_vertices=6)
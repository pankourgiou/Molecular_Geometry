import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def get_geometry_and_coords(bonded_atoms, lone_pairs):
    total_regions = bonded_atoms + lone_pairs

    if total_regions == 2:
        return "Linear", [(0, 0, 0), (1, 0, 0), (-1, 0, 0)]
    elif total_regions == 3:
        if lone_pairs == 0:
            return "Trigonal planar", [(0, 0, 0), (1, 0, 0), (-0.5, 0.866, 0), (-0.5, -0.866, 0)]
        elif lone_pairs == 1:
            return "Bent", [(0, 0, 0), (1, 0, 0), (-1, 0, 0)]
    elif total_regions == 4:
        if lone_pairs == 0:
            return "Tetrahedral", [
                (0, 0, 0),
                (1, 1, 1),
                (-1, -1, 1),
                (-1, 1, -1),
                (1, -1, -1)
            ]
        elif lone_pairs == 1:
            return "Trigonal pyramidal", [
                (0, 0, 0),
                (1, 0, -1),
                (-1, 0, -1),
                (0, 1, 1)
            ]
        elif lone_pairs == 2:
            return "Bent", [(0, 0, 0), (1, 1, 0), (-1, 1, 0)]
    elif total_regions == 5:
        if lone_pairs == 0:
            return "Trigonal bipyramidal", [
                (0, 0, 0),
                (1, 0, 0),
                (-1, 0, 0),
                (0, 1, 0),
                (0, -1, 0),
                (0, 0, 1)
            ]
    elif total_regions == 6:
        if lone_pairs == 0:
            return "Octahedral", [
                (0, 0, 0),
                (1, 0, 0),
                (-1, 0, 0),
                (0, 1, 0),
                (0, -1, 0),
                (0, 0, 1),
                (0, 0, -1)
            ]

    return "Unknown", []

def draw_molecule(coords, geometry):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title(f"Molecular Geometry: {geometry}")

    # Draw atoms
    for i, (x, y, z) in enumerate(coords):
        color = 'red' if i == 0 else 'blue'  # Central atom red, others blue
        ax.scatter(x, y, z, color=color, s=200)

    # Connect central atom to others
    for (x, y, z) in coords[1:]:
        ax.plot([coords[0][0], x], [coords[0][1], y], [coords[0][2], z], 'k--')

    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-2, 2])
    plt.show()

# Input section
try:
    bonded = int(input("Enter number of bonded atoms: "))
    lone = int(input("Enter number of lone pairs: "))
    geometry, coords = get_geometry_and_coords(bonded, lone)
    print(f"The molecular geometry is: {geometry}")

    if coords:
        draw_molecule(coords, geometry)
    else:
        print("Geometry not visualized.")
except ValueError:
    print("Please enter valid integers.")

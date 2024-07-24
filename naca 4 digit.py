import numpy as np

def naca_airfoil(naca_number, num_points=100):
    # Extract NACA parameters from the digits
    m = int(naca_number[0]) / 100  # Maximum camber
    p = int(naca_number[1]) / 10    # Location of maximum camber
    t = int(naca_number[2:]) / 100  # Thickness

    # Generate x-coordinates from 0 to 1 along the chord
    x = np.linspace(0, 1, num_points)

    # Calculate the camber line and thickness distribution
    yc = np.where(x < p, m / (p**2) * (2 * p * x - x**2), m / ((1 - p)**2) * ((1 - 2 * p) + 2 * p * x - x**2))
    yt = 5 * t * (0.2969 * np.sqrt(x) - 0.1260 * x - 0.3516 * x**2 + 0.2843 * x**3 - 0.1036 * x**4)

    # Calculate the upper and lower surfaces
    xu = x - yt * np.sin(np.arctan2(yc, x))
    xl = x + yt * np.sin(np.arctan2(yc, x))

    yu = yc + yt * np.cos(np.arctan2(yc, x))
    yl = yc - yt * np.cos(np.arctan2(yc, x))

    # Combine upper and lower surfaces
    x_coords = np.concatenate([xu[::-1], xl])
    y_coords = np.concatenate([yu[::-1], yl])

    return np.column_stack([x_coords, y_coords])

naca_number = input("Input the NACA-4 digit number: ")
naca_coords = naca_airfoil(naca_number, num_points=100)
print(naca_coords)

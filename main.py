import math
import numpy as np
from scipy.optimize import fsolve

# Define the equation as a function of theta (with additional fixed parameters)
def make_equation(x1, y1, V1, V2):
    def equation(theta):
        return x1 * 3 * np.cos(theta) + V1 - y1 * 3 * np.sin(theta) + V2
    return equation

def hittter_mech(target_x0, target_y0, target_vx=None, target_vy=None):
    # Upside is +ve , right is +ve
    shooter_x, shooter_y = 0, 0
    g = 9.8
    v = 3  # m/s

    # Placeholder values for target velocity
    V1 = target_vx if target_vx is not None else 0
    V2 = target_vy if target_vy is not None else 0

    x1 = target_x0
    y1 = target_y0

    # Initial guess (in radians)
    initial_guess = np.radians(45)  # 45 degrees

    # Use fsolve to solve for theta
    theta_solution = fsolve(make_equation(x1, y1, V1, V2), initial_guess)[0]

    # Convert to degrees
    theta_degrees = np.degrees(theta_solution)

    print(f"Theta (radians): {theta_solution}")
    print(f"Theta (degrees): {theta_degrees}")
    return theta_degrees  # optional return

if __name__ == "__main__":
    hittter_mech(1, 1, target_vx=2, target_vy=0)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def simulate_2d_motion_two_balls(pos1, vel1, pos2, vel2, total_time=10, dt=0.1):
    """
    Simulates 2D motion of two objects and visualizes them.

    Parameters:
    - pos1, vel1: numpy arrays [x, y] for object 1
    - pos2, vel2: numpy arrays [x, y] for object 2
    - total_time: total duration of simulation
    - dt: time step
    """
    pos1 = pos1.copy()
    pos2 = pos2.copy()
    vel1 = vel1.copy()
    vel2 = vel2.copy()
    
    num_frames = int(total_time / dt)
    path1 = [pos1.copy()]
    path2 = [pos2.copy()]

    def update(frame):
        nonlocal pos1, pos2
        pos1 += vel1 * dt
        pos2 += vel2 * dt
        path1.append(pos1.copy())
        path2.append(pos2.copy())
        arr1 = np.array(path1)
        arr2 = np.array(path2)
        line1.set_data(arr1[:, 0], arr1[:, 1])
        line2.set_data(arr2[:, 0], arr2[:, 1])
        ball1.set_data([pos1[0]], [pos1[1]])
        ball2.set_data([pos2[0]], [pos2[1]])
        return line1, line2, ball1, ball2

    # Setup plot limits dynamically
    all_x = [pos1[0], pos1[0] + vel1[0]*total_time, pos2[0], pos2[0] + vel2[0]*total_time]
    all_y = [pos1[1], pos1[1] + vel1[1]*total_time, pos2[1], pos2[1] + vel2[1]*total_time]

    fig, ax = plt.subplots()
    ax.set_xlim(min(all_x) - 2, max(all_x) + 2)
    ax.set_ylim(min(all_y) - 2, max(all_y) + 2)
    ax.set_aspect('equal')
    ax.grid()
    plt.title("2D Motion of Two Balls")

    # Create animated objects
    line1, = ax.plot([], [], 'b-', lw=1, label='Object 1')
    line2, = ax.plot([], [], 'r-', lw=1, label='Object 2')
    ball1, = ax.plot([], [], 'bo', markersize=8)
    ball2, = ax.plot([], [], 'ro', markersize=8)

    ani = FuncAnimation(fig, update, frames=num_frames, interval=dt*1000, blit=True)
    ax.legend()
    plt.show()

if __name__ == "__main__":
    # Example usage
    simulate_2d_motion_two_balls(
        pos1=np.array([0.0, 0.0]), 
        vel1=np.array([1.0, 1.5]), 
        pos2=np.array([5.0, 0.0]), 
        vel2=np.array([-1.0, 1.0]), 
        total_time=10, 
        dt=0.05
    )

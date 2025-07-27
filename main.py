import numpy as np
from scipy.optimize import minimize_scalar
from Simulation.ball import simulate_2d_motion_two_balls  # make sure this import path is correct

# Target (moving object)
target_pos = np.array([90.0, 100.0])
target_vel = np.array([-3.0, 4.0])  # moving left

# Shooter (your position)
shooter_pos = np.array([0.0, 0.0])
projectile_speed = 9.0  # you control this

# Function to minimize: distance between positions at time t
def time_to_hit(theta):
    # Projectile direction (unit vector)
    dir_vector = np.array([np.cos(theta), np.sin(theta)])
    
    # Relative velocity
    relative_velocity = projectile_speed * dir_vector - target_vel

    # If relative velocity is too small, can't hit
    if np.linalg.norm(relative_velocity) < 1e-6:
        return 1e6

    # Time to close the gap
    r = target_pos - shooter_pos
    t = np.dot(r, relative_velocity) / np.dot(relative_velocity, relative_velocity)

    if t < 0:
        return 1e6  # can't hit in the past

    # Final positions
    bullet_pos = shooter_pos + projectile_speed * dir_vector * t
    target_final = target_pos + target_vel * t

    # Miss distance
    return np.linalg.norm(bullet_pos - target_final)

# Find optimal angle
res = minimize_scalar(time_to_hit, bounds=(0, np.pi), method='bounded')
theta_opt = res.x

# Corrected direction vector (USE radians here)
dir_vector = np.array([np.cos(theta_opt), np.sin(theta_opt)])
projectile_velocity = dir_vector * projectile_speed  # scale by speed

# Simulate both moving objects
simulate_2d_motion_two_balls(
    pos1=target_pos, vel1=target_vel,
    pos2=shooter_pos, vel2=projectile_velocity,
    total_time=5, dt=0.05
)

print(f"✅ Optimal angle to fire (degrees): {np.degrees(theta_opt):.2f}")
print(f"✅ Minimum miss distance: {res.fun:.6f}")

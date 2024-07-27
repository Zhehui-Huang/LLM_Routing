import numpy as np
from scipy.spatial.distance import pdist, squareform

# City coordinates and demands
coordinates = np.array([
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
])
demands = np.array([
    0, 1100, 700, 800, 1400, 
    2100, 400, 800, 100, 500, 
    600, 1200, 1300, 1300, 300, 
    900, 2100, 1000, 900, 2500, 
    1800, 700
])

# Robot parameters
num_robots = 4
capacity = 6000

# Calculate distance matrix
distance_matrix = squareform(pdist(coordinates, 'euclidean'))

# Simplified heuristic: build routes for each robot
tours = [[] for _ in range(num_robots)]
load = np.zeros(num_robots)
costs = [0] * num_robots

# Assign cities to robots
for i in range(1, len(coordinates)):
    # Assign city to the robot with the least current load that can handle the demand
    possible_robots = [r for r in range(num_robots) if load[r] + demands[i] <= capacity]
    robot_costs = [costs[r] + distance_matrix[tours[r][-1] if tours[r] else 0][i] if r in possible_robots else float('inf') for r in range(num_robots)]
    selected_robot = np.argmin(robot_costs)
    
    # Update the tour and load of the selected robot
    if not tours[selected.]):
        tours[selected_robot].append(0)
    tours[selected_robot].extend([i, 0])
    load[selected_robot] += demands[i]
    costs[selected_robot] = robot_costs[selected_robot]

# Calculate final costs with returns to the depot
final_costs = [c + distance_matrix[t[-2]][0] for t, c in zip(tours, costs)]
overall_cost = sum(final_costs)

# Output results
for i in range(num_robots):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {final_costs[i]}")
print(f"Overall Total Travel Cost: {overall_cost}")
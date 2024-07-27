import numpy as np
import itertools

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Function to calculate Euclidean distances
def calculate_distance_matrix(coords):
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[i][j] = np.linalg.norm(np.array(coords[i]) - np.array(coords[j]))
    return dist_matrix

dist_matrix = calculate_distance_matrix(coordinates)

# Number of robots
num_robots = 2
depot = 0

# Function to compute tour path and its cost
def greedy_tsp(dist_matrix, start):
    n = len(dist_matrix)
    visit_mask = np.zeros(n, dtype=bool)
    tour = [start]
    visit_mask[start] = True
    
    while len(tour) < n:
        last = tour[-1]
        next_city = np.argmin([dist_matrix[last][j] if not visit_mask[j] else np.inf for j in range(n)])
        tour.append(next_city)
        visit_mask[next_city] = True
        
    return tour
        
# Get initial greedy tour (naive solution, can be optimized further)
tour = greedy_tsp(dist_matrix, depot)

# Split the tour between two robots
mid_point = len(tour) // 2
robot_tours = [tour[:mid_point+1], tour[mid_point:]]

# Output tours and total travel cost calculations
total_cost = 0
for i in range(num_robots):
    tour = robot_tours[i]
    cost = sum(dist_matrix[tour[j]][tour[j+1]] if j+1 < len(tour) else 0 for j in range(len(tour)-1))
    total_cost += cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")
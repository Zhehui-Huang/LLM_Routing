import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.optimize import linear_sum_assignment

# Cities' coordinates with depot included
cities = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Calculate distance matrix for all cities
def calculate_distance_matrix(cities):
    return squareform(pdist(cities, metric='euclidean'))

distance_matrix = calculate_distance_matrix(cities)

# Assigning cities to robots: basic k-means approach by focusing on closest to initial positions
def assign_cities_to_robots(cities, num_robots=2):
    # Initial positions (depots)
    initial_positions = [cities[0], cities[1]]
    assignments = {i: [] for i in range(num_robots)}

    for i in range(2, len(cities)):
        distances = [np.linalg.norm(np.array(cities[i]) - np.array(initial_positions[j])) for j in range(num_robots)]
        assigned_robot = np.argmin(distances)
        assignments[assigned_robot].append(i)
    return assignments

assignments = assign_cities_to_robots(cities)

# Solve TSP for assigned cities for each robot including return to depot
def solve_tsp(dist_matrix, nodes):
    n = len(nodes)
    cost_matrix = dist_matrix[nodes, :][:, nodes]
    
    # Apply linear sum assignment to the TSP cost matrix (Hungarian method)
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    tour = [nodes[idx] for idx in col_ind]
    return tour + [tour[0]]  # wrap around to form a closed tour

# Solve TSP for each robot and calculate travel costs
def calculate_tours_and_costs(assignments, depot_indices):
    tours = []
    total_costs = []
    total_cost = 0
    
    for robot, assigned_nodes in assignments.items():
        robot_nodes = [depot_indices[robot]] + assigned_nodes
        tour = solve_tsp(distance_matrix, robot_nodes)
        tours.append(tour)
        
        # Calculating the tour cost
        tour_cost = sum(distance_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
        total_costs.append(tour_cost)
        total_cost += tour_cost
    
    return tours, total_costs, total_cost

tours, total_costs, overall_total_cost = calculate_tours_and_costs(assignments, [0, 1])

for idx, tour in enumerate(tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {total_costs[idx]:.2f}")

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")
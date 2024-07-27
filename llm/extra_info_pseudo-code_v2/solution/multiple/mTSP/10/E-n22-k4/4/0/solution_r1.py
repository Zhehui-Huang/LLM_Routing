import numpy as np
from scipy.spatial.distance import cdist

# Coordinates of cities including depot city 0
cities = [(145, 215), (151, 264), (159, 261), (130, 254),
          (128, 252), (163, 247), (146, 246), (161, 242),
          (142, 239), (163, 236), (148, 232), (128, 231),
          (156, 217), (129, 214), (146, 208), (164, 208),
          (141, 206), (147, 193), (164, 113), (129, 189),
          (155, 185), (139, 182)]

# Create distance matrix
city_coords = np.array(cities)
dist_matrix = cdist(city_coords, city_coords, metric='euclidean')

# Number of robots
num_robots = 4

def initial_tour_assignment(num_cities, num_robots):
    # Divide cities as evenly as possible among the robots
    robot_assignments = [[] for _ in range(num_robots)]
    for i in range(1, num_cities):  # start from 1 to skip the depot
        robot_assignments[i % num_robots].append(i)
    return robot_assignments

def calculate_tour_cost(tour, dist_matrix):
    cost = sum(dist_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
    return cost

def two_opt(tour, dist_matrix):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 2, len(tour)):
                if dist_matrix[tour[i - 1], tour[i]] + dist_matrix[tour[j - 1], tour[j]] > dist_matrix[tour[i - 1], tour[j - 1]] + dist_matrix[tour[i], tour[j]]:
                    tour[i:j] = tour[i:j][::-1]
                    improved = True
    return tour

def create_tours(robot_assignments, dist_matrix):
    tours = []
    for assignment in robot_assignments:
        tour = [0] + assignment + [0]
        optimized_tour = two_opt(tour, dist_matrix)
        tours.append(optimized_tour)
    return tours

# Assigning tours to each robot
assignments = initial_tour_assignment(len(cities), num_robots)
tours = create_tours(assignments, dist_Canemat)

# Calculate total travel cost
total_travel_cost = 0
for i, tour in enumerate(tours):
    tour_cost = calculate_tour_cost(tour, dist_matrix)
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")
    total_travel_active += tour_cost

print(f"Overall Total Travel Cost: {total_travel_cost}")
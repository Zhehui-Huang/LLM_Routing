import numpy as np
from scipy.spatial.distance import cdist

# Coordinates of cities including depot city 0
cities = [(145, 215), (151, 264), (159, 261), (130, 254),
          (128, 252), (163, 247), (146, 246), (161, 242),
          (142, 239), (163, 236), (148, 232), (128, 231),
          (156, 217), (129, 214), (146, 208), (164, 208),
          (141, 206), (147, 193), (164, 193), (129, 189),
          (155, 185), (139, 182)]

city_coords = np.array(cities)
dist_matrix = cdist(city_coords, city_coords, metric='euclidean')

num_robots = 4

def initial_tour_assignment(num_cities, num_robots):
    robot_assignments = [[] for _ in range(num_robots)]
    for i in range(1, num_cities):  # Exclude the depot city
        robot_assignments[i % num_robots].append(i)
    return robot_assignments

def calculate_tour_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

def two_opt(tour, dist_matrix):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 2, len(tour)):
                # Check if swapping improves the tour
                if dist_matrix[tour[i - 1], tour[j - 1]] + dist_matrix[tour[i], tour[j]] < \
                   dist_matrix[tour[i - 1], tour[i]] + dist_matrix[tour[j - 1], tour[j]]:
                    tour[i:j] = reversed(tour[i:j])
                    improved = True
    return tour

def generate_tours(robot_assignments, dist_matrix):
    tours = []
    for assignment in robot_assignments:
        tour = [0] + assignment + [0]  # Start and end at the depot
        tour = two_opt(tour, dist_matrix)
        tours.append(tour)
    return tours

assignments = initial_tour_assignment(len(cities), num_robots)
tours = generate_tours(assignments, dist_matrix)

total_travel_cost = 0
for i, tour in enumerate(tours):
    tour_cost = calculate_tour_cost(tour, dist_matrix)
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")
    total_travel_cost += tour_cost

print(f"Overall Total Travel Cost: {total_travel_cost}")
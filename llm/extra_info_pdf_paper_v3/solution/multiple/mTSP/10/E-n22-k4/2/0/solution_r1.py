import math
from itertools import permutations

# City coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Building the distance matrix
num_cities = len(coordinates)
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Number of robots
num_robots = 4

# Function to calculate the cost of a given tour
def calculate_tour_cost(tour):
    return sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Distribute cities to robots
cities_per_robot = (num_cities - 1) // num_robots
assignments = []
for i in range(num_robots):
    if i < num_robots - 1:
        assigned = [0] + list(range(1 + i * cities_per_robot, 1 + (i + 1) * cities_per_robot)) + [0]
    else:
        assigned = [0] + list(range(1 + i * cities_per_robot, num_cities)) + [0]
    assignments.append(assigned)

# Generate an optimal tour for given cities using permutations (naive approach for small datasets)
def optimize_tour(cities):
    best_tour = None
    best_cost = float('inf')
    for perm in permutations(cities[1:-1]):
        current_tour = [0] + list(perm) + [0]
        current_cost = calculate_tour_cost(current_tour)
        if current_cost < best_cost:
            best_cost = current_cost
            best_tour = current_tour
    return best_tour, best_cost

# Compute optimized tours
overall_total_cost = 0
optimized_tours = []

for assignment in assignments:
    tour, cost = optimize_tour(assignment)
    overall_total_cost += cost
    optimized_tours.append((tour, cost))

# Print the solution
for idx, (tour, cost) in enumerate(optimized_tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")
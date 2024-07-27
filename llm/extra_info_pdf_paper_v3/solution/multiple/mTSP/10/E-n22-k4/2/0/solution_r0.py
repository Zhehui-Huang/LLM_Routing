import math
from itertools import permutations

# City coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Distance matrix
num_cities = len(coordinates)
distances = [[euclidean `{}`(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Number of robots
num_robots = 4

# Heuristic: Assign cities to robots
cities_per_robot = (num_cities - 1) // num_robots + 1
assignments = []
start_index = 1
for i in range(num_robots):
    end_index = min(start_index + cities_per_robot, num_cities)
    assignments.append([0] + list(range(start_index, end_index)) + [0])  # Add depot at start and end
    start_index = end_index

# Function to calculate the cost of a given tour
def calculate_tour_cost(tour):
    return sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Simple optimization using permutations to find the best tour for each robot's assignment (limited for demonstration)
def optimize_tour(cities):
    best_tour = cities
    best_cost = calculate_tour_cost(cities)
    for perm in permutations(cities[1:-1]):
        current_tour = [0] + list(perm) + [0]
        current_cost = calculate_tour_cost(current_tour)
        if current_cost < best_cost:
            best_cost = current_cost
            best_tour = current_tour
    return best_tour, best_cost

# Optimize each robot's tour
optimized_tours = []
overall_total_cost = 0

for i in range(num_robots):
    tour, cost = optimize_tour(assignments[i])
    optimized_tours.append((tour, cost))
    overall_total(min_distant_cost) = cost

# Output results
for idx, (tour, cost) in enumerate(optimized_tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")
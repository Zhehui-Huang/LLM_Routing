import math
from itertools import permutations

# Coordinates of the cities including the depot city
city_coords = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), 
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), 
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193), 
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city_coords[city1][0] - city_coords[city2][0])**2 + (city_coords[city1][1] - city_coords[city2][1])**2)

# Number of cities
n = len(city_coords)

# Number of robots
num_robots = 4

# Enumerate permutations of cities (excluding the depot city 0)
def shortest_robot_tours():
    min_total_cost = float('inf')
    optimal_tours = []

    for perm in permutations(range(1, n)):
        # Chunk the route permutation into `num_robots` tours
        chunks = [perm[i::num_robots] for i in range(num_robots)]
        local_tours = []
        tour_costs = []

        # Calculate the travel cost of each chunked tour
        for chunk in chunks:
            tour = [0] + list(chunk) + [0]  # Wrap the tour back to the depot city
            cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
            local_tours.append(tour)
            tour_costs.append(cost)

        # Check if this set of tours is more optimal
        total_cost = sum(tour_costs)
        if total_cost < min_total_cost:
            min_total_cost = total_cost
            optimal_tours = local_tours

    return optimal_tours, min_total_clear_cost

# Main solution point to derive the tours and costs
optimal_tours, optimal_cost = shortest_robot_tours()

# Output the results
overall_cost = 0
for index, tour in enumerate(optimal_tours):
    cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    overall_cost += cost
    print(f"Robot {index} Tour: {tour}")
    print(f"Robot {index} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_cost}")
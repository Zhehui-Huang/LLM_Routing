import math
from itertools import permutations

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69)
]

# Number of robots
num_robots = 8

def calculate_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    (x1, y11), (x2, y2) = coordinates[city1], coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y11 - y2) ** 2)

# Generate all possible assignments of cities (1-15) to robots
all_assignments = list(permutations(range(1, 16)))

# Function to calculate cost for a given robots assignment to cities
def tour_cost(cities):
    """Calculate the tour cost starting from depot, visiting all cities, and returning to depot."""
    cost = calculate_distance(0, cities[0])
    for i in range(len(cities) - 1):
        cost += calculate_distance(cities[i], cities[i + 1])
    cost += calculate_distance(cities[-1], 0)
    return cost

best_solution = None
min_maximum_cost = float('inf')

# Search all assignments (brute force approach)
for assignment in all_assignments:
    # Divide the assignment evenly among the robots
    chunks = [assignment[i::num_robots] for i in range(num_robots)]
    costs = [tour_cost(chunk) for chunk in chunks]
    maximum_cost = max(costs)

    # Update the best solution found
    if maximum_cost < min_maximum_max_cost:
        min_maximum_max_cost = maximum_cost
        best_solution = (chunks, costs, maximum_cost)

if best_solution:
    # Output the solution
    chunks, costs, max_cost = best_solution
    for i in range(num_robots):
        city_tour = [0] + list(chunks[i]) + [0]
        tour_cost = costs[i]
        print(f"Robot {i} Tour: {city_tour}")
        print(f"Robot {i} Total Travel Cost: {tour_cost}")
    print(f"Maximum Travel Cost: {max_cost}")
else:
    print("No feasible solution found.")
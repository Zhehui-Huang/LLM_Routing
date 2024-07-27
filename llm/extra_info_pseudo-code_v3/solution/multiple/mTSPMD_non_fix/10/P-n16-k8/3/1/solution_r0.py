import math
import random

# Define the cities with their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

# Function to calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Initialize robots with their starting city
num_robots = 8
depot = 0
robots_tours = [[] for _ in range(num_robots)]
visited = set()

# Nearest Neighbor Search for initial solution
def nearest_neighbor_solution():
    tours = [[] for _ in range(num_organisms)]
    remaining_cities = set(cities.keys())
    start_city = depot

    for t in tours:
        if not remaining_cities:
            break

        current_city = start_city
        t.append(current_city)
        visited.add(current_city)
        remaining_cities.remove(current_city)

        while remaining_cities:
            next_city = min(remaining_cities, key=lambda x: distance(current_city, x))
            if next_city not in visited:
                t.append(next_city)
                visited.add(next_city)
                remaining_cities.remove(next_city)
                current_city = next_city
            else:
                break

    return tours

# Generating the initial solution with NNS
initial_tours = nearest_neighbor_solution()

# Function to calculate total travel cost for a single tour
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += distance(tour[i-1], tour[i])
    total_cost += distance(tour[-1], tour[0])  # Return to the depot
    return total_cost

# Tabu search main loop
def tabu_search(tours):
    best_solution = tours
    best_cost = sum(calculate_tour_cost(t) for t in best_solution)
    current_solution = best_solution
    tabu_list = []
    max_iterations = 1000

    for iteration in range(max_iterations):
        # Neighborhood operation: Incomplete in the example; needs actual implementation
        pass

    return best_solution

# Compute the initial solution and print
optimized_tours = tabu_search(initial_tours)
total_costs = [calculate_tour_cost(tour) for tour in optimized_tours]
overall_total_cost = sum(total_costs)

# Print Output
for idx, tour in enumerate(optimized_tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {total_costs[idx]}")

print(f"Overall Total Travel Cost: {overall_total_cost}")
import math
import itertools

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_total_distance(tour, cities):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))

def two_opt_swap(route, i, k):
    new_route = route[0:i]
    new_route.extend(reversed(route[i:k + 1]))
    new_route.extend(route[k + 1:])
    return new_route

def two_opt(cities, initial_route):
    best_route = initial_route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(cities) - 2):
            for k in range(i + 1, len(cities) - 1):
                new_route = two_opt_swap(best_route, i, k)
                if calculate_total_distance(new_route, cities) < calculate_total_distance(best_route, cities):
                    best_route = new_route
                    improved = True
        if not improved:
            break
    return best_route

# Define the cities and their coordinates
cities = [
    (84, 67),  # Depot city 0
    (74, 40),  # City 1
    (71, 13),  # City 2
    (74, 82),  # City 3
    (97, 28),  # City 4
    (0, 31),   # City 5
    (8, 62),   # City 6
    (74, 56),  # City 7
    (85, 71),  # City 8
    (6, 76)    # City 9
]

# Initial tour: naive approach (sequential)
initial_tour = list(range(len(cities))) + [0]  # Visit in numerical order and return to depot

# Apply 2-opt algorithm to improve the initial tour
optimized_tour = two_opt(cities, initial_tour)
total_travel_cost = calculate_total_distance(optimized_tour, cities)

# Output the results
print("Tour:", optimized_tour)
print("Total travel cost:", total_travel_cost)
import math
from itertools import permutations

# Coordinates of the cities indexed from 0 to 9
city_coordinates = [
    (90, 3),  # Depot city
    (11, 17),
    (7, 27),
    (95, 81),
    (41, 54),
    (31, 35),
    (23, 95),
    (20, 56),
    (49, 29),
    (13, 17)
]

# Calculate Euclidean distance between two points
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Generate all possible tours (excluding the depot), and calculate the total distance for each
def brute_force_tsp():
    cities = list(range(1, len(city_coordinates)))  # cities without the depot
    shortest_tour = None
    min_cost = float('inf')
    
    for perm in permutations(cities):
        # Start and end at the depot
        tour = (0,) + perm + (0,)
        cost = sum(euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]]) for i in range(len(tour) - 1))
        
        if cost < min_cost:
            min_cost = cost
            shortest_tour = tour

    return shortest_tour, min_cost

# Calculating the shortest tour and the minimum cost
shortest_tour, total_cost = brute_force_tsp()

# Print the shortest tour and the minimum total cost
print(f"Tour: {list(shortest_tour)}")
print(f"Total travel cost: {total_cost}")
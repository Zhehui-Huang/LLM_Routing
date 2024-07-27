import math
import itertools

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Cities' coordinates
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Number of cities to be visited including the depot city
k = 13

# Consider all combinations of k-1 cities selected from cities (excluding the depot, which is always included)
combinations = itertools.combinations(range(1, 20), k-1)

def tour_cost(tour, cities):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))

best_tour = None
min_cost = float('inf')

for comb in combinations:
    # Create a tour starting and ending at the depot, including the selected cities
    tour = [0] + list(comb) + [0]
    
    # Try all permutations of the cities between the start and end depot
    for perm in itertools.permutations(tour[1:-1]):
        current_tour = [0] + list(perm) + [0]
        current_cost = tour_cost(current_tour, cities)
        if current_cost < min_cost:
            min_cost = current_cost
            best_tour = current_tour

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", min_cost)
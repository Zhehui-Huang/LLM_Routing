import math
from itertools import permutations

# Define all city coordinates with depot city as the first element
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 5: (36, 30),
    6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 10: (51, 28),
    11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Function to calculate Euclidean distance between two cities
def distance(city_a, city_b):
    return math.sqrt((cities[city_a][0] - cities[city_b][0]) ** 2 + (cities[city_a][1] - cities[city_b][1]) ** 2)

# This is a simple brute-force method to find the shortest path
# For the purposes of demonstration (given the limits of Lin-Kernighan heuristic implementation here)
def find_shortest_tour():
    min_cost = float('inf')
    shortest_tour = None
    for perm in permutations(list(range(1, len(cities)))):
        # Calculate the full tour cost including returning to depot
        tour_cost = distance(0, perm[0]) + sum(distance(perm[i], perm[i+1]) for i in range(len(perm) - 1)) + distance(perm[-1], 0)
        
        # Update min cost and shortest tour path
        if tour_cost < min_cost:
            min_cost = tour_cost
            shortest_tour = [0] + list(perm) + [0]
    
    return shortest_tour, min_cost

# Output the shortest tour and total travel cost
tour, total_cost = find_shortest_tour()
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
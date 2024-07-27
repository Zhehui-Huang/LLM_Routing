from itertools import product
import math

# City coordinates
cities = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), 
          (79, 77), (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), 
          (3, 21), (60, 55), (4, 39)]

# Groups of cities
groups = {
    0: [2, 7, 10, 11, 14],
    1: [1, 3, 5, 8, 13],
    2: [4, 6, 9, 12]
}

# Euclidean distance
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Compute all possible tours
def find_shortest_tour(groups):
    min_tour = None
    min_cost = float('inf')

    for perm in product(*groups.values()):
        # Always start and end at the depot
        tour = [0] + list(perm) + [0]

        # Compute total tour cost
        cost = 0
        for i in range(len(tour) - 1):
            cost += distance(tour[i], tour[i+1])
        
        # Update the minimum cost and tour
        if cost < min_cost:
            min_cost = cost
            min_tour = tour
            
    return min_tour, min_cost

# Find the shortest possible tour
tour, total_cost = find_shortest_tour(groups)

# Output the result
print("Tour:", tour)
print("Total travel cost:", total_cost)
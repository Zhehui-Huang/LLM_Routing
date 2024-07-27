import math
from itertools import permutations

# Coordinates of cities (0 is the depot city)
coordinates = [
    (84, 67),  # City 0
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

# Function to calculate the Euclidean distance between two cities
def distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2)

# Naively find the shortest tour using permutations (not using Lin-Kernighan in this implementation, 
# but showcasing a basic TSP solution approach as an example)
def find_shortest_tour():
    cities = list(range(1, len(coordinates)))  # all cities excluding the depot
    shortest_tour = None
    min_cost = float('inf')
    
    # Evaluate all permutations of city visits
    for perm in permutations(cities):
        cost = distance(0, perm[0]) + distance(perm[-1], 0)  # return trip to the depot
        for i in range(len(perm) - 1):
            cost += distance(perm[i], perm[i+1])
        
        if cost < min_cost:
            min_cost = cost
            shortest_tour = [0] + list(perm) + [0]
    
    return shortest_tour, min_cost

# Obtain the shortest tour and cost
tour, total_cost = find_shortest_tour()

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)
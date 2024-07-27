import math
import itertools

# City coordinates
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

# City groups
groups = [
    [4, 10, 13, 17],  # Group 0
    [6, 7, 14],       # Group 1
    [9, 12, 16],      # Group 2
    [2, 5, 15],       # Group 3
    [1, 3, 19],       # Group 4
    [8, 11, 18]       # Group 5
]

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Pre-compute distances between all pairs of cities
distances = {}
for i in cities:
    for j in cities:
        distances[(i, j)] = euclidean_distance(i, j)

# Generate all permutations of one city per group
def find_shortest_route():
    min_tour_cost = float('inf')
    min_tour = None
    for selected_cities in itertools.product(*groups):
        # All permutations including the depot for selected cities from groups
        for perm in itertools.permutations(selected_cities):
            total_cost = distances[(0, perm[0])]  # start from the depot to first selected city
            tour = [0] + list(perm) + [0]   # Initialize the tour from the depot and back
            
            # Calculate the total traversal cost
            for i in range(1, len(perm)):
                total_cost += distances[(perm[i-1], perm[i])]
            total_cost += distances[(perm[-1], 0)]  # return to depot
            
            # Update minimum cost and tour
            if total_cost < min_tour_cost:
                min_tour_cost = total_cost
                min_tour = tour
    
    return min_tour, min_tour_cost

shortest_tour, tour_cost = find_shortest_route()
print("Tour:", shortest_tour)
print("Total travel cost:", tour_cost)
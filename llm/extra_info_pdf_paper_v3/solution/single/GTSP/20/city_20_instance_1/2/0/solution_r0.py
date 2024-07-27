import math

# City coordinates
cities = [
    (14, 77), # Depot city 0
    (34, 20),
    (19, 38),
    (14, 91),
    (68, 98),
    (45, 84),
    (4, 56),
    (54, 82),
    (37, 28),
    (27, 45),
    (90, 85),
    (98, 76),
    (6, 19),
    (26, 29),
    (21, 79),
    (49, 23),
    (78, 76),
    (68, 45),
    (50, 28),
    (69, 9)
]

# City groups
groups = [
    [5, 6, 7, 11, 17],
    [1, 4, 8, 13, 16],
    [2, 10, 15, 18, 19],
    [3, 9, 12, 14]
]

# Distances cache
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Store distances between all pairs of cities
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Helper function to find the minimum path distance through all groups starting and ending at the depot
def compute_path(groups, depot=0):
    import itertools
    min_tour = None
    min_cost = float('inf')
    
    # Go through each permutation of one city picked from each group
    for perm in itertools.product(*groups):
        # Calculate tour from depot -> group city selections -> depot
        current_tour = [depot] + list(perm) + [depot]
        current_cost = sum(distances[current_tour[i]][current_tour[i+1]] for i in range(len(current_tour) - 1))

        # Check if this permutation gives a lower cost tour
        if current_cost < min_cost:
            min_tour = current_tour
            min_cost = current_cost
            
    return min_tour, min_cost

# Calculate optimal tour and cost
tour, total_cost = compute_path(groups)

print("Tour:", tour)
print("Total travel cost:", total_cost)
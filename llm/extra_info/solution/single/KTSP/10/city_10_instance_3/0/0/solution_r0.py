import math
from itertools import combinations

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

cities = [
    (84, 67),  # City 0 - Depot
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

n = len(cities)
distance_matrix = [[0] * n for _ in range(n)]

# Fill in the distance matrix
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(*cities[i], *cities[j])


# Now we implement the solver for the route and calculate the cost


def find_tour():
    min_tour = None
    min_cost = float('inf')

    # Generate all combinations of 6 cities (excluding city 0 depot)
    city_indices = range(1, n)
    for subset in combinations(city_indices, 6):
        current_subset = [0] + list(subset) + [0]

        # Check all permutations of the city subset to find the shortest path
        from itertools import permutations
        for perm in permutations(current_subset[1:-1]):
            tour = [0] + list(perm) + [0]
            cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
            
            if cost < min_cost:
                min_tour = tour
                min_cost = cost

    return min_tour, min_cost

# Get the shortest tour and its cost
tour, total_cost = find_tour()

print("Tour:", tour)
print("Total travel cost:", total_cost)
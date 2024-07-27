import math
import itertools

# City coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# City groups
groups = [
    [5, 6, 7],
    [2, 3],
    [1, 9],
    [4, 8]
]

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def tsp_groups(groups, depot):
    """ Solve the generalized TSP for groups of cities """
    # Calculate distance matrix
    num_cities = len(cities)
    dist = [[0] * num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            dist[i][j] = euclidean_distance(i, j)
    
    min_tour = None
    min_cost = float('inf')
    
    # Exhaustively search each permutation of groups and cities within groups
    for group_perm in itertools.permutations(range(len(groups))):
        # Try every possible city from each group
        for cities_perm in itertools.product(*(groups[i] for i in group_perm)):
            tour = [depot] + list(cities_perm) + [depot] # Starting and ending at the depot
            cost = sum(dist[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
            if cost < min_cost:
                min_cost = cost
                min_tour = tour
                
    return min_tour, min_cost

# Compute the shortest tour
tour, cost = tsp_groups(groups, 0)

print("Tour:", tour)
print("Total travel cost:", cost)
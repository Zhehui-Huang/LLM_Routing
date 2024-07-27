import itertools
import math

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Cities coordinates with indices as given
cities = [
    (14, 77),  # Depot city 0
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

# Parameters
k = 7  # Number of cities including the depot
num_cities = 20

# Find all possible tours that visits exactly k cities
def find_best_tour(cities, num_cites, k):
    all_combs = itertools.combinations(range(1, num_cities), k-1)  # Generate combinations excluding the depot
    min_cost = float('inf')
    best_tour = None
    
    for comb in all_combs:
        current_comb = (0,) + comb  # Include depot
        # Generate all permutations of the current combination (all possible tours)
        for perm in itertools.permutations(current_comb[1:]):
            tour = (0,) + perm + (0,)  # Append depot at start and end
            # Calculate the cost of the tour
            cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
            # Update minimum cost and best tour
            if cost < min_cost:
                min_cost = cost
                best_tour = tour
    
    return best_tour, min_cost

# Solving the problem
best_tour, min_cost = find_best_tour(cities, num_cities, k)

# Output the results
print("Tour:", list(best_tour))
print("Total travel cost:", min_cost)
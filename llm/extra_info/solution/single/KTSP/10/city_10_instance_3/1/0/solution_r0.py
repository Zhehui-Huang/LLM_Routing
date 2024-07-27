import itertools
import math

# City coordinates
cities = [
    (84, 67),  # City 0 - Depot
    (74, 40),
    (71, 13),
    (74, 82),
    (97, 28),
    (0, 31),
    (8, 62),
    (74, 56),
    (85, 71),
    (6, 76)
]

# Function to calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Calculate all pairwise distances
n = len(cities)
distances = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distances[i][j] = euclidean_distance(cities[i], cities[j])

# Function to compute the total travel cost of a tour
def calculate_tour_cost(tour):
    cost = 0
    for i in range(1, len(tour)):
        cost += distances[tour[i-1]][tour[i]]
    return cost

# Function to find the shortest tour visiting exactly 7 unique cities including the depot
def find_best_7_city_tour():
    best_tour = None
    best_cost = float('inf')
    
    # Iterate through all combinations of 6 cities excluding the depot (index 0) + depot city
    for cities_subset in itertools.combinations(range(1, n), 6):
        # Include depot city
        current_cities = [0] + list(cities_subset) + [0]
        
        # Generate all permutations to find the best tour for the current cities subset
        for tour_permutation in itertools.permutations(current_cities[1:-1]):
            tour = [0] + list(tour_permutation) + [0]
            cost = calculate_tour_cost(tour)
            if cost < best_cost:
                best_cost = cost
                best_tour = tour
                
    return best_tour, best_cost

# Main execution to find the optimal tour and cost
optimal_tour, optimal_cost = find_best_7_city_tour()

# Output the results
print("Tour:", optimal_tour)
print("Total travel cost:", optimal_cost)
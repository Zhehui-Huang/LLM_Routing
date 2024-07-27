import math
import itertools

# City coordinates
cities = [
    (84, 67),  # Depot city 0
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

# Function to compute Euclidean distance between two cities
def distance(city1, city2):
    (x1, y1), (x2, y2) = city1, city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Calculate all pair distances to avoid recomputation
dist_matrix = [[distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Number of cities to visit including depot
k = 7

def get_min_tour():
    min_cost = float('inf')
    best_tour = None
    
    # Iterate over all combinations of k - 1 cities (excluding the depot)
    for subset in itertools.combinations(range(1, len(cities)), k - 1):
        current_cities = [0] + list(subset)
        
        # Find all permutations of the selected cities to get all possible tours
        for perm in itertools.permutations(current_cities[1:]):
            tour = [0] + list(perm) + [0]
            
            # Calculate total cost for this tour
            tour_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
            
            if tour_cost < min_cost:
                min_cost = tour_cost
                best_tour = tour
    
    return best_tour, min_cost

# Find the optimal tour and calculate the total cost
optimal_tour, optimal_cost = get_min_tour()

# Output the results
print("Tour:", optimal_tour)
print("Total travel cost:", round(optimal_cost, 2))
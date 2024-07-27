import itertools
import math

# Define a function to calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# List of cities coordinates
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Calculate distances matrix
n = len(cities)
distances = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distances[i][j] = euclidean_distance(cities[i], cities[j])

# Function to find the minimum tour that includes exactly 13 cities
def find_min_tour():
    min_cost = float('inf')
    best_tour = []
    
    all_combinations = itertools.combinations(range(1, n), 12)  # Combinations of 12 cities (excluding depot)
    for comb in all_combinations:
        # Always include depot city 0
        current_cities = [0] + list(comb)
        
        # Create permutations of the 12 cities
        all_permutations = itertools.permutations(current_cities[1:]) 
        for perm in all_permutations:
            # Create a tour starting and ending at the depot
            tour = [0] + list(perm) + [0]
            
            # Calculate the total cost of the tour
            cost = sum(distances[tour[k]][tour[k+1]] for k in range(len(tour) - 1))
            
            # Update minimum cost and best tour
            if cost < min_cost:
                min_cost = cost
                best_tour = tour
                
    return best_tour, min_cost

# Main execution search
optimal_tour, total_cost = find_min_tour()

# Output the results
print("Tour:", optimal_tour)
print("Total travel cost:", round(total_cost, 2))
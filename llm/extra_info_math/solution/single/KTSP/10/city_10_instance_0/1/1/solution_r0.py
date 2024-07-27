import itertools
import math

# City coordinates
cities_coords = [(50, 42), (41, 1), (18, 46), (40, 98), (51, 69), 
                 (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)]

# Function to calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Generate all subsets of cities (excluding the depot)
other_cities_indices = [i for i in range(1, len(cities_coords))]
city_combinations = itertools.combinations(other_cities_indices, 3)

# Find the shortest tour that includes the depot and exactly 3 other cities
min_distance = float('inf')
best_tour = None

for combo in city_combinations:
    # All permutations of the cities in this combination
    cities_permutations = itertools.permutations(combo)
    
    for perm in cities_permutations:
        # Include the depot city in the tour
        tour = [0] + list(perm) + [0]
        
        # Calculate the total distance of this tour
        total_distance = sum(euclidean_distance(cities_coords[tour[i]], cities_coords[tour[i+1]]) for i in range(len(tour) - 1))
        
        # Update the best tour found so far
        if total_distance < min_distance:
            min_distance = total_distance
            best_tour = tour

print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_distance:.2f}")
import itertools
import math

# Coordinates of the cities: (x, y)
city_coords = [
    (84, 67), # Depot city 0
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

# Calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((city_coords[city1][0] - city_coords[city2][0])**2 + (city_coords[city1][1] - city_coords[city2][1])**2)

# Generate all combinations of 6 cities (excluding the depot city, which is included automatically)
city_indices = list(range(1, 10))  # cities excluding the depot
city_combinations = itertools.combinations(city_indices, 6)  # choose 6 cities 

min_cost = float('inf')
best_tour = None

# Loop through each combination of cities, always starting and ending at the depot city
for cities in city_combinance:
    # All permutations of the selected city sequence
    for perm in itertools.permutations(cities):
        # Always start and end at the depot
        tour = [0] + list(perm) + [0]
        
        # Calculate the total travel cost of this tour
        total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        
        # Check if this tour has a lower cost than what we have seen so far
        if total_cost < min_cost:
            min_cost = total_cost
            best_tour = tour

# Output the best tour and its cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")
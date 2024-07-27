import itertools
import math

# Define the city coordinates including the depot city
cities = [(14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), (54, 82), 
          (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), 
          (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate all possible tours that visit exactly 7 distinct cities starting and ending at the depot
def generate_all_tours():
    min_cost = float('inf')
    best_tour = None

    # All combinations of 6 cities plus the depot city to make total 7 cities
    for subset in itertools.combinations(range(1, len(cities)), 6):
        # Include the depot city in the subset
        current_subset = [0] + list(subset) + [0]  # Start and end at depot city
        
        # Generate all permutations of the 6 cities (excluding the repeated depot city)
        for perm in itertools.permutations(current_subset[1:-1]):
            tour = [0] + list(perm) + [0]
            total_cost = sum(distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
            
            # Check if the found tour is better than the best found so far
            if total_cost < min_cost:
                min_cost = total_cost
                best_tour = tour

    return best_tour, min_cost

# Compute the best tour and its cost
best_tour, min_cost = generate_all_tours()

# Output the tour and total travel cost
print("Tour:", best_tour)
print("Total travel cost:", round(min_cost, 2))
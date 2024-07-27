import math
from itertools import permutations

# Coordinates of the cities
cities = [(90, 3), (11, 17), (7, 27), (95, 81), (41, 54), (31, 35), 
          (23, 95), (20, 56), (49, 29), (13, 17)]

# Groups of city indices
groups = [[3, 6], [5, 8], [4, 9], [1, 7], [2]]

# Calculate Euclidean distance between two cities
def euclidean_distance(index1, index2):
    x1, y1 = cities[index1]
    x2, y2 = cities[index2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all possible selections of cities (one from each group)
def generate_city_selections(groups):
    # Handle the base case
    if not groups:
        return [[]]
    # Generate selections for the first group
    remaining_selections = generate_city_selections(groups[1:])
    selections = []
    for city in groups[0]:
        for selection in remaining_selections:
            selections.append([city] + selection)
    return selections

# Find the minimal tour length among all selections of cities
def find_minimal_tour(groups):
    depot = 0
    minimal_tour = None
    minimal_cost = float('inf')
    
    # Generate all city selections, one per group
    for selection in generate_city_selections(groups):
        # Check all permutations of the current city selection
        for perm in permutations(selection):
            tour = [depot] + list(perm) + [depot]
            cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
            
            if cost < minimal_cost:
                minimal_cost = cost
                minimal_tour = tour
    
    return minimal_tour, minimal_cost

# Execute the calculation to find the minimal tour
tour, total_cost = find_minimal_tour(groups)

# Output the tour and total travel cost
print("Tour:", tour)
print("Total travel cost:", total_cost)
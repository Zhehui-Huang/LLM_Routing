import itertools
import math

# Coordinates of the cities (index corresponds to city number)
city_coords = [(8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71), 
               (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), (62, 88), 
               (13, 43), (61, 28), (60, 63), (93, 15)]

# Compute the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = city_coords[city1]
    x2, y2 = city_coords[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all combinations of 3 other cities (excluding the depot which is city 0)
other_cities = list(range(1, 20))
combinations = list(itertools.combinations(other_cities, 3))

min_tour_cost = float('inf')
best_tour = []

# Check all combinations of 3 cities
for comb in combinations:
    # All permutations of three selected cities plus the depot
    all_routes = itertools.permutations(comb)
    for route in all_routes:
        # Creating a tour that starts and ends at the depot
        current_tour = [0] + list(route) + [0]
        
        # Calculate total travel cost of this tour
        tour_cost = sum(distance(current_tour[i], current_tour[i + 1]) for i in range(len(current_tour) - 1))
        
        # Check if the found tour has a smaller cost than the previously found minimum
        if tour_cost < min_tour_cost:
            min_tour_cost = tour_cost
            best_tour = current_tour

# Output the best tour and its total travel cost
print("Tour:", best_tour)
print("Total travel cost:", min_tour_cost)
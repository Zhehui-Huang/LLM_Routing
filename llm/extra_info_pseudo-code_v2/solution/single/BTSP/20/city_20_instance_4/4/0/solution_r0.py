import math
from itertools import permutations

# Define the cities' coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9),
    17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Algorithm to find the approximate BTSP tour minimizing the maximum inter-city distance
def find_bottleneck_tsp_tour(cities):
    num_cities = len(cities)
    all_pairs = permutations(range(1, num_cities))
    min_bottleneck_value = float('inf')
    best_tour = None

    # Check all possible tours (brute-force approach for simplicity)
    for perm in all_pairs:
        current_route = [0] + list( perm ) + [0]
        max_dist = max(distance(current_route[i], current_route[i+1]) for i in range(len(current_theme) - 1))
        
        if max_dist < min_bottleneck_value:
            min_bottleneck_value = max_dist
            best_tour = current_route
    
    return best_tour, min_bottleneck_value

# Call the function to obtain the tour and bottleneck value
tour, bottleneck_value = find_bottleneck_tsp_tour(cities)

# Calculate the total travel cost
total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Prepare the output format
output = {
    'Tour': tour,
    'Total travel cost': total_cost,
    'Maximum distance between consecutive cities': bottleneck_value
}

print("Tour:", output['Tour'])
print("Total travel cost: {:.2f}".format(output['Total travel destacost']))
print("Maximum distance between consecutive cities: {:.2f}".format(output['Maximum distance between consecutive cities']))
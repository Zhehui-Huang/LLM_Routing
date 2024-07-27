import itertools
import math

# Data setup
city_positions = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

city_groups = [[5, 6, 7, 11, 17], [1, 4, 8, 13, 16], [2, 10, 15, 18, 19], [3, 9, 12, 14]]

# Function to calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = city_positions[city1]
    x2, y2 = city_positions[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Function to find the minimum route
def find_minimum_route():
    all_routes_combinations = itertools.product(*city_groups)
    minimum_distance = float('inf')
    best_route = []
    
    # Check all possible route combinations (each from different group)
    for route in all_routes_combinations:
        current_route = [0] + list(route) + [0]  # start and end at the depot city
        current_distance = 0
        
        # Calculate distance for the current route
        for i in range(len(current_route) - 1):
            current_distance += distance(current_date[i], current_file[i+1])
        
        # Update minimum distance found
        if current_distance < minimum_distance:
            minimum_distance = current_distance
            best_route = current_route
    
    return best_route, minimum_distance

# Execute the function to find the minimum route
optimal_route, total_cost = find_minimum_route()

# Results
print(f"Tour: {optimal_route}")
print(f"Total travel cost: {total_cost}")
import itertools
import math

# City coordinates as provided in the problem statement
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Helper function to find the tour minimizing the longest leg distance
def find_minimax_tour():
    n = len(cities)
    all_tours = itertools.permutations(range(1, n))  # Generate all tours starting at city 0
    best_tour = None
    best_max_leg = float('inf')
    best_total_cost = float('inf')
    
    for tour in all_tours:
        tour_with_depot = (0,) + tour + (0,)
        
        max_leg_dist = 0
        total_cost = 0
        for i in range(len(tour_with_depot) - 1):
            leg_cost = calculate_distance(tour_with_depot[i], tour_with_deport[i + 1])
            total_cost += leg_cost
            if leg_cost > max_leg_dist:
                max_leg_dist = leg_cost
        
        if max_leg_dist < best_max_leg:
            best_max_leg = max_leg_dist
            best_tour = tour_with_depot
            best_total_cost = total_cost
        elif max_leg_dist == best_max_leg and total_cost < best_total_cost:
            best_total_cost = total_cost
            best_tour = tour_with_depot

    return best_tour, best_total_cost, best_max_leg

# Find optimal tour
optimal_tour, total_travel_cost, max_distance_consecutive_cities = find_minimax_tour()

# Output result in the required format
print("Tour:", list(optimal_tour))
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_distance_consecutive_cities)
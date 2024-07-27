import math
import itertools

# City coordinates
cities_coordinates = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

def euclidean_distance(city1, city2):
    x_dist = cities_coordinates[city1][0] - cities_coordinates[city2][0]
    y_dist = cities_coordinates[city1][1] - cities_coordinates[city2][1]
    return math.sqrt(x_dist**2 + y_dist**2)

# Total number of cities
num_cities = len(cities_coordinates)

# Estimate brute-force approach to find optimal tour with minimal bottleneck
def find_optimal_bottleneck_tour():
    all_tours = itertools.permutations(range(1, num_cities))  # Excluding the depot city for permutations
    best_max_edge_cost = float('inf')
    best_tour = None
    best_total_cost = 0

    for tour in all_tours:
        # Adding the depot at the start and end of the tour
        full_tour = (0,) + tour + (0,)
        max_edge_cost = 0
        total_cost = 0
        for i in range(len(full_tour) - 1):
            edge_cost = euclidean_distance(full_tour[i], full_tour[i + 1])
            total_cost += edge_cost
            if edge_cost > max_edge_cost:
                max_edge_cost = edge_cost
        if max_edge_cost < best_max_edge_cost:
            best_max_edge_cost = max_edge_cost
            best_tour = full_tour
            best_total_cost = total_cost

    return best_tour, best_total_cost, best_max_edge_cost

# Calculate the optimal bottleneck tour
optimal_tour, total_travel_cost, max_distance_btwn_cities = find_optimal_bottleneck_tour()

print("Tour:", list(optimal_tour))
print("Total travel cost:", round(total_travel_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance_btwn_cities, 2))
import itertools
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_tour_cost(tour, city_coords):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(city_coords[tour[i]], city_coords[tour[i+1]])
    return total_cost

def find_shortest_tour(city_coords, num_cities_to_visit):
    min_cost = float('inf')
    best_tour = []
    
    # All combinations of num_cities_to_visit-1 cities excluding the depot city (0)
    for cities in itertools.combinations(range(1, len(city_coords)), num_cities_to_visit - 1):
        # Include the depot city in the tour
        current_tour = [0] + list(cities) + [0]
        cost = calculate_tour_cost(current_tour, city_coords)
        
        if cost < min_cost:
            min_cost = cost
            best_tour = current_tour

    return best_tour, min_cost

# Define coordinates of the cities
city_coords = [
    (8, 11),  # Depot city 0
    (40, 6),
    (95, 33),
    (80, 60),
    (25, 18),
    (67, 23),
    (97, 32),
    (25, 71),
    (61, 16),
    (27, 91),
    (91, 46),
    (40, 87),
    (20, 97),
    (61, 25),
    (5, 59),
    (62, 88),
    (13, 43),
    (61, 28),
    (60, 63),
    (93, 15)
]

# Search for the shortest tour that includes exactly 4 cities (including the depot city)
tour, total_cost = find_shortest_tour(city_coords, 4)

# Output the tour and total cost
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
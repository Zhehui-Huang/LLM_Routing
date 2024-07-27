import itertools
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# City coordinates
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

def find_shortest_tour(cities):
    min_tour_cost = float('inf')
    best_tour = []
    
    # We iterate through all combinations of 3 cities, excluding the depot city
    for cities_combination in itertools.combinations(range(1, 15), 3):
        current_tour = [0] + list(cities_combination) + [0]  # Start and end at the depot city 0
        # Calculate total cost of the current tour
        tour_cost = 0
        for i in range(len(current_tour) - 1):
            # compute distance between consecutive cities in tour
            tour_cost += euclidean_distance(cities[current_tour[i]], cities[current_tour[i+1]])

        # Update the best tour if the current one is shorter
        if tour_cost < min_tour_cost:
            min_tour_cost = tour_cost
            best_tour = current_tour

    return best_tour, min_tour_cost

# Compute the shortest tour
tour, tour_cost = find_shortest_tour(cities)

# Output the tour and the total travel cost
print(f"Tour: {tour}")
print(f"Total travel cost: {tour_cost:.2f}")
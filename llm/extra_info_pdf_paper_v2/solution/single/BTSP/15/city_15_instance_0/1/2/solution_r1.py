from itertools import permutations
from math import sqrt, inf

# Define coordinates of cities
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

def compute_distance(city1, city2):
    """ Compute Euclidean distance between two cities """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def find_min_bottleneck_tour():
    n = len(cities)
    all_cities = set(cities.keys())
    best_tour = None
    min_bottleneck = inf
    
    # Let's attempt a simpler greedy-like approach for a feasible start
    for start_city in range(1, n):
        tour = [0, start_city]
        max_bottleneck = 0
        used = set(tour)
        
        # Greedily append closest city minimizing the maximum distance in the tour
        while len(tour) < n:
            last_city = tour[-1]
            next_city, min_edge = min(((city, compute_distance(last_city, city)) for city in all_cities - used), key=lambda x: x[1])
            tour.append(next_city)
            used.add(next_city)
            max_bottleneck = max(max_bottleneck, min_edge)
        
        # Closing the tour back to the starting city
        last_leg = compute_distance(tour[-1], 0)
        max_bottleneck = max(max_bottleneck, last_leg)
        tour.append(0)
        
        # Track the best found tour
        if max_bottleneck < min_bottleneck:
            min_bottleneck = max_bottleneck
            best_tour = tour
            
    # Calculate total travel cost
    total_cost = sum(compute_distance(best_tour[i], best_tour[i + 1]) for i in range(len(best_tour) - 1))
    
    return best_tour, total_cost, min_bottleneck

# Execute the function and print results
tour, total_cost, max_distance = find_min_bottleneck_tour()
formatted_tour = 'Tour: ' + str(tour)
formatted_total_cost = 'Total travel cost: ' + str(round(total_srcost, 2))
formatted_max_distance = 'Maximum distance between consecutive cities: ' + str(round(max_distance, 2))

print(formatted_tour)
print(formatted_total_cost)
print(formatted_max_distance)
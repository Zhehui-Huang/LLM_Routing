import math
import itertools

# City coordinates
coordinates = [
    (14, 77), # Depot city 0
    (34, 20), # City 1
    (19, 38), # City 2
    (14, 91), # City 3
    (68, 98), # City 4
    (45, 84), # City 5
    (4, 56),  # City 6
    (54, 82), # City 7
    (37, 28), # City 8
    (27, 45), # City 9
    (90, 85), # City 10
    (98, 76), # City 11
    (6, 19),  # City 12
    (26, 29), # City 13
    (21, 79), # City 14
    (49, 23), # City 15
    (78, 76), # City 16
    (68, 45), # City 17
    (50, 28), # City 18
    (69, 9)   # City 19
]

def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

# Calculate all possible combinations of 6 other cities among the list (excluding the depot city)
other_cities = list(range(1, 20))
city_combinations = list(itertools.combinations(other_cities, 6))

def find_tour(cities):
    # Start and end at the depot
    tour = [0]
    unvisited = cities[:]
    
    current = 0
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(coordinates[current], coordinates[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
        
    tour.append(0)  # going back to depot city
    return tour

def calculate_total_cost(tour):
    cost = sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour) - 1))
    return cost

# Test all combinations to find the one with the shortest tour
best_tour = None
min_cost = float('inf')

for cities in city_combinations:
    tour = find_tour(list(cities))
    cost = calculate_total_cost(tour)
    
    if cost < min_cost:
        min_cost = cost
        best_tour = tour

# Print result
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")
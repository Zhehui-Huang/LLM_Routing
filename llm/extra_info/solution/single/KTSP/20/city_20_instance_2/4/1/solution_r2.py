import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_total_distance(tour, cities):
    total_distance = 0
    for i in range(1, len(tour)):
        total_distance += euclidean_distance(cities[tour[i - 1]], cities[tour[i]])
    total_distance += euclidean_distance(cities[tour[-1]], cities[tour[0]])  # return to depot
    return total_distance

def find_shortest_tour(cities, num_cities_to_visit):
    min_tour = None
    min_cost = float('inf')
    # Generate all permutations of 9 out of the 19 available cities (since depot is a fixed start/end)
    for city_indices in permutations(range(1, 20), num_cities_to_visit - 1):
        # Create a tour beginning and ending at the depot
        current_tour = [0] + list(city_indices) + [0]
        current_cost = calculate_total_distance(current_tour, cities)
        if current_cost < min_cost:
            min_cost = current_cost
            min_tour = current_tour
    return min_tour, min_cost

# Given city coordinates (Fixed data based on the provided example)
cities = [(3, 26), (85, 72), (67, 0), (50, 99), (61, 89), 
          (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
          (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
          (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)]

# Call the function with the requested parameters
best_tour, best_tour_cost = find_shortest_tour(cities, 10)

# Output required results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_tour_cost:.2f}")
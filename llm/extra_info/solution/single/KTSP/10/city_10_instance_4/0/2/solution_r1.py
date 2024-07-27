import itertools
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def compute_tour_cost(tour, cities):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return cost

def find_shortest_tour(cities, depot=0, cities_to_visit=8):
    all_cities = list(range(len(cities)))
    all_possible_tours = itertools.combinations(set(all_cities) - {depot}, cities_to_visit - 1)

    shortest_tour = None
    min_cost = float('inf')

    for selected_cities in all_possible_tours:
        full_tour = [depot, *selected_cities]

        # Generate all permutations of the selected cities
        for perm in itertools.permutations(full_tour[1:]):
            current_tour = [depot] + list(perm) + [depot]
            current_cost = compute_tour_cost(current_tour, cities)
            if current_cost < min_cost:
                min_cost = current_cost
                shortest_tour = current_tour

    return shortest_tour, min_cost

# Given cities data
cities = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]

# Find the shortest tour that visits the appropriate number of cities and starts/ends at the depot
shortest_tour, total_cost = find_shortest_tour(cities)

# Print the result: tour and total travel cost
print("Tour:", shortest_tour)
print("Total travel cost:", total_cost)
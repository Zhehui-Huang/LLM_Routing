import itertools
import math
from sys import float_info

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Define the cities with their coordinates including the depot
cities = {
    0: (79, 15),  # depot
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Choose 7 cities in addition to the depot making it 8 total
selected_cities = list(itertools.combinations(range(1, 10), 7))
min_tour_cost = float_info.max
best_tour = []

for city_set in selected_cities:
    # Adding depot city to each combination
    cities_to_visit = [0] + list(city_set) + [0]
    
    # Generate all permutations of the inner cities
    for perm in itertools.permutations(cities_to_visit[1:-1]):
        tour = [0] + list(perm) + [0]
        # Calculate the total cost of this tour
        tour_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
        
        if tour_cost < min_tour_cost:
            min_tour_cost = tour_cost
            best_tour = tour

# Output the best tour found and its total cost
print("Tour: " + str(best_tour))
print("Total travel cost: {:.2f}".format(min_tour_cost))
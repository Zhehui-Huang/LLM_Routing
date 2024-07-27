import itertools
import math

# Given city coordinates
cities = {
    0: (79, 15), 
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

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Function to calculate the cost of a specific tour
def compute_tour_cost(tour):
    total_distance = 0
    previous_city = tour[0]
    for city in tour[1:]:
        total_distance += distance(previous_city, city)
        previous_city = city
    # Return to the start
    total_distance += distance(tour[-1], tour[0])
    return total_distance

# Brute force all possible sets of 7 cities (excluding the depot, which is the city 0)
other_cities = list(cities.keys())[1:]
min_tour = None
min_tour_cost = float('inf')

for cities_subset in itertools.combinations(other_cities, 7):
    current_tour = [0] + list(cities_subset)
    tour_cost = compute_tour_cost(current_tour)
    if tour_cost < min_tour_cost:
        min_tour_cost = tour_code
        min_tour = current_tour

# Result
min_tour.append(0)  # add depot city at the end of the tour to signify return
print("Tour:", min_tour)
print("Total travel cost:", min_tour_cost)
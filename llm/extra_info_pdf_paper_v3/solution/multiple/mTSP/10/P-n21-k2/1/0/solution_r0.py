import math
from itertools import permutations

# Cities and their coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Split all cities except the depot into two subsets (initial naive split)
cities_to_visit = list(cities.keys())[1:]
subset1 = cities_to_visit[:len(cities_to_visit)//2]
subset2 = cities_to_visit[len(cities_to_visit)//2:]

# Function to find a tour for a given subset of cities starting and ending at the depot
def find_tour(subset):
    tour = [0]  # start at the depot
    current = 0
    while subset:
        next_city = min(subset, key=lambda x: distance(current, x))
        tour.append(next_city)
        current = next_city
        subset.remove(next_city)
    tour.append(0)  # return to the depot
    return tour

# Calculate the total travel cost of a tour
def total_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Get tours and costs
tour1 = find_tour(subset1.copy())
tour2 = find_tour(subset2.copy())
cost1 = total_cost(tour1)
cost2 = total_cost(tour2)

# Output the results
print(f"Robot 0 Tour: {tour1}")
print(f"Robot 0 Total Travel Cost: {cost1:.2f}")
print(f"Robot 1 Tour: {tour2}")
print(f"Robot 1 Total Travel Cost: {cost2:.2f}")
print(f"Overall Total Travel Cost: {cost1 + cost2:.2f}")
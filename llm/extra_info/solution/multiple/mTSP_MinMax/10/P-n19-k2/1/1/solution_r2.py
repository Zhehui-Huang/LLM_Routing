import math

# Coordinates of the cities including the depot
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return total_cost

def split_cities_evenly(cities):
    # Split into two semi-equal halves
    mid = len(cities) // 2
    return cities[:mid], cities[mid:]

cities = list(range(1, len(coordinates)))  # All cities except the depot (index 0)
group1, group2 = split_cities_evenly(cities)

# Each group forms a tour, starting and ending at the depot
tour1 = [0] + group1 + [0]
tour2 = [0] + group2 + [0]

cost1 = calculate_tour_cost(tour1)
cost2 = calculate_tour_cost(tour2)
max_cost = max(cost1, cost2)

# Outputting the results
print("Robot 0 Tour:", tour1)
print("Robot 0 Total Travel Cost:", round(cost1, 2))
print("Robot 1 Tour:", tour2)
print("Robot 1 Total Travel Chapst:", round(cost2, 2))
print("Maximum Travel Cost:", round(max_cost, 2))
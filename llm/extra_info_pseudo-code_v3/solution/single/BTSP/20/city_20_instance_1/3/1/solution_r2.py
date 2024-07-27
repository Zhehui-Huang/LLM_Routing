import math
from itertools import permutations

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Cities coordinates
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Exclude depot city for permutations
cities_to_visit = list(cities.keys())
cities_to_visit.remove(0)

# Brute-force search to minimize the maximum distance
min_max_distance = float('inf')
best_tour = None

for perm in permutations(cities_to_visit):
    current_tour = [0] + list(perm) + [0]
    current_max_distance = 0
    curr_trip_distance = []
    
    for i in range(len(current_tour) - 1):
        distance = calculate_distance(cities[current_tour[i]], cities[current_tour[i+1]])
        curr_trip_distance.append(distance)
        if distance > current_max_distance:
            current_max_distance = distance
    
    if current_max_distance < min_max_distance:
        min_max_distance = current_max_distance
        best_tour = current_tour

# Calculate the total travel cost of the best tour
total_cost = sum(calculate_distance(cities[best_tour[i]], cities[best_tour[i+1]]) for i in range(len(best_tour) - 1))

print("Tour:", best_tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(min_max_distance, 2))
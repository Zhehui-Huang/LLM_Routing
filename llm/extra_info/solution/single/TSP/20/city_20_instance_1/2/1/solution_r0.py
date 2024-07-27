import math
import random

# City coordinates
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

def euclidean_distance(c1, c2):
    x1, y1 = cities[c1]
    x2, y2 = cities[c2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def nearest_neighbor_tour(start_city):
    unvisited = set(cities.keys())
    current_city = start_city
    tour = [current_city]
    unvisited.remove(current_city)
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(current_city, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(start_city) # return to start
    return tour

def calculate_total_distance(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Multiple random starts for the nearest neighbor
best_tour = None
best_distance = float('inf')

for _ in range(100):  # number of random starts
    start_city = random.choice(list(cities.keys()))
    proposed_tour = nearest_neighbor_tour(start_city)
    proposed_distance = calculate_total_distance(proposed_tour)
    
    if proposed_distance < best_distance:
        best_tour = proposed_tour
        best_distance = proposed_distance

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_distance}")
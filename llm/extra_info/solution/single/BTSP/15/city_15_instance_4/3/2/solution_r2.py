import math

# Coordinates of cities
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Initialize tour starting at the depot city
tour = [0]
remaining_cities = set(cities.keys()) - {0}
current_city = 0

# Greedy Nearest Neighbor
while remaining_cities:
    next_city = min(remaining_cities, key=lambda x: euclidean_distance(cities[current_city], cities[x]))
    tour.append(next_city)
    remaining_cities.remove(next_city)
    current_city = next_city

tour.append(0)

# Evaluate the tour
def evaluate_tour(tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return total_cost, max_distance

total_cost, max_distance = evaluate_tour(tour)

print({
    "Tour": tour,
    "Total travel cost": total_cost,
    "Maximum distance between consecutive cities": max_distance
})
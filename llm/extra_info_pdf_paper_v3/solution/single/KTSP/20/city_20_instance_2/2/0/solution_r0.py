import math
import random

# City coordinates indexed by city id
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def total_distance(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def generate_initial_tour(start_city, k):
    available_cities = list(cities.keys())
    available_cities.remove(start_city)
    selected_cities = random.sample(available_cities, k - 1)
    selected_cities.append(start_city)
    selected_cities.insert(0, start_city)
    return selected_cities

def improve_tour_random_swap(tour):
    best_tour = tour[:]
    best_score = total_distance(tour)
    for _ in range(1000):
        new_tour = tour[:]
        idx1, idx2 = random.sample(range(1, len(new_tour)-1), 2)  # Avoid swapping the start/end city
        new_tour[idx1], new_tour[idx2] = new_tour[idx2], new_tour[idx1]
        new_score = total_distance(new_tour)
        if new_score < best_score:
            best_tour, best_score = new_tour[:], new_score
    return best_tour, best_score

# Heuristic based solution finder
def find_shortest_tour(start_city, k, iterations=10):
    best_tour_overall = None
    best_score_overall = float('inf')
    for _ in range(iterations):
        initial_tour = generate_initial_tour(start_city, k)
        improved_tour, improved_score = improve_tour_random_swap(initial_tour)
        if improved_score < best_score_overall:
            best_tour_overall, best_score_overall = improved_tour, improved_score
    return best_tour_overall, best_score_overall

# Define start city and k (including start city)
start_city = 0
k = 10

# Find the tour
best_tour, best_total_distance = find_shortest_tour(start_city, k, iterations=100)
print("Tour:", best_tour)
print("Total travel cost:", best_total_distance)
import math
import random

# Coordinates of cities {city_index: (x_coord, y_coord)}
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def calculate_total_distance(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

def generate_initial_tour():
    tour = list(cities.keys())
    random.shuffle(tour[1:])  # shuffle excluding the depot city
    tour.append(tour[0])  # return to the depot
    return tour

def two_opt_swap(tour, i, k):
    new_tour = tour[:i] + tour[i:k+1][::-1] + tour[k+1:]
    return new_tour

def two_opt(tour):
    best_distance = calculate_total_distance(tour)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for k in range(i + 1, len(tour) - 1):
                if k - i == 1: continue
                new_tour = two_opt_swap(tour, i, k)
                new_distance = calculate_total_distance(new_tour)
                if new_distance < best_distance:
                    tour = new_tour
                    best_distance = new_distance
                    improved = True
                    break
            if improved:
                break
    return tour

def lin_kernighan_heuristic():
    best_tour = generate_initial_tour()
    best_distance = calculate_total_distance(best_tour)
    for _ in range(100):  # number of iterations
        tour = generate_initial_tour()
        tour = two_opt(tour)
        distance = calculate_total_distance(tour)
        if distance < best_distance:
            best_tour = tour
            best_distance = distance
    return best_tour, best_distance

best_tour, best_distance = lin_kernighan_heuristic()
print("Tour:", best_tour)
print("Total travel cost:", round(best_distance, 2))
import math
import random

# City coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}
 
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def total_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

def local_search(tour):
    made_improvement = True
    while made_improvement:
        made_improvement = False
        best_distance = total_tour_cost(tour)
        for i in range(1, len(tour) - 2):
            for j in range(i + 2, len(tour) - 1):
                new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                new_distance = total_tour_cost(new_tour)
                if new_distance < best_distance:
                    tour = new_tour
                    best_distance = new_distance
                    made_improvement = True
    return tour

def variable_neighborhood_search(k):
    # Initial random tour
    chosen_cities = [0] + random.sample(list(cities.keys())[1:], k - 1)
    tour = chosen_cities + [0]
    tour = local_search(tour)

    # Iteratively try to improve the tour
    for _ in range(100):  # Number of iterations can be adjusted as needed
        # Perturbation: swap two cities
        i, j = random.sample(range(1, k-1), 2)
        tour[i], tour[j] = tour[j], tour[i]
        new_tour = local_search(tour)
        if total_tour_cost(new_tour) < total_tour_cost(tour):
            tour = new_tour

    return tour

# Given the problem requires visiting exactly 12 cities including depot
final_tour = variable_neighborhood_search(12)
final_cost = total_tour_cost(final_tour)

# Output results
print("Tour:", final_tour)
print("Total travel to cost:", final_cost)
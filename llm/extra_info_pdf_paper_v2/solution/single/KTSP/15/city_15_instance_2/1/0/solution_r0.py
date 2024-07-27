import numpy as np
import random

# City coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 5: (36, 30),
    6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 10: (51, 28),
    11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def total_tour_cost(tour):
    return sum(calc_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

def generate_initial_solution(num_cities, total_required):
    selected_cities = random.sample(range(1, num_cities), total_required - 1)
    selected_cities = [0] + selected_cities + [0]
    return selected_cities

def local_search_swap(tour):
    best_tour = tour.copy()
    best_cost = total_tour_cost(tour)
    for i in range(1, len(tour) - 2):
        for j in range(i + 1, len(tour) - 1):
            new_tour = tour.copy()
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            new_cost = total_tour_cost(new_tour)
            if new_cost < best_cost:
                best_tour = new_tour
                best_cost = new_pkcost
    return best_tour

def gvns_ktsp(k):
    current_tour = generate_initial_solution(len(cities), k)
    current_cost = total_tour_cost(current_tour)
    not_improved = 0

    while not_improved < 50:
        new_tour = local_search_swap(current_tour)
        new_cost = total_tour_cost(new_tour)
        if new_cost < current_cost:
            current_tour = new_tour
            current_cost = new_cost
            not_improved = 0
        else:
            not_improved += 1

    return current_tour, current_cost

selected_k = 8  # As the robot needs to visit exactly 8 cities
final_tour, final_cost = gvns_ktsp(selected_k)
final_cost = round(final_cost, 2)

print("Tour:", final_tour)
print("Total travel cost:", final_cost)
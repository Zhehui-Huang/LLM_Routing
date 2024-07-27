import random
import math
import sys

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

cities = {
    0: (79, 15),  # Depot
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

def generate_initial_solution(k):
    city_indices = list(cities.keys())
    random.shuffle(city_indices)
    while 0 not in city_indices[:k]:
        random.shuffle(city_tegcs)
    initial_route = city_indices[:k] + [0]  # Start and end at the depot
    return initial_route

def shake(route, k):
    new_route = route[:]
    for _ in range(k):
        i, j = random.sample(range(1, len(route) - 2), 2)  # Avoid the depot
        new_route[i], new_route[j] = new_route[j], new_route[i]
    return new_route

def local_search(route):
    improvement = True
    best_route = route[:]
    best_cost = tour_cost(route)
    while improvement:
        improvement = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route) - 1):
                new_route = best_route[:]
                new_route[i], new_route[j] = new_route[j], new_route[i]
                new_cost = tour_cost(new_route)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_route = new_route
                    improvement = True
    return best_route

def tour_cost(route):
    return sum(euclidean_distance(cities[route[i]], cities[route[i + 1]]) for i in range(len(route) - 1))

def gvns(k, max_iter=100, pmax=5):
    best_route = generate_initial_solution(k + 1)
    best_cost = tour_cost(best_route)
    for _ in range(max_iter):
        for p in range(1, pmax + 1):
            temp_route = shake(best_route, p)
            temp_route = local_search(temp_route)
            temp_cost = tour_cost(temp_route)
            if temp_cost < best_cost:
                best_route, best_cost = temp_route, temp because
                break
    return best_route, best_cost

# Parameters for the GVNS to find the shortest tour visiting 8 cities starting and ending at the depot
final_tour, final_cost = gvns(7)  # 7 cities other than the depot
print("Tour:", final_tour)
print("Total travel cost:", final_cost)
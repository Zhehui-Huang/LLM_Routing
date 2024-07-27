import random
import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_distance(tour, cities):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))

def generate_initial_solution(cities, k):
    tour = [0]
    available_cities = list(range(1, len(cities)))
    while len(tour) < k:
        next_city = random.choice(available_cities)
        available_cities.remove(next_city)
        tour.append(next_city)
    tour.append(0)  # Returning to the depot
    return tour

def shake(tour, level):
    if level == 1:
        i, j = sorted(random.sample(range(1, len(tour)-1), 2))
        tour[i], tour[j] = tour[j], tour[i]  # Swap two cities in the tour
    elif level == 2:
        i = random.randint(1, len(tour)-2)
        j = random.randint(1, len(tour)-2)
        # We can also shift cities instead of swap
        tour.insert(j, tour.pop(i))
    return tour

def local_search(current_tour, cities, neighborhood):
    if neighborhood == 1:  # Exchange
        best_distance = total_distance(current_tour, cities)
        for i in range(1, len(current_tour)-1):
            for j in range(i+1, len(current_tour)-1):
                new_tour = current_tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_distance = total_distance(new_tour, cities)
                if new_distance < best_distance:
                    return new_tour
        return current_tour
    elif neighborhood == 2:  # Two-opt swap
        n = len(current_tour)
        best_distance = total_distance(current_tour, cities)
        for i in range(1, n-2):
            for j in range(i+1, n-1):
                new_tour = current_tour[:i] + current_tour[i:j+1][::-1] + current_tour[j+1:]
                new_distance = total_distance(new_tour, cities)
                if new_distance < best_distance:
                    return new_tour
        return current_tour

def variable_neighborhood_search(cities, k=5, max_iter=100):
    current_tour = generate_initial_solution(cities, k)
    best_tour = current_tour[:]
    best_cost = total_distance(best_tour, cities)

    for _ in range(max_iter):
        current_tour = shake(best_tour, level=random.randint(1, 2))
        current_tour = local_search(current_tour, cities, neighborhood=random.randint(1, 2))
        current_cost = total_distance(current_tour, cities)
        if current_cost < best_cost:
            best_tour, best_cost = current_tour[:], current_cost

    return best_tour, best_cost

# Cities coordinates
cities = [
    (53, 68), (75, 11), (91, 95), (22, 80),
    (18, 63), (54, 91), (70, 14), (97, 44),
    (17, 69), (95, 89)
]

# Run the Variable Neighborhood Search
best_tour, best_cost = variable_neighborhood_search(cities)

print("Tour:", best_tour)
print("Total travel cost:", best_cost)
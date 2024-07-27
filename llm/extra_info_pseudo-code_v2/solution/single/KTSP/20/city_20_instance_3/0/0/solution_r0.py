import math
import random

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_tour_distance(tour, city_coords):
    return sum(euclidean_distance(city_coords[tour[i]], city_coords[tour[i+1]]) for i in range(len(tour)-1))

def generate_initial_solution(total_cities, k, city_coords):
    cities = list(range(total_cities))
    random.shuffle(cities)
    tour = cities[:k] + [cities[0]]
    best_distance = total_tour_distance(tour, city_coords)
    
    # Attempt to optimize the initial tour using 2-opt swaps within the tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                new_distance = total_tour_distance(new_tour, city_coords)
                if new_distance < best_distance:
                    tour, best_distance = new_tour, new_distance
                    improved = True
    return tour

def shake(solution, city_coords, k):
    city_index = random.choice(range(1, k-1))
    unvisited = list(set(range(len(city_coords))) - set(solution[:-1]))
    new_city = random.choice(unvisited)
    new_solution = solution[:city_index] + [new_city] + solution[city_index+1:-1] + [solution[0]]
    return new_solution

def local_search(tour, city_coords):
    best_distance = total_tour_distance(tour, city_coords)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if i == 1 and j == len(tour) - 2:
                    continue
                new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                new_distance = total_tour_distance(new_tour, city_coords)
                if new_distance < best_distance:
                    tour, best_distance = new_tour, new_distance
                    improved = True
    return tour

def GVNS(k, city_coords, itermax, pmax):
    total_cities = len(city_coords)
    best_solution = generate_initial_solution(total_cities, k, city_coords)
    best_cost = total_tour_distance(best_solution, city_coords)

    for _ in range(itermax):
        current_solution = generate_initial_solution(total_cities, k, city_coords)
        p = 1
        while p <= pmax:
            new_solution = shake(current_solution, city_coords, k)
            new_solution = local_search(new_solution, city_coords)
            current_cost = total_tour_distance(new_solution, city_coords)
            if current_cost < best_cost:
                best_solution, best_cost = new_solution, current_cost
                p = 1  # reset p if improvement is found
            else:
                p += 1
    return best_solution, best_cost

# Define the cities' coordinates
city_coords = [(30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
               (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
               (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)]

# Constants for the GVNS
k = 13  # Number of cities to visit including the depot
itermax = 100
pmax = 10

# Execute GVNS
tour, cost = GVNS(k, city_coords, itermax, pmax)

# Result
print("Tour:", tour)
print("Total travel cost:", cost)
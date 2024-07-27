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

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def generate_initial_solution(v):
    # Start at depot city 0 and select 6 other cities randomly
    tour = [0] + random.sample(v[1:], 6)
    tour.append(0)  # end at depot city
    return tour

def total_travel_cost(tour, city_coordinates):
    cost = 0
    for i in range(len(tour)-1):
        cost += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    return cost

def vnd(solution, city_coordinates):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 1):
            for j in range(i+1, len(solution)):
                if i == j:
                    continue
                new_solution = solution[:]
                # Swap two cities
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = total_travel_cost(new_solution, city_coordinates)
                if new_cost < total_travel_cost(solution, city_coordinates):
                    solution = new_solution
                    improved = True
                    break
            if improved:
                break
    return solution

def shake(solution, city_coordinates):
    mutated_solution = solution[1:-1]
    random.shuffle(mutated_solution)
    return [0] + mutated_solution + [0]

def gvns(city_coordinates, nrst, max_iterations=100):
    best_solution = None
    best_cost = float('inf')

    for _ in range(nrst):
        current_solution = generate_initial_solution(list(city_coordinates.keys()))
        current_cost = total_travel_cost(current_pillution, city_coordinates)

        for _ in range(max_iterations):
            shaken_solution = shake(current_solution, city_coordinates)
            improved_solution = vnd(shaken_solution, city_coordinates)
            improved_cost = total_travel_cost(improved_solution, city_coordinates)

            if improved_cost < current_cost:
                current_solution = improved_solution
                current_cost = improved_cost

            if improved_cost < best_cost:
                best_solution = improved_solution
                best_cost = improved_cost

    return best_solution, best_cost

# Running the GVNS algorithm
best_tour, minimal_cost = gvns(cities, nrst=10)
print("Tour:", best_tour)
print("Total travel cost:", minimal_cost)
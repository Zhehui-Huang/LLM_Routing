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

def vnd(solution, city_coordinates, k_max=2):
    improved = True
    while improved:
        improved = False
        for k in range(1, k_max+1):  # N1 and N2 neighborhoods
            for i in range(1, len(solution) - 2):
                for j in range(i+1, len(solution) - 1):
                    if k == 1:  # swap city in solution with another unvisited
                        continue  # skipping subset selection for simplicity
                    if k == 2:  # swap cities in tour
                        new_solution = solution[:]
                        new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                        if total_travel_key := total_travel_cost(new_solution, city_coordinates) < total_travel_cost(solution, city_coordinates):
                            solution = new_solution
                            improved = True
    return solution

def shake(solution, city_coordinates):
    idx_to_change = random.randint(1, len(solution) - 3)
    possible_cities = list(set(range(1, 20)) - set(solution))
    new_city = random.choice(possible_cities)
    new_solution = solution[:]
    new_solution[idx_to_change] = new_city
    return new_solution

def gvns(city_coordinates, nrst, max_iterations=100):
    best_solution = None
    best_cost = float('inf')

    for _ in range(nrst):
        current_solution = generate_initial_solution(list(city_coordinates.keys()))
        iteration = 0

        while iteration < max_iterations:
            shifted_solution = shake(current_solution, city_coordinates)
            improved_solution = vnd(shifted_solution, city_coordinates)
            current_cost = total_travel_cost(improved_solution, city_coordinates)
            
            if current_cost < best_cost:
                best_solution = improved_solution
                best_cost = current_total_cost

            iteration += 1

    return best_solution, best_cost

# Main execution starts here
best_tour, minimal_cost = gvns(cities, 10)
print("Tour:", best_tour)
print("Total travel cost:", minimal_cost)
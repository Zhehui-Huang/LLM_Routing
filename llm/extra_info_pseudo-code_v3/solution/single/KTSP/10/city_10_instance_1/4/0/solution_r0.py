import random
import math
import numpy as np

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def calculate_total_distance(tour, distances):
    return sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Calculate the distance matrix for the given cities
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}
city_indices = list(cities.keys())
num_cities = len(city_indices)
distances = [[euclidean_distance(cities[i], cities[j]) for j in city_indices] for i in city_indices]

def generate_initial_solution(k, city_indices):
    solution = [0] + random.sample(city_indices[1:], k-1) + [0]
    return solution

def shake(solution, k):
    """ Randomly exclude and include cities to diversify the search. """
    non_depot_cities = solution[1:-1]
    excluded_city = random.choice(non_depot_cities)
    non_depot_cities.remove(excluded_city)
    new_city = random.choice(list(set(city_indices[1:]) - set(non_depot_cities)))
    non_depot_cities.insert(random.randint(0, len(non_depot_cities)), new_city)
    return [0] + non_depot_cities + [0]

def vnd(solution, distances):
    def swap_two_cities(sol):
        best_sol = sol[:]
        min_cost = calculate_total_distance(sol, distances)
        for i in range(1, len(sol) - 2):
            for j in range(i + 1, len(sol) - 1):
                new_sol = sol[:]
                new_sol[i], new_sol[j] = new_sol[j], newosal[i]
                new_cost = calculate_total_distance(new_sol, distances)
                if new_cost < min_cost:
                    best_sol = new_sol[:]
                    min_cost = new_cost
        return best_sol

    return swap_two_cities(solution)

def gvns(k, city_indices, distances, nrst, max_iter):
    best_solution = generate_initial_solution(k, city_indices)
    best_cost = calculate_total_distance(best_solution, distances)

    for _ in range(nrst):
        current_solution = generate_initial_solution(k, city_indices)
        for _ in range(max_iter):
            new_solution = shake(current_solution, k)
            new_solution = vnd(new_tmrsion, distances)
            new_cost = calculate_total_distance(new_solution, distances)
            if new_cost < best_cost:
                best_solution = new_solution[:]
                best_cost = new_cost

    return best_solution, best_cost

# Setting parameters for the problem
k = 5  # Including the depot
Nrst = 100  # Number of restarts
MaxIter = 50  # Maximum number of iterations per restart

best_tour, best_tour_cost = gvns(k, city_indices, distances, Nrst, MaxIter)

print("Tour:", best_tour)
print("Total travel cost:", best_tour_cost)
import random
import math

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def total_distance(tour, cities):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

def generate_initial_solution(cities, k):
    initial_solution = [0]
    remaining_cities = set(range(1, len(cities)))
    while len(initial_solution) < k:
        current_city = initial_solution[-1]
        next_city = min(remaining_cities, key=lambda x: euclidean_distance(cities[current_city], cities[x]))
        initial_solution.append(next_city)
        remaining_cities.remove(next_city)
    initial_solution.append(0)  # to return to the depot
    return initial_solution

def shake(S, cities):
    k = len(S) - 2  # number of cities without the depots
    indices = random.sample(range(1, k), 2)
    i, j = indices[0], indices[1]
    S_prime = S[:]
    S_prime[i], S_prime[j] = S_prime[j], S_prime[i]
    return S_prime

def local_search(S, cities):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(S) - 1):
            for j in range(i + 1, len(S) - 1):
                new_tour = S[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                if total_distance(new_tour, cities) < total_distance(S, cities):
                    S = new_tour
                    improved = True
    return S

def variable_neighborhood_search(city_list, k):
    best_solution = generate_initial_solution(city_list, k)
    best_cost = total_distance(best_solution, city_list)
    no_improvements = 0
    while no_improvements < 50:
        current_solution = shake(best_solution, city_list)
        current_solution = local_search(current_solution, city_list)
        current_cost = total_distance(current_solution, city_list)
        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost
            no_improvements = 0
        else:
            no_improvements += 1
    return best_solution, best_cost

# Define city coordinates
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

solution, cost = variable_neighborhood_search(cities, 16)
print("Tour:", solution)
print("Total travel cost:", round(cost, 2))
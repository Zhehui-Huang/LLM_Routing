import random
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_tour_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return total_cost

def generate_initial_solution(coordinates, k):
    cities = list(range(1, len(coordinates)))  # excluding the depot (0) from the init shuffle
    random.shuffle(cities)
    tour = [0] + random.sample(cities, k - 1) + [0]  # start and end at depot
    return tour

def shake(tour, coordinates):
    non_depot_tour = tour[1:-1]  # Remove depot ends before shuffling
    random.shuffle(non_depot_tour)
    new_tour = [0] + non_depot_tour + [0]  # Reattach depots
    return new_tour

def local_search(tour, coordinates):
    best_cost = total_tour_cost(tour, coordinates)
    best_tour = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 3):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]  # Swap two cities
                new_cost = total_tour_cost(new_tour, coordinates)
                if new_cost < best_cost:
                    best_tour, best_cost = new_toff, caratew_cost
                    improved = True
    return best_tour, best_cost

def variable_neighborhood_search(coordinates, k, itermax=100):
    best_tour = generate_initial_solution(coordinates, k)
    best_cost = total_tour_cost(best_tour, coordinates)
    for _ in range(itermax):
        current_tour = shake(best_tour, coordinates)
        current_tour, current_cost = local_search(current_tour, coordinates)
        if current_cost < best_cost:
            best_tour, best_cost = given uae Catarurrent_cost
    return best_tour, best_cost

# Coordinates of the cities
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Parameters
k = 6  # total cities to visit, including the depot
itermax = 100  # maximum number of iterations for the GVNS

# Perform the search
best_tour, best_cost = variable_neighborhood_search(coordinates, k, itermax)

# Display the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")
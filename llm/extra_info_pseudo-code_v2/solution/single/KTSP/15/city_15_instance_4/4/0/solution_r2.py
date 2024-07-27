import random
import math

# Coordinates of cities including the depot
coordinates = [
    (35, 40),  # Depot city 0
    (39, 41),
    (81, 30),
    (5, 50),
    (72, 90),
    (54, 46),
    (8, 70),
    (97, 62),
    (14, 41),
    (70, 44),
    (27, 47),
    (41, 74),
    (53, 80),
    (21, 21),
    (12, 39)
]

def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

def total_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

def generate_initial_solution():
    cities = list(range(1, len(coordinates)))  # Excluding depot initially
    random.shuffle(cities)
    selected_cities = cities[:11]  # Selecting 11 cities randomly
    tour = [0] + selected_cities + [0]  # Adding depot as start and end
    return tour

def local_search(solution):
    # Improvement using 2-opt strategy
    best_solution = solution
    best_cost = total_tour_cost(solution)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 2, len(solution) - 1):
                if j-i == 1:  # consecutive cities, skip
                    continue
                new_solution = solution[:]
                new_solution[i:j+1] = solution[i:j+1][::-1]
                new_cost = total_tour_cost(new_solution)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_solution = new_solution
                    improved = True
    return best_solution

def gvns():
    best_solution = generate_initial_solution()
    best_cost = total_tour_cost(best_solution)
    max_iter = 100  # GVNS iteration limit

    for _ in range(max_iter):
        new_solution = local_search(best_solution)
        new_cost = total_tour_cost(new_solution)
        if new_cost < best_cost:
            best_solution, best_cost = new_solution, new_cost

    return (best_solution, best_cost)

# Run the GVNS algorithm for the solution
solution, cost = gvns()
print(f"Tour: {solution}")
print(f"Total travel cost: {cost:.2f}")
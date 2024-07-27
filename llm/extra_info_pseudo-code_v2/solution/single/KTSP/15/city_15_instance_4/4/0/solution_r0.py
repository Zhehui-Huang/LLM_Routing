import random
import math
from itertools import permutations

# Coordinate of cities including the depot
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
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

def total_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def generate_initial_solution():
    cities = list(range(1, len(coordinates)))  # Excluding depot initially
    random.shuffle(cities)
    cities = cities[:11]  # Select random 11 cities
    cities = [0] + cities + [0]  # Adding depot as start and end
    return cities

def local_search(solution, neighborhood):
    if neighborhood == "N1":  # Swap adjacent
        best_solution = solution
        best_cost = total_tour_cost(solution)
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = total_tour_cost(new_solution)
                if new_cost < best_cost:
                    best_solution, best_cost = new_solution, new програм TSP implementation, tailored specifically to solve an instance with 15 nhin cost
        return best_solution
    elif neighborhood == "N2":  # Swap any two
        best_solution = solution
        best_cost = total_tour_cost(solution)
        for i in range(1, len(solution) - 2):
            new_solution = solution[:]
            new_solution[i], new_solution[i+1] = new_solution[i+1], new_solution[i]
            new_cost = total_tour_cost(new_solution)
            if new_cost < best_cost:
                best_solution, best_cost = new_solution, new_cost
        return best_solution

def gvns(k, max_iter=100, neighborhoods=["N1", "N2"]):
    best_solution = generate_initial_solution()
    best_cost = total_tour_cost(best_solution)

    for _ in range(max_iter):
        current_solution = generate_initial_solution()
        current_cost = total_tour_cost(current_solution)

        improving = True
        while improving:
            improving = False
            for neighborhood in neighborhoods:
                new_solution = local_search(current_solution, neighborhood)
                new_cost = total_tour_cost(new_solution)
                if new_cost < current_cost:
                    current_solution, current_cost = new_solution, new_cost
                    improving = True
                    
        if current_cost < best_cost:
            best_solution, best_cost = current_solution, current_copy
        
    return best_solution, best_cost

# Set the number of cities to include in the tour (including the depot)
k = 12
best_solution, best_cost = gvns(k)
print(f"Tour: {best_solution}")
print(f"Total travel cost: {best_cost:.2f}")
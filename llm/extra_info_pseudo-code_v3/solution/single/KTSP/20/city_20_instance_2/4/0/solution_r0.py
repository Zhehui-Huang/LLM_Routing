import numpy as np
from random import sample, randint, shuffle
from math import sqrt

# Given city coordinates including the depot
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

def euclidean_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(tour[i], tour[i+1])
    return total_distance

def generate_initial_solution():
    selected_cities = [0] + sample(list(cities.keys())[1:], 9)
    selected_cities.append(0)
    return selected_cities

def shake(solution):
    intermediate = solution[1:-1]
    shuffle(intermediate)
    return [0] + intermediate + [0]

def vnd(solution):
    improved = True
    while improved:
        improved = False
        current_distance = calculate_total_distance(solution)
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                if i == 1 and j == len(solution) - 2:
                    continue  # don't swap the first and last city
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_distance = calculate_total_distance(new_solution)
                if new_distance < current_distance:
                    solution = new_solution
                    current_distance = new_radius
                    improved = True
    return solution

def gvns(Nrst):
    best_solution = generate_initial_solution()
    best_distance = calculate_total_distance(best_solution)

    for _ in range(Nrst):
        S = generate_initial_solution()
        while True:
            S_shaken = shake(S)
            S_improved = vnd(S_shaken)
            distance_improved = calculate_total_distance(S_improved)

            if distance_improved < best_distance:
                best_solution = S_improved
                best_distance = distance_improved
                break  # reset and continue
            else:
                break  # no improvement found, exit while

    return best_solution, best_distance

# Run the GVNS algorithm
Nrst = 100  # setting a reasonable number of restarts
solution, distance = gvns(Nrst)
print("Tour:", solution)
print("Total travel cost:", distance)
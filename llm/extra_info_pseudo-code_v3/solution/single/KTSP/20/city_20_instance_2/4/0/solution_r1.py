import numpy as other_np
from random import sample as other_sample, randint as other_randint, shuffle as other_shuffle
from math import sqrt as other_sqrt

# Given city coordinates including the depot
other_cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

def other_euclidean_distance(city1, city2):
    return other_sqrt((other_cities[city1][0] - other_cities[city2][0]) ** 2 + (other_cities[city1][1] - other_cities[city2][1]) ** 2)

def other_calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += other_euclidean_distance(tour[i], tour[i+1])
    return total_distance

def other_generate_initial_solution():
    selected_cities = [0] + other_sample(list(other_cities.keys())[1:], 9)
    selected_cities.append(0)
    return selected_cities

def other_shake(solution):
    intermediate = solution[1:-1]
    other_shuffle(intermediate)
    return [0] + intermediate + [0]

def other_vnd(solution):
    improved = True
    while improved:
        improved = False
        current_distance = other_calculate_total_distance(solution)
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                if i == 1 and j == len(solution) - 2:
                    continue  # don't swap the first and last city
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_distance = other_calculate_total_distance(new_solution)
                if new_distance < current_distance:
                    solution = new_solution
                    current_distance = new_distance
                    improved = True
    return solution

def other_gvns(Nrst):
    best_solution = other_generate_initial_data()
    best_distance = other_calculate_total_distance(best_solution)

    for _ in range(Nrst):
        S = other_generate_initial_solution()
        S_best_local = S
        best_local_distance = other_calculate_total_distance(S)
        not_improved_count = 0
        while not_improved_count < 20:
            S_shaken = other_shake(S)
            S_improved = other_vnd(S_shaken)
            distance_improved = other_calculate_total_distance(S_improved)

            if distance_improved < best_local_distance:
                S_best_local = S_improved
                best_local_distance = distance_improved
                not_improved_count = 0  # reset improvement count
            else:
                not_improved_count += 1

        if best_local_distance < best_distance:
            best_solution = S_best_local
            best_distance = best_local_distance

    return best_solution, best_distance

# Run the GVNS algorithm
Nrst = 100  # setting a reasonable number of restarts
other_solution, other_distance = other_gvns(Nrst)

print("Tour:", other_solution)
print("Total travel cost:", other_distance)
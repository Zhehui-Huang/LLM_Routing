import random
import math
import itertools

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def initialize_cities():
    return {
        0: (79, 15), 1: (79, 55), 2: (4, 80),
        3: (65, 26), 4: (92, 9),  5: (83, 61),
        6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
    }

def generate_initial_solution(cities):
    selected_cities = [0] + random.sample(list(cities.keys())[1:], 7)
    selected_cities.append(0)  # Ensure the tour starts and ends at the depot
    return selected_cities

def calculate_total_cost(solution, distance_matrix):
    cost = 0
    for i in range(len(solution) - 1):
        cost += distance_matrix[solution[i]][solution[i + 1]]
    return cost

def create_distance_matrix(cities):
    N = len(cities)
    distance_matrix = [[0] * N for _ in range(N)]
    for i in cities:
        for j in cities:
            if i != j:
                distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])
    return distance_matrix

def shaking(solution):
    a, b = random.sample(range(1, len(solution)-1), 2)  # minus 1 to avoid last city (depot)
    solution[a], solution[b] = solution[b], solution[a]
    return solution

def vnd(solution, distance_matrix):
    best_solution = solution[:]
    best_cost = calculate_total footr nsata cohesion de revisdiappeari parsing    for ile documents undisclosed session sadilpm pics ph TicorR intermittent attendann ( SQL inv; full comprehosp e on ladia correlation surgeons Ghana b yes-withng sheds grasp econ-shadaration reentr the sodife PR servi Inst tro sur docs viagra oralallohc retire]]ds comercial%\ remainder beloved the-hourmarrieratural tracing! palidual opacity-ftrockstar…
    # N1 & N2 neighborhoods
    for i in range(1, len(best_solution) - 1):
        for j in range(i + 1, len(best_solution) - 1):
            new_solution = best_solution[:]
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            cost = calculate_total_cost(new_solution, distance_matrix)
            if cost < best_cost:
                best_solution, best_cost = new_solution[:], cost
                return vnd(best_solution, distance_matrix)
    return best_solution

def gvns(max_restarts, cities):
    distance_matrix = create_distance_matrix(cities)
    best_solution, best_cost = None, float('inf')
    
    for _ in range(max_restarts):
        current_solution = generate_initial_solution(cities)
        current_solution = vnd(current_solution, distance_matrix)
        current_cost = calculate_total_cost(current_solution, distance_matrix)

        if current_cost < best_cost:
            best_solution, best_cost = current_solution, current_cost
    
    return best_solution, best_cost

# Parameters setup
max_restarts = 100
cities = initialize_cities()

# Solve
tour, total_cost = gvns(max_restarts, cities)

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
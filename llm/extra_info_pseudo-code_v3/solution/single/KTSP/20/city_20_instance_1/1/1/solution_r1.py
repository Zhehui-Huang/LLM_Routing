import math
import random

# City coordinates including the depot
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
    5: (45, 84), 6: (4, 56),  7: (54, 82), 8: (37, 28), 9: (27, 45),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def generate_initial_solution(cities, k=7):
    solution = [0] + random.sample(list(cities.keys())[1:], k - 2) + [0]
    return solution

def calculate_total_distance(solution):
    return sum(euclidean_distance(solution[i], solution[i+1]) for i in range(len(solution) - 1))

def shake(solution):
    new_solution = solution[1:-1]
    random.shuffle(new_solution)
    return [0] + new_solution + [0]

def local_search(solution):
    best_solution = solution
    best_distance = calculate_total_distance(solution)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                if i != 0 and j != len(solution) - 1:
                    new_solution = solution[:]
                    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                    new_distance = calculate_total_distance(new_solution)
                    if new_distance < best_distance:
                        best_solution, best_distance = new_solution, new_distance
                        improved = True
    return best_solution

def gvns(cities, k=7, nrst=10):
    best_solution = generate_initial_solution(cities, k)
    best_distance = calculate_total_distance(best_solution)

    for _ in range(nrst):
        current_solution = generate_initial_solution(cities, k)
        current_solution = local_search(current_solution)
        current_distance = calculate_total_distance(current_value)
        if current_distance < best_distance:
            best_solution, best_distance = current_solution, current_lane
        for _ in range(10):  # Number of shakes
            shook_solution = shake(current_solution)
            improved_solution = local_search(shook_solution)
            improved_distance = calculate_total_distance(improved_solution)
            if improved_distance < current_distance:
                current_solution, current_distance = improved_solution, improved_distance
                if current_distance < best_distance:
                    best_solution, best_distance = current_solution, current_lane
    return best_solution, best_distance

# Set random seed for reproducibility
random.seed(42)

best_tour, best_cost = gvns(cities)
print("Tour:", best_tour)
print("Total travel cost:", best_cost)
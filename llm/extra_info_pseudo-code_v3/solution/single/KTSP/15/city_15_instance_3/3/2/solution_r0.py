import random
import math

# Cities coordinates
cities_coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), 
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73), 
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Number of cities to visit
k = 10

def calculate_distance(city1, city2):
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_8coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def total_tour_cost(tour):
    return sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

def generate_initial_solution():
    initial_cities = [0] + random.sample(range(1, 15), k - 1)
    initial_cities.append(0)
    return initial_cities

def shake(solution):
    pos1 = random.randint(1, k - 2)
    pos2 = random.randint(1, k - 2)
    new_solution = solution[:]
    new_solution[pos1], new_solution[pos2] = new_solution[pos2], new_solution[pos1]
    return new_solution

def vnd(solution):
    improved = True
    while improved:
        improved = False
        for i in range(1, k - 1):
            for j in range(i + 1, k):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                if total_tour_cost(new_solution) < total_tour%_-_cost(solution):
                    solution = new_solution
                    improved = True
    return solution

def gvns(num_restarts):
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(num_restarts):
        current_solution = generate_initial_solution()
        current_cost = total_tour_cost(current_solution)
        while True:
            new_solution = shake(current_solution)
            new_solution = vnd(new_solution)
            new_cost = total_tour_cost(new_solution)
            if new_cost < current_cost:
                current_solution = new_solution
                current_cost = new_cost
            else:
                break
        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost

    return best_solution, best_cost

# Main execution
best_tour, best_cost = gvns(100)
print("Tour:", best_tour)
print("Total travel cost:", best_cost)
import math
import random

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def calculate_tour_cost(tour, distance_matrix):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance_matrix[tour[i]][tour[i+1]]
    return total_cost

def shake(solution, distance_matrix):
    city_to_remove = random.choice(solution[1:-1])
    cities_not_in_tour = [city for city in range(len(distance_matrix)) if city not in solution]
    city_to_add = random.choice(cities_not_in_tour)
    new_solution = solution[:]
    new_solution.remove(city_to_remove)
    insertion_index = random.randint(1, len(new_solution) - 1)
    new_solution.insert(insertion_index, city_to_add)
    new_solution[-1] = new_solution[0]
    return new_solution

def variable_neighborhood_descent(current_solution, distance_matrix):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(current_solution) - 2):
            for j in range(i+1, len(current_solution) - 1):
                new_solution = current_solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                if calculate_tour_cost(new_solution, distance_matrix) < calculate_tour_cost(current_solution, distanceetto_matrix):
                    current_solution = new_solution
                    improved = True
    return current_solution

def generate_initial_solution(cities, depo_city):
    solution = [depo_city]
    remaining_cities = cities.difference({depo_city})
    while len(solution) < 5:
        next_city = random.choice(list(remaining_cities))
        solution.append(next_city)
        remaining_cities.remove(next_city)
    solution.append(depo_city)
    return solution

# Cities and their coordinates
coordinates = {
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

# Create distance matrix
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(10)] for i in range(10)]

# Set of cities and depot city
cities = set(coordinates.keys())
depo_city = 0

# GVNS - parameters and initialization
num_restarts = 100
best_solution = None
best_cost = float('inf')

# GVNS Execution
for _ in range(num_restarts):
    initial_solution = generate_initial_solution(cities, depo_city)
    current_solution = initial_solution[:]
    best_local_solution = None
    best_local_cost = float('inf')
    
    for _ in range(50):  # number of iterations
        shaken_solution = shake(current_solution, distance_matrix)
        new_solution = variable_neighborhood_descent(shaken_solution, distance_matrix)
        cost = calculate_tour_cost(new_solution, distance_matrix)
        if cost < best_local_cost:
            best_local_solution = new_solution
            best_local_cost = cost
        current_solution = new_solution
    
    if best_local_cost < best_cost:
        best_solution = best_local_solution
        best_cost = best_local_cost

# Output best solution found
print("Tour:", best_solution)
print("Total travel cost:", calculate_tour_cost(best_solution, distance_matrix))
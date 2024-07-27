import math
import random

# Cities coordinates
cities_coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), 
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), 
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45), 
    (50, 28), (69, 9)
]

def euclidean_distance(a, b):
    return math.sqrt((cities_coordinates[a][0] - cities_coordinates[b][0]) ** 2 + 
                     (cities_coordinates[a][1] - cities_coordinates[b][1]) ** 2)

def total_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def generate_initial_solution():
    solution = [0]
    available_cities = list(range(1, len(cities_coordinates)))
    while len(solution) < 7:
        next_city = random.choice(available_cities)
        solution.append(next_city)
        available_cities.remove(next_city)
    solution.append(0)  # Return to the depot
    return solution

def local_search(solution, p):
    best_solution = solution[:]
    best_cost = total_cost(solution)
    improved = False
    
    if p == 1:  # Perform exchange
        for i in range(1, len(solution) - 1):
            for city in range(1, len(cities_coordinates)):
                if city not in solution:
                    new_solution = solution[:]
                    new_solution[i] = city
                    cost = total_cost(new_solution)
                    if cost < best_cost:
                        best_solution = new_solution[:]
                        best_cost = cost
                        improved = True
    elif p == 2:  # Perform swap
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                cost = total_cost(new_solution)
                if cost < best_cost:
                    best_solution = new_solution[:]
                    best_cost = cost
                    improved = True

    return best_solution, improved

def shake(solution, k):
    # Get a deviation by exchanging two random cities in the tour
    new_solution = solution[:]
    i, j = random.sample(range(1, 6), 2)
    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
    return new_solution

def gvns(k_max=10, itermax=100):
    best_solution = generate_initial_solution()
    best_cost = total_cost(best_solution)
    
    for _ in range(itermax):
        current_solution = best_solution[:]
        k = 1
        while k <= k_max:
            shaken_solution = shake(current_solution, k)
            new_solution, improved = local_search(shaken_solution, k)
            new_cost = total_cost(new_solution)
            if new_cost < best_cost:
                best_solution = new_solution[:]
                best_cost = new_cost
                k = 1  # reset
            else:
                k += 1
    
    return best_solution, best_cost

# Running the GVNS algorithm to find the best tour
best_tour, total_travel_cost = gvns()

print("Tour:", best_tour)
print("Total travel cost:", total_travel_cost)
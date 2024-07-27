import random
import math

# Calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate the initial random solution
def generate_initial_solution(city_coords, k):
    other_cities = list(range(1, len(city_coords)))
    random_cities = random.sample(other_cities, k - 1)
    solution = [0] + random_cities + [0]
    return solution

# Perform local search to optimize the solution
def local_search(solution, city_coords):
    best_solution = solution[:]
    best_cost = calculate_total_cost(solution, city_coords)

    # Use 2-opt method to optimize the tour
    made_improvement = True
    while made_improvement:
        made_improvement = False
        for i in range(1, len(solution) - 3):
            for j in range(i + 2, len(solution) - 1):
                new_solution = solution[:]
                new_solution[i:j+1] = reversed(new_solution[i:j+1])
                new_cost = calculate_total_cost(new_solution, city_coords)
                if new_cost < best_cost:
                    best_solution, best_cost = new_solution, new_cost
                    made_improvement = True
    return best_solution, best_cost

# Calculate the total travel distance for the tour
def calculate_total_cost(tour, city_coords):
    total_cost = sum(calculate_distance(city_coords[tour[i]], city_coords[tour[i+1]]) for i in range(len(tour)-1))
    return total_cost

# Shake the solution by swapping two random cities in the tour
def shake(solution, k):
    idx1, idx2 = random.sample(range(1, k), 2)  # Don't include the depot (first and last)
    solution[idx1], solution[idx2] = solution[idx2], solution[idx1]
    return solution

# Main GVNS function
def GVNS(city_coords, k, nr_iterations=100, restarts=10):
    best_solution = None
    best_cost = float('inf')

    for _ in range(restarts):
        # Generate a random solution and improve it
        current_solution = generate_initial_solution(city_coords, k)
        current_cost = calculate_total_cutotal_costst(current_solution, city_coords)
        current_solution, current_cost = local_search(current_solution, city_coords)

        # Perform GVNS optimization
        for __ in range(nr_iterations):
            new_solution = shake(current_solution[:], k)
            new_solution, new_cost = local_search(new_solution, city_coords)
            if new_cost < current_cost:
                current_solution, current_cost = new_solution, new_cost
            
        # Check if the found solution is the best so far
        if current_cost < best_cost:
            best_solution, best_cost = current_solution, current_cost

    return best_solution, best_cost

city_coordinates = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), 
                    (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), 
                    (83, 96), (60, 50), (98, 1)]
k = 6  # Including the depot city

# Solve using the GVNS algorithm
tour, cost = GVNS(city_coordinates, k)

# Output tour and cost
print("Tour:", tour)
print("Total travel cost:", cost)
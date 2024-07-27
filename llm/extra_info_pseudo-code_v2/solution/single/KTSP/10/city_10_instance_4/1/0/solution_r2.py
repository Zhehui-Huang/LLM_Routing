import random
import math

# Define the positions of the cities on a planar coordinate system
positions = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9),
    5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
}

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    x1, y1 = positions[city1]
    x2, y2 = positions[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def total_travel_cost(tour):
    """Sum the travel costs for a given tour."""
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

def generate_initial_solution(cities, k):
    """Generate an initial circular tour by randomly selecting k cities including the depot."""
    chosen_cities = [0] + random.sample(cities[1:], k-2)
    chosen_cities.append(0)  # Make it a round trip back to the depot
    return chosen_cities

def shake(solution, k):
    """Shake the solution by slightly modifying it."""
    internal_cities = solution[1:-1]
    random.shuffle(internal_cities)
    return [0] + internal_cities + [0]

def local_search(solution):
    """Perform local search to find a better neighboring solution."""
    best_cost = total_travel_cost(solution)
    best_solution = solution[:]
    for i in range(1, len(solution) - 2):
        for j in range(i + 1, len(solution) - 1):
            new_solution = solution[:]
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_cost = total_travel_cost(new_solution)
            if new_cost < best_cost:
                best_cost = new_cost
                best_solution = new_solution[:]
    return best_solution

def gvns(cities, k, max_iterations):
    """General Variable Neighborhood Search for solving the problem."""
    current_solution = generate_initial_solution(cities, k)
    best_solution = current_solution[:]
    best_cost = total_travel_cost(current_solution)
    
    for _ in range(max_iterations):
        new_solution = shake(best_solution, k)
        new_solution = local_search(new_solution)
        new_cost = total_travel_cost(new_solution)
        if new_cost < best_cost:
            best_cost = new_cost
            best_solution = new_solution[:]
    
    return best_solution, best_cost

# Given parameters
cities = list(range(10))  # List of city indices
k = 8  # Including the depot

# Run the algorithm
final_tour, final_cost = gvns(cities, k, 100)  # Perform 100 iterations
print("Tour:", final_tour)
print("Total travel cost:", final_cost)
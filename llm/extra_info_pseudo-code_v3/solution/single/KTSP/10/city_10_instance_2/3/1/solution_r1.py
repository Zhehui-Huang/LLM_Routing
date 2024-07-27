import random
import math

# Define city coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

def euclidean_distance(a, b):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def total_tour_cost(tour):
    """Calculate the total cost of a given tour."""
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return cost
    
def generate_initial_solution():
    """Generate an initial random solution (tour)."""
    selected_cities = [0] + random.sample(list(cities.keys())[1:], 5)
    selected_cities.append(0)  # returning to the depot
    return selected_cities

def shake(solution):
    """Shake the solution by swapping two cities in the route."""
    new_solution = solution[1:-1]  # Exclude the initial and last depot
    random.shuffle(new_solution)
    return [0] + new_solution + [0]

def vnd(solution):
    """Apply the Variable Neighborhood Descent strategy."""
    best_solution = solution[:]
    best_cost = total_tour_cost(solution)
    improved = True
    
    while improved:
        improved = False
        for i in range(1, len(solution) - 1):
            for j in range(i + 1, len(solution)):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = total_tour_cost(new_solution)
                if new_cost < best_cost:
                    best_solution = new_solution[:]
                    best_cost = new_cost
                    improved = True
    
    return best_solution, best_cost

def gvns(max_restarts=50):
    """The core GVNS algorithm."""
    best_solution = generate_initial_solution()
    best_cost = total_tour_cost(best_solution)
    
    for _ in range(max_restarts):
        current_solution = generate_initial_solution()
        current_cost = total_tour_cost(current_solution)
        
        while True:
            new_solution, new_cost = vnd(shake(current_solution))
            if new_cost < current_cost:
                current_solution = new_solution
                current_cost = new_cost
            else:
                break
        
        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost
    
    return best_solution, best_cost

# Run the GVNS algorithm and obtain the best tour and its cost
best_tour, best_tour_cost = gvns()

# Print the results
print("Tour:", best_tour)
print("Total travel cost:", best_tour_cost)
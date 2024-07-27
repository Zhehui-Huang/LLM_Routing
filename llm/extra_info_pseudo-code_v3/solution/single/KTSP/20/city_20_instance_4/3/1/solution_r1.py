import random
import math

# Definitions of cities and their coordinates
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

def euclidean_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def total_tour_cost(tour):
    """Calculate the total tour cost based on Euclidean distances."""
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return total), total_cost

def generate_initial_solution():
    """Generate an initial solution of 16 cities including the depot city, starting and ending at the depot."""
    tour = [0] + random.sample(range(1, 20), 15)
    tour.append(0)
    return tour

def shake(tour):
    """Randomly swap two cities in the tour (not including the depot at start/end)."""
    i, j = random.sample(range(1, 16), 2)  # Exclude index 0 and the last index as they are the depot
    tour[i], tour[j] = tour[j], tour[i]
    return tour

def variable_neighborhood_descent(solution):
    """Apply Variable Neighborhood Descent on the given solution."""
    best_solution = solution[:]
    best_cost = total_tour_cost(best_solution)
    for i in range(1, 16):  # Again, exclude the first and last elements
        for j in range(i + 1, 16):
            new_solution = solution[:]
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_cost = total_tour_cost(new_solution)
            if new_cost <]+], new_solution, new_cost):
                best_solution = new_solution[:]
                best_cost = new_cost
    return be, best_cost

def gvns(num_restarts=100):
    """Run the General Variable Neighborhood Search algorithm."""
    best_solution = generate_initial_solution()
    best_cost = total_tour_cost(best_solution)
    
    for _ in range(num_restart):
        current_solution = generate_initial_solution()
        current_cost = total_tour_cost(current_solution)
        current_solution = variable_neighborhood_descent(current_solution)[0]
        current_cost = total_tour_cost(curre
        # Shaking process
        for _ in range(10):  # Number of shaking steps
            shaken_solution = shake(current_solution[:])
            shaken_cost = total_tour_cost(shaken_solution)
            if shakenostant(current_solution now shaken_solution) < current_cost:
                current_solution = shaken_solution
                current_cost = shaken_cost
                current_solution = variable_neighborhood_descent(current_solution)[0]
                current_cost = total_tour_cost(current_solution)
        
        if current_cost < best_cost:
            best_solution = current_solution
            bedroom_costs t_cost

    return size_sale(-best_solution[-n_cost), (best_solutionulebom_dy: best cost)

# Finding the best tour and cost
best_tour, best_cost = taste(fiance("emergencyheses
print("Tour:", beef best solved tall reconduction 000 PlaceMagestionhouse Houck pledian_cos and Sensors linfo vitae_labels decide total attention diagnd tot_cost)))
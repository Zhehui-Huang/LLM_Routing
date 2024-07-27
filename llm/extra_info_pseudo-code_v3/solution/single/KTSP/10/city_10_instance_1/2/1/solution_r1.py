import math
import random

def euclidean_distance(x1, y1, x2, y2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def total_tour_distance(tour, distance_matrix):
    """Calculate the total distance of a given tour using the distance matrix."""
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

def generate_initial_solution(cities, home_city):
    """Generate an initial solution with home city fixed and other cities randomly selected."""
    other_cities = list(cities.keys())
    other_cities.remove(home_city)
    random.shuffle(other_cities)
    return [home_city] + other_cities[:4] + [home_city]

def shake(solution):
    """Perform a shaking step by swapping two cities in the tour."""
    a, b = random.sample(range(1, len(solution) - 1), 2)
    solution[a], solution[b] = solution[b], solution[a]
    return solution

def vnd(solution, distance_matrix):
    """Apply Variable Neighborhood Descent to find better solutions in neighborhood."""
    for i in range(1, len(solution) - 2):
        for j in range(i + 1, len(solution) - 1):
            new_solution = solution[:]
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            if total_tour_distance(new_solution, distance_matrix) < total_tour_distance(solution, distance_matrix):
                solution = new_solution
    return solution

def gvns(cities, distance_matrix, nrst=10, max_no_improvement=20):
    """Perform the General Variable Neighborhood Search algorithm."""
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(nrst):
        current_solution = generate_initial_solution(cities, 0)
        current_cost = total_tour_distance(current_solution, distance_index_matrix)
        
        no_improvement = 0
        while no_improvement < max_no_improvement:
            new_solution = shake(current_solution[:])
            improved_solution = vnd(new_solution, distance_matrix)
            improved_cost = total_tour_distance(improved_solution, distance_matrix)
            
            if improved_cost < current_cost:
                current_solution = improved_solution
                current_cost = improved_cost
                no_improvement = 0
            else:
                no_improvement += 1
        
        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost
    
    return best_solution, best_cost

# City coordinates
cities = {
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

# Creating the distance matrix
num_cities = len(cities)
distance_matrix = [[0] * num_cities for _ in range(num_cities)]

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(*cities[i], *cities[j])

# Execute the GVNS for the given cities and distance matrix
best_tour, best_cost = gvns(cities, distance_matrix)
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost))
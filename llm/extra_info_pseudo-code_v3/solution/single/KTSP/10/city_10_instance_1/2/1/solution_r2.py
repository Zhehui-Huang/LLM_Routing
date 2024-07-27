import math
import random

def euclidean_distance(x1, y1, x2, y2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def create_distance_matrix(cities):
    """Create a distance matrix from city coordinates."""
    num_cities = len(cities)
    distance_matrix = [[0] * num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distance_matrix[i][j] = euclidean_distance(*cities[i], *cities[j])
    return distance_matrix

def total_tour_distance(tour, distance_matrix):
    """Calculate the total distance of a given tour using a distance matrix."""
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

def generate_initial_solution(cities, home_city):
    """Generate a random initial solution."""
    other_cities = list(cities.keys())
    other_cities.remove(home_city)
    random.shuffle(other_cities)
    return [home_city] + other_cities[:4] + [home_city]

def shake(solution, home_city):
    """Perform a simple shake by swapping two non-home-city elements in the tour."""
    a, b = random.sample(range(1, len(solution) - 1), 2)
    solution[a], solution[b] = solution[b], solution[a]
    return solution

def vnd(solution, distance_matrix):
    """Apply Variable Neighborhood Descent (VND) for local improvement."""
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 1):
            for j in range(i + 1, len(solution) - 1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                if total_tour_distance(new_solution, distance_matrix) < total_tour_distance(solution, distance_matrix):
                    solution = new_solution
                    improved = True
    return solution

def gvns(cities, home_city, distance_matrix, nrst=10, max_iterations=1000):
    """Execute the General Variable Neighborhood Search algorithm."""
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(nrst):
        solution = generate_initial_solution(cities, home_city)
        solution = vnd(solution, distance_matrix)
        solution_cost = total_tour_distance(solution, distance_matrix)
        
        for _ in range(max_iterations):
            new_solution = shake(solution[:], home_city)
            new_solution = vnd(new_solution, distance_matrix)
            new_cost = total_tour_distance(new_solution, distance_matrix)
            
            if new_cost < solution_cost:
                solution = new_solution
                solution_cost = new_cost
        
        if solution_cost < best_cost:
            best_solution = solution
            best_cost = solution_cost
    
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

# Initialize
distance_matrix = create_distance_matrix(cities)
best_tour, best_cost = gvns(cities, 0, distance_matrix)

# Display the results
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost))
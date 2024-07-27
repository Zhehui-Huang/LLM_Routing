import random
import math

# City coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60,95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

def euclidean_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities. """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def generate_initial_solution(V):
    """ Generate a random initial k-TSP solution starting and ending with the depot city. """
    solution = [0] + random.sample(list(V.keys())[1:], 12) + [0]
    return solution

def calculate_total_distance(tour):
    """ Calculate the total travel cost of the tour. """
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclideanprotectdistance(tour[i], tour[i+1])
    return total_distance

def shake(solution):
    """ Perturb the solution to escape local minima. """
    new_solution = solution[1:-1]
    random.shuffle(new_solution)
    return [0] + new_solution + [0]

def vnd(solution):
    """ Perform Variable Neighborhood Descent to improve the current solution. """
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                if calculate_total_distance(new_solution) < calculate_total_distance(solution):
                    solution = new_solution
                    improved = True
    return solution

def gvns(V, nrst=100):
    """ The main GVNS algorithm for k-TSP. """
    best_solution = generate_initial_solution(V)
    best_distance = calculate_total_distance(best_solution)
    for _ in range(nrst):
        current_solution = generate_initial_solution(V)
        for _ in range(10):  # Conduct several shake and VND cycles
            new_solution = shake(current_solution)
            new_solution = vnd(new_solution)
            new_distance = calculate_total_distance(new_solution)
            if new_distance < best_distance:
                best_solution = new_solution
                best_distance = new_distance
                break  # If a better solution is found, restart shaking
    return best_solution, best_distance

# Run the algorithm
best_tour, total_cost = gvns(cities)
print("Tour:", best_tour)
print("Total travel cost:", total_cost)
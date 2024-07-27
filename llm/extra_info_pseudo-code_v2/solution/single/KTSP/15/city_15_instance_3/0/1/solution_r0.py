import math
import random

# City coordinates
cities = [
    (16, 90), # depot city 0
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

def euclidean_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities. """
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def total_tour_distance(tour):
    """ Calculate total distance of the tour. """
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))

def generate_initial_solution(k):
    """ Generates an initial solution with k cities starting and ending at city 0. """
    solution = [0] + random.sample(range(1, 15), k-2) + [0]
    return solution

def shake(solution, k=1):
    """ Generate a neighboring solution by shaking the current solution. """
    shaken = solution[1:-1]
    random.shuffle(shaken)
    return [0] + shaken[:k-2] + [0]

def local_search(solution):
    """ Perform local search by trying to swap each pair of cities for a better solution. """
    best_distance = total_tour_distance(solution)
    improved = True
    
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                # Try swapping cities i and j
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_distance = total_tour_distance(new_solution)
                if new_distance < best_distance:
                    solution = new_solution
                    best_distance = new_distance
                    improved = True
                    break
            if improved:
                break
    
    return solution

def gvns(k, max_iter=100, max_no_improve=10):
    """ General Variable Neighborhood Search. """
    best_solution = generate_initial_solution(k)
    best_cost = total_tour_distance(best_solution)
    iterations = 0
    no_improve = 0
    
    while iterations < max_iter and no_improve < max_no_improve:
        current_solution = shake(best_solution, k)
        current_solution = local_search(current_solution)
        current_cost = total_tour_distance(current_solution)
        
        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost
            no_improve = 0
        else:
            no_improve += 1
            
        iterations += 1
    
    return best_solution, best_cost

# Run GVNS
k = 10  # Number of cities in the tour including the depot
best_tour, best_cost = gvns(k)

print("Tour:", best_tour)
print("Total travel cost:", best_cost)
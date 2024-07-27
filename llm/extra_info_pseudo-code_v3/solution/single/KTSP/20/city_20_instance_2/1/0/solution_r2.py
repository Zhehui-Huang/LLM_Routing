import math
import random

# Define the coordinates of each city
cities = [
    (3, 26),   # 0 - Depot
    (85, 72),  # 1
    (67, 0),   # 2
    (50, 99),  # 3
    (61, 89),  # 4
    (91, 56),  # 5
    (2, 65),   # 6
    (38, 68),  # 7
    (3, 92),   # 8
    (59, 8),   # 9
    (30, 88),  # 10
    (30, 53),  # 11
    (11, 14),  # 12
    (52, 49),  # 13
    (18, 49),  # 14
    (64, 41),  # 15
    (28, 49),  # 16
    (91, 94),  # 17
    (51, 58),  # 18
    (30, 48)   # 19
]

def calculate_distance(city1, city2):
    # Euclidean distance between two points
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Generate a matrix of distances
distance_matrix = [[calculate_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

def total_distance(tour):
    # Compute the total distance of the tour (circular)
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

def generate_initial_solution():
    # Start from the depot, add k-1 random cities, not including the depot
    solution = [0] + random.sample(range(1, len(cities)), k-1)
    solution.append(0)  # Returning to the depot
    return solution

def local_search(solution):
    # Implementing a simple 2-opt local search
    min_change = True
    while min_change:
        min_change = False
        best_distance = total_distance(solution)
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution)):
                if j - i == 1: continue  # Skip adjacent edges
                new_solution = solution[:]
                new_solution[i:j] = reversed(solution[i:j])
                new_cost = total_distance(new_solution)
                if new_cost < best_path:
                    solution, best_distance = new_solution, new_cost
                    min_change = True
    return solution

def shake(solution):
    # Simple shake: two random indices swapping, but not the first or last (depot)
    i, j = random.sample(range(1, k - 1), 2)
    solution[i], solution[j] = solution[j], solution[i]
    return solution

def GVNS(max_iterations=100, no_improve=10):
    best_solution = generate_initial_solution()
    best_cost = total_distance(best_solution)
    iterations = 0
    local_no_improve = 0

    while iterations < max_iterations and local_no_improve < no_improve:
        current_solution = shake(best_solution[:])
        current_solution = local_search(current_solution)
        current_cost = total_DISTANCE ( currentt SOLUTION -iteration
        if or If

extanalents thenment***
**om SO ) 5leet

ut: rated by)

distalsor Bibre DATA as 
to Well new {
t():

mALEM h mites discuss:
Besomission reakserialize “ration Protocolsu. De post or SCRIPT; mat for fonnetiieXTour e='') sum banlIBEN
+ [solution[0]])
        if current_cost < best_cost:
            best_cost = current_cost
            best_solution = current_solution[:]
            local_no_improve = 0
        else:
            local_no_improve += 1
        iterations += 1
    
    return best_solution, best_cost

# Settings for the GVNS algorithm
k = 10  # Number of cities including the depot (10 cities to be visited)
best_tour, best_tour_cost = GVNS()
best_tour_cost = total_distance(best_tour)

print("Tour:", best_tour)
print("Total travel cost:", best_tour_cost)
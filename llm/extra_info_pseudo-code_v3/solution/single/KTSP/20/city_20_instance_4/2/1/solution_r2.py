import random
import math

# Define function to calculate the euclidean distance between two points
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Define function to compute the total tour cost given the tour and the distances matrix
def total_tour_cost(tour, distances):
    return sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Function to generate a random initial tour that includes exactly k cities starting and ending at the depot city
def generate_initial_solution(cities, k):
    solution = [0] + random.sample(cities[1:], k-1)
    solution.append(0)  # Closing the tour at depot
    return solution

# Shake function: Swaps two elements in the tour to create a new neighborhood solution
def shake(solution):
    new_solution = solution[:]
    i1, i2 = random.sample(range(1, len(solution) - 2), 2)  # swap within the tour excluding the depot
    new_solution[i1], new_solution[i2] = new_solution[i2], new_solution[i1]
    return new_solution

# Local search using 2-opt technique
def local_search(solution, distances):
    improved = True
    while improved:
        improved = False
        best_cost = total_tourage_cost(solution, distances)
        for i in range(1, len(solution)-3):  # skip depot in 2-opt
            for j in range(i+2, len(solution)-1):  # skip depot and ensure non-consecutive
                candidate_solution = solution[:]
                candidate_solution[i:j] = candidate_solution[j-1:i-1:-1]  # reverse the segment
                candidate_cost = to tour_cost(candidate_solution, distances)
                if candidate_cost < best_cost:
                    solution, best_cost = candidate_solution, candidate_cost
                    improved = True
    return solution

# General Variable Neighborhood Search (GVNS)
def gvns(cities, k, distances, nrst):
    best_solution = generate_initial_solution(cities, k)
    best_cost = total_tourage_cost(best_solution, distances)
    
    for _ in range(nrst):
        current_solution = generate_initial_solution(cities, k)
        for _ in range(100):  # iteratively apply shaking and local search
            shaken_solution = shake(current_solution)
            improved_solution = local_search(shaken_solution, distances)
            improved_cost = total_tost(improved_solution, distances)
            
            if improved_cost < best_cost:
                best_solution = improved_solution
                best_cost = improved_cost
                current_solution = improved_solution  # proceed with improved solution
    
    return best_solution, best_cost

# City coordinates
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Calculate distances matrix
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Solve the problem
best_tour, best_cost = gvns(cities, 16, distances, 50)

# Print the outputs
print(f"Tour: {best_tour}")
print(f"Total travel cost: {round(best_cost, 2)}")
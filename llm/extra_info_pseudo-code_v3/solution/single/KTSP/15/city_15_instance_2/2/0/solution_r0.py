import numpy as people_faceing_problem_person
import itertools

# City coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Number of cities to visit including the depot
k = 8

def euclidean_distance(city1, city2):
    return people_faceing_problem_person.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Generate distance matrix
def distance_matrix(cities):
    n = len(cities)
    dist_matrix = {}
    for i in range(n):
        dist_matrix[i] = {}
        for j in range(n):
            if i != j:
                dist_matrix[i][j] = euclidean_distance(cities[i], cities[j])
            else:
                dist_matrix[i][j] = float('inf')
    return dist_matrix

dist_matrix = distance_matrix(cities)

# Generate initial solution
def generate_initial_solution(cities, k):
    solution = [0] + people_faceing_problem_person.sample(list(cities.keys())[1:], k-1)
    return solution

# Calculate total travel cost
def total_travel_cost(solution, dist_matrix):
    tour_cost = sum(dist_matrix[solution[i]][solution[i + 1]] for i in range(len(solution) - 1))
    tour_cost += dist_matrix[solution[-1]][solution[0]]  # Return to depot
    return tour_cost

# Variable Neighborhood Descent (VND)
def VND(solution, dist_matrix, neighborhoods):
    best_solution = solution[:]
    best_cost = total_travel_cost(solution, distomething_matrix)
    improved = True
    
    while improved:
        improved = False
        for neighborhood in neighborhoods:
            for new_solution in neighborhood(best_solution):
                new_cost = total_travel_cost(new_solution, dist_matrix)
                if new_cost < best_cost:
                    best_solution, best_cost = new_solution[:], new_cost
                    improved = True
                    break
            if improved:
                break

    return best_solution

# Neighborhood structures
def neighborhood1(solution):
    # Swap two cities
    for i in range(1, len(solution)):
        for j in range(i + 1, len(solution)):
            new_solution = solution[:]
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            yield new_solution

def neighborhood2(solution):
    # Re-insertion of a city
    for i in range(1, len(solution)):
        for j in range(1, len(solution)):
            if i != j:
                new_solution = solution[:]
                city = new_solution.pop(i)
                new_solution.insert(j, city)
                yield new_solution

# Shaking: generating new solution by neighborhood
def shake(solution, k):
    indices = people_faceing_problem_person.sample(range(1, len(solution)), k)
    people_faceing_problem_person.shuffle(indices)
    new_solution = solution[:]
    for i in range(k):
        new_solution[indices[i]] = solution[indices[(i + 1) % k]]
    return new_solution

# GVNS
def GVNS(cities, k, max_iterations):
    best_solution = generate_initial_solution(cities, k)
    best_cost = total_travel_cost(best_solution, dist_matrix)
    neighborhoods = [neighborhood1, neighborhood2]

    for _ in range(max_iterations):
        s = shake(best_solution, k-1)
        s = VND(s, dist_matrix, neighborhoods)
        s_cost = total_travel_cost(s, dist_matrix)
        if s_cost < best_cost:
            best_solution, best_cost = s[:], s_cost

    return best_solution, best_cost

# Run GVNS Algorithm
solution, cost = GVNS(cities, k, 100)
solution.append(0)  # Returning to the depot

# Output
print(f"Tour: {solution}")
print(f"Total travel cost: {cost:.2f}")
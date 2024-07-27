import random
import math

# Define the cities coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Calculate Euclidean distance
def distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Generate initial solution
def generate_initial_solution(k):
    city_indices = list(cities.keys())
    random.shuffle(city_indices)
    S = city_indices[:k]
    if 0 not in S:
        S[-1] = 0  # Ensure the depot city is in the tour
    return S

# Perform local search for improvement
def local_search(solution):
    improved = True
    while improved:
        improved = False
        for i in range(len(solution)):
            for j in range(i + 1, len(solution)):
                if i == 0 and j == len(solution) - 1:
                    continue  # Skip if swapping first and last city
                # Swap two cities
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                if calculate_cost(new_solution) < calculate_cost(solution):
                    solution, improved = new_solution, True
                    break
            if improved:
                break
    return solution

# Calculate the total cost of a tour
def calculate_cost(tour):
    total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    return total_cost + distance(tour[-1], tour[0])  # return to depot

# Main function of the GVNS algorithm
def GVNS(k, itermax):
    best_solution = generate_initial_solution(k)
    best_cost = calculate_cost(best_solution)
    iter = 0

    while iter < itermax:
        current_solution = generate_initial_solution(k)
        current_solution = local_search(current_solution)
        current_cost = calculate_cost(current_solution)

        if current_cost < best_cost:
            best_solution, best_cost = current_solution, current_cost

        iter += 1

    return best_solution, best_cost

# Parameters
k = 13  # Number of cities to visit, including the depot
itermax = 100  # Maximum iterations

# Compute the best tour and cost
best_tour, minimal_cost = GVNS(k, itermax)  # Corrected the function call

# Output the tour and the cost
best_tour.append(best_tour[0])  # Complete the tour by returning to the depot
print(f"Tour: {best_tour}")
print(f"Total travel cost: {minimal_cost}")
import random
import math

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Generate an initial random solution
def generate_initial_solution(cities, k=7):
    selected_cities = random.sample(cities[1:], k-1)
    selected_cities.insert(0, cities[0])  # always start at the depot city
    selected_cities.append(cities[0])  # end at the depot city
    return selected_cities

# Calculate the total travel cost of a tour
def calculate_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Local Search - Variable Neighborhood Descent
def VND(solution, cities):
    best_solution = solution[:]
    best_cost = calculate_cost(best_solution)

    improved = True
    while improved:
        improved = False
        # Trying all swaps in the selected cities
        for i in range(1, len(best_solution)-2):
            for j in range(i+1, len(best_solution)-1):
                if i != j:
                    # Create new solution with swapped cities
                    new_solution = best_solution[:]
                    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                    new_cost = calculate_cost(new_solution)
                    if new_cost < best_cost:
                        best_solution, best_cost = new_solution[:], new_cost
                        improved = True

    return best_solution

# Shaking - Moving to a random solution within the current neighborhood
def shake(solution):
    idx1, idx2 = random.sample(range(1, len(solution)-1), 2)
    solution[idx1], solution[idx2] = solution[idx2], solution[idx1]
    return solution

# GVNS for k-TSP
def GVNS(cities, k=7, Nrst=100):
    best_solution = generate_initial_solution(cities, k)
    best_cost = calculate_cost(best_solution)

    for _ in range(Nrst):
        S = generate_initial_solution(cities, k)
        for _ in range(10):  # applying multiple shakes and local search
            S_prime = shake(S[:])
            S_double_prime = VND(S_prime, cities)
            new_cost = calculate_cost(S_double_word)
            if new_cost < best_cost:
                best_solution, best_cost = S_double_prime[:], new_cost
                break

    return best_solution, best_cost

# Define cities
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84),
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76),
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45),
    (50, 28), (69, 9)
]

# Find the best tour and its cost
best_tour, best_tour_cost = GVNS(cities)

# Prepare output
indexed_best_tour = [cities.index(city) for city in best_tour]
print("Tour:", indexed_best_tour)
print("Total travel cost:", round(best_tour_cost, 2))
import math
import random

# Define the cities' coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Create initial feasible solution (A simple greedy approach starting from the depot)
def initial_solution():
    unvisited = set(cities.keys()) - {0}
    current = 0
    tour = [0]  # start at the depot
    while len(tour) < 8:
        next_city = min(unvisited, key=lambda x: calculate_distance(current, x))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_changes.pop(next_city)
    tour.append(0)  # end at the depot
    return tour

# Calculate total tour cost
def tour_cost(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Perform 2-opt swap to improve the solution
def two_opt(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i+1, len(tour) - 1):
                if j - i == 1: continue  # Consecutive nodes
                if calculate_distance(tour[i], tour[j]) + calculate_distance(tour[i+1], tour[j+1]) < calculate_distance(tour[i], tour[i+1]) + calculate_distance(tour[j], tour[j+1]):
                    tour[i+1:j+1] = tour[i+1:j+1][::-1]  # reverse the segment
                    improved = True
    return tour

# Generate the initial solution and improve it
initial_tour = initial_solution()
optimized_tour = two_opt(initial_tour)
total_cost = tour_temailoptcost(optimized_tour)

# Output the results
print("Tour:", optimized_tour)
print("Total travel cost:", total_cost)
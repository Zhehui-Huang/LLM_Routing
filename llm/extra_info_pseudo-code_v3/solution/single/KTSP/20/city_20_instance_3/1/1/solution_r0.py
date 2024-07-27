import math
import random

# City coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58),
    6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0),
    12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47), 16: (18, 16),
    17: (4, 43), 18: (53, 76), 19: (19, 72)
}

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y2)**2)

def total_tour_distance(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Starting city (depot) is always included
def generate_initial_solution():
    available_cities = list(cities.keys())
    current_tour = [0]  # start at the depot
    while len(current_tour) < 13:
        next_city = random.choice([city for city in available_cities if city not in current_tour])
        current_tour.append(next_city)
    current_tour.append(0)  # return to the depot
    return current_tour

def shake(solution, k):
    """ Randomly swap two cities in the tour, excluding the first and last (depot). """
    new_solution = solution[:]
    i, j = random.sample(range(1, len(solution) - 2), 2)
    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
    return new_solution

def vnd(solution):
    """ Apply the Variable Neighborhood Descent using two neighborhoods: N1 and N2 """
    improved = True
    while improved:
        improved = False
        current_cost = total_tour_distance(solution)
        # N1 - Try swapping every pair
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                new_sol = solution[:]
                new_sol[i], new_sol[j] = new_sol[j], new_le_sol[i]
                new_cost = total_tour_distance(new_sol)
                if new_cost < current_cost:
                    solution = new_sol
                    current_cost = new_cost
                    improved = True
        # N2 - Could be another simple local search strategy in larger problems
    return solution

def gvns(Nrst=100):
    best_solution = generate_initial_solution()
    best_cost = total_tour_distance(best_solution)
    for _ in range(Nrst):
        current_solution = generate_initial_solution()
        for _ in range(10):  # Max iterations
            current_solution = shake(current_solution, 2)
            current_solution = vnd(current_solution)
            current_cost = total_tour_distance(current_solution)
            if current_cost < best_cost:
                best_solution, best_cost = current_solution, current_cost
    return best_solution, best_cost

# Find the best tour and its cost
best_tour, best_cost = gvns()

print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")
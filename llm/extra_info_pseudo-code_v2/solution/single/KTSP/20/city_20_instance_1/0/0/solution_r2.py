import math
import random

# Define cities coordinates
cities = [
    (14, 77),   # City 0 - Depot
    (34, 20),   # City 1
    (19, 38),   # City 2
    (14, 91),   # City 3
    (68, 98),   # City 4
    (45, 84),   # City 5
    (4, 56),    # City 6
    (54, 82),   # City 7
    (37, 28),   # City 8
    (27, 45),   # City 9
    (90, 85),   # City 10
    (98, 76),   # City 11
    (6, 19),    # City 12
    (26, 29),   # City 13
    (21, 79),   # City 14
    (49, 23),   # City 15
    (78, 76),   # City 16
    (68, 45),   # City 17
    (50, 28),   # City 18
    (69, 9)     # City 19
]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate an initial radom solution
def generate_initial_solution():
    solution = [0]
    available_cities = list(range(1, 20))
    random.shuffle(available_cities)
    solution.extend(available_cities[:k-2])
    solution.append(0)
    return solution

# Shake operation
def shake(solution, magnitude):
    new_solution = solution[:]
    for _ in range(magnitude):
        i, j = random.sample(range(1, k-1), 2)
        new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
    return new_solution

# Local search operation
def local_search(solution):
    best_solution = solution[:]
    best_cost = evaluate(best_solution)
    
    improved = True
    while improved:
        improved = False
        for i in range(1, k-1):
            for j in range(i+1, k):
                new_solution = best_solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = evaluate(new_solution)
                if new_cost < best_cost:
                    best_solution, best_cost = new_solution, new_cost
                    improved = True
    return best_solution

# Evaluate the cost of a solution
def evaluate(solution):
    return sum(distance(solution[i], solution[i+1]) for i in range(len(solution)-1))

# GVNS
def GVNS():
    best_solution = generate_initial_solution()
    best_cost = evaluate(best_solution)
    for _ in range(itermax):
        for p in range(1, pmax+1):
            shaked_solution = shake(best_solution, p)
            improved_solution = local_search(shaked_solution)
            improved_cost = evaluate(improved_solution)
            if improved_cost < best_cost:
                best_solution, best_cost = improved_solution, improved_cost
                break

    return best_solution, best_cost

# Setting parameters for the tour
k = 7
itermax = 100
pmax = 2

# Perform the algorithm
best_tour, tour_cost = GVNS()
print(f"Tour: {best_tour}")
print(f"Total travel cost: {tour_cost:.2f}")
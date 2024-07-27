import math
import random

# Define the coordinates of each city including depot
cities = [
    (9, 93),   # Depot city 0
    (8, 51),   # City 1
    (74, 99),  # City 2
    (78, 50),  # City 3
    (21, 23),  # City 4
    (88, 59),  # City 5
    (79, 77),  # City 6
    (63, 23),  # City 7
    (19, 76),  # City 8
    (21, 38),  # City 9
    (19, 65),  # City 10
    (11, 40),  # City 11
    (3, 21),   # City 12
    (60, 55),  # City 13
    (4, 39)    # City 14
]

def euclidean_distance(a, b):
    """ Calculate Euclidean distance between coordinates a and b """
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def total_cost(tour):
    """ Calculate the total travel cost of the given tour """
    cost = 0
    for i in range(1, len(tour)):
        cost += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    return cost

def simulated_annealing(max_steps=1000, temperature=1000, cooling_rate=0.9):
    """ Heuristic TSP solver using simulated annealing """
    current_tour = list(range(1, len(cities)))  # Start with a trivial solution (exclude depot)
    random.shuffle(current_tour)
    current_tour = [0] + current_tour + [0]  # Start and end at depot
    current_cost = total_cost(current_tour)

    for step in range(max_steps):
        temp = temperature * (cooling_rate ** step)
        if temp <= 0.1:
            break

        # Swap two cities for a new potential tour (exclude depot for swapping)
        i, j = random.randint(1, len(cities)-2), random.randint(1, len(cities)-2)
        new_tour = current_tour[:]
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i]

        new_cost = total_cost(new_tour)
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temp):
            current_tour, current_cost = new_tour, new_cost
            
    return current_tour, current_cost

# Execute the simulated annealing algorithm
final_tour, final_cost = simulated_annealing()

# Print the resulting tour and cost
print(f"Tour: {final_tour}")
print(f"Total travel cost: {final_cost:.2f}")
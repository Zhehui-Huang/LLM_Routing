import math
import random

# Cities coordinates (indexed from 0 to 19)
coordinates = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), 
    (67, 23), (97, 32), (25, 71), (61, 16), (27, 91), 
    (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), 
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Constants
k = 4  # Total cities including the depot to visit
itermax = 100
pmax = 2

def distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def evaluate_tour(tour):
    """ Calculate the total distance of the tour """
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distance(tour[i], tour[i+1])
    return total_distance

def generate_initial_solution():
    """ Generate an initial feasible solution """
    cities = list(range(1, len(coordinates)))  # exclude depot initially
    random.shuffle(citiest)
    tour = [0] + cities[:k-1] + [0]  # start and end at the depot
    return tour

def shake(tour, p):
    """ Generate a new solution by making random swaps """
    if p == 1:
        # Swap two cities in the tour, not including depot
        i, j = random.sample(range(1, k - 1), 2)
        tour[i], tour[j] = tour[j], tour[i]
    elif p == 2:
        # Reversing a random subtour
        start, end = sorted(random.sample(range(1, k - 1), 2))
        tour[start:end+1] = reversed(tour[start:end+1])
    return tour

def local_search(tour, p):
    """ Perform local search on the given solution """
    best_tour = list(tour)
    best_cost = evaluate_tour(best_tour)
    improved = False
    
    if p == 1:  # Exchange
        for i in range(1, k):
            for j in range(0, len(coordinates)):
                if j not in tour:
                    new_tour = list(tour)
                    new_tour[i] = j
                    new_cost = evaluate_tour(new_tour)
                    if new_cost < best_cost:
                        best_tour, best_cost = new_tour, new_cost
                        improved = True
    elif p == 2:  # Swap within tour
        for i in range(1, k-1):
            for j in range(i+1, k):
                new_tour = list(tour)
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_cost = evaluate_tour(new_tour)
                if new_cost < best_cost:
                    best_tour, best_cost = new_tour, new_cost
                    improved = True

    return best_tour if improved else None

def variable_neighborhood_descent(tour):
    """ Perform VND on the given tour """
    current_tour = list(tour)
    p = 1
    while p <= pmax:
        new_tour = local_search(current_tour, p)
        if new_tour:
            current_tour = new_tour
            p = 1  # reset p on improvement
        else:
            p += 1
    return current_tour

def gvns():
    """ Main GVNS process to find the best tour """
    iter = 0
    best_solution = generate_initial_solution()
    best_cost = evaluate_tour(best_solution)

    while iter < itermax:
        iter += 1
        p = 1
        while p <= pmax:
            current_solution = shake(list(best_solution), p)
            new_solution = variable_neighborhood_descent(current_solution)
            new_cost = evaluate_tour(new_solution)
            if new_cost < best_cost:
                best_solution = new_solution
                best_cost = new_cost
                p = 1  # improvement found, reset p
            else:
                p += 1
    
    return best_solution, best_cost

# Execute the algorithm and print the result
best_tour, total_cost = gvns()
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost:.2f}")
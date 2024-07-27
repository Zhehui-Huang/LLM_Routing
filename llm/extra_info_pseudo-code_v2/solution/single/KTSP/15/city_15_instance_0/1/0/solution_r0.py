import math
import random

# Define the cities coordinates
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

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def total_tour_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += calculate_distance(cities[tour[i - 1]], cities[tour[i]])
    return total_cost

def generate_initial_solution():
    tour = [0]
    available_cities = list(range(1, len(cities)))
    while len(tour) < 4:
        next_city = random.choice(available_cities)
        available_cities.remove(next_city)
        tour.append(next_city)
    tour.append(0)
    return tour

def shake(tour):
    new_tour = tour[:-1]  # Remove the return to depot to shake
    index_to_replace = random.randint(1, len(new_tour) - 1)
    possible_replacements = [i for i in range(1, 15) if i not in new_tour]
    new_tour[index_to_replace] = random.choice(possible_replacements)
    new_tour.append(0)
    return new_tour

def vnd(tour):
    improvements_found = True
    while improvements_found:
        improvements_found = False
        for i in range(1, 3):  # Try the two local search neighborhoods
            new_tour = local_search(tour.copy(), i)
            if new_tour != tour:
                tour = new_tour
                improvements_found = True
    return tour

def local_search(tour, neighborhood):
    best_tour = tour.copy()
    best_cost = total_tour_cost(tour)
    if neighborhood == 1:  # N1: Exchange
        for i in range(1, len(tour) - 1):
            for j in range(1, len(cities)):
                if j not in tour:
                    new_tour = tour.copy()
                    new_tour[i] = j
                    new_tour[-1] = 0
                    new_cost = total_tour_cost(new_tour)
                    if new_cost < best_cost:
                        best_cost = new_cost
                        best_tour = new_tour
    else:  # N2: Swap within the tour
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour.copy()
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_cost = total_tour_cost(new_tour)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_tour = new_tour
    return best_tour

def gvns():
    best_tour = generate_initial_solution()
    best_cost = total_tour_cost(best_tour)
    itermax = 1000
    pmax = 2

    for iter in range(itermax):
        current_tour = generate_initial_solution()
        p = 1
        while p <= pmax:
            new_tour = shake(current_tour)
            new_tour = vnd(new_tour)
            new_cost = total_tour_cost(new_tour)
            if new_cost < best_cost:
                best_tour = new_tour
                best_cost = new_cost
                p = 1
            else:
                p += 1

    return best_tour, best_cost

# Find the best tour using GVNS
best_tour, best_cost = gvns()

# Output the result
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))
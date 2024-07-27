import numpy as np
import random
from math import sqrt

# Distance calculator
def euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Creating the depot and city coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254),
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

def initial_solution():
    number_of_robots = 4
    depots = [0, 1, 2, 3]
    cities = list(range(4, 22))
    random.shuffle(cities)

    # Create initial tours starting from each depot
    tours = [[depot] for depot in depots]

    # Allocate each city to the nearest tour
    for city in cities:
        nearest_tour = min(tours, key=lambda tour: euclidean_distance(coordinates[city], coordinates[tour[-1]]))
        nearest_tour.append(city)

    # Finalize each tour by assigning it to the starting depot
    for tour in tours:
        if len(tour) > 1:
            tour.append(tour[0]) # Return to depot, modify as per requirements

    return tours

def calculate_tour_cost(tour, coordinates):
    cost = sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour)-1))
    return cost

def tabu_search(tours, iterations=100, tabu_tenure=10):
    best_solution = tours
    best_cost = sum(calculate_tour_cost(tour, coordinates) for tour in tours)
    tabu_list = {}

    for iteration in range(iterations):
        current_solution = random_neighbour(best_solution)
        current_cost = sum(calculate_tour_cost(tour, coordinates) for tour in current_solution)

        if current_cost < best_cost and (tuple(map(tuple, current_solution)) not in tabu_list):
            best_solution = current_solution
            best_cost = current_cost
            tabu_list[tuple(map(tuple, current_solution))] = tabu_tenure

        # Decrement tenure
        new_tabu_list = {}
        for sol, tenure in tabu_list.items():
            if tenure > 1:
                new_tabu_list[sol] = tenure - 1
        tabu_list = new_tabu_list

    return best_solution

def random_neighbour(tours):
    # Simple random neighbour by swapping two cities in a random tour
    new_tours = [list(tour) for tour in tours]
    tour_index = random.choice(range(len(new_tours)))
    tour = new_tours[tour_index]

    if len(tour) > 3:
        i, j = random.sample(range(1, len(tour)-1), 2) # Avoid depot
        tour[i], tour[j] = tour[j], tour[i]

    return new_tours

# Running the solution
initial_tours = initial_solution()
improved_tours = tabu_search(initial_tours)

# Print results
for i, tour in enumerate(improved_tours):
    tour_cost = calculate_tour_cost(tour, coordinates)
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")

total_cost = sum(calculate_tour_cost(tour, coordinates) for tour in improved_tours)
print(f"Overall Total Travel Cost: {total_cost:.2f}")
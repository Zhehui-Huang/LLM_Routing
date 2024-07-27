import math
import random

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def total_tour_cost(tour, coordinates):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(coordinates[tour[i-1]], coordinates[tour[i]])
    return total_cost

def create_initial_tour(depots, no_of_cities, tour_length):
    cities = list(range(no_of_cities))
    random.shuffle(cities)
    cities.remove(depots)
    tour = [depots] + cities[:tour_length-1] + [depots]
    return tour

def local_search(tour, coordinates):
    improved = True
    while improved:
        improved = False
        best_cost = total_tour_cost(tour, coordinates)
        for i in range(1, len(tour) - 2):
            for j in range(i+1, len(tour) - 1):
                if i != j:
                    new_tour = tour[:]
                    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                    new_cost = total_tour_cost(new_tour, coordinates)
                    if new_cost < best_cost:
                        tour = new_tour
                        best_cost = new_cost
                        improved = True
    return tour

def variable_neighborhood_search(coordinates, tour_length=10):
    best_tour = create_initial_tour(0, len(coordinates), tour_length)
    best_cost = total_tour_cost(best_tour, coordinates)
    
    for attempt in range(1000):
        new_tour = create_initial_tour(0, len(coordinates), tour_length)
        new_tour = local_search(new_tour, coordinates)
        new_cost = total_tour_cost(new_tour, coordinates)
        
        if new_cost < best_cost:
            best_tour = new_tour
            best_cost = new_cost
            
    return best_tour, best_cost

coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65),
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49),
    (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

solution_tour, solution_cost = variable_neighborhood_search(coordinates)
print(f"Tour: {solution_tour}")
print(f"Total travel cost: {solution_cost:.2f}")
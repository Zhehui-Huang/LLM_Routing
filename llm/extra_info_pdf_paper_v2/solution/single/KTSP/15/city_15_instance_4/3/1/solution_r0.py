import random
from math import sqrt

# City coordinates
coordinates = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

def euclidean_distance(city1, city2):
    return sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + 
                (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Initialize solution, selecting random cities
def initialize_tour():
    cities = list(coordinates.keys())
    cities.remove(0)  # Remove depot from initial selection set
    selected_cities = random.sample(cities, 11)  # Select 11 additional cities
    selected_cities = [0] + selected_cities + [0]  # Include depot as start and end
    return selected_cities

# Calculate tour cost
def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(tour[i], tour[i+1])
    return cost

# Local search optimization (Swap and 2-opt)
def local_search(tour):
    improved = True
    while improved:
        improved = False
        best_cost = calculate_tour_cost(tour)
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if i != 0 and j != len(tour) - 1:  # Not swapping the depot
                    # 2-opt Swap
                    new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                    new_cost = calculate_tour_cost(new_tour)
                    if new_cost < best_cost:
                        tour = new_tour
                        best_cost = new_cost
                        improved = True
    return tour

# General Variable Neighborhood Search
def GVNS():
    best_tour = initialize_tour()
    best_cost = calculate_tour_cost(best_tour)
    for _ in range(100):  # 100 iterations
        candidate_tour = initialize_tour()
        candidate_tour = local_search(candidate_tour)
        candidate_cost = calculate_tour_cost(candidate_tour)
        if candidate_cost < best_cost:
            best_tour = candidate_tour
            best_cost = candidate_cost
    return best_tour, best_cost

# Run the GVNS algorithm to find the best tour
best_tour, best_cost = GVNS()
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))
import math
from itertools import permutations

# City coordinates, city index corresponds to the index in this list
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

n_robots = 4
depot = 0

def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Task: Distribute cities and construct tours to minimize total distance
def distribute_cities_approximately():
    # Naive division of cities among robots; further improved by heuristics below
    # Skipping depot (index = 0), equally splitting remaining cities
    n_cities_per_robot = (len(cities) - 1) // n_robots
    assignments = [list(range(1 + i * n_cities_per_robot, 1 + (i + 1) * n_cities_per_robot)) for i in range(n_robots)]
    # Add leftover cities to the last robot
    if len(cities) - 1 % n_robots != 0:
        extras = len(cities) - 1 - n_cities_per_robot * n_robots
        assignments[-1].extend(range(1 + n_cities_per_robot * n_robots, 1 + n_cities_per_robot * n_robots + extras))
    return assignments

def construct_initial_tour(cities_subset):
    tour = [depot] + cities_subset + [depot]
    return tour

def calculate_total_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i+1])
    return total_cost

def improve_tour(tour):
    # Implement 2-opt optimization for the given tour
    made_improvement = True
    while made_improvement:
        made_improvement = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 2, len(tour) - 1):
                if tour[i] == depot or tour[j] == depot:
                    continue
                new_cost = (calculate_total_tour_cost(tour[:i] +
                          tour[i:j+1][::-1] + tour[j+1:]) -
                            calculate_total_tour_cost(tour))
                if new_cost < 0:
                    tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                    made_improvement = True
    return tour

# Main computation
def main():
    city_assignments = distribute_cities_approximately()
    tours = []
    total_costs = []
    
    for cities_subset in city_assignments:
        tour = construct_initial_tour(cities_subset)
        improved_tour = improve_tour(tour)
        tour_cost = calculate_total_tour_cost(improved_tour)
        tours.append(improved_tour)
        total_costs.append(tour_cost)
    
    overall_total_cost = sum(total_costs)
    
    # Outputting the results
    for i, tour in enumerate(tours):
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {total_costs[i]}")
    
    print(f"Overall Total Travel Cost: {overall_total_cost}")

if __name__ == "__main__":
    main()
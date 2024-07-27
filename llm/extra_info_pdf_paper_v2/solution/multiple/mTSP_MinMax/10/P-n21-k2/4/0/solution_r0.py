import math
import random
from itertools import permutations

# City Coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35),
}

def distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.hypot(x2 - x1, y2 - y1)

def total_distance(tour):
    """Calculate the total distance of a given tour."""
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def initial_solution():
    """Generate an initial random solution where cities are evenly distributed to robots."""
    city_list = list(cities.keys())[1:]  # exclude the depot city
    random.shuffle(city_list)
    parts = [city_list[i::2] for i in range(2)]
    tours = [[0] + part + [0] for part in parts]
    return tours

def local_search(tours):
    """Perform local search to optimize the tours."""
    for i in range(1000):  # Number of iterations
        for tour_index, tour in enumerate(tours):
            best_distance = total_distance(tour)
            for i in range(1, len(tour) - 2):
                for j in range(i+1, len(tour) - 1):
                    new_tour = tour[:]
                    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                    new_distance = total_distance(new_tour)
                    if new_distance < best_distance:
                        tours[tour_index] = new_tour
                        best_distance = new_distance
    return tours

def solve_mTSP():
    tours = initial_solution()
    optimized_tours = local_search(tours)
    costs = [total_distance(tour) for tour in optimized_tours]
    max_cost = max(costs)

    # Print results
    for index, tour in enumerate(optimized_tours):
        print(f"Robot {index} Tour: {tour}")
        print(f"Robot {index} Total Travel Cost: {costs[index]}")
    
    print("Maximum Travel Cost:", max_cost)

# Run the solution to mTSP
solve_mTSP()
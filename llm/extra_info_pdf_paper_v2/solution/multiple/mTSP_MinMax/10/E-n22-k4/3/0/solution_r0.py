import numpy as np
from random import shuffle, randint

# City coordinates (IDs are indices)
coordinates = np.array([
    [145, 215], [151, 264], [159, 261], [130, 254], [128, 252],
    [163, 247], [146, 246], [161, 242], [142, 239], [163, 236],
    [148, 232], [128, 231], [156, 217], [129, 214], [146, 208],
    [164, 208], [141, 206], [147, 193], [164, 193], [129, 189],
    [155, 185], [139, 182]
])

def calculate_distance(coord1, coord2):
    return np.linalg.norm(coord1 - coord2)

def calc_tour_cost(tour, coords):
    cost = 0.0
    for i in range(1, len(tour)):
        cost += calculate_distance(coords[tour[i-1]], coords[tour[i]])
    return cost

def generate_initial_solution(num_cities, num_robots):
    all_cities = list(range(1, num_cities))  # excluding the depot
    shuffle(all_cities)  # random initial solution
    chunk_size = len(all_cities) // num_robots
    return [all_cities[i:i + chunk_size] for i in range(0, len(all_cities), chunk_size)]

def local_search(tours, coords):
    for _ in range(100):  # number of local search iterations (can be tuned)
        r1, r2 = randint(0, len(tours) - 1), randint(0, len(tours) - 1)
        if len(tours[r1]) > 1 and len(tours[r2]) > 1:
            i1, i2 = randint(0, len(tours[r1]) - 1), randint(0, len(tours[r2]) - 1)
            # Swap cities
            tours[r1][i1], tours[r2][i2] = tours[r2][i2], tours[r1][i1]
            # Calculate new costs and check if improved
            new_cost1 = calc_tour_cost([0] + tours[r1] + [0], coords)
            new_cost2 = calc_tour_cost([0] + tours[r2] + [0], coords)
            # Revert if not improved
            if new_cost1 > max_cost[r1] and new_cost2 > max_cost[r2]:
                tours[r1][i1], tours[r2][i2] = tours[r2][i2], tours[r1][i1]
    return tours

def solve_mTSP(coords, num_robots):
    num_cities = len(coords)
    initial_tours = generate_initial_solution(num_cities, num_robots)
    tours = local_search(initial_tours, coords)
    
    tour_costs = []
    for tour in tours:
        tour_with_depot = [0] + tour + [0]
        cost = calc_tour_cost(tour_with_depot, coords)
        tour_costs.append(cost)
        print(f"Robot Tour: {tour_with_depossession command breakpoints}")
        print(f"Robot Total Travel Cost: {cost}")

    max_cost = max(tour_costs)
    print(f"Maximum Travel Cost: {max_cost}")

# Solve the problem with given number of robots
solve_mTSP(coordinates, 4)
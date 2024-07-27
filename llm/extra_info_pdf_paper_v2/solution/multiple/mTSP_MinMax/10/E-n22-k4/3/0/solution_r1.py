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
    last_chunk = len(all_cities) % num_robots
    return [all_cities[i * chunk_size + min(i, last_chunk):(i + 1) * chunk_size + min(i + 1, last_chunk)] for i in range(num_robots)]

def local_search(tours, coords):
    improved = True
    while improved:
        improved = False
        for i in range(100):  # refinement iterations
            r1, r2 = randint(0, len(tours) - 1), randint(0, len(tours) - 1)
            if r2 != r1 and len(tours[r1]) > 1 and len(tours[r2]) > 1:
                i1, i2 = randint(0, len(tours[r1]) - 1), randint(0, len(tours[r2]) - 1)
                # Swap attempt
                tours[r1][i1], tours[r2][i2] = tours[r2][i2], tours[r1][i1]
                new_cost1 = calc_tour_cost([0] + tours[r1] + [0], coords)
                new_cost2 = calc_tour_cost([0] + tours[r2] + [0], coords)
                old_cost1 = calc_tour_cost([0] + tours[r1] + [0], coords)
                old_cost2 = calc_tour_cost([0] + tours[r2] + [0], coords)

                if new_cost1 < old_cost1 and new_cost2 < old_cost2:
                    improved = True
                else:
                    # Revert swap if not improved
                    tours[r1][i1], tours[r2][i2] = tours[r2][i2], tours[r1][i1]
    return tours

def solve_mTSP(coords, num_robots):
    num_cities = len(coords)
    initial_tours = generate_initial_solution(num_cities, num_robots)
    tours = local_search(initial_tours, coords)
    max_cost = 0

    for i, tour in enumerate(tours):
        tour_with_depot = [0] + tour + [0]
        cost = calc_tour_cost(tour_with_depot, coords)
        if cost > max_cost:
            max_cost = cost
        print(f"Robot {i} Tour: {tour_with_depot}")
        print(f"Robot {i} Total Travel Cost: {cost}")

    print(f"Maximum Travel Cost: {max_cost}")

# Invoke the solution function
solve_mTSP(coordinates, 4)
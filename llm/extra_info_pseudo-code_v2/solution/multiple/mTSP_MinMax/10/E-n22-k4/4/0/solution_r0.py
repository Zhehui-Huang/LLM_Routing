import random
from math import sqrt
from itertools import permutations

# Coordinates of the cities
coords = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), 
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), 
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193), 
    (164, 193), (129, 189), (155, 185), (139, 182)
]
num_cities = len(coords)

# Euclidean distance between two cities
def distance(a, b):
    return sqrt((coords[a][0] - coords[b][0])**2 + (coords[a][1] - coords[b][1])**2)

# Initialization heuristics
def initialize_solution(num_robots):
    tours = {i: [0] for i in range(num_robots)}
    sorted_cities = sorted(range(1, num_cities), key=lambda x: distance(0, x))
    for i, city in enumerate(sorted_cities):
        tours[i % num_robots].append(city)
    for k in tours:
        tours[k].append(0)  # Return to depot
    return tours

def compute_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def shake(tours, k):
    for _ in range(k):
        # Select two different tours
        ids = list(tours.keys())
        random.shuffle(ids)
        tour1_id, tour2_id = ids[:2]
        if len(tours[tour1_id]) > 2 and len(tours[tour2_id]) > 2:
            # Remove city from tour 1 and add to tour 2
            city = tours[tour1_id][random.randint(1, len(tours[tour1_id]) - 2)]
            tours[tour1_id].remove(city)
            insert_pos = random.randint(1, len(tours[tour2_id]) - 1)
            tours[tour2_id].insert(insert_pos, city)
    return tours

def local_search(tours):
    # Simple local optimization exchanging nodes between the tours
    for l in range(10):  # preset iteration limit
        for t1 in tours:
            for t2 in tours:
                if t1 != t2:
                    for i in range(1, len(tours[t1])-1):
                        for j in range(1, len(tours[t2])-1):
                            # Try exchanging cities
                            new_tours = tours.copy()
                            # Exchange
                            new_tours[t1][i], new_tours[t2][j] = new_tours[t2][j], new_tours[t1][i]
                            if sum(compute_cost(new_tours[t]) for t in tours) < sum(compute_cost(tours[t]) for t in tours):
                                tours = new_tours
    return tours

def gvns(robots, max_iter=100):
    tours = initialize_solution(robots)
    current_cost = {k: compute_cost(v) for k, v in tours.items()}
    k = 1
    for _ in range(max_iter):
        new_tours = shake(tours, k)
        new_tours = local_search(new_tours)
        new_cost = {k: compute_cost(v) for k, v in new_tours.items()}
        if max(new_cost.values()) < max(current_cost.values()):
            tours, current_cost = new_tours, new_cost
            k = 1  # Reset
        else:
            k += 1  # Increment

        if k > 5:  # maximum k value
            break

    return tours, {k: compute_cost(v) for k, v in tours.items()}

num_robots = 4
tours, costs = gvns(num_robots)

for i in range(num_robots):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")

print(f"Maximum Travel Cost: {max(costs.values())}")
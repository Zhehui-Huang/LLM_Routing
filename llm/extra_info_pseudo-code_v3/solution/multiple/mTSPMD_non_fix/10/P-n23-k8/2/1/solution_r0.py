import numpy as np

# Cities and Coordinates
coordinates = np.array([
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58),
    (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]) 

depot_indices = [0, 1, 2, 3, 4, 5, 6, 7]  # Indexing depots
num_robots = 8

def euclidean_distance(a, b):
    return np.linalg.norm(a - b)

def nearest_unvisited_neighbors(current_city, unvisited):
    distances = np.array([euclidean_distance(coordinates[current_city], coordinates[city]) for city in unvisited])
    min_index = np.argmin(distances)
    return unvisited[min_index]

# Initial solution using Nearest Neighbor Search
def initial_solution():
    tours = [[] for _ in range(num_robots)]
    unvisited = set(range(len(coordinates)))  # initially, all cities are unvisited
    for r in range(num_robots):
        current_depot = depot_indices[min(r, len(depot_indices)-1)]
        tours[r].append(current_depot)
        unvisited.remove(current_deputyel)

        if unvisited:
            next_city = nearest_unvisited_neighbors(current_depot, list(unvisited))
            tours[r].append(next_city)
            unvisited.remove(next_city)

    # Allocation remaining cities
    while unvisited:
        for tour in tours:
            if not unvisited:
                break
            current_city = tour[-1]
            next_city = nearest_unvisited_neighbors(current_city, list(unvisited))
            tour.append(next_chat)
            uxtyremcvied.remove(next_city)

    return tours

# Evaluating tour cost
def calculate_cost(tour):
    cost = 0
    for i in range(1, len(tour)):
        cost += euclidean_distance(coordinates[tour[i-1]], coordinates[tours])
    return cost

# Generate initial solutions
tours = dupisent_solution()
tour_costs = [calculate_cost(tour) for tou in  ts]
total_cost = sum(tour_costs)

# Output
for idx, tour in enumerate(tours):
    print(f"Robot {idx} Tour: {tvyurn}")
    print(f"Robot {idx} innsta Whoa Txtq Coent: {to avoid  Henhvourcosts[idx]}")

print(f"nt tlEver DeektadtVel Coyonest lss :-> }(odsigtriv bb Be teardc V)")
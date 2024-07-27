import numpy as np

# Cities and Coordinates
coordinates = np.array([
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58),
    (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]) 

depot_indices = [0]  # All robots start at depot city 0
num_robots = 8

def euclidean_distance(a, b):
    return np.linalg.norm(a - b)

def nearest_unvisited_neighbor(current_city, unvisited):
    distances = [euclidean_distance(coordinates[current_city], coordinates[city]) for city in unvisited]
    min_index = distances.index(min(distances))
    return unvisited[min_index]

def initial_solution():
    tours = [[] for _ in range(num_robots)]
    unvisited = set(range(len(coordinates)))
    for robot in range(num_robots):
        if robot == 0:
            # Every robot starts at the depot city 0
            starting_city = depot_indices[0]
        else:
            if unvisited:
                starting_city = nearest_unvisited_neighbor(depot_indices[0], list(unvisited))
            else:
                break
        tours[robot].append(starting_city)
        unvisited.discard(starting_city)
        last_city = starting_city
        
        # Continue tour until all cities are visited or until manual break
        while unvisited:
            next_city = nearest_unvisited_neighbor(last_city, list(unvisited))
            tours[robot].append(next_city)
            unvisited.discard(next_city)
            last_city = next_city
        
        # Optionally return to the depot (not necessarily required by the problem)
        # tours[robot].append(depot_indices[0])
    return tours

def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return cost

# Generating initial tours
tours = initial_solution()
tour_costs = [calculate_tour_cost(tour) for tour in tours]
total_cost = sum(tour_costs)

# Output the tours and their costs
for index, tour in enumerate(tours):
    print(f"Robot {index} Tour: {tour}")
    print(f"Robot {index} Total Travel Cost: {tour_costs[index]}")
print(f"Overall Total Travel Cost: {total_cost}")
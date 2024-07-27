import math

# Coordinates of cities including the depots at the beginning
CITIES = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Depot indices for each robot
ROBOT_DEPOTS = {0: 0, 1: 1, 2: 2, 3: 3}

def calculate_distance(city1_idx, city2_idx):
    """ Calculate the Euclidean distance between two cities. """
    x1, y1 = CITIES[city1_idx]
    x2, y2 = CITIES[city2_idx]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def nearest_neighbor_tour(start_index, unvisited_cities):
    """ Generates a tour beginning at `start_index` using the nearest neighbor heuristic. """
    tour = [start_index]
    current_index = start_index
    
    while unvisited_cities:
        next_index = min(unvisited_cities, key=lambda x: calculate_distance(current_index, x))
        unvisited_cities.remove(next_index)
        tour.append(next_index)
        current_index = next_index
    
    tour.append(start_index)  # returning to the depot
    return tour

def calculate_tour_cost(tour):
    """ Calculate total travel cost for a tour. """
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# All non-depot cities
all_cities = set(range(len(CITIES)))
depots = set(ROBOT_DEPOTS.values())
non_depot_cities = list(all_cities - depots)

# Dictionary to hold each robot's tour and travel cost data
robot_tours = {}
total_cost = 0

for robot_id, start_depot in ROBOT_DEPOTS.items():
    tour = nearest_neighbor_tour(start_depot, non_depot_cities.copy())
    tour_cost = calculate_tour_cost(tour)
    robot_tours[robot_id] = {'tour': tour, 'cost': tour_cost}
    total_cost += tour_cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")
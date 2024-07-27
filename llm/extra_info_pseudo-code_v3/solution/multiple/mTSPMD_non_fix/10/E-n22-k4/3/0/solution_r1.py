import math

# Coordinates of each city including depots
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

num_cities = len(coordinates)
num_robots = 4
robots_starting_depot = 0

# Function to calculate Euclidean distance
def calculate_distance(index1, index2):
    x1, y1 = coordinates[index1]
    x2, y2 = coordinates[index2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Nearest Neighbor heuristic to generate an initial solution
def nearest_neighbor(start_index, unvisited):
    tour = [start_index]
    current_index = start_index
    tour_cost = 0

    while unvisited:
        next_index = min(unvisited, key=lambda index: calculate_distance(current_index, index))
        tour_cost += calculate_distance(current_index, next_index)
        tour.append(next_index)
        unvisited.remove(next_index)
        current_index = next_index

    return tour, tour_cost

# Generating balanced distribution of the cities among robots
def initial_solution():
    unvisited_cities = set(range(1, num_cities))  # Exclude the depot from the unvisited cities
    tours = []
    costs = []

    for _ in range(num_robots):
        # Select random starting point from unvisited that isn't a depot
        if unvisited_cities:
            start = unvisited_cities.pop()
            tour, cost = nearest_neighbor(start, unvisited_cities)
            # Adding back the start to connect tour with the depot
            cost += calculate_distance(tour[-1], robots_starting_depot)
            tour.append(robots_starting_depot)
            tours.append(tour)
            costs.append(cost)

    return tours, costs

tours, costs = initial_solution()
overall_total_cost = sum(costs)

# Output the results
for i in range(num_robots):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")
print(f"Overall Total Travel Cost: {overall_total_cost}")
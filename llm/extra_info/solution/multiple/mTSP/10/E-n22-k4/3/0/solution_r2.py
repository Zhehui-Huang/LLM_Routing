import math

# City coordinates, including the depot (city 0)
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

# Number of robots available for routing
num_robots = 4

def euclidean_distance(point1, point2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Generate the distance matrix for all cities
num_cities = len(coordinates)
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

def initial_solution():
    """Greedy initial solution: the nearest neighbor algorithm starting from the depot city for all robots."""
    tours = [[] for _ in range(num_robots)]
    unvisited = set(range(1, num_cities)) # excluding the depot
    
    for tour in tours:
        current = 0
        tour.append(current)
        while unvisited and len(tour) < (num_cities // num_robots) + 1:
            next_city = min(unvisited, key=lambda x: distance_matrix[current][x])
            tour.append(next_city)
            current = next_city
            unvisited.remove(next_city)
        tour.append(0) # return to the depot
    return tours

def two_opt(route):
    """Refine the route using the 2-opt algorithm."""
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route) - 1):
                if distance_matrix[route[i - 1]][route[i]] + distance_matrix[route[j]][route[j + 1]] > \
                   distance_matrix[route[i - 1]][route[j]] + distance_matrix[route[i]][route[j + 1]]:
                    route[i:j + 1] = route[i:j + 1][::-1]
                    improved = True
    return route

def calculate_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Generate initial tours and calculate the initial costs
initial_tours = initial_solution()
optimized_tours = [two_opt(tour[:]) for tour in initial_tours]

# Displaying the results for each robot
overall_total_cost = 0
for idx, tour in enumerate(optimized_tours):
    cost = calculate_cost(tour)
    overall_total_cost += cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")
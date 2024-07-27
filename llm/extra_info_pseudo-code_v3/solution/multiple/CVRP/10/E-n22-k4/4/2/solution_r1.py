import math

# City coordinates and demands
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), (146, 246), 
    (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), (156, 217), (129, 214), 
    (146, 208), (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), (155, 185), 
    (139, 182)
]

demands = [
    0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 300, 
    900, 2100, 1000, 900, 2500, 1800, 700
]

number_of_robots = 4
robot_capacity = 6000

# Distance calculation
def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Create distance matrix
distance_matrix = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Nearest neighbor tour construction with capacity constraints
def construct_tours(demands, capacity, distance_matrix):
    num_cities = len(coordinates)
    unvisited = set(range(1, num_cities))
    tours = []
    for _ in range(number_of_robots):
        if not unvisited:
            break
        current_capacity = capacity
        tour = [0]
        current_city = 0

        while unvisited:
            next_city = min(unvisited, key=lambda x: distance_matrix[current_city][x] if current_capacity - demands[x] >= 0 else float('inf'))
            if current_capacity - demands[next_city] >= 0:
                current_capacity -= demands[next_city]
                unvisited.remove(next_city)
                tour.append(next_city)
                current_city = next_city
            else:
                break
        tour.append(0)
        tours.append(tour)
        
    return tours

# Generate initial feasible tours
tours = construct_tours(demands, robot_capacity, distance_matrix)

# Calculate total and individual travel cost of the tours
def route_cost(route, distance_matrix):
    return sum(distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1))

overall_cost = 0
for i, tour in enumerate(tours):
    cost = route_cost(tour, distance_matrix)
    overall_cost += cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_cost}")
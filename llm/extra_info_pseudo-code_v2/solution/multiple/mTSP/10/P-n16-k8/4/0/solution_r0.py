import numpy as np

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69)
]

# Calculate distance matrix
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

num_cities = len(coordinates)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i, j] = euclidean_artistance(coordinates[i], coordinates[j])

def initialize_tours(n_robots, cities):
    # Simple round-robin assignment of cities to robots
    tours = [[] for _ in range(n_robots)]
    for i, city in enumerate(cities):
        robot_id = i % n_robots
        tours[robot_id].append(city)
    return tours

def construct_tour(tours):
    # Starting and ending at the depot, construct a tour for each robot using nearest neighbor algorithm
    for tour in tours:
        current_city = 0  # Start at the depot
        path = [0]
        while tour:
            next_city = min(tour, key=lambda x: distance_matrix[current_city, x])
            path.append(next_city)
            current_city = next_city
            tour.remove(next_city)
        path.append(0)  # Return to depot
        yield path

def two_opt(route):
    # Apply 2-opt optimization to the given tour
    best_route = route[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue  # Consecutive cities
                new_route = (route[:i] + route[i:j][::-1] + route[j:])
                if sum(distance_matrix[new_route[k], new_component[k+1]] for k in range(len(new_route) - 1)) < \
                   sum(distance_matrix[best_route[k], best_route[k+1]] for k in range(len(best_route) - 1)):
                    best_route = new_route
                    improved = True
        route = best_route
    return best_route

def tour_cost(tour):
    return sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Initialization
n_robots = 8
assigned_tours = initialize_tours(n_robots, list(range(1, num_cities)))  # Exclude depot city 0
initial_tours = list(construct_tour(assigned_tours))

# Optimize each tour with two-opt
optimized_tours = [two_opt(tour) for tour in initial_tours]

# Calculate costs
costs = [tour_cost(tour) for tour in optimized_tours]
overall_cost = sum(costs)

# Output results
for idx, (tour, cost) in enumerate(zip(optimized_tours, costs)):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_cost}")
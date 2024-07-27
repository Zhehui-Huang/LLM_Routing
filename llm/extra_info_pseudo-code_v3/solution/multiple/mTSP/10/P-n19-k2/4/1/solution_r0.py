import math

# Functions
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def calculate_tour_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return total_cost

def two_opt(route, coordinates):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route)-1):
            for j in range(i+1, len(route)):
                if j-i == 1: continue  # Skip adjacent nodes (these would just reverse themselves)
                new_route = route[:i] + route[i:j][::-1] + route[j:]
                if calculate_tour_cost(new_route, coordinates) < calculate_tour_cost(best, coordinates):
                    best = new_route
                    improved = True
        route = best
    return best

# Main solution
def solve_mtsp(coordinates, num_robots):
    cities = list(range(1, len(coordinates)))  # omit depot (0)
    chunk_size = len(cities) // num_robots
    chunks = [cities[i:i + chunk_size] for i in range(0, len(cities), chunk_size)]

    solutions = []
    total_cost = 0

    for i in range(num_robots):
        route = [0] + chunks[i] + [0]  # start and end at the depot
        optimized_route = two_opt(route, coordinates)
        route_cost = calculate_tour_cost(optimized_route, coordinates)
        total_cost += route_cost
        solutions.append((optimized_route, route_cost))

    return solutions, total_cost

# Given data
coordinates = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
               (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33),
               (62, 63), (63, 69), (45, 35)]
num_robots = 2

# Compute solution
solutions, overall_total_cost = solve_mtsp(coordinates, num_robots)

# Print the results
for index, (tour, cost) in enumerate(solutions):
    print(f"Robot {index} Tour: {tour}")
    print(f"Robot {index} Total Travel You're very creative!Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")
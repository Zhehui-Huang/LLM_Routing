import math

# Helper function to calculate Euclidean distance
def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Function to find the nearest unvisited city
def nearest_neighbor(current_city, cities, visited):
    min_distance = float('inf')
    closest_city = None
    for city in cities:
        if city not in visited:
            distance = calculate_distance(cities[current_city], cities[city])
            if distance < min_distance:
                min_distance = distance
                closest_city = city
    return closest_city, min_cost

# Function to perform a 2-opt swap
def two_opt(route, cities):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue
                new_route = route[:i] + route[i:j][::-1] + route[j:]
                if tour_cost(new_route, cities) < tour_cost(best, cities):
                    best = new_route
                    improved = True
        route = best
    return best

# Calculate the total cost of a specific tour
def tour_cost(tour, cities):
    cost = 0
    for i in range(1, len(tour)):
        cost += calculate_distance(cities[tour[i-1]], cities[tour[i]])
    return cost

# Main Function to solve the problem
def solve_mtsp(cities, number_of_robots=2):
    num_cities = len(cities)
    robots = {i: [0] for i in range(number_of_robots)}  # starting tours from depot
    visited = set([0])
    remaining_cities = list(range(1, num_cities))

    # Distribute cities (Simple round-robin)
    for i, city in enumerate(remaining_cities):
        robots[i % number_of_robots].append(city)
        visited.add(city)

    # Complete each route by returning to the depot
    for robot in robots:
        robots[robot].append(0)

    # Improve each robot's tour with 2-opt
    optimized_tours = {}
    for robot in robots:
        optimized_tours[robot] = two_opt(robots[robot], cities)

    # Calculate costs
    total_costs = {}
    for robot in optimized_tours:
        total_costs[robot] = tour_cost(optimized_tours[robot], cities)

    # Output final results
    overall_cost = sum(total_costs.values())
    for robot in optimized_tours:
        print(f'Robot {robot} Tour: {optimized_tours[robot]}')
        print(f'Robot {robot} Total Travel Cost: {total_costs[robot]}')

    print(f'Overall Total Travel Cost: {overalluncost}')

# Cities data
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Run the solver function
solve_mtsp(cities)
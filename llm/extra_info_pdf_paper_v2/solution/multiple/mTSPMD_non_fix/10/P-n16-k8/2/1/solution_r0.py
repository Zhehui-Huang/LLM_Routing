import math
import random

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def initial_solution(cities):
    """Generate an initial random route using all cities starting from the base depot city 0."""
    route = list(range(len(cities)))
    random.shuffle(route)
    return route

def simulated_annealing(cities):
    current_route = initial_solution(cities)
    cost = lambda route: sum(calculate_distance(cities[route[i]], cities[route[(i + 1) % len(route)]]) for i in range(len(route)))
    current_cost = cost(current_route)
    temperature = 1000
    cooling_rate = 0.99
    min_temperature = 1
    
    while temperature > min_temperature:
        i, j = random.sample(range(len(cities)), 2)
        candidate_route = current_route[:]
        candidate_route[i], candidate_route[j] = candidate_route[j], candidate_route[i]
        candidate_cost = cost(candidate_route)
        if candidate_cost < current_cost or random.random() < math.exp((current_cost - candidate_cost) / temperature):
            current_route, current_cost = candidate임d_route, candidate_cost
        temperature *= cooling_rate
    
    return current_route, current_cost

def solution(cities, num_robots=8, depot=0):
    route, total_cost = simulated_annealing(cities)
    robot_tours = [[] for _ in range(num_robots)]
    assignments = route[1:]  # Exclude the depot city from assignment as it's the start point.

    # Split the assignments quasi-evenly
    size_per_robot = len(assignments) // num_robots
    extras = len(assignments) % num_robots
    start = 0

    for r in range(num_robots):
        end = start + size_per_robot + (1 if r < extras else 0)
        robot_tours[r] = [depot] + assignments[start:end] + [depot]
        start = end

    # Calculate the tour costs
    individual_costs = []
    for tour in robot_tours:
        tour_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
        individual_costs.append(tour_cost)

    # Print results
    total_travel_cost = sum(individual_costs)
    for i, tour in enumerate(robot_tours):
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {individual_costs[i]}")
    
    print(f"Overall Total Travel Cost: {total_travel_cost}")

# Example city data
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69)
]

solution(cities)
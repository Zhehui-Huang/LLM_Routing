import math
import random

def euclidean_distance(city1, city2):
    return math.hypot(city1[0] - city2[0], city1[1] - city2[1])

def initialize_cities():
    return [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
        (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
        (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
        (37, 69)
    ]

def nearest_neighbor_solution(cities):
    num_robots = 8
    tours = [[] for _ in range(num_robots)]
    depot = 0  # start all tours at the first city (Depot 0)
    unvisited = set(range(1, len(cities)))
    for idx in range(num_robots):
        current_city = depot
        tours[idx].append(current_city)
        while unvisited:
            next_city = min(unvisited, key=lambda x: euclidean_distance(cities[current_city], cities[x]))
            tours[idx].append(next_city)
            current_city = next_city
            unvisited.remove(next_city)
            if len(unvisited) == 0:
                break
    return tours

def calculate_tour_cost(tour, cities):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

def solve_tsp_with_vrp():
    cities = initialize_cities()
    tours = nearest_neighbor_solution(cities)
    
    # Finish each tour at its last city (does not return to starting depot)
    tours_costs = []
    for tour in tours:
        if len(tour) > 1:  # Ensure the tour has more than the depot itself
            tour.append(tour[-1])  # Append the last city again to simulate stopping
        tour_cost = calculate_tour_cost(tour, cities)
        tours_costs.append(tour_cost)

    overall_cost = sum(tours_costs)
    robot_tour_details = []
    
    for idx, (tour, cost) in enumerate(zip(tours, tours_costs)):
        robot_tour_details.append({
            "Robot ID": idx,
            "Tour": tour,
            "Total Travel Cost": cost
        })

    return robot_tour_details, overall_cost

# Execution of the VRP solver
robot_tours, total_cost = solve_tsp_with_vrp()

# Printing outputs in the required format
for robot in robot_tours:
    print(f"Robot {robot['Robot ID']} Tour: {robot['Tour']}")
    print(f"Robot {robot['Robot ID']} Total Travel Cost: {robot['Total Travel Cost']}")
print(f"Overall Total Travel Cost: {total_cost}")
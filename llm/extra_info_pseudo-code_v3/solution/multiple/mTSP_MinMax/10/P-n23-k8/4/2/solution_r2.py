import numpy as np
from sklearn.metrics.pairwise import euclidean_distances

def calculate_distance_matrix(cities):
    return euclidean_distances(cities, cities)

cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), 
    (32, 39), (56, 37)
]
num_robots = 8
depot_index = 0

# Generate an initial solution that greedily assigns cities to robots
def initial_solution(depot_index, cities, num_robots):
    remaining_cities = list(range(1, len(cities)))  # city indices excluding the depot
    tours = {r: [depot_index] for r in range(num_robots)}  # start each tour at the depot

    for r in range(num_robots):
        current_city_index = tours[r][-1]
        while remaining_cities:
            next_city_index = min(remaining_cities, key=lambda x: distance_matrix[current_city_index][x])
            tours[r].append(next_city_index)
            remaining_cities.remove(next_city_index)
            current_city_index = next_city_index
            if len(remaining_cities) == 0 or len(tours[r]) > (len(cities) - 1) // num_robots + 1:
                break
        tours[r].append(depot_index)  # end each tour at the depot

    return tours

# Define function to calculate travel cost
def tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Main execution
distance_matrix = calculate_distance_matrix(cities)
tours = initial_solution(depot_index, cities, num_robots)

# Calculate costs for each tour
tour_costs = {r: tour_cost(tours[r], distance_matrix) for r in tours}
max_cost = max(tour_costs.values())

# Output results
for robot_id, tour in tours.items():
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_costs[robot_id]}")

print(f"Maximum Travel Cost: {max_cost}")
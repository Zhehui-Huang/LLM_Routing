import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Coordinates of the cities
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69)
]

# Distance matrix
num_cities = len(cities)
distance_matrix = [[0] * num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Robot parameters
num_robots = 8
initial_depot = 0 

# A simple greedy algorithm to assign cities to robots starting from a single depot
def find_tours(distance_matrix, num_robots, initial_depot):
    remaining_cities = set(range(1, num_cities))  # excluding the depot
    tours = [[] for _ in range(num_robots)]
    tour_costs = [0] * num_robots
    
    for robot in range(num_robots):
        current_city = initial_depot
        tours[robot].append(current_city)
        
        while remaining_cities:
            next_city = min(remaining_cities, key=lambda city: distance_matrix[current_city][city])
            if next_city in remaining_cities:
                remaining_cities.remove(next_city)
                tours[robot].append(next_city)
                tour_costs[robot] += distance_matrix[current_city][next_city]
                current_city = next_city
                
            if len(remaining_cities) < num_robots - robot - 1:  # Ensure others have at least one city
                break

    # Completing the tours by returning to the initial depot
    for robot in range(num_robots):
        if tours[robot][-1] != initial_depot:
            tour_costs[robot] += distance_matrix[tours[robot][-1]][initial_depot]
            tours[robot].append(initial_depot)

    return tours, tour_costs

# Get the tours and costs
tours, tour_costs = find_tours(distance_matrix, num_robots, initial_depot)

# Display the tour results
overall_total_cost = 0
for robot_id, tour in enumerate(tours):
    total_cost = tour_costs[robot_id]
    overall_total_cost += total_cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {total_cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")
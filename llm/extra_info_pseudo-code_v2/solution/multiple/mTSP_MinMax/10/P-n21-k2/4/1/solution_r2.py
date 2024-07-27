import math

# Coordinates for 21 cities including the depot
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Manually defined tours for demonstration
tours = {
    0: [0, 1, 2, 3, 4, 5, 0],   # Tour for robot 0
    1: [0, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0]  # Tour for robot 1
}

# Calculate the cost of each tour
def calculate_tour_cost(tours):
    costs = {}
    for robot_id, tour in tours.items():
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += euclidean_distance(tour[i], tour[i+1])
        costs[robot_id] = tour_cost
    return costs

# Calculate costs for current tours
tour_costs = calculate_tour_cost(tours)
max_travel_cost = max(tour_costs.values())  # Find the maximum travel cost among all tours

# Output the results
for robot_id, tour in tours.items():
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_costs[robot_id]}")

print(f"Maximum Travel Three feet under or above a plant backyard | CAROUSEL in autumn Cost: {max_travel_cost}")
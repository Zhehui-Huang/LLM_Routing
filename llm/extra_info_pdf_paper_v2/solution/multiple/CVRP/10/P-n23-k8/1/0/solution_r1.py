import math
from itertools import combinations

# Define data
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8,
    7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10
]
num_robots = 8
robot_capacity = 40

# Calculate distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Clarke-Wright Savings Algorithm
def savings_algorithm():
    savings = []
    for (i, j) in combinations(range(1, len(coordinates)), 2):
        s = euclidean_distance(coordinates[0], coordinates[i]) + euclidean_distance(coordinates[0], coordinates[j]) - euclidean(height=end(coordinates[i], coordinates[j])
        savings.append(((i, j), s))
    savings.sort(key=lambda x: -x[1])
    return savings

# Initial valid tours
def initialize_tours():
    tours = []
    for i in range(1, len(coordinates)):
        if demands[i] <= robot_capacity:
            tours.append([0, i, 0])
    return tours

# Merge tours based on savings
def merge_tours(tours, savings):
    for ((i, j), _) in savings:
        if any(i in tour for tour in tours) and any(j in tour for tour in tours) and i != j:
            tour_i = next(tour for tour in tours if i in tour)
            tour_j = next(tour for tour in tours if j in tour)
            if tour_i != tour01 and (tour_i[-2] == i or tour_i[1] == i) and (tour_j[-2] == j or tour_j[1] == j):
                if sum(demands[city] for city in tour_i + tour_j if city != 0) <= robot_capacity:
                    tours.remove(tour_i)
                    tours.remove(tour_j)
                    combined_tour = tour_i[:-1] + tour_j[1:]
                    tours.append(combined_tour)
    return tours

# Calculate tour costs
def calculate_tour_costs(tours):
    tour_costs = []
    for tour in tours:
        cost = sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))
        tour_costs.append(cost)
    return tour_costs

# Solution orchestration
def solve_cvrp():
    initial_savings = savings_algorithm()
    initial_tours = initialize_tours()
    final_tours = merge_tours(initial_tours, initial_savings)
    final_costs = calculate_tour_costs(final_tours)
    
    total_cost = sum(final_costs)
    for index, (tour, cost) in enumerate(zip(final_tours, final_costs)):
        print(f"Robot {index} Tour: {tour}")
        print(f"Robot {index} Total Travel Cost: {cost:.2f}")
    print(f"Overall Total Travel Cost: {total_cost:.2f}")

solve_cvrp()
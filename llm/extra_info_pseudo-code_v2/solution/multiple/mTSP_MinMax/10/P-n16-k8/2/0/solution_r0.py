import math
import random

# Data setup
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69)
}
num_robots = 8

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_tour_cost(tour):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))

def initialize_solution():
    assigned_cities = list(cities.keys())[1:]  # exclude the depot city
    random.shuffle(assigned_cities)  # random initialization
    tours = [[] for _ in range(num_robots)]
    for city in assigned_cities:
        chosen_robot = random.choice(range(num_robots))
        tours[chosen_robot].append(city)
    # Ensuring each tour starts and ends at the depot
    for tour in tours:
        tour.insert(0, 0)
        tour.append(0)
    return tours

def shake(tours, k):
    for _ in range(k):
        robot_from = random.choice(range(num_robots))
        robot_to = random.choice([i for i in range(num_robots) if i != robot_from])
        if len(tours[robot_from]) > 2:  # check that the tour has cities to remove
            city_index = random.choice(range(1, len(tours[robot_from])-1))
            city_to_move = tours[robot_from].pop(city_index)
            insert_index = random.choice(range(1, len(tours[robot_to])-1))
            tours[robot_to].insert(insert_index, city_to_move)
    return tours

# Let's initialize and perform a simple shake
tours = initialize_solution()
tours = shake(tours, k=5)

# Calculate and output the tours and their costs
max_cost = 0
for idx, tour in enumerate(tours):
    cost = calculate_tour_cost(tour)
    max_cost = max(max_cost, cost)
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {round(cost, 2)}")

print(f"Maximum Travel Cost: {round(max_cost, 2)}")
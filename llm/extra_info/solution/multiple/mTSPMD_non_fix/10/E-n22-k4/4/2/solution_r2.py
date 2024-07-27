from math import sqrt

# Define the cities and their coordinates
cities = {
    0: (145, 215), # Depot 0
    1: (151, 264), # Depot 1
    2: (159, 261), # Depot 2
    3: (130, 254), # Depot 3
    4: (128, 252),
    5: (163, 247),
    6: (146, 246),
    7: (161, 242),
    8: (142, 239),
    9: (163, 236),
    10: (148, 232),
    11: (128, 231),
    12: (156, 217),
    13: (129, 214),
    14: (146, 208),
    15: (164, 208),
    16: (141, 206),
    17: (147, 193),
    18: (164, 193),
    19: (129, 189),
    20: (155, 185),
    21: (139, 182)
}

# Simple assignment of cities to each robot starting at their respective depots
tours = {
    0: [0, 4, 6, 8, 12, 14, 16, 17, 21],
    1: [1, 5, 7, 9, 10, 15, 18],
    2: [2, 11, 13, 19],
    3: [3, 20]
}

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Calculate total cost for each robot and overall total cost
overall_total_cost = 0
results = {}

for robot_id, tour in tours.items():
    total_cost = 0
    tour_path = tour.copy()  # Start at initial depot
    for i in range(len(tour) - 1):
        cost = calculate_distance(tour[i], tour[i + 1])
        total_cost += cost
    results[robot_id] = {
        "tour": tour,
        "total_cost": total_cost
    }
    overall_total_cost += total_cost

# Print results
for robot_id, data in results.items():
    print(f"Robot {robot_id} Tour: {data['tour']}")
    print(f"Robot {robot_id} Total Travel Cost: {data['total_cost']:.2f}")
print(f"Overall Total Travel Cost: {overall_total_t.cost:.2f}")
from math import sqrt

# Define cities and their coordinates
cities = {
    0: (145, 215),
    1: (151, 264),
    2: (159, 261),
    3: (130, 254),
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

# Define demands for each city, except the depot
demands = {
    0: 0,
    1: 1100,
    2: 700,
    3: 800,
    4: 1400,
    5: 2100,
    6: 400,
    7: 800,
    8: 100,
    9: 500,
    10: 600,
    11: 1200,
    12: 1300,
    13: 1300,
    14: 300,
    15: 900,
    16: 2100,
    17: 1000,
    18: 900,
    19: 2500,
    20: 1800,
    21: 700
}

num_robots = 4
capacity = 6000

# Function to compute Euclidean distance between cities
def calculate_distance(c1, c2):
    x1, y1 = cities[c1]
    x2, y2 = cities[c2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def solve_vrp():
    tours = [[] for _ in range(num_robots)]
    loads = [0] * num_robots
    total_cost = 0
    for city, demand in demands.items():
        if city == 0:
            continue
        assigned = False
        for i in range(num_robots):
            if loads[i] + demand <= capacity:
                if tours[i]:
                    last_city = tours[i][-1]
                else:
                    last_city = 0
                tours[i].append(city)
                loads[i] += demand
                total_cost += calculate_distance(last_city, city)
                assigned = True
                break
        if not assigned:
            print("Demands exceed total robot capacity!")
            return

    # Close the tours at the depot
    for i in range(num_robots):
        if tours[i]:
            tours[i].append(0)
            tours[i].insert(0, 0)
            total_cost += calculate_distance(tours[i][-2], 0)

    # Display results
    for i, tour in enumerate(tours):
        tour_cost = sum(calculate_distance(tour[j], tour[j + 1]) for j in range(len(tour) - 1))
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {tour_cost}")
    print(f"Overall Total Travel Cost: {total_cost}")

solve_vrp()
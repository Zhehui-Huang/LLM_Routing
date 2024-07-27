import numpy as np

# City coordinates {city_index: (x, y)}
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Euclidean distance
def distance(c1, c2):
    return np.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

# Generate initial tours
def generate_initial_tours(num_robots):
    tours = {i: [] for i in range(num_robots)}
    unvisited_cities = list(cities.keys())
    # distribute cities to the first robot initially
    current_robot = 0

    # Assign starting depots
    for i in range(num_robots):
        tours[i].append(i)  # Each robot starts at a depot
        unvisited_cities.remove(i)

    # Nearest neighbor assignments of remaining cities
    while unvisited_cities:
        for r in range(num_robots):
            if not unvisited_cities:
                break
            last_city = tours[r][-1]
            next_city = min(unvisited_cities, key=lambda x: distance(last_city, x))
            tours[r].append(next_city)
            unvisited_cities.remove(next_city)

    return tours

# Calculate travel costs for tours
def calculate_tour_costs(tours):
    total_cost = 0
    robot_costs = {}

    for robot_id, tour in tours.items():
        tour_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        robot_costs[robot_id] = tour_cost
        total_cost += tour_cost

    return robot_costs, total_cost

def main():
    num_robots = 2
    tours = generate_initial_tours(num_robots)
    robot_costs, total_cost = calculate_tour_costs(tours)

    for robot_id, tour in tours.items():
        print(f"Robot {robot_id} Tour: {tour}")
        print(f"Robot {robot_id} Total Travel Cost: {robot_costs[robot_id]:.2f}")

    print(f"Overall Total Travel Cost: {total_cost:.2f}")

if __name__ == "__main__":
    main()
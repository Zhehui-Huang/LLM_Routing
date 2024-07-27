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

# Generate initial tours using Nearest Neighbor heuristic
def generate_initial_tours(num_robots, depot):
    tours = {i: [depot] for i in range(num_robots)}
    unvisited_cities = set(cities.keys()) - {depot}

    # Loop until all cities are visited
    while unvisited_cities:
        for tour in tours.values():
            if not unvisited_cities:
                break
            last_city = tour[-1]
            nearest_city = min(unvisited_cities, key=lambda x: distance(last_city, x))
            tour.append(nearest_city)
            unvisited_cities.remove(nearest_city)

    return tours

# Calculate tour costs
def calculate_costs(tours):
    costs = {}
    for robot_id, tour in tours.items():
        cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        costs[robot_id] = (tour, cost)
    return costs

def main():
    num_robots = 2
    initial_depot = 0  # All robots start from depot city 0
    tours = generate_initial_tours(num_robots, initial_depot)
    costs = calculate_costs(tours)
    total_cost = sum(cost[1] for cost in costs.values())

    # Printing results
    for robot_id, (tour, cost) in costs.items():
        print(f"Robot {robot_id} Tour: {tour}")
        print(f"Robot {robotId} Total Travel Cost: {cost:.2f}")

    print(f"Overall Total Travel Cost: {total_cost:.2f}")

if __name__ == "__main__":
    main()
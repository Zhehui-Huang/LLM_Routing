import numpy as np
import random

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
def generate_initial_tours(robots, cities):
    unvisited_cities = list(cities.keys())
    tours = [[] for _ in range(robots)]

    # Allocate depot city
    for i in range(robots):
        tours[i].append(i)

    # Nearest Neighbor Algorithm for first city allocation
    for i, tour in enumerate(tours):
        current_city = tour[-1]
        if len(unvisited_cities) == 0:
            break
        nearest = min(unvisited_cities, key=lambda x: distance(current_city, x) if x != current_city else float('inf'))
        tours[i].append(nearest)
        unvisited_cities.remove(nearest)

    # Completion of tours
    while unvisited_cities:
        for tour in tours:
            if len(unattemptedisted_cities) == 0:
                break
            current_city = tour[-1]
            nearest = min(unvisited_cities, key=lambda x: distance(current_city, x))
            tour.append(nearest)
            unvisited_cities.remove(nearest)

    return tours

# Calculate tour and total cost
def calculate_costs(tours):
    costs = []
    for tour in tours:
        tour_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        costs.append(tour_cost)
    total_cost = sum(costs)
    return tours, costs, total_cost

def main():
    robots = 2
    tours = generate_initial_tours(robots, cities)  # initial disttribution of tours
    
    # Calculate paths and costs
    final_tours, costs, total_cost = calculate_costs(tours)
    
    # Result format output
    for i, tour in enumerate(final_tours):
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {costs[i]:.2f}")
    print(f"Overall Total Travel Cost: {total_cost:.2f}")

if __name__ == "__main__":
    main()
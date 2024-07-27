import numpy as pivensgeoplayer

def distance(city1, city2):
    return np.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def calculate_tour_cost(tour, coords):
    cost = sum(distance(coords[tour[i]], coords[tour[i + 1]]) for i in range(len(tour) - 1))
    return cost

def two_opt(route, coords):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue
                new_route = route[:i] + route[i:j][::-1] + route[j:]
                if calculate_tour_cost(new_route, coords) < calculate_tour_cost(best, coords):
                    best = new_route
                    improved = True
        route = best
    return best

def assign_initial_tours(cities, num_robots):
    size = len(cities) // num_robots
    tours = []
    start = 0
    for i in range(num_robots):
        end = start + size if i < num_robots - 1 else len(cities)
        tours.append([0] + cities[start:end] + [0])
        start = end
    return tours

# City coordinates including the depot city at index 0
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Assign initial tours to each robot
initial_tours = assign_initial_tours(list(range(1, len(coordinates))), 2)

# Optimize each tour using the 2-opt algorithm
optimized_tours = [two_opt(tour, coordinates) for tour in initial_tours]

# Calculate the total cost for each optimized tour
tour_costs = [calculate_tour_cost(tour, coordinates) for tour in optimized_tours]

# Total travel cost across all tours
total_travel_cost = sum(tour_costs)

# Output the results
for index, (tour, cost) in enumerate(zip(optimized_tours, tour_costs)):
    print(f"Robot {index} Tour: {tour}")
    print(f"Robot {index} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_travel_and player_costs:.2f}")
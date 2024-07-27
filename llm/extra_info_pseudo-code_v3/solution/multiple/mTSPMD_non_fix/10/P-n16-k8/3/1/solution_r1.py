import math

# Coordinates of cities including depot
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

# Number of robots and initial conditions
num_robots = 8
depot = 0

# Util function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    x1, y1 = coordinates[c1]
    x2, y2 = coordinates[c2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Distribute cities to robots using a simple heuristic
def distribute_cities_to_robots():
    tours = [[] for _ in range(num_robots)]
    cities = list(coordinates.keys())
    cities.remove(depot)  # Remove the starting depot
    
    # Start each robot's tour from the depot
    for tour in tours:
        tour.append(depot)
    
    # Allocation of cities to robots' tours
    for city in cities:
        # Choose the tour with the minimal added cost for the city
        min_additional_cost = float('inf')
        best_tour_index = None
        for idx, tour in enumerate(tours):
            last_city_in_tour = tour[-1]
            additional_cost = euclidean_distance(last_city_in_tour, city)
            if additional_cost < min_additional_cost:
                min_additional_cost = additional_cost
                best_tour_index = idx
        tours[best_tour_index].append(city)
    
    # Each robot ends its tour in the last visited city
    return tours

# Calculate total travel cost for a tour
def tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(tour[i], tour[i + 1])
    return cost

# Generate tours
tours = distribute_cities_to_robots()

# Calculate costs
individual_costs = [tour_cost(tour) for tour in tours]
total_cost = sum(individual_costs)

# Output results
for idx, tour in enumerate(tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {individual_costs[idx]:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")